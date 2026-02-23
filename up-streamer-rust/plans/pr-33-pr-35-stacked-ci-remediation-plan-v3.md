# Plan v3: PR #33/#34/#35 Stacked CI Remediation

Date: 2026-02-14
Repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Fork repo: `PLeVasseur/up-streamer-rust`
Primary feedback source: `reports/pr-33-35-remediation-v3-feedback.md`

## Objectives

- [ ] Restore green CI for the stacked set without reintroducing sequencing debt.
  - [ ] PR A (`#33`) passes bundled + unbundled workflows.
  - [ ] PR B (`#34`) remains green after restack.
  - [ ] PR C (`#35`) passes bundled + unbundled workflows.
- [ ] Preserve intended stack boundaries.
  - [ ] PR A remains a 4-commit stack (c0..c3).
  - [ ] PR B remains a 1-commit benchmark delta on top of PR A.
  - [ ] PR C remains a 1-commit smoke delta on top of PR A.

## Non-Negotiable Invariants

- [ ] Branch safety and publishing policy
  - [ ] Push to `origin` only (never `upstream`).
  - [ ] Use `--force-with-lease` for rewritten branch updates.
  - [ ] Keep backup refs/tags before any history rewrite.
- [ ] Scope safety
  - [ ] Root-cause fix is authored in c2 (not as a new top commit).
  - [ ] No broad lint suppression (`#[allow(dead_code)]`) unless explicitly required after failed source fix attempt.
  - [ ] `.gitattributes` rules are amended into PR C smoke commit (no separate housekeeping commit).

## Phase 0: Evidence and Parity Gate (Blocker)

- [ ] Capture current state and prepare rollback points
  - [ ] Record tips of `cleanup/refactor-upstream-main-prA-architecture`, `cleanup/refactor-upstream-main-prB-benchmark`, `cleanup/refactor-upstream-main-prC-smoke`.
  - [ ] Create backup refs for all three branches before mutation.
  - [ ] Confirm clean local worktree.
- [ ] Confirm failure set from real CI logs
  - [ ] Pull failed logs for PR A bundled + unbundled runs.
  - [ ] Pull failed logs for PR C bundled + unbundled runs.
  - [ ] Confirm first actionable error is `dead_code` on `lookup_route_subscribers`.
  - [ ] Confirm no secondary `-D warnings` violations are present.
- [ ] Make local vs CI parity actionable
  - [ ] Capture CI `rustc`, `cargo`, and `clippy` versions from workflow logs.
  - [ ] Capture local `rustc`, `cargo`, and `clippy` versions.
  - [ ] If mismatched, align local toolchain to CI (`rustup override set <ci-version>`) before Phase 1 validation.
  - [ ] Record parity decision and exact local command matrix used for reproduction.

## Phase 1: Fix PR A by Amending c2 (No New 5th Commit)

- [ ] Switch to PR A and rewrite history at commit granularity
  - [ ] `git switch cleanup/refactor-upstream-main-prA-architecture`
  - [ ] `git fetch --all --prune`
  - [ ] Start interactive rebase from c0 parent (`git rebase -i fb49056^`).
  - [ ] Mark c2 (`cbef885`) as `edit`.
- [ ] Apply root-cause fix in c2 scope
  - [ ] In `up-streamer/src/routing/subscription_directory.rs`, remove `lookup_route_subscribers`.
  - [ ] Update test callsite to `lookup_route_subscribers_with_version("authority-b").await.1`.
  - [ ] Verify no stale references to removed symbol remain.
  - [ ] `git add -u && git commit --amend --no-edit` at c2 stop.
  - [ ] Continue rebase and replay c3 cleanly.
- [ ] Confirm PR A shape after rewrite
  - [ ] Verify PR A is still 4 commits from base (`git log --oneline origin/main..HEAD`).
  - [ ] Verify no scope drift outside intended c2 fix.
- [ ] Mandatory validation (CI-parity + tests)
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo test --workspace`
- [ ] Publish PR A and refresh PR text
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prA-architecture`
  - [ ] Update PR A body with new c2/c3 SHAs.
  - [ ] Add note that dead-code fix was amended into c2 to preserve 4-commit boundary.
  - [ ] Refresh validation section with remediation run results.

## Phase 2: Rebase PR B onto Updated PR A

- [ ] Restack PR B
  - [ ] `git switch cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
  - [ ] Resolve API drift in benchmark code only.
  - [ ] Update `up-streamer/src/benchmark_support.rs` callsites to `lookup_route_subscribers_with_version(...).await.1` if needed.
- [ ] Mandatory validation for PR B
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`
  - [ ] `cargo check -p up-streamer --benches`
  - [ ] `cargo test --workspace`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Publish PR B and refresh PR text
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] Update PR B body SHA references if commit hash changed after rebase.

## Phase 3: Rebase PR C onto Updated PR A and Close R5

- [ ] Restack PR C
  - [ ] `git switch cleanup/refactor-upstream-main-prC-smoke`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
  - [ ] Resolve conflicts without pulling benchmark-only files.
- [ ] Close R5 with explicit commit strategy
  - [ ] Add `.gitattributes` rule: `utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true`
  - [ ] Add `.gitattributes` rule: `utils/transport-smoke-suite/claims/** linguist-generated=true`
  - [ ] Amend these rules into existing smoke commit (`git commit --amend --no-edit`).
  - [ ] Verify PR C remains one commit ahead of PR A.
- [ ] Mandatory validation for PR C
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`
  - [ ] `cargo test --workspace`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Publish PR C and refresh PR text
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prC-smoke`
  - [ ] Update PR C SHA note to new hash.
  - [ ] Add explicit R5 closure note in PR C body.

## Phase 4: CI Verification and Fail-Fast Loop

- [ ] Verify all PR checks
  - [ ] `gh pr checks 33 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 34 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 35 --repo PLeVasseur/up-streamer-rust`
- [ ] Verify stack topology still correct
  - [ ] PR A base is `main`.
  - [ ] PR B base is PR A branch.
  - [ ] PR C base is PR A branch.
  - [ ] PR B remains benchmark-only delta.
  - [ ] PR C remains smoke-only delta plus `.gitattributes` closure.
- [ ] If any check fails, iterate safely
  - [ ] Capture failing run/job and first actionable error.
  - [ ] Apply smallest fix at lowest affected branch in stack.
  - [ ] Rebase descendants and republish with `--force-with-lease`.

## Completion Criteria

- [ ] All three PRs are green.
  - [ ] PR A green.
  - [ ] PR B green.
  - [ ] PR C green.
- [ ] All v3 review issues are closed.
  - [ ] Issue 1 closed: c2 amended in place; no 5th fixup commit in PR A.
  - [ ] Issue 2 closed: `cargo test --workspace` added to mandatory validation in Phase 1 and Phase 2.
  - [ ] Issue 3 closed: `.gitattributes` amended into PR C smoke commit (single-commit PR C preserved).
  - [ ] Issue 4 closed: PR A/B/C bodies updated for new SHAs and validation notes.
  - [ ] Issue 5 closed: local/CI parity made actionable and enforced before validation.
