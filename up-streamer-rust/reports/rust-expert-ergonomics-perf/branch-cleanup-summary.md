# Upstream-Main Branch Cleanup Summary

Date: 2026-02-11

Target branch: `refactor/up-streamer-domain-architecture`
Canonical base: `upstream/main` (`ae8afd92c1285bb09beadb0dfb5cf1f8884e1e52`)

## Session Bootstrap Checks

- PASS: `git rev-parse --abbrev-ref HEAD`
  - Output: `refactor/up-streamer-domain-architecture`
- PASS: `git status --short --branch`
  - Output: `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture` (clean)
- PASS: `git fetch origin --prune`
  - Key line: `5440295..ae8afd9  main -> origin/main`
- PASS: `git fetch upstream --prune`
  - Key line: no updates required
- PASS: `export BASE_UPSTREAM="$(git rev-parse upstream/main)"`
  - Output: `BASE_UPSTREAM=ae8afd92c1285bb09beadb0dfb5cf1f8884e1e52`
- PASS: `export OLD_HEAD="$(git rev-parse refactor/up-streamer-domain-architecture)"`
  - Output: `OLD_HEAD=4ed7f1006a4455eea028eddc93c5ec02094557d8`
- PASS: `git rev-list --count upstream/main..refactor/up-streamer-domain-architecture`
  - Output: `68`
- PASS: `git rev-list --count refactor/up-streamer-domain-architecture..upstream/main`
  - Output: `2`
- PASS: `git cat-file -e 0d441dc48eba8fb84a71560a02138a5f22d9efb3^{commit}`
- PASS: `git cat-file -e 4ed7f1006a4455eea028eddc93c5ec02094557d8^{commit}`

## Replay / Cherry-Pick Execution

- PASS: `git status --short --branch` at rewrite start
  - Output: clean worktree
- PASS: backup refs created before rewrite
  - `git branch backup/refactor-upstream-cleanup-20260211-141114 refactor/up-streamer-domain-architecture`
  - `git tag backup-refactor-upstream-cleanup-20260211-141114 refactor/up-streamer-domain-architecture`
  - Verified both resolve to: `4ed7f1006a4455eea028eddc93c5ec02094557d8`
- PASS: `git checkout -b cleanup/refactor-upstream-main upstream/main`
  - Output: switched to new branch tracking `upstream/main`
- PASS: `git cherry-pick 0d441dc^..4ed7f10`
  - Output: contiguous replay succeeded; branch became `ahead 44`
  - Final replayed HEAD: `f16f155adbc38cb015b31c4faaea71eb55111047`
  - Conflict handling: not needed (`git status` clean, no cherry-pick pause)

## Obsolete-Range Removal Verification

- PASS: `git log --oneline --reverse upstream/main..HEAD`
  - Key result: rebuilt history contains 44 intended keeper commits
- PASS: dropped-range absence check
  - Command:
    - `missing=0; for c in $(git rev-list fb7e497^..5f7e6b6); do if git merge-base --is-ancestor "$c" HEAD; then echo "FOUND $c"; missing=1; fi; done; if [ "$missing" -eq 0 ]; then echo "DROP_RANGE_ABSENT=PASS"; else echo "DROP_RANGE_ABSENT=FAIL"; exit 1; fi`
  - Output: `DROP_RANGE_ABSENT=PASS`

## PR-Preservation Assertions

- PASS: `git cherry -v HEAD bugfix/issue-74-left-topic-authority`
  - Key result: 10 lines, all prefixed `-` (patch-equivalent preserved)
- PASS: `git rev-list --count upstream/main..bugfix/issue-74-left-topic-authority`
  - Output: `10`
- PASS: `git cherry -v HEAD bugfix/issue-74-left-topic-authority | rg '^-' | wc -l`
  - Output: `10`
- FAIL (regex semantics): `git cherry -v HEAD bugfix/issue-74-left-topic-authority | rg '^+' | wc -l`
  - Output: `10` (matches due unescaped `+`)
- PASS (equivalent literal-plus assertion): `git cherry -v HEAD bugfix/issue-74-left-topic-authority | rg '^\+' | wc -l`
  - Output: `0`

Preservation decision: PASS (expected `10` preserved patch-equivalent commits, `0` non-preserved).

## Validation Gates

Minimum gates:

- PASS: `source build/envsetup.sh highest`
- PASS: `cargo fmt -- --check`
- PASS: `cargo clippy --all-targets -- -W warnings -D warnings`
- PASS: `cargo check --workspace --all-targets`
- PASS: `cargo test --workspace`
  - Key lines: `test result: ok` across workspace/unit/integration/doc tests

Extended parity matrix executed:

- PASS: `cargo build`
- PASS: `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- PASS: `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- PASS: `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
- PASS: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`

## Final Push / Cutover and Post-Cutover Counts

- PASS: `git push origin cleanup/refactor-upstream-main`
  - Key line: new remote branch created
- PASS: temporary-branch shape checks
  - `git rev-list --count upstream/main..cleanup/refactor-upstream-main` -> `44`
  - `git rev-list --count cleanup/refactor-upstream-main..upstream/main` -> `0`
  - `git log --oneline --reverse upstream/main..cleanup/refactor-upstream-main` -> expected 44-commit keeper history
- OPTIONAL gate not executed: remote draft-PR CI confidence gate
- PASS: `git push --force-with-lease origin cleanup/refactor-upstream-main:refactor/up-streamer-domain-architecture`
  - Key line: `+ 4ed7f10...f16f155 ... (forced update)`
- PASS: post-cutover verification
  - `git fetch origin --prune`
  - `git rev-parse origin/refactor/up-streamer-domain-architecture` -> `f16f155adbc38cb015b31c4faaea71eb55111047`
  - `git rev-list --count upstream/main..origin/refactor/up-streamer-domain-architecture` -> `44`

## Range and Rollback Confirmation

- Dropped obsolete range: `fb7e497..5f7e6b6` (absent from rebuilt ancestry)
- Kept range (PR-equivalent): `0d441dc..42d5a26` (`10` commits, patch-equivalent preserved)
- Kept range (newer domain/runtime/perf/test): `e553e4f..4ed7f10` (`34` commits)
- Backup refs retained for rollback:
  - `backup/refactor-upstream-cleanup-20260211-141114`
  - `backup-refactor-upstream-cleanup-20260211-141114`
- Rollback command remains available:
  - `git push --force-with-lease origin backup/refactor-upstream-cleanup-20260211-141114:refactor/up-streamer-domain-architecture`

## Final State

- Current local branch: `cleanup/refactor-upstream-main`
- Current local HEAD: `f16f155adbc38cb015b31c4faaea71eb55111047`
- Final counts vs `upstream/main`:
  - Local `HEAD`: ahead `44`, behind `0`
  - Remote `origin/refactor/up-streamer-domain-architecture`: ahead `44`, behind `0`
- Rollback readiness: AVAILABLE (backup refs verified and retained)
