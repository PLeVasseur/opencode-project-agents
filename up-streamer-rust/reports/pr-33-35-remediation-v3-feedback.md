# PR #33/#34/#35 CI Remediation Plan v2 — Implementor Feedback

Date: 2026-02-14
Reviewer context: This feedback is based on inspection of the live PR branches (`origin/prA` at `75610d5`, `origin/prB` at `bdb4151`, `origin/prC` at `8670bca`), the actual source files, the CI workflow definitions, and six prior rounds of plan review that produced the commit structure now deployed.

---

## Executive Summary

The plan's approach is correct: fix the root cause in PR A, rebase B and C, validate, push. Three issues need to be fixed before execution, and two smaller items are worth addressing. None change the overall structure — they refine how individual phases execute.

---

## Issue 1: The fix commit should amend c2, not append a 5th commit

**Severity: Medium — re-introduces the exact problem the restructuring was designed to solve.**

### What the plan does

Phase 1 uses a plain `git push` (no `--force-with-lease`), which means it appends a 5th commit on top of PR A's existing 4 commits. That 5th commit removes `lookup_route_subscribers` and rewrites the test callsite.

### Why this is a problem

The original PR had a standalone copyright-fixup commit (c6 in the old 43-commit structure) that retroactively patched files that should have been correct from the start. Reviewer traceability target R3 was created specifically to eliminate this pattern. A standalone "remove dead function" commit is structurally identical — it signals to a reviewer that c2 wasn't cleanly authored.

The function was introduced in c2 (`subscription_directory.rs` is squarely in c2's scope at `cbef885`). Its only PR-A caller is a test on line 173 of the same file, inside a `#[cfg(test)]` block. So c2 created a `pub(crate)` function that c2 itself only uses from a test. The lint violation belongs to c2, and c2 is where it should be fixed.

### What to do instead

Use `git rebase -i` to amend c2 directly:

1. Start an interactive rebase from c0's parent: `git rebase -i fb49056^`
2. Mark c2 (`cbef885`) as `edit`.
3. When the rebase pauses at c2:
   - In `up-streamer/src/routing/subscription_directory.rs`:
     - Either remove `lookup_route_subscribers` entirely, or gate it with `#[cfg(test)]`.
     - If removed: update the test at line 173 to use `lookup_route_subscribers_with_version("authority-b").await.1`.
     - If gated with `#[cfg(test)]`: no test change needed, but removing is cleaner since `_with_version` is the real production API.
   - `git add -u && git commit --amend --no-edit`
4. Let the rebase continue. c3 should replay cleanly — it doesn't touch `subscription_directory.rs`.
5. Push with `--force-with-lease`.

PR A stays at 4 commits. R3 remains closed. The commit-by-commit summary in the PR body doesn't need a new entry — just a note that c2's SHA changed.

### Impact on the rest of the plan

Phase 1's push becomes `git push --force-with-lease origin cleanup/refactor-upstream-main-prA-architecture`, matching what Phases 2 and 3 already do for PR B and PR C. Since B and C are already being rebased onto the updated PR A tip, the force-push of A doesn't add any new workflow complexity.

---

## Issue 2: Phase 1 and Phase 2 are missing `cargo test`

**Severity: Medium — CI runs tests; local validation should too.**

### What the plan does

Phase 1's mandatory validation is clippy-only (three clippy variants). Phase 2 runs targeted `cargo check` and `cargo test` for `criterion-guardrail` only, plus the clippy matrix.

### Why this matters

The fix removes a function called in a `#[tokio::test]` block and rewrites the call to a different API with a different return type (adding `.await.1` to destructure a tuple). Clippy will catch compilation failures, but if the assertion logic depends on behavioral differences between the two functions (it doesn't in this case, but the principle holds), a test failure would only surface in CI rather than locally.

The CI workflows run `cargo test --workspace`. Local validation should match.

### What to do

Add `cargo test --workspace` to Phase 1's mandatory validation block, after the clippy runs and before the push. For Phase 2, add `cargo test --workspace` after the targeted checks and before the clippy matrix — the targeted `criterion-guardrail` tests alone don't exercise the rewritten callsite in `benchmark_support.rs` against the full workspace.

---

## Issue 3: `.gitattributes` commit strategy is unspecified

**Severity: Low-Medium — ambiguity in execution, not a correctness issue.**

### What the plan does

Phase 3 rebases PR C onto updated PR A, then adds `.gitattributes` rules. The plan doesn't say whether this is a second commit or amended into the existing smoke commit.

### Why this matters

PR C is currently a single-commit delta (`8670bca`), mirroring PR B's structure. If `.gitattributes` lands as a separate commit, PR C becomes a 2-commit PR: one commit with the entire smoke suite and another with a 2-line file. That's not wrong, but it's asymmetric with PR B and slightly odd — a reviewer would wonder why the fixture-collapsing rules weren't part of the smoke commit.

### What to do

Amend the `.gitattributes` addition into the existing smoke commit. After the rebase in Phase 3:

```bash
# Add the .gitattributes rules
echo 'utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true' >> .gitattributes
echo 'utils/transport-smoke-suite/claims/** linguist-generated=true' >> .gitattributes
git add .gitattributes
git commit --amend --no-edit
```

PR C stays at 1 commit. R5 is closed. The PR body's SHA note should be updated to reflect the new commit hash.

Make the plan explicit about this: "Amend `.gitattributes` into existing smoke commit; do not create a separate commit."

---

## Issue 4: PR body updates are not in scope

**Severity: Low — won't break CI, but leaves stale documentation.**

### What the plan does

The plan has no step for updating PR body text after the fixes land.

### Why this matters

PR A's body currently lists 4 commits with specific SHAs (`fb49056`, `cd436ae`, `cbef885`, `75610d5`). After the interactive rebase, c2 and c3 will have new SHAs. The commit-by-commit summary will reference orphaned hashes.

PR C's body has a "SHA note" section documenting the cherry-pick topology. After the rebase and `.gitattributes` amend, the commit hash changes.

PR A's validation section claims local clippy passed — which is now known to be inaccurate for CI's environment. That's misleading if left as-is.

### What to do

Add a step after each push in Phases 1, 2, and 3:

- Phase 1: Update PR A body — refresh commit SHAs in the commit-by-commit section, note the c2 amendment for dead-code fix, and update the validation section to reflect the remediation run's results.
- Phase 2: No PR B body change needed unless the rebase changes the commit hash (it will — update the SHA in the body).
- Phase 3: Update PR C body — refresh the SHA note and add R5 closure to the summary.

This can be done via `gh pr edit` or manually in the GitHub UI.

---

## Issue 5: Local/CI parity investigation should be actionable

**Severity: Low — the plan includes it, but it's vague.**

### What the plan does

Phase 0 records local and CI toolchain versions. But it doesn't say what to do with the information.

### Why this matters

The PR A body claims `PASS: cargo clippy --all-targets -- -W warnings -D warnings`. CI says otherwise. If the mismatch is a toolchain version difference, the fix is to pin the local toolchain to match CI (e.g., via `rust-toolchain.toml`). If it's an environment difference (`envsetup.sh` changing include paths or feature flags), the fix is different. The plan should drive toward a concrete outcome, not just note-taking.

### What to do

Add to Phase 0: after recording versions, if they differ, either (a) switch to CI's toolchain locally via `rustup override set <version>` before running Phase 1 validation, or (b) document the specific lint behavior difference and confirm the local environment isn't masking warnings. The goal is that by the end of Phase 0, you have confidence that local clippy reproduces CI's behavior — so that Phase 1's local validation is authoritative.

---

## Items that check out — no changes needed

**Phase 0 log inspection (Gap 1 closure):** Correctly gates all mutations behind evidence. Good.

**Full clippy matrix mandatory for PR B (Gap 2 closure):** Phase 2 now includes all three clippy variants. Correct.

**`.gitattributes` in Phase 3 scope (Gap 3 closure):** Present and correctly placed. Just needs the commit strategy clarification above.

**Secondary dead-code guard (Gap 5 closure):** The full clippy matrix in Phase 1 catches any orphaned functions after the removal. Verified: `lookup_route_subscribers_with_version` has a production caller in `ingress_registry.rs:184` and a test caller in `subscription_directory.rs:196`, so it won't trigger `dead_code`.

**Non-negotiable invariants:** Fork-only push, `--force-with-lease`, stack ordering — all correctly specified.

**Phase 4 fallback loop:** Appropriately generic. No changes needed.

---

## Revised Phase 1 (for reference)

For clarity, here's what Phase 1 looks like with all feedback applied:

```
Phase 1: Fix PR A Root Cause

- [ ] Update PR A branch
  - [ ] git switch cleanup/refactor-upstream-main-prA-architecture
  - [ ] git fetch --all --prune
  - [ ] Ensure worktree is clean before edit.

- [ ] Amend c2 via interactive rebase (do NOT append a 5th commit)
  - [ ] git rebase -i fb49056^   (c0's parent)
  - [ ] Mark c2 (cbef885) as "edit".
  - [ ] At c2 pause:
    - [ ] Remove lookup_route_subscribers from subscription_directory.rs.
    - [ ] Update test at line 173 to use
          lookup_route_subscribers_with_version("authority-b").await.1
    - [ ] Verify no stale references to removed symbol remain.
    - [ ] git add -u && git commit --amend --no-edit
  - [ ] Continue rebase; c3 should replay cleanly.
  - [ ] Verify PR A is still 4 commits: git log --oneline origin/main..HEAD

- [ ] Mandatory PR A validation (CI-parity)
  - [ ] cargo clippy --all-targets -- -W warnings -D warnings
  - [ ] env -u VSOMEIP_INSTALL_PATH cargo clippy \
        --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport \
        --all-targets -- -W warnings -D warnings
  - [ ] cargo clippy \
        --features vsomeip-transport,zenoh-transport,mqtt-transport \
        --all-targets -- -W warnings -D warnings
  - [ ] cargo test --workspace

- [ ] Publish PR A update
  - [ ] Commit message unchanged (c2 amended in place).
  - [ ] git push --force-with-lease origin cleanup/refactor-upstream-main-prA-architecture
  - [ ] Update PR A body: refresh c2/c3 SHAs, note dead-code amendment,
        update validation results.
```

---

## Summary of required changes

| # | Issue | Severity | Action |
|---|-------|----------|--------|
| 1 | Fix appended as 5th commit instead of amending c2 | Medium | Use `git rebase -i` to amend c2; push with `--force-with-lease`; keep PR A at 4 commits |
| 2 | No `cargo test` in Phase 1 or Phase 2 | Medium | Add `cargo test --workspace` to both phases' mandatory validation |
| 3 | `.gitattributes` commit strategy unspecified | Low-Medium | Explicitly amend into existing smoke commit; keep PR C at 1 commit |
| 4 | PR bodies not updated after SHAs change | Low | Add `gh pr edit` or manual body update step after each phase's push |
| 5 | Parity investigation has no actionable outcome | Low | Drive toward matching CI's toolchain locally before Phase 1 validation |
