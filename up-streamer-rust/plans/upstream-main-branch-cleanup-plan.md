# Branch Cleanup Plan (Base on upstream/main)

Date: 2026-02-11
Status: ready-for-execution
Target branch to clean: `refactor/up-streamer-domain-architecture`
Canonical base: `upstream/main` (currently includes `ae8afd9`)

## Objective

Make `refactor/up-streamer-domain-architecture` as clean as possible by dropping already-merged dependency/CI history while preserving open PR work and newer refactor/perf/test commits.

## Current Snapshot (from latest check)

- [x] Branch is `68` commits ahead and `2` commits behind `upstream/main`.
- [x] `upstream/main` is `1` commit ahead of `origin/main` (`ae8afd9`).
- [x] Open PR branch `bugfix/issue-74-left-topic-authority` is `10` commits ahead of `upstream/main` and should be preserved by patch-equivalent content.
- [x] Candidate obsolete range to drop: `fb7e497..5f7e6b6` (`24` commits).
- [x] Candidate keeper ranges:
  - [x] PR-equivalent keeper range: `0d441dc..42d5a26` (`10` commits).
  - [x] Newer domain/runtime/perf/test range: `e553e4f..4ed7f10` (`34` commits).

## Guardrails

- [x] Do not use interactive git commands (`-i`) or destructive reset.
- [x] Keep a hard backup ref before any history rewrite.
- [x] Preserve all open-PR-equivalent commit content.
- [x] Use `--force-with-lease` only after full validation.

## Session Bootstrap (must-pass)

- [x] Confirm execution branch and clean local state.
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Refresh remote refs before any rewrite decisions.
  - [x] `git fetch origin --prune`
  - [x] `git fetch upstream --prune`
- [x] Snapshot immutable baseline pointers for this run.
  - [x] `export BASE_UPSTREAM="$(git rev-parse upstream/main)"`
  - [x] `export OLD_HEAD="$(git rev-parse refactor/up-streamer-domain-architecture)"`
  - [x] `echo "BASE_UPSTREAM=$BASE_UPSTREAM"`
  - [x] `echo "OLD_HEAD=$OLD_HEAD"`
- [x] Record ahead/behind counters against `upstream/main` at start.
  - [x] `git rev-list --count upstream/main..refactor/up-streamer-domain-architecture`
  - [x] `git rev-list --count refactor/up-streamer-domain-architecture..upstream/main`
- [x] Hard-fail if keeper boundaries are missing.
  - [x] `git cat-file -e 0d441dc48eba8fb84a71560a02138a5f22d9efb3^{commit}`
  - [x] `git cat-file -e 4ed7f1006a4455eea028eddc93c5ec02094557d8^{commit}`

## Phase 0 - Safety Setup

- [x] Confirm clean worktree before rewrite.
  - [x] `git status --short --branch`
- [x] Create immutable backup refs for rollback.
  - [x] `git branch backup/refactor-upstream-cleanup-<timestamp> refactor/up-streamer-domain-architecture`
  - [x] `git tag backup-refactor-upstream-cleanup-<timestamp> refactor/up-streamer-domain-architecture`
- [x] Record backup refs and verify they resolve.
  - [x] `git rev-parse backup/refactor-upstream-cleanup-<timestamp>`
  - [x] `git rev-parse backup-refactor-upstream-cleanup-<timestamp>`

## Phase 1 - Rebuild on upstream/main

- [x] Create temporary cleanup branch from `upstream/main`.
  - [x] `git checkout -b cleanup/refactor-upstream-main upstream/main`
- [x] Replay one contiguous keeper range in order (preferred to avoid boundary mistakes).
  - [x] `git cherry-pick 0d441dc^..4ed7f10`
- [x] Keeper-range intent cross-check (reference only).
  - [x] Range A (open PR equivalent): `0d441dc..42d5a26` (10)
  - [x] Range B (newer refactor/perf/test): `e553e4f..4ed7f10` (34)
- [x] If conflicts occur, resolve and continue.
  - [x] `git status`
  - [x] resolve files intentionally (not needed; no conflicts)
  - [x] `git cherry-pick --continue` (not needed; no conflicts)

## Phase 2 - Validate Cleanliness and Preservation

- [x] Confirm dropped obsolete range is absent from rebuilt branch history.
  - [x] `git log --oneline --reverse upstream/main..HEAD`
  - [x] Verify none of `fb7e497..5f7e6b6` appear.
- [x] Confirm PR content is preserved (patch-equivalent).
  - [x] `git cherry -v HEAD bugfix/issue-74-left-topic-authority`
  - [x] `git rev-list --count upstream/main..bugfix/issue-74-left-topic-authority` returns `10`.
  - [x] `git cherry -v HEAD bugfix/issue-74-left-topic-authority | rg '^-' | wc -l` returns `10`.
  - [x] `git cherry -v HEAD bugfix/issue-74-left-topic-authority | rg '^+' | wc -l` returns `0` (validated via escaped `^\+` pattern).
- [x] Compare old branch vs rebuilt branch tree for unintended drift.
  - [x] `git diff --stat backup/refactor-upstream-cleanup-<timestamp>..HEAD`
- [x] Validate commit counts against expectation.
  - [x] Expected branch-only count near `44` commits over `upstream/main` (10 + 34).

## Phase 3 - Validation Gates

- [x] Run minimum verification gates.
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo fmt -- --check`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo test --workspace`
- [x] If conflicts touched runtime/transport/plugin files, run full parity matrix.
  - [x] `cargo build`
  - [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`

## Phase 4 - Cutover and Push

- [x] Push temporary cleanup branch first (pre-cutover safety).
  - [x] `git push origin cleanup/refactor-upstream-main`
- [x] Verify temporary branch shape before overwrite.
  - [x] `git rev-list --count upstream/main..cleanup/refactor-upstream-main`
  - [x] `git rev-list --count cleanup/refactor-upstream-main..upstream/main`
  - [x] `git log --oneline --reverse upstream/main..cleanup/refactor-upstream-main`
- [ ] Optional remote CI confidence gate (recommended when available).
  - [ ] open draft PR for `cleanup/refactor-upstream-main` into `main`, or run equivalent CI workflow manually
  - [ ] confirm required checks are green before target overwrite
- [x] Overwrite target branch only after checks pass.
  - [x] `git push --force-with-lease origin cleanup/refactor-upstream-main:refactor/up-streamer-domain-architecture`
- [x] Post-cutover verification.
  - [x] `git fetch origin --prune`
  - [x] `git rev-parse origin/refactor/up-streamer-domain-architecture`
  - [x] `git rev-list --count upstream/main..origin/refactor/up-streamer-domain-architecture`

## Phase 5 - Post-Cutover Documentation

- [x] Record cleanup summary report under:
  - [x] `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/branch-cleanup-summary.md`
- [x] Include in summary:
  - [x] backup refs created
  - [x] dropped commit range
  - [x] kept commit ranges
  - [x] validation outcomes
  - [x] final ahead/behind counts vs `upstream/main`

## Rollback (copy/paste ready)

- [ ] If any post-cutover issue appears, restore from backup ref immediately.
  - [ ] `git push --force-with-lease origin backup/refactor-upstream-cleanup-<timestamp>:refactor/up-streamer-domain-architecture`
  - [ ] `git fetch origin --prune && git rev-parse origin/refactor/up-streamer-domain-architecture`

## Resume Protocol (fresh-session safety)

- [ ] Re-run Session Bootstrap section fully.
- [ ] Confirm backup refs still exist and point to expected commit.
  - [ ] `git rev-parse backup/refactor-upstream-cleanup-<timestamp>`
  - [ ] `git show --no-patch --oneline backup/refactor-upstream-cleanup-<timestamp>`
- [ ] Confirm current execution phase and next unchecked item.
- [ ] Re-verify branch cleanliness before continuing.
  - [ ] `git status --short --branch`

## Done Criteria

- [x] Branch is rebased/rebuilt on top of `upstream/main` (includes `ae8afd9`).
- [x] Obsolete dependency/CI range `fb7e497..5f7e6b6` is removed.
- [x] Open PR (`#77`) content remains preserved by patch equivalence.
- [x] Validation gates pass.
- [x] Force push completed with `--force-with-lease`.
- [x] Backup refs retained until final merge.
