# Plan v5: PR #33/#34/#35 Stacked CI Remediation

Date: 2026-02-14
Repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Fork repo: `PLeVasseur/up-streamer-rust`
Feedback sources:
- `reports/pr-33-35-remediation-v3-feedback.md`
- `reports/pr-33-pr-35-stacked-ci-remediation-plan-v4-feedback.md`
- final reviewer note on c3 cherry-pick conflict fallback handling

## Objectives

- [x] Restore green CI for the stacked PR set without reintroducing sequencing debt.
  - [x] PR A (`#33`) passes required bundled/unbundled workflows.
  - [x] PR B (`#34`) remains green after restack.
  - [x] PR C (`#35`) passes required bundled/unbundled workflows.
- [x] Preserve stack boundaries and reviewer ergonomics.
  - [x] PR A remains exactly 4 commits (`c0..c3`).
  - [x] PR B remains exactly 1 benchmark commit on top of PR A.
  - [x] PR C remains exactly 1 smoke commit on top of PR B.
  - [x] R5 is closed in PR C via `.gitattributes` fixture collapsing rules.

## Non-Negotiable Invariants

- [x] Branch and publish safety
  - [x] Push to `origin` only (never `upstream`).
  - [x] Use `--force-with-lease` for all rewritten branch updates.
  - [x] Create backup refs before each history rewrite.
- [x] Scope safety
  - [x] Root-cause fix is authored in c2 (no appended fifth fixup commit in PR A).
  - [x] No broad lint suppression (`#[allow(dead_code)]`) unless source fix is proven unworkable.
  - [x] `.gitattributes` lands by amending the existing PR C smoke commit (no extra housekeeping commit).
- [x] Conflict-scope firewall
  - [x] During replay/conflict resolution, keep edits inside the commit being replayed.
  - [x] If c3 replay conflicts, resolve within c3 test/helper scope only; do not widen c2 amendment scope. (N/A: no c3 conflicts)
- [x] Environment parity safety
  - [x] Run `source build/envsetup.sh highest` before cargo commands in each phase.
  - [x] Treat unbundled clippy as conditional on valid `VSOMEIP_INSTALL_PATH`.

## Phase 0: Evidence, Parity, and Environment Gate (Blocking)

- [x] Capture current state and rollback anchors
  - [x] Record tips of `cleanup/refactor-upstream-main-prA-architecture`, `cleanup/refactor-upstream-main-prB-benchmark`, and `cleanup/refactor-upstream-main-prC-smoke`.
  - [x] Create backup refs/tags for all three branch tips.
  - [x] Confirm local worktree is clean.
- [x] Confirm true CI failure set from logs
  - [x] Pull failed logs for PR A bundled + unbundled runs.
  - [x] Pull failed logs for PR C bundled + unbundled runs.
  - [x] Confirm first actionable failure is `dead_code` on `lookup_route_subscribers`.
  - [x] Confirm no additional `-D warnings` violations are present after that failure.
- [x] Make local/CI parity actionable
  - [x] Record CI `rustc`, `cargo`, `clippy` versions from job logs.
  - [x] Record local `rustc`, `cargo`, `clippy` versions.
  - [x] If versions differ, align local toolchain to CI before Phase 1 validation.
  - [x] Record parity decision and exact command matrix in remediation notes.
- [x] Establish build environment prerequisites
  - [x] Run `source build/envsetup.sh highest`.
  - [x] Check whether `VSOMEIP_INSTALL_PATH` exists and points to a valid install tree.
  - [x] If valid, mark unbundled clippy as mandatory. (N/A: local `VSOMEIP_INSTALL_PATH` invalid)
  - [x] If invalid/unset, mark unbundled clippy as skipped-with-rationale and record evidence.

## Phase 1: Fix PR A by Rewriting c2 In Place (No New Commit)

- [x] Switch to PR A and prepare non-interactive rewrite flow
  - [x] `git switch cleanup/refactor-upstream-main-prA-architecture`
  - [x] `git fetch --all --prune`
  - [x] Identify c0/c1/c2/c3 SHAs on PR A tip. (`fb49056ff0c05ebcc15bdfd5b48aa00e84b7d40d`, `cd436ae08fd752dcbc778a5e0968b4275cf0f7d1`, `cbef88502769269471e8ad7bcca6716dd24109a2`, `75610d579355f5e56a997abb3ec1b8ea7e30d721`)
  - [x] Create a temporary rewrite branch from c1 SHA.
- [x] Recreate c2 with root-cause fix
  - [x] Cherry-pick c2 onto the temporary branch.
  - [x] In `up-streamer/src/routing/subscription_directory.rs`, remove `lookup_route_subscribers`.
  - [x] Update test callsite to `lookup_route_subscribers_with_version("authority-b").await.1`.
  - [x] Verify no stale references to removed symbol remain.
  - [x] Amend the cherry-picked c2 commit (`git add -u && git commit --amend --no-edit`).
  - [x] Create a post-c2 checkpoint tag/ref before replaying c3.
- [x] Reapply c3 and verify PR A shape
  - [x] Cherry-pick c3 onto rewritten c2.
  - [x] If c3 cherry-pick conflicts, resolve within c3 test/helper scope only; do not widen c2's amendment. (N/A: no c3 conflicts)
  - [x] If conflict resolution appears to require c2-owned production files, abort c3 replay, reset to post-c2 checkpoint, and retry c3 without widening c2 scope. (N/A: no c3 conflicts)
  - [x] After conflict resolution, verify changed files remain in c3-intended scope.
  - [x] Force-move PR A branch to rewritten tip.
  - [x] Verify PR A remains exactly 4 commits from base.
  - [x] Verify no scope drift beyond intended c2 dead-code remediation.
- [x] Mandatory validation for PR A (CI-parity + tests)
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] If unbundled is enabled: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (N/A: unbundled disabled locally)
  - [x] If unbundled is disabled: record skip rationale in remediation notes.
  - [x] `cargo test --workspace`
- [x] Publish PR A and refresh PR metadata
  - [x] `git push --force-with-lease origin cleanup/refactor-upstream-main-prA-architecture`
  - [x] Update PR A body with new c2/c3 SHAs.
  - [x] Note that dead-code fix was amended into c2 to preserve commit boundary quality.
  - [x] If c3 replay conflicted, document that resolution stayed within c3 scope. (N/A: no c3 conflict)
  - [x] Update validation section with remediation run results and any unbundled skip rationale.

## Phase 2: Rebase PR B onto Updated PR A

- [x] Restack PR B
  - [x] `git switch cleanup/refactor-upstream-main-prB-benchmark`
  - [x] `git rebase cleanup/refactor-upstream-main-prA-architecture`
- [x] Mandatory API drift fix in benchmark scope
  - [x] In `up-streamer/src/benchmark_support.rs`, replace callsites at lines 126 and 158:
    - [x] `lookup_route_subscribers(...)`
    - [x] with `lookup_route_subscribers_with_version(...).await.1`
  - [x] Amend PR B commit (`git add -u && git commit --amend --no-edit`).
  - [x] Verify no non-benchmark scope drift.
  - [x] Verify PR B remains exactly 1 commit ahead of PR A.
- [x] Mandatory validation for PR B
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo check -p criterion-guardrail --all-targets`
  - [x] `cargo test -p criterion-guardrail --all-targets`
  - [x] `cargo check -p up-streamer --benches`
  - [x] `cargo test --workspace`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] If unbundled is enabled: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (N/A: unbundled disabled locally)
  - [x] If unbundled is disabled: record skip rationale in remediation notes.
- [x] Publish PR B and refresh PR metadata
  - [x] `git push --force-with-lease origin cleanup/refactor-upstream-main-prB-benchmark`
  - [x] Update PR B body SHA references if commit hash changed.

## Phase 3: Rebase PR C onto Updated PR B and Close R5

- [x] Restack PR C
  - [x] `git switch cleanup/refactor-upstream-main-prC-smoke`
  - [x] `git rebase cleanup/refactor-upstream-main-prB-benchmark`
  - [x] Resolve conflicts without introducing benchmark-only files.
- [x] Close R5 by amending smoke commit
  - [x] Add `.gitattributes` line: `utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true`
  - [x] Add `.gitattributes` line: `utils/transport-smoke-suite/claims/** linguist-generated=true`
  - [x] Amend existing smoke commit (`git add .gitattributes && git commit --amend --no-edit`).
  - [x] Verify PR C remains exactly 1 commit ahead of PR B.
- [x] Mandatory validation for PR C
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo check -p transport-smoke-suite --all-targets`
  - [x] `cargo test -p transport-smoke-suite --tests`
  - [x] `cargo test --workspace`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] If unbundled is enabled: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (N/A: unbundled disabled locally)
  - [x] If unbundled is disabled: record skip rationale in remediation notes.
- [x] Publish PR C and refresh PR metadata
  - [x] `git push --force-with-lease origin cleanup/refactor-upstream-main-prC-smoke`
  - [x] Update PR C SHA note with new commit hash.
  - [x] Add explicit R5 closure note in PR C body.

## Phase 4: CI Verification and Fail-Fast Loop

- [x] Verify PR checks
  - [x] `gh pr checks 33 --repo PLeVasseur/up-streamer-rust`
  - [x] `gh pr checks 34 --repo PLeVasseur/up-streamer-rust`
  - [x] `gh pr checks 35 --repo PLeVasseur/up-streamer-rust`
- [x] Verify stack topology and scope remain correct
  - [x] PR A base is `main`.
  - [x] PR B base is PR A branch.
  - [x] PR C base is PR B branch.
  - [x] PR B delta is benchmark-only.
  - [x] PR C delta is smoke + `.gitattributes` R5 closure only.
- [x] If any check fails, iterate from lowest affected branch. (N/A: all checks passed)
  - [x] Capture failing run/job and first actionable error. (N/A)
  - [x] Apply smallest fix in the lowest branch where root cause exists. (N/A)
  - [x] Rebase descendants and republish with `--force-with-lease`. (N/A)

## Completion Criteria

- [x] All three PRs are green.
  - [x] PR A green.
  - [x] PR B green.
  - [x] PR C green.
- [x] Prior review issues are explicitly closed.
  - [x] v2 Issue 1: c2 fixed in place; no fifth fixup commit on PR A.
  - [x] v2 Issue 2: `cargo test --workspace` mandatory in relevant phases.
  - [x] v2 Issue 3: `.gitattributes` amended into PR C smoke commit.
  - [x] v2 Issue 4: PR bodies updated for SHA and validation drift.
  - [x] v2 Issue 5: local/CI parity made actionable before validation.
  - [x] v3 Issue 1: PR B API drift fix explicit and mandatory.
  - [x] v3 Issue 2: unbundled clippy gated by `VSOMEIP_INSTALL_PATH` validity and documented skip behavior.
  - [x] v3 Issue 3: `source build/envsetup.sh highest` included before cargo commands in all phases.
  - [x] final observation closed: explicit c3 cherry-pick conflict fallback preserves c2 boundary purity.
