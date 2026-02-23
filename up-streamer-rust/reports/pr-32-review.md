# PR #32 Review: Actionable Feedback

## At a Glance

| Metric | Value |
|--------|-------|
| Total diff | **+12,453 / −2,995** across **168 files** |
| Commits | 6 |
| Files touched by 3+ commits | **30** |
| Files touched by commits 1 AND 2 | **28** |
| Largest single commit | Commit 5: 94 files, +4,914 lines |
| Commit bodies with reviewer context | **0 of 6** |

---

## Problem #1: Commits 1–3 are not independently reviewable

The first three commits share so many files that reviewing any one of them in isolation gives you an incomplete, misleading picture.

**Concrete overlap:**

| File | C1 | C2 | C3 | What happens |
|------|:--:|:--:|:--:|-------------|
| `ingress_registry.rs` | ✓ | ✓ | ✓ | Created in C1 (545 lines), reshaped in C2 (+22/−?), heavily rewritten in C3 (+469/−?) |
| `publish_resolution.rs` | ✓ | ✓ | ✓ | Created in C1, API changed in C2, instrumented + cached in C3 |
| `subscription_directory.rs` | ✓ | ✓ | ✓ | Created in C1, expanded in C2, instrumented in C3 |
| `route_lifecycle.rs` | ✓ | ✓ | ✓ | Created in C1, contract changed in C2, +110 lines in C3 |
| `ustreamer.rs` | ✓ | ✓ | ✓ | Gutted in C1, rebuilt in C2, instrumented in C3 |
| `lib.rs` | ✓ | ✓ | ✓ | Re-exported in C1, more re-exports in C2, more in C3 |

28 total files are modified in both C1 and C2. A reviewer looking at C1's `ingress_registry.rs` cannot evaluate the design — it will be substantially changed one commit later. This makes per-commit review theater rather than substance.

**Action:** Re-slice commits 1–3 so that each file reaches its final state in exactly one commit. See the proposed breakdown below.

---

## Problem #2: Commit 3 bundles three unrelated concerns

Commit 3 (`perf+obs`) at +2,853 lines is doing:

1. **New observability module** — `observability/events.rs`, `observability/fields.rs`, `observability/mod.rs` (leaf module, no internal deps, ~293 lines)
2. **Performance/structural rework** of workers, registry, runtime (~2,200+ lines touching 20+ existing files)
3. **`benchmark_support.rs`** — 329 lines of deterministic Criterion fixtures that are consumed by commit 4's harness

These are three different reviewer focus areas crammed into one diff. The observability module is a clean leaf that could be reviewed in 5 minutes on its own. The benchmark fixtures logically belong with commit 4. The performance rework deserves isolated attention.

**Action:** Pull `observability/` into its own commit (lands first since it's a dependency leaf). Move `benchmark_support.rs` into commit 4 where it's consumed.

---

## Problem #3: Commit 6 exists because commits 1–5 ship files without copyright headers

Commit 6 touches **49 files** to add copyright headers that should have been present when those files were created. Examples:

- `benchmark_support.rs` → created in C3, header added in C6
- `route_lifecycle.rs` → created in C1, header added in C6
- Every file in `transport-smoke-suite/` → created in C5, headers in C6

This means commits 1–5 all produce license-non-compliant files, and commit 6 is a pure fixup.

**Action:** During the rebase, include the copyright header in each file at creation time. Delete commit 6 entirely.

---

## Problem #4: Commit 4 patches a file commit 3 just created

Commit 4's diff to `benchmark_support.rs` is a single removed blank line:

```diff
-
 fn subscription(topic: UUri, subscriber: UUri) -> Subscription {
```

This leaked across the commit boundary during the squash/rewrite.

**Action:** Absorb this one-liner into commit 3 (or into the commit that creates `benchmark_support.rs` in the revised layout).

---

## Problem #5: Commit 5 buries code under 56 fixture files

Commit 5 adds 94 files. Of those, 56 are `.log` and `.json` test fixtures (3–6 lines each). The meaningful code — the smoke runner, claims engine, scenario framework, and CI workflow — is ~3,600 lines across 38 files. On GitHub, a reviewer clicking through the file list hits dozens of `pass/publisher.log` files before reaching the actual logic.

**Action:** Either split fixtures into a separate commit marked as generated/no-review, or add a `.gitattributes` entry:

```gitattributes
utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true
utils/transport-smoke-suite/claims/** linguist-generated=true
```

This causes GitHub to collapse those files by default in the diff view.

---

## Problem #6: Zero commit bodies

All 6 commits have only a subject line. For a 12,500-line architectural rewrite, this leaves a reviewer with no guidance on:

- What the new architecture *is* and why boundaries were drawn where they are
- Which files contain the important design decisions vs. mechanical moves
- What changed from the old `subscription-cache` crate (deleted entirely) to the new `routing/subscription_cache.rs`
- Why `ustreamer.rs` went from ~2,000 lines down then back up

**Action:** Add a body to every commit. Template:

```
refactor: modernize up-streamer domain architecture boundaries

Extract the monolithic ustreamer.rs into four domain modules:
- data_plane/: egress pool, workers, ingress listener + registry
- routing/: publish resolution, subscription directory + cache
- control_plane/: route lifecycle, route table, transport identity
- runtime/: worker and subscription runtimes

The old subscription-cache crate is folded into routing/subscription_cache.rs
because [reason].

Key files to review: data_plane/ingress_registry.rs (core dispatch logic),
routing/publish_resolution.rs (new resolution strategy).

Mechanical: test files updated for new import paths only — no logic changes.
```

---

## Proposed PR Breakdown

I traced the internal dependency graph in the final state of the code:

```
observability/  →  (leaf, no crate-internal deps)
routing/        →  depends on observability/
data_plane/     →  depends on observability/, routing/, control_plane/, runtime/
control_plane/  →  depends on data_plane/, routing/, observability/
runtime/        →  depends on observability/
ustreamer.rs    →  depends on everything above
```

### Option A: One PR, better commits (minimum viable fix)

Keep it as one PR but restructure the 6 commits into 7 commits where **each file reaches its final state in exactly one commit**:

| New commit | Scope | Est. size | Why this order |
|-----------|-------|-----------|----------------|
| **1. `refactor: add observability module`** | `observability/events.rs`, `fields.rs`, `mod.rs` + copyright headers | ~300 lines, 3 files | Leaf module. No internal deps. Reviewable in 5 min. |
| **2. `refactor: extract routing module from monolith`** | `routing/` (all 6 files in final state), delete `subscription-cache` crate | ~1,000 lines, 8 files | Depends only on observability. Includes the subscription-cache fold-in. |
| **3. `refactor: extract data_plane, control_plane, runtime modules`** | All files in `data_plane/`, `control_plane/`, `runtime/` in final state. Gut `ustreamer.rs`. | ~2,400 lines, 15 files | These three modules have circular deps — they must land together. |
| **4. `refactor: rewire top-level API, plugin, and entrypoints`** | `ustreamer.rs`, `lib.rs`, `endpoint.rs`, `subscription_sync_health.rs`, plugin/streamer entrypoints, `Cargo.toml` changes | ~1,300 lines, 17 files | Wires everything together. All tests should pass after this commit. |
| **5. `test: update integration and unit tests`** | All files under `tests/`, `integration-test-utils/`, `usubscription-static-file/` | ~900 lines, 15 files | Purely test changes — fast to review, easy to skim. |
| **6. `feat(ci): add benchmark guardrail harness`** | `benchmark_support.rs`, `criterion-guardrail/`, benches, CI workflow, script | ~1,450 lines, 25 files | Self-contained. Includes the fixture CSVs. |
| **7. `feat(smoke): add cross-transport smoke suite`** | Entire `transport-smoke-suite/`, CI workflow, `.gitattributes` for fixtures | ~4,900 lines, 77 files | Self-contained. `.gitattributes` collapses fixture diffs. |

**How to execute this:**

```bash
# From the current cleanup/refactor-upstream-main branch
git checkout -b cleanup/refactor-upstream-main-v2 cleanup/refactor-upstream-main

# Soft-reset to main so all changes are staged but uncommitted
git reset --soft origin/main

# Now unstage everything
git reset HEAD .

# Re-commit file by file / module by module using:
#   git add <paths>
#   git commit

# Commit 1: observability
git add up-streamer/src/observability/
git commit -m "refactor: add observability event and field vocabulary

Introduces the observability/ module as a leaf dependency with no internal
imports. Defines structured tracing field helpers and event name constants
used by all other modules in subsequent commits."

# Commit 2: routing
git add up-streamer/src/routing/ subscription-cache/
git commit -m "refactor: extract routing module, fold in subscription-cache crate

Moves publish resolution, subscription directory, subscription cache,
authority filtering, and URI identity key logic into routing/.
Deletes the standalone subscription-cache crate — its logic now lives
in routing/subscription_cache.rs because [your reason here]."

# Commit 3: data_plane + control_plane + runtime
git add up-streamer/src/data_plane/ up-streamer/src/control_plane/ \
        up-streamer/src/runtime/
git commit -m "refactor: extract data_plane, control_plane, and runtime modules

These three modules have mutual dependencies and must land together:
- data_plane: egress pool/workers, ingress listener/registry
- control_plane: route lifecycle, route table, transport identity
- runtime: worker and subscription runtimes"

# Commit 4: top-level wiring
git add up-streamer/src/ustreamer.rs up-streamer/src/lib.rs \
        up-streamer/src/endpoint.rs up-streamer/src/subscription_sync_health.rs \
        up-streamer/Cargo.toml Cargo.toml Cargo.lock \
        up-linux-streamer-plugin/ configurable-streamer/ \
        example-streamer-implementations/ up-streamer/README.md \
        up-linux-streamer-plugin/DEFAULT_CONFIG.json5
git commit -m "refactor: rewire top-level API, plugin, and streamer entrypoints

Connects the new module structure through ustreamer.rs and lib.rs.
Updates all binary/plugin entrypoints to use the new imports."

# Commit 5: tests
git add up-streamer/tests/ utils/integration-test-utils/ \
        utils/usubscription-static-file/
git commit -m "test: update integration tests for new module structure

All test logic changes are mechanical import-path updates unless noted.
[Call out any actual test logic changes here.]"

# Commit 6: benchmarks (includes benchmark_support.rs)
git add up-streamer/src/benchmark_support.rs up-streamer/benches/ \
        utils/criterion-guardrail/ scripts/bench_streamer_criterion.sh \
        .github/workflows/benchmark-guardrail-advisory.yaml
git commit -m "feat(ci): add Criterion benchmark harness and guardrail workflow

Adds benchmark_support.rs with deterministic fixtures, a Criterion bench
suite, the criterion-guardrail analysis crate, and a CI workflow that
posts advisory comments on regressions."

# Commit 7: smoke suite
git add utils/transport-smoke-suite/ \
        .github/workflows/transport-smoke-capstone.yaml
# Also add the .gitattributes entry for fixture collapsing
git commit -m "feat(smoke): add deterministic cross-transport smoke suite

Adds the transport-smoke-suite crate with claim-based pass/fail
assertions, a matrix runner, and CI workflow.
56 fixture files (.log/.json) are marked linguist-generated."

# Verify the tree matches
git diff cleanup/refactor-upstream-main --stat
# Should show: 0 files changed
```

**Caveat on intermediate compilability:** Commits 1–3 above may not compile individually because `routing/` imports from `observability/` and `data_plane/` imports from `routing/`, but the modules they depend on *in the existing code* (e.g., `ustreamer.rs` which `use`s them) won't be wired until commit 4. If intermediate compilation is a hard requirement, you may need to merge commits 1–4 into a single "extract all modules + rewire" commit, which is still a massive improvement over the current layout since you'd go from 3 commits touching the same 28 files to 1 commit that does the whole extraction cleanly.

### Option B: Three stacked PRs (better for large teams / thorough review)

If the upstream project expects smaller PRs or has multiple reviewers:

| PR | Commits | Est. size | Depends on |
|----|---------|-----------|-----------|
| **PR A: Architecture refactor** | Commits 1–5 from Option A | ~5,900 lines, 60 files | Nothing |
| **PR B: Benchmark guardrail** | Commit 6 from Option A | ~1,450 lines, 25 files | PR A |
| **PR C: Smoke test suite** | Commit 7 from Option A | ~4,900 lines, 77 files | PR A |

This keeps the core refactor separate from the two additive feature PRs. PR B and C can be reviewed in parallel once PR A lands. The core refactor at ~5,900 lines is still large, but it's a cohesive architectural change that's hard to split further without breaking compilation.

### Why module-by-file beats phase-by-concept

The current approach splits by *conceptual phase*: "first the architecture, then the subscription migration, then the performance work." This feels logical to the author because it mirrors the development timeline. But it's hostile to reviewers because:

1. **A reviewer evaluates code, not timelines.** When I open `ingress_registry.rs`, I want to understand what it does *now*, not what it looked like in three successive drafts.

2. **Phase splits create false confidence.** Commit 1 looks like a complete refactor, but it's actually an unstable intermediate state. A reviewer who approves C1 is approving code that won't exist by C3.

3. **File overlap forces mental diff-of-diffs.** For each shared file, the reviewer must hold C1's version in mind while reading C2's changes to it, then again for C3. With 28 shared files, this is unreasonable.

The module-by-file approach means: when you see `ingress_registry.rs`, that's the final version. Review it once, move on. No mental stack required.

---

## Checklist Before Resubmitting

- [ ] Every file reaches its final state in exactly one commit (no file appears in 2+ commit diffs, `Cargo.lock` excepted)
- [ ] Every commit compiles: `cargo check --workspace --all-targets` passes at each commit
- [ ] Every commit has a body explaining what, why, and what to focus on
- [ ] Copyright headers are included when files are created (no retroactive fixup commit)
- [ ] `benchmark_support.rs` is created in the same commit as the benchmark harness
- [ ] `.gitattributes` marks fixture files as `linguist-generated` so GitHub collapses them
- [ ] The final tree is identical to the current branch tip: `git diff cleanup/refactor-upstream-main --stat` shows 0 changes
- [ ] `cargo test --workspace` passes on the final commit
- [ ] The blank-line-only diff in `benchmark_support.rs` between current C3→C4 is eliminated
