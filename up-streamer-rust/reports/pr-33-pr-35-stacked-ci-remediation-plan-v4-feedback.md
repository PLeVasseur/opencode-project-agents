# Plan v4: PR #33/#34/#35 Stacked CI Remediation

Date: 2026-02-14
Repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Fork repo: `PLeVasseur/up-streamer-rust`
Feedback lineage: v2 feedback → v3 plan → v3 feedback → this document

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
- [ ] Establish build environment prerequisites
  - [ ] Confirm `source build/envsetup.sh highest` is available and run it before any cargo commands in all subsequent phases.
  - [ ] Check if `VSOMEIP_INSTALL_PATH` points to a valid install tree.
  - [ ] If `VSOMEIP_INSTALL_PATH` is unset or invalid, record skip rationale for unbundled clippy variant in remediation notes. Bundled variant (which compiles vsomeip from source) remains mandatory.

## Phase 1: Fix PR A by Amending c2 (No New 5th Commit)

- [ ] Switch to PR A and rewrite history at commit granularity
  - [ ] `git switch cleanup/refactor-upstream-main-prA-architecture`
  - [ ] `git fetch --all --prune`
  - [ ] `source build/envsetup.sh highest`
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
  - [ ] If `VSOMEIP_INSTALL_PATH` is valid: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If `VSOMEIP_INSTALL_PATH` is unset/invalid: skip unbundled variant and record skip in remediation notes.
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
- [ ] Resolve API drift in benchmark code (required, not conditional)
  - [ ] Update `up-streamer/src/benchmark_support.rs` callsites at lines 126 and 158: replace `lookup_route_subscribers(...)` with `lookup_route_subscribers_with_version(...).await.1`.
  - [ ] Confirm no non-benchmark scope drift enters PR B.
  - [ ] `git add -u && git commit --amend --no-edit`
  - [ ] Verify PR B remains 1 commit ahead of PR A (`git log --oneline cleanup/refactor-upstream-main-prA-architecture..HEAD`).
- [ ] Mandatory validation for PR B
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`
  - [ ] `cargo check -p up-streamer --benches`
  - [ ] `cargo test --workspace`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If `VSOMEIP_INSTALL_PATH` is valid: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If `VSOMEIP_INSTALL_PATH` is unset/invalid: skip unbundled variant and record skip in remediation notes.
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
  - [ ] Amend these rules into existing smoke commit (`git add .gitattributes && git commit --amend --no-edit`).
  - [ ] Verify PR C remains one commit ahead of PR A (`git log --oneline cleanup/refactor-upstream-main-prA-architecture..HEAD`).
- [ ] Mandatory validation for PR C
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`
  - [ ] `cargo test --workspace`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If `VSOMEIP_INSTALL_PATH` is valid: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] If `VSOMEIP_INSTALL_PATH` is unset/invalid: skip unbundled variant and record skip in remediation notes.
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
- [ ] All prior review issues are closed.
  - [ ] v2 Issue 1 closed: c2 amended in place; no 5th fixup commit in PR A.
  - [ ] v2 Issue 2 closed: `cargo test --workspace` in mandatory validation for Phases 1, 2, and 3.
  - [ ] v2 Issue 3 closed: `.gitattributes` amended into PR C smoke commit (single-commit PR C preserved).
  - [ ] v2 Issue 4 closed: PR A/B/C bodies updated for new SHAs and validation notes.
  - [ ] v2 Issue 5 closed: local/CI parity made actionable and enforced before validation.
  - [ ] v3 Issue 1 closed: PR B amend step explicit; API drift fix is mandatory, not conditional.
  - [ ] v3 Issue 2 closed: unbundled clippy variant gated on `VSOMEIP_INSTALL_PATH` validity with skip-and-record pattern.
  - [ ] v3 Issue 3 closed: `source build/envsetup.sh highest` included before cargo commands in all phases.
