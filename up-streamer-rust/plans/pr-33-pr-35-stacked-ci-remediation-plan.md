# Plan: Remediate Stacked CI Failures (PR A + PR C)

Date: 2026-02-14
Repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Fork repo: `PLeVasseur/up-streamer-rust`

## Context

- [ ] Confirm failing PRs and root error
  - [ ] PR A: `https://github.com/PLeVasseur/up-streamer-rust/pull/33`
  - [ ] PR C: `https://github.com/PLeVasseur/up-streamer-rust/pull/35`
  - [ ] PR B currently green: `https://github.com/PLeVasseur/up-streamer-rust/pull/34`
  - [ ] First actionable error in all failing runs is `dead_code` for `lookup_route_subscribers` in `up-streamer/src/routing/subscription_directory.rs`

## Stacking Constraints (Must Hold)

- [ ] Preserve stacked topology while fixing
  - [ ] PR A remains base (`main` -> PR A)
  - [ ] PR B remains stacked on PR A and contains benchmark-only delta
  - [ ] PR C remains stacked on PR A and contains smoke-only delta
- [ ] Do not push to upstream
  - [ ] Push only to `origin` fork branches
  - [ ] Use `--force-with-lease` for rebased branch updates
- [ ] Keep fix narrow and lint-clean
  - [ ] Prefer source fix over `#[allow(dead_code)]`
  - [ ] Only use suppression as fallback if source-level fix proves unsafe

## Phase 0 - Baseline + Safety

- [ ] Capture current branch and SHA baseline
  - [ ] Record current tips of `cleanup/refactor-upstream-main-prA-architecture`, `cleanup/refactor-upstream-main-prB-benchmark`, `cleanup/refactor-upstream-main-prC-smoke`
  - [ ] Record current failing run IDs for PR A and PR C in remediation notes
- [ ] Ensure clean local worktree before mutation
  - [ ] `git status --short --branch` is clean on active branch
  - [ ] `git fetch --all --prune` completed

## Phase 1 - Fix Root Cause in PR A (Base)

- [ ] Switch to PR A branch
  - [ ] `git switch cleanup/refactor-upstream-main-prA-architecture`
- [ ] Apply minimal source-level fix for dead code
  - [ ] Remove `lookup_route_subscribers` from `up-streamer/src/routing/subscription_directory.rs`
  - [ ] Update local test callsites in `up-streamer/src/routing/subscription_directory.rs` to use `lookup_route_subscribers_with_version(...).await.1`
  - [ ] Verify no behavior change beyond API cleanup
- [ ] Validate PR A locally against failing CI dimensions
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Commit and push PR A fix
  - [ ] Create a narrow commit message focused on dead-code lint remediation
  - [ ] `git push origin cleanup/refactor-upstream-main-prA-architecture`

## Phase 2 - Restack PR B on Updated PR A

- [ ] Switch to PR B branch and rebase
  - [ ] `git switch cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
- [ ] Resolve API drift introduced by PR A fix
  - [ ] Update benchmark callsites in `up-streamer/src/benchmark_support.rs`
  - [ ] Replace removed API usage with `lookup_route_subscribers_with_version(...).await.1`
- [ ] Validate PR B local scope
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`
  - [ ] `cargo check -p up-streamer --benches`
  - [ ] Optional confidence pass: `cargo clippy --all-targets -- -W warnings -D warnings`
- [ ] Push PR B update
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prB-benchmark`

## Phase 3 - Restack PR C on Updated PR A

- [ ] Switch to PR C branch and rebase
  - [ ] `git switch cleanup/refactor-upstream-main-prC-smoke`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
- [ ] Resolve any rebase conflicts without widening PR C scope
  - [ ] Keep smoke-suite intent intact
  - [ ] Avoid introducing benchmark changes into PR C
- [ ] Validate PR C local scope
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Push PR C update
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prC-smoke`

## Phase 4 - CI Verification + Closeout

- [ ] Verify GitHub checks on all three PRs
  - [ ] `gh pr checks 33 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 34 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 35 --repo PLeVasseur/up-streamer-rust`
- [ ] If any check fails, triage and iterate from first actionable failing job
  - [ ] Capture failing workflow/job/run-id
  - [ ] Capture first actionable error line
  - [ ] Apply smallest stack-safe fix at the correct base branch

## Completion Criteria

- [ ] PR A lint failures are resolved in bundled + unbundled workflows
- [ ] PR C lint failures are resolved in bundled + unbundled workflows
- [ ] PR B remains green after rebase
- [ ] Stack order and branch ownership are preserved (`A` base; `B` and `C` stacked on `A`)
- [ ] No upstream pushes and no force pushes without lease
