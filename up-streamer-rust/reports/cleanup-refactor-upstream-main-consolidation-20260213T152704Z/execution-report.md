# Commit Consolidation Execution Report

## Run Metadata

- `RUN_ID`: `cleanup-refactor-upstream-main-consolidation-20260213T152704Z`
- Repo path: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Branch: `cleanup/refactor-upstream-main`
- Base branch/ref: `upstream/main` (`b6bc245ceaf2ae94b9272c3be86a2502c8fdac81`)
- Pre-rewrite local SHA: `cbe631a823481785e7a0b631c2e0b3240d499f01`
- Pre-rewrite remote SHA (`origin/cleanup/refactor-upstream-main`): `cbe631a823481785e7a0b631c2e0b3240d499f01`
- Final rewritten branch SHA: `1ed5614e8850b32115a465356b92bf52c94e97f1`
- Final commits on top of `upstream/main`: `6`

## Backup Metadata

- Backup branch: `backup/cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
- Backup tag: `backup-cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
- Backup branch SHA: `cbe631a823481785e7a0b631c2e0b3240d499f01`
- Backup tag SHA: `cbe631a823481785e7a0b631c2e0b3240d499f01`
- Push proof commands executed:
  - `git push origin backup/cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
  - `git push origin backup-cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
  - `git ls-remote --heads origin backup/cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
  - `git ls-remote --tags origin backup-cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`

## Crash/Resume Metadata

- Active run pointer: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/cleanup-refactor-upstream-main-consolidation.current`
- State file: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/cleanup-refactor-upstream-main-consolidation-20260213T152704Z/session-state.env`
- Phase markers: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/cleanup-refactor-upstream-main-consolidation-20260213T152704Z/phase-markers.log`
- Command transcript: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/cleanup-refactor-upstream-main-consolidation-20260213T152704Z/command-transcript.log`
- Resume flow used: `yes` (Phase 0R executed after interruption during rebase continue; stale lock rotated and re-acquired; resumed from first unchecked item in Phase 3)
- Phase timeline:

```text
2026-02-13T15:29:44Z PHASE_0_COMPLETE
2026-02-13T15:30:17Z PHASE_1_COMPLETE
2026-02-13T15:31:22Z PHASE_2_COMPLETE
2026-02-13T15:37:39Z COMMIT_1_VALIDATED
2026-02-13T15:59:39Z COMMIT_2_VALIDATED
2026-02-13T16:04:14Z COMMIT_3_VALIDATED
2026-02-13T16:06:46Z COMMIT_3_VALIDATED_RERUN
2026-02-13T16:09:43Z COMMIT_4_VALIDATED
2026-02-13T16:14:23Z COMMIT_5_VALIDATED
2026-02-13T16:14:53Z COMMIT_6_VALIDATED_OR_FOLDED
2026-02-13T16:15:05Z PHASE_3_COMPLETE
2026-02-13T16:15:05Z PHASE_3A_COMPLETE
2026-02-13T16:17:04Z COMMIT_6_VALIDATED_RERUN
2026-02-13T16:17:20Z PHASE_4_COMPLETE
2026-02-13T16:28:09Z PHASE_5_COMPLETE
2026-02-13T16:28:49Z PHASE_6_COMPLETE
```

## Remote Checkpoint Tags Created

- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase1-backup-ready`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase2-analysis-ready`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase3-pre-rebase`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit1-validated`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit2-validated`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit3-validated`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit3-validated-rerun`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit4-validated`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit5-validated`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit6-validated`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase3-rebase-complete`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-commit6-validated-rerun`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase4-integrity-proved`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase5-validation-passed`
- `checkpoint-cleanup-refactor-upstream-main-cleanup-refactor-upstream-main-consolidation-20260213T152704Z-phase6-pushed`

## Command Transcript Summary by Phase

### Phase 0 / 0R / 1 / 2

- Verified invariants and tools (`git status`, branch, clean tree, no rebase dirs, tool versions).
- Captured baseline (`git fetch --all --prune`; pre/local/upstream SHAs).
- Created and pushed backup refs and initial checkpoint tags.
- Captured divergence artifacts (`merge-base`, `rev-list`, `diff-stat`, `name-status`, pre-commit list).
- Built deterministic artifacts (`commit-buckets.md`, `rebase-todo.txt`, SHA256, sequence editor script).
- On resume: executed Phase 0R, rotated stale lock, rehydrated state, resumed in-progress rebase.

### Phase 3 / 3A

- Launched headless rebase:
  - `GIT_SEQUENCE_EDITOR="$REPORT_DIR/set-rebase-todo.sh" GIT_EDITOR="$REPORT_DIR/set-reword-message.sh" git rebase -i upstream/main`
- Rebase checkpoint/gate loop executed at each `break`:
  - `git show --no-patch --format='%H %s' HEAD`
  - `git diff --check HEAD^..HEAD`
  - `cargo check --workspace --all-targets`
- Commit gates executed per plan (`cargo check/test/clippy` command sets for commits 1..6).
- Conflict handling during rebase:
  - Resolved `up-streamer/src/benchmark_support.rs` (modify/delete) via `git add` keep-updated version.
  - Resolved `up-streamer/Cargo.toml` conflict while applying `f917011` by keeping required `criterion` and `futures` dev deps.
  - Resolved `Cargo.lock`, `up-streamer/Cargo.toml`, and `up-streamer/src/benchmark_support.rs` conflicts while applying `46e5bf3` by retaining API-compatible file content and including `criterion-guardrail` lock entry.
- No empty-pick commits were skipped.

### Phase 4

- Verified stack shape (`6` commits) and ancestry (`merge-base` unchanged).
- Proved tree equality to backup (final `HEAD^{tree}` equals backup tree).
- Captured scope/integrity artifacts:
  - `diff-vs-backup.txt`
  - `diff-stat-post.txt`
  - `cherry-post.txt`
  - `range-diff-post.txt`

### Phase 5

- Ran base CI parity checks:
  - `source build/envsetup.sh highest`
  - `cargo build`
  - `cargo clippy --all-targets -- -W warnings -D warnings`
  - `cargo fmt -- --check`
- Ran bundled matrix checks:
  - `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- Unbundled matrix skipped explicitly:
  - `VSOMEIP_INSTALL_PATH` unavailable (`unset or invalid directory`)
- Ran workspace checks:
  - `cargo check --workspace --all-targets`
  - `cargo test --workspace`
- Ran branch-guarded smoke matrix with skip-build:
  - `SMOKE_EXPECTED_BRANCH=cleanup/refactor-upstream-main cargo run -p transport-smoke-suite --bin transport-smoke-matrix -- --all --expected-branch cleanup/refactor-upstream-main --skip-build --artifacts-root "target/transport-smoke/rewrite-final-cleanup-refactor-upstream-main-consolidation-20260213T152704Z"`

### Phase 6

- Verified clean working tree and remote invariant before rewrite push.
- Force-pushed with explicit lease:
  - `git push --force-with-lease=cleanup/refactor-upstream-main:cbe631a823481785e7a0b631c2e0b3240d499f01 origin cleanup/refactor-upstream-main`
- Verified post-push head parity and PR metadata (`gh pr view 78 ...`).

## Per-Commit Validation Results

- Commit 1 (`164279555b555648a22b94dfcef9f067a721a5ad`): all requested checks passed; tag `...-commit1-validated`.
- Commit 2 (`7b2a4ecc497f31411daaadf1001d8ef0df6b577d`): all requested checks passed; tag `...-commit2-validated`.
- Commit 3:
  - Initial validated SHA `96e4bd6f6b8ef6d1ac8c30f23a104010852c8216` (`...-commit3-validated`).
  - Amended during rebase conflict cleanup; revalidated final SHA `15dbd20a09f44784ec892d651fe275f8e4c52dff` (`...-commit3-validated-rerun`).
- Commit 4 (`650d9f5315eff8dbeef68b0038a08f0b4bffe82f`): all requested checks passed; tag `...-commit4-validated`.
- Commit 5 (`7c4f7ef23813126c1d37b966e9c50433b9a2899e`): all requested checks passed; tag `...-commit5-validated`.
- Commit 6:
  - Initial validated SHA `2708362692cd1de86d0d44f976a9e4ad07aaf02b` (`...-commit6-validated`).
  - Final post-integrity amend to restore exact tree parity; revalidated SHA `1ed5614e8850b32115a465356b92bf52c94e97f1` (`...-commit6-validated-rerun`).

## Integrity Proof Outputs

- `merge-base-post.txt`: `b6bc245ceaf2ae94b9272c3be86a2502c8fdac81`
- `commits-post.txt`: 6 logical commits (<= 6)
- Tree equality: `HEAD^{tree}` == `${BACKUP_BRANCH}^{tree}` (`fe78ee939fd5c68896d2041edaf5f43124526026`)
- `diff-vs-backup.txt`: empty (no content loss)
- `diff-stat-post.txt`: scope matches pre-rewrite scope (168 files, additions/deletions preserved)
- `cherry-post.txt`: six rewritten commits present
- `range-diff-post.txt`: rewritten stack mapping captured

## Final Smoke Evidence

- Command:

```bash
SMOKE_EXPECTED_BRANCH=cleanup/refactor-upstream-main cargo run -p transport-smoke-suite --bin transport-smoke-matrix -- --all --expected-branch cleanup/refactor-upstream-main --skip-build --artifacts-root "target/transport-smoke/rewrite-final-cleanup-refactor-upstream-main-consolidation-20260213T152704Z"
```

- Matrix artifact directory:
  - `target/transport-smoke/rewrite-final-cleanup-refactor-upstream-main-consolidation-20260213T152704Z/matrix/20260213T162511Z`
- Matrix summary files:
  - `target/transport-smoke/rewrite-final-cleanup-refactor-upstream-main-consolidation-20260213T152704Z/matrix/20260213T162511Z/matrix-summary.json`
  - `target/transport-smoke/rewrite-final-cleanup-refactor-upstream-main-consolidation-20260213T152704Z/matrix/20260213T162511Z/matrix-summary.txt`
- `fail_count`: `0`
- Aggregate rationale: `all selected scenarios passed`

## Push and PR Verification

- Force push command used exactly:

```bash
git push --force-with-lease=cleanup/refactor-upstream-main:cbe631a823481785e7a0b631c2e0b3240d499f01 origin cleanup/refactor-upstream-main
```

- Remote branch head after push: `1ed5614e8850b32115a465356b92bf52c94e97f1` (matches local `HEAD`).
- PR URL: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/78`
- PR head OID: `1ed5614e8850b32115a465356b92bf52c94e97f1`
- PR commit count: `6` (verified <= 6)
- PR diff scope: `changedFiles=168`, `additions=12453`, `deletions=2995` (matches intended scope)

## Rollback Refs and Exact Commands

- Durable rollback refs:
  - Branch: `backup/cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
  - Tag: `backup-cleanup-refactor-upstream-main-pre-squash-20260213T153012Z`
- Before push (if rewrite unacceptable):

```bash
git rebase --abort
git checkout cleanup/refactor-upstream-main
git reset --hard backup/cleanup-refactor-upstream-main-pre-squash-20260213T153012Z
```

- After push (if rewrite must be reverted):

```bash
git checkout cleanup/refactor-upstream-main
git reset --hard backup/cleanup-refactor-upstream-main-pre-squash-20260213T153012Z
git push --force-with-lease origin cleanup/refactor-upstream-main
```

- Checkpoint recovery (partial-progress recovery):

```bash
git fetch origin --tags
git checkout <checkpoint-tag>
git checkout -B cleanup/refactor-upstream-main-recovery <checkpoint-tag>
```
