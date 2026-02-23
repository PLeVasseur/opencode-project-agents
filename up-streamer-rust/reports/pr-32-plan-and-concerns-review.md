# PR #32: Plan & Concerns Review

## Overall Assessment

The plan is structurally thorough and demonstrates genuine care about traceability and rollback safety. The concerns document correctly identifies the most important conflict (single-touch vs. compilability). However, both documents **underestimate the severity of that conflict**, and the plan contains several other issues ranging from a fundamental dependency it hasn't accounted for to significant over-engineering in its recovery infrastructure.

---

## The Plan

### What's good

The phased structure is sound. The progression from safety baseline → workspace setup → rebuild → split → validate → publish is the right skeleton. Reviewer requirement traceability (R1–R6) mapped to checkboxes is excellent — it makes it easy to audit whether each piece of feedback was actually addressed. The rollback refs and backup tags before history rewrite are good practice. The post-stack proof gates (tree identity, per-commit compile, overlap matrix, header audit) are the right things to check.

### Critical issue: the `log` → `tracing` migration is a hidden cross-cutting dependency

This is the single biggest problem the plan hasn't accounted for.

The workspace `Cargo.toml` diff removes `log` and `env_logger` as workspace dependencies. But **24 files** across every layer of the codebase migrate from `use log::*` to `use tracing::*`:

- `configurable-streamer/src/main.rs`
- `example-streamer-implementations/src/bin/zenoh_someip.rs`
- `up-streamer/src/ustreamer.rs`
- 4 files in `utils/integration-test-utils/`
- `utils/usubscription-static-file/src/lib.rs`
- 4 test files in `up-streamer/tests/`
- 10 files in `example-streamer-uses/`

These files are spread across proposed commits 1–5. The workspace `Cargo.toml` can only remove `log` **once**, and every file that uses `log` must already be migrated at that point. This means the `log → tracing` migration is an atomic operation that must happen in a single commit touching files from every proposed boundary. The plan doesn't mention this at all.

**Concrete impact:** If commit 2 (routing) adds `tracing` to the crate-level `Cargo.toml` but the old `ustreamer.rs` still uses `use log::*`, it won't fail to compile (both deps can coexist). But the workspace-level removal of `log` can't happen until **all** 24 files are migrated. If that removal lands in commit 4 (the "rewire" commit), then commit 4 must also touch the 10 `example-streamer-uses` files, the `integration-test-utils` files, and the test files — blowing through the proposed commit 4 and 5 boundaries.

**Resolution options:**
1. Make the `log → tracing` migration its own commit (commit 0, before everything else). This is a mechanical find-and-replace that a reviewer can skim in 30 seconds. It touches many files but the changes are trivially verifiable.
2. Defer the workspace-level `log`/`env_logger` removal to commit 5 (tests) and accept that both `log` and `tracing` coexist in intermediate commits. This is messy but preserves compilability.
3. Accept that the workspace `Cargo.toml` is a multi-touch file (like `Cargo.lock`).

Option 1 is cleanest. It also means the observability module, routing module, etc. can use `tracing` from the start without any dep gymnastics.

### Critical issue: the subscription-cache deletion makes commit 2 uncompilable

The plan assigns `subscription-cache` crate deletion to commit 2 (routing extraction + fold-in). But the **old** `ustreamer.rs` (which isn't supposed to change until commit 4) contains:

```rust
use subscription_cache::{SubscriptionCache, SubscriptionInformation};
```

And the crate-level `Cargo.toml` has:

```toml
subscription-cache = {path="../subscription-cache"}
```

Deleting the `subscription-cache` directory in commit 2 while the old `ustreamer.rs` still imports from it means `cargo check` will fail. The plan's per-commit compile gate will catch this — but only to block progress, not to solve the problem.

**Resolution:** The `subscription-cache` deletion cannot happen in commit 2 unless commit 2 also rewrites `ustreamer.rs`, which violates the single-touch rule. The realistic options are:
- Fold the `subscription-cache` deletion into the "rewire" commit (commit 4), not into the routing commit.
- Collapse commits 2–4 into a single "extract all internal modules + rewire" commit. This is the most honest approach — these three commits have a dependency chain that doesn't permit clean intermediate compilation.

### Significant issue: the multi-touch file list is larger than acknowledged

The plan says `Cargo.lock` is the only exception to single-touch. In reality, the following files **must** be touched by multiple commits for compilation:

| File | Why it's multi-touch |
|------|---------------------|
| `up-streamer/src/lib.rs` | Each module extraction commit adds `mod X;` declarations |
| `up-streamer/Cargo.toml` | Commit 2 adds `arc-swap`, `tracing`; commit 6 adds `criterion` + bench config |
| `Cargo.toml` (workspace) | Removes `subscription-cache` member; adds `criterion-guardrail`, `transport-smoke-suite` members; removes `log`/`env_logger` deps |
| `Cargo.lock` | Already acknowledged |

The plan needs to either expand the exception list or collapse commits to avoid the touches. I'd recommend expanding the exception list to include `lib.rs`, both `Cargo.toml` files, and `Cargo.lock`, since these are all "manifest/wiring" files whose multi-touch nature is obvious and non-confusing to reviewers.

### Over-engineering: the recovery infrastructure

Phases 0 and 0R — the bootstrap/resume protocol with `RUN_ID`, `REPORT_DIR`, `STATE_FILE`, `PHASE_FILE`, `TRANSCRIPT_FILE`, `RUN_POINTER` symlinks, `exec > >(tee -a ...)` transcript capture, session crash detection, and rehydration — are extremely heavy for what this operation actually is.

This is a `git reset --soft` followed by 7 `git add` / `git commit` cycles. If anything goes wrong, you `git reset` back to the backup branch and start over. The entire redo takes 15 minutes. The recovery infrastructure would take longer to debug if it breaks than the underlying operation takes to redo from scratch.

The backup branch + backup tag (Phase 1) are genuinely useful. Everything else in Phase 0/0R is overhead that adds complexity without proportional safety benefit. If this plan is being executed by an automated agent, the agent's own session state is sufficient. If executed by a human, the human can just... look at `git log` and see where they are.

**Recommendation:** Keep Phase 1 (backup refs). Delete Phases 0 and 0R entirely. Add a one-liner to the top: "If anything fails, reset to `$BACKUP_BRANCH` and start from Phase 2."

### Minor issue: Phase 4 branch topology

Phase 4 creates PR B by cherry-picking C6 onto C5, and PR C by cherry-picking C7 onto C5. This is correct in principle but means the cherry-picked commits will have different SHAs than the originals on `pr-32-restack-work`. This is fine, but the plan should note this explicitly because the `STATE_FILE` captures the original C6/C7 SHAs, and someone debugging later might be confused when PR B's commit doesn't match.

### Minor issue: Phase 5 validation calls `source build/envsetup.sh highest`

This appears without prior context. What is this script? Is it checked into the repo? If it's a local environment setup script, the plan should note that and explain what it does, because anyone else (or a future session) executing this plan won't have it.

---

## The Concerns Document

### Concern #1 (single-touch vs. compilability): Correctly identified, insufficiently resolved

The concern correctly names the fundamental tension. But the resolution — "prefer collapsing adjacent commit boundaries" — is too vague to be actionable. It doesn't answer: which commits collapse? What does the resulting structure look like?

Based on the dependency analysis, here's what actually happens when you try to compile each proposed commit:

| Commit | Can it compile on its own? | Why / why not |
|--------|:-------------------------:|---------------|
| 1 (observability) | **Maybe** | Needs `mod observability;` in `lib.rs`, and `lib.rs` is supposed to be finalized in commit 4. But if we add ONLY `pub mod observability;` as an additive line, and the old code still compiles, this might work. The old `ustreamer.rs` doesn't reference observability, so adding the module declaration shouldn't break anything. |
| 2 (routing + subscription-cache fold-in) | **No** | Deleting `subscription-cache` crate breaks old `ustreamer.rs` import. Adding `mod routing;` to `lib.rs` touches a file committed later. |
| 3 (data_plane + control_plane + runtime) | **No** | These modules import from `routing/` and `observability/` (which exist) but also from each other and from `lib.rs` re-exports. The old `ustreamer.rs` would need to be gone/replaced for these new modules to wire correctly. |
| 4 (rewire) | **Yes** | This is where everything actually comes together. |
| 5 (tests) | **Yes** | Test-only changes after the wiring is complete. |
| 6 (benchmark) | **Yes** | Self-contained addition. |
| 7 (smoke) | **Yes** | Self-contained addition. |

So commits 1–3 are the problem zone. The realistic collapse is **commits 2–4 into a single commit** (or 1–4 if commit 1 also can't compile alone). This gives you:

| Revised commit | Scope | Compilable? |
|---------------|-------|:-----------:|
| 1. `refactor: add observability vocabulary` | `observability/` + `mod observability;` in lib.rs | Probably yes |
| 2. `refactor: extract domain modules and rewire` | `routing/`, `data_plane/`, `control_plane/`, `runtime/`, `ustreamer.rs`, `lib.rs`, `Cargo.toml`, entrypoints, subscription-cache deletion | Yes |
| 3. `test: update tests for new module layout` | Tests + test utils | Yes |
| 4. `feat(ci): benchmark harness` | benchmark_support.rs + criterion-guardrail + CI | Yes |
| 5. `feat(smoke): smoke suite` | transport-smoke-suite + CI | Yes |

This is 5 commits, not 7. It sacrifices the fine-grained module-by-module extraction for compilability. But 5 genuinely compilable, reviewable commits is better than 7 commits where 3 don't compile.

If the `log → tracing` migration is pulled into a commit 0 as I suggested above, the structure becomes 6 commits, with the big "extract + rewire" commit being somewhat smaller because the log→tracing changes are already done.

### Concern #2 (end-loaded overlap proof): Good catch, practical fix

The per-commit fail-fast overlap check is a simple, effective improvement. The implementation is straightforward — maintain a cumulative set of file paths and diff against each new commit's `--name-only` output. This is the best concern in the document. No issues.

### Concern #3 (stacked PR operational risk): Correctly identified but understated

The mitigation says "avoid force-updating PR B/C until PR A review stabilizes." In practice, if PR A gets review feedback that requires changes (which is likely for a 5,900-line architectural PR), you need to:

1. Amend/rebase commits in PR A
2. Force-push PR A
3. Rebase PR B onto new PR A tip
4. Rebase PR C onto new PR A tip
5. Force-push PR B and PR C

This is three force-pushes and two rebases triggered by every round of review on PR A. The plan should include explicit procedures for this because it **will** happen. It's not an edge case; it's the normal workflow for stacked PRs.

### Concern #4 (commit-body quality): Fine as stated

The four-point template (what changed, why this boundary, key review files, behavioral vs. mechanical) is exactly right. No issues.

### Missing concerns

**The `log → tracing` migration.** This cross-cutting dependency spanning 24 files across all module boundaries is not mentioned in either document. It's arguably the hardest dependency to resolve cleanly.

**The workspace `Cargo.toml` is multi-touch.** The plan only acknowledges `Cargo.lock`, but the workspace manifest changes in at least 3 commits (member list changes + dep removals).

**The `example-streamer-uses/` files.** These 10 files have `log → tracing` changes but don't appear in any of the 7 proposed commits' scope descriptions. They'd need to land somewhere.

---

## Recommended Revised Commit Structure

Taking all the above into account:

| # | Commit | Files | Compiles? | Notes |
|---|--------|-------|:---------:|-------|
| 0 | `chore: migrate log/env_logger to tracing` | 24 files (mechanical find-replace) + workspace Cargo.toml dep changes | Yes | Reviewer: skim only, all changes are `s/log/tracing/` |
| 1 | `refactor: add observability vocabulary` | 3 files + `lib.rs` mod declaration | Yes | Leaf module, 5-min review |
| 2 | `refactor: extract domain modules, fold subscription-cache, rewire API` | ~40 files (routing/, data_plane/, control_plane/, runtime/, ustreamer.rs, lib.rs, Cargo.toml, entrypoints) | Yes | The big commit. Collapse is necessary. Copyright headers included at creation. |
| 3 | `test: update integration and unit tests` | ~15 files | Yes | Mechanical path changes flagged, behavioral changes called out |
| 4 | `feat(ci): criterion benchmark harness and guardrail` | ~25 files (includes benchmark_support.rs) | Yes | Self-contained |
| 5 | `feat(smoke): cross-transport smoke suite` | ~77 files + .gitattributes | Yes | Self-contained, fixtures collapsed |

Six commits, all compilable, no file touched in more than one commit (except `Cargo.lock` and workspace `Cargo.toml` which are in the explicit exception list). The tradeoff is that commit 2 is large (~3,500 lines), but it's a single coherent architectural extraction that a reviewer can evaluate as a unit.

This can then go out as:
- **PR A:** Commits 0–3 (migration + architecture + tests)
- **PR B:** Commit 4 (benchmarks), based on PR A
- **PR C:** Commit 5 (smoke suite), based on PR A

---

## Summary

| Aspect | Verdict |
|--------|---------|
| Phase structure (1→7) | Good skeleton, right progression |
| Recovery infrastructure (Phase 0/0R) | Over-engineered; delete and rely on backup refs |
| Commit boundary design | Doesn't survive contact with the dependency graph; commits 2–4 must collapse |
| `log → tracing` migration | Completely unaccounted for; needs its own commit or integrated resolution |
| Multi-touch file exceptions | Under-counted (`lib.rs`, `Cargo.toml` workspace + crate are also multi-touch) |
| Concern #1 (single-touch vs compile) | Correctly identified, but resolution too vague to execute |
| Concern #2 (fail-fast overlap) | Solid, adopt as-is |
| Concern #3 (stacked PR rebase churn) | Understated; needs explicit re-push procedures |
| Concern #4 (commit bodies) | Correct and sufficient |
| Traceability & proof gates | Excellent |
| Rollback safety | Excellent |
