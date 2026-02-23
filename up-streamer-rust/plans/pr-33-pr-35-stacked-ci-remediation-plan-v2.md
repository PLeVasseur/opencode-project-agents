# Plan v2: PR #33/#34/#35 Stacked CI Remediation

Date: 2026-02-14
Repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Fork repo: `PLeVasseur/up-streamer-rust`

## Goal

- [ ] Restore green CI for PR A and PR C without breaking stack topology or widening review scope.
  - [ ] PR A (`#33`) passes bundled + unbundled lint/test workflows.
  - [ ] PR B (`#34`) remains green after restack.
  - [ ] PR C (`#35`) passes bundled + unbundled lint/test workflows.
  - [ ] Stacked bases remain `A` as base, `B` and `C` stacked on `A`.

## Explicit Open-Issue Closure (from feedback review)

- [ ] Gap 1: verify `dead_code` is the only failure before mutating branches.
  - [ ] Pull failed-job logs for each failing run on PR A and PR C.
  - [ ] Confirm first actionable error is `lookup_route_subscribers` dead code.
  - [ ] Confirm no secondary `-D warnings` violations are present.
- [ ] Gap 2: make PR B validation strict enough for CI parity.
  - [ ] Promote full clippy matrix from optional to mandatory on PR B.
- [ ] Gap 3: close missing R5 deliverable.
  - [ ] Add `.gitattributes` fixture rules in PR C before push.
- [ ] Gap 4: investigate local-vs-CI clippy mismatch.
  - [ ] Record CI toolchain versions and local toolchain versions.
  - [ ] Document parity guidance used for this run.
- [ ] Gap 5: guard against secondary dead code after API cleanup.
  - [ ] Run full clippy matrix after PR A fix and before push.

## Non-Negotiable Invariants

- [ ] Branch/publish safety
  - [ ] Push to `origin` only (never `upstream`).
  - [ ] Use `--force-with-lease` for rebased updates.
  - [ ] Do not rewrite unrelated branches.
- [ ] Stack integrity
  - [ ] Apply root-cause fix on PR A first.
  - [ ] Rebase PR B onto updated PR A.
  - [ ] Rebase PR C onto updated PR A.
- [ ] Scope discipline
  - [ ] Keep PR A fix minimal and source-based (no lint suppression by default).
  - [ ] Keep PR B benchmark-only.
  - [ ] Keep PR C smoke-scope plus `.gitattributes` R5 closure only.

## Phase 0: Evidence + Parity Preflight (Gate)

- [ ] Capture current stack state
  - [ ] `gh pr checks 33 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 34 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 35 --repo PLeVasseur/up-streamer-rust`
  - [ ] Record branch tips for `cleanup/refactor-upstream-main-prA-architecture`, `cleanup/refactor-upstream-main-prB-benchmark`, `cleanup/refactor-upstream-main-prC-smoke`.
- [ ] Pull failed logs and confirm failure set
  - [ ] Fetch failed logs for PR A bundled + unbundled runs.
  - [ ] Fetch failed logs for PR C bundled + unbundled runs.
  - [ ] Confirm only actionable failure is dead code on `lookup_route_subscribers`.
- [ ] Establish local/CI parity reference
  - [ ] Record CI `rustc`/`cargo`/`clippy` versions from workflow/job output.
  - [ ] Record local `rustc`/`cargo`/`clippy` versions.
  - [ ] Record exact local command set used to mirror CI.

## Phase 1: Fix PR A Root Cause

- [ ] Update PR A branch
  - [ ] `git switch cleanup/refactor-upstream-main-prA-architecture`
  - [ ] `git fetch --all --prune`
  - [ ] Ensure worktree is clean before edit.
- [ ] Apply minimal source fix
  - [ ] Remove `lookup_route_subscribers` from `up-streamer/src/routing/subscription_directory.rs`.
  - [ ] Update test/call sites to use `lookup_route_subscribers_with_version(...).await.1`.
  - [ ] Confirm no behavior change beyond API cleanup.
  - [ ] Confirm no stale references to removed symbol remain.
- [ ] Mandatory PR A validation (CI-parity)
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Publish PR A update
  - [ ] Commit with narrow dead-code remediation scope.
  - [ ] `git push origin cleanup/refactor-upstream-main-prA-architecture`

## Phase 2: Rebase and Validate PR B (Mandatory Full Clippy)

- [ ] Restack PR B on updated PR A
  - [ ] `git switch cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
- [ ] Resolve API drift in benchmark scope only
  - [ ] Update `up-streamer/src/benchmark_support.rs` callsites to `lookup_route_subscribers_with_version(...).await.1`.
  - [ ] Confirm no non-benchmark scope drift enters PR B.
- [ ] PR B validation
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`
  - [ ] `cargo check -p up-streamer --benches`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Publish PR B update
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prB-benchmark`

## Phase 3: Rebase and Validate PR C + Close R5

- [ ] Restack PR C on updated PR A
  - [ ] `git switch cleanup/refactor-upstream-main-prC-smoke`
  - [ ] `git rebase cleanup/refactor-upstream-main-prA-architecture`
- [ ] Close R5 in PR C
  - [ ] Add `.gitattributes` rule: `utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true`
  - [ ] Add `.gitattributes` rule: `utils/transport-smoke-suite/claims/** linguist-generated=true`
  - [ ] Confirm GitHub diff focus improves for code-vs-fixture review.
- [ ] Keep PR C scope strict
  - [ ] Do not pull benchmark-only files from PR B.
  - [ ] Do not introduce unrelated architecture churn.
- [ ] PR C validation
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `env -u VSOMEIP_INSTALL_PATH cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Publish PR C update
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main-prC-smoke`

## Phase 4: CI Verification and Fallback Loop

- [ ] Verify all PR checks
  - [ ] `gh pr checks 33 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 34 --repo PLeVasseur/up-streamer-rust`
  - [ ] `gh pr checks 35 --repo PLeVasseur/up-streamer-rust`
- [ ] Verify stack topology after updates
  - [ ] PR A base is `main`.
  - [ ] PR B base is PR A branch.
  - [ ] PR C base is PR A branch.
  - [ ] `PRA..PRB` contains benchmark-only delta.
  - [ ] `PRA..PRC` contains smoke + `.gitattributes` delta.
- [ ] If any check still fails, run fail-fast triage loop
  - [ ] Capture failing run/job and first actionable error.
  - [ ] Apply smallest fix at lowest stack branch where root cause lives.
  - [ ] Rebase descendants and republish with `--force-with-lease`.

## Completion Criteria

- [ ] PR A, PR B, and PR C checks are all green.
- [ ] Dead-code regression is removed without lint suppression.
- [ ] R5 is explicitly closed via `.gitattributes` in PR C.
- [ ] Local/CI parity notes are captured for future reproducibility.
- [ ] No upstream pushes occurred; stack ordering remained intact.
