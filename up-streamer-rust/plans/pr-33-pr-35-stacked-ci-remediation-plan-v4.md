# Plan v4: PR #33/#34/#35 Stacked CI Remediation

Date: 2026-02-14
Repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Fork repo: `PLeVasseur/up-streamer-rust`
Feedback sources:
- `reports/pr-33-35-remediation-v3-feedback.md`
- `reports/pr-33-pr-35-stacked-ci-remediation-plan-v4-feedback.md`

## Objectives

- [ ] Restore green CI for the stacked PR set without reintroducing sequencing debt.
  - [ ] PR A (`#33`) passes required bundled/unbundled workflows.
  - [ ] PR B (`#34`) remains green after restack.
  - [ ] PR C (`#35`) passes required bundled/unbundled workflows.
- [ ] Preserve stack boundaries and reviewer ergonomics.
  - [ ] PR A remains exactly 4 commits (`c0..c3`).
  - [ ] PR B remains exactly 1 benchmark commit on top of PR A.
  - [ ] PR C remains exactly 1 smoke commit on top of PR A.
  - [ ] R5 is closed in PR C via `.gitattributes` fixture collapsing rules.

## Non-Negotiable Invariants

- [ ] Branch and publish safety
  - [ ] Push to `origin` only (never `upstream`).
  - [ ] Use `--force-with-lease` for all rewritten branch updates.
  - [ ] Create backup refs before each history rewrite.
- [ ] Scope safety
  - [ ] Root-cause fix is authored in c2 (no appended fifth fixup commit in PR A).
  - [ ] No broad lint suppression (`#[allow(dead_code)]`) unless source fix is proven unworkable.
  - [ ] `.gitattributes` lands by amending the existing PR C smoke commit (no extra housekeeping commit).
- [ ] Environment parity safety
  - [ ] Run `source build/envsetup.sh highest` before cargo commands in each phase.
  - [ ] Treat unbundled clippy as conditional on valid `VSOMEIP_INSTALL_PATH`.

## Phase 0: Evidence, Parity, and Environment Gate (Blocking)

- [ ] Capture current state and rollback anchors
  - [ ] Record tips of `cleanup/refactor-upstream-main-prA-architecture`, `cleanup/refactor-upstream-main-prB-benchmark`, and `cleanup/refactor-upstream-main-prC-smoke`.
  - [ ] Create backup refs/tags for all three branch tips.
  - [ ] Confirm local worktree is clean.
- [ ] Confirm true CI failure set from logs
  - [ ] Pull failed logs for PR A bundled + unbundled runs.
  - [ ] Pull failed logs for PR C bundled + unbundled runs.
  - [ ] Confirm first actionable failure is `dead_code` on `lookup_route_subscribers`.
  - [ ] Confirm no additional `-D warnings` violations are present after that failure.
- [ ] Make local/CI parity actionable
  - [ ] Record CI `rustc`, `cargo`, `clippy` versions from job logs.
  - [ ] Record local `rustc`, `cargo`, `clippy` versions.
  - [ ] If versions differ, align local toolchain to CI before Phase 1 validation.
  - [ ] Record parity decision and exact command matrix in remediation notes.
- [ ] Establish build environment prerequisites
  - [ ] Run `source build/envsetup.sh highest`.
  - [ ] Check whether `VSOMEIP_INSTALL_PATH` exists and points to a valid install tree.
  - [ ] If valid, mark unbundled clippy as mandatory.
  - [ ] If invalid/unset, mark unbundled clippy as skipped-with-rationale and record evidence.

## Phase 1: Fix PR A by Rewriting c2 In Place (No New Commit)

- [ ] Switch to PR A and prepare non-interactive rewrite flow
  - [ ] `git switch cleanup/refactor-upstream-main-prA-architecture`
  - [ ] `git fetch --all --prune`
  - [ ] Identify c0/c1/c2/c3 SHAs on PR A tip.
  - [ ] Create a temporary rewrite branch from c1 SHA.
- [ ] Recreate c2 with root-cause fix
  - [ ] Cherry-pick c2 onto the temporary branch.
  - [ ] In `up-streamer/src/routing/subscription_directory.rs`, remove `lookup_route_subscribers`.
  - [ ] Update test callsite to `lookup_route_subscribers_with_version("authority-b").await.1`.
  - [ ] Verify no stale references to removed symbol remain.
  - [ ] Amend the cherry-picked c2 commit (`git add -u && git commit --amend --no-edit`).
- [ ] Reapply c3 and verify PR A shape
  - [ ] Cherry-pick c3 onto rewritten c2.
  - [ ] Force-move PR A branch to rewritten tip.
  - [ ] Verify PR A remains exactly 4 commits from base.
  - [ ] Verify no scope drift beyond intended c2 dead-code remediation.
- [ ] Mandatory validation for PR A (CI-parity + tests)
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If unbundled is enabled: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If unbundled is disabled: record skip rationale in remediation notes.
  - [ ] `cargo test --workspace`
- [ ] Publish PR A and refresh PR metadata
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prA-architecture`
  - [ ] Update PR A body with new c2/c3 SHAs.
  - [ ] Note that dead-code fix was amended into c2 to preserve commit boundary quality.
  - [ ] Update validation section with remediation run results and any unbundled skip rationale.

## Phase 2: Rebase PR B onto Updated PR A

- [ ] Restack PR B
  - [ ] `git switch cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
- [ ] Mandatory API drift fix in benchmark scope
  - [ ] In `up-streamer/src/benchmark_support.rs`, replace callsites at lines 126 and 158:
    - [ ] `lookup_route_subscribers(...)`
    - [ ] with `lookup_route_subscribers_with_version(...).await.1`
  - [ ] Amend PR B commit (`git add -u && git commit --amend --no-edit`).
  - [ ] Verify no non-benchmark scope drift.
  - [ ] Verify PR B remains exactly 1 commit ahead of PR A.
- [ ] Mandatory validation for PR B
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`
  - [ ] `cargo check -p up-streamer --benches`
  - [ ] `cargo test --workspace`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If unbundled is enabled: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If unbundled is disabled: record skip rationale in remediation notes.
- [ ] Publish PR B and refresh PR metadata
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] Update PR B body SHA references if commit hash changed.

## Phase 3: Rebase PR C onto Updated PR A and Close R5

- [ ] Restack PR C
  - [ ] `git switch cleanup/refactor-upstream-main-prC-smoke`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
  - [ ] Resolve conflicts without introducing benchmark-only files.
- [ ] Close R5 by amending smoke commit
  - [ ] Add `.gitattributes` line: `utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true`
  - [ ] Add `.gitattributes` line: `utils/transport-smoke-suite/claims/** linguist-generated=true`
  - [ ] Amend existing smoke commit (`git add .gitattributes && git commit --amend --no-edit`).
  - [ ] Verify PR C remains exactly 1 commit ahead of PR A.
- [ ] Mandatory validation for PR C
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`
  - [ ] `cargo test --workspace`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If unbundled is enabled: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If unbundled is disabled: record skip rationale in remediation notes.
- [ ] Publish PR C and refresh PR metadata
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prC-smoke`
  - [ ] Update PR C SHA note with new commit hash.
  - [ ] Add explicit R5 closure note in PR C body.

## Phase 4: CI Verification and Fail-Fast Loop

- [ ] Verify PR checks
  - [ ] `gh pr checks 33 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 34 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 35 --repo PLeVasseur/up-streamer-rust`
- [ ] Verify stack topology and scope remain correct
  - [ ] PR A base is `main`.
  - [ ] PR B base is PR A branch.
  - [ ] PR C base is PR A branch.
  - [ ] PR B delta is benchmark-only.
  - [ ] PR C delta is smoke + `.gitattributes` R5 closure only.
- [ ] If any check fails, iterate from lowest affected branch
  - [ ] Capture failing run/job and first actionable error.
  - [ ] Apply smallest fix in the lowest branch where root cause exists.
  - [ ] Rebase descendants and republish with `--force-with-lease`.

## Completion Criteria

- [ ] All three PRs are green.
  - [ ] PR A green.
  - [ ] PR B green.
  - [ ] PR C green.
- [ ] Prior review issues are explicitly closed.
  - [ ] v2 Issue 1: c2 fixed in place; no fifth fixup commit on PR A.
  - [ ] v2 Issue 2: `cargo test --workspace` mandatory in relevant phases.
  - [ ] v2 Issue 3: `.gitattributes` amended into PR C smoke commit.
  - [ ] v2 Issue 4: PR bodies updated for SHA and validation drift.
  - [ ] v2 Issue 5: local/CI parity made actionable before validation.
  - [ ] v3 Issue 1: PR B API drift fix explicit and mandatory.
  - [ ] v3 Issue 2: unbundled clippy gated by `VSOMEIP_INSTALL_PATH` validity and documented skip behavior.
  - [ ] v3 Issue 3: `source build/envsetup.sh highest` included before cargo commands in all phases.
