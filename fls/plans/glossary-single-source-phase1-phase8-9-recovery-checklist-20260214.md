# Glossary Single-Source Phase1 Phase8/9 Recovery Checklist (Fresh Session, Strict Four-Commit)

Date: 2026-02-14

## Objective
- [ ] Resume at the first defect boundary (Phase 8 capstone recreation), without rerunning Phases 1-7.
- [ ] Replace commit 4 from `COMMIT3_SHA` so verifier policy behavior is committed and auditable.
- [ ] Re-run Phase 9 integrity checks from clean commit refs/worktrees only.
- [ ] Preserve strict topology: exactly four commits over pinned `UPSTREAM_MAIN_PIN`.

## Explicit Non-Goals
- [ ] Do not rerun the relayer from the top.
- [ ] Do not add a fifth commit.
- [ ] Do not push to upstream.

## Fixed Inputs (From Canonical State)
- [ ] `OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/fls`
- [ ] `STATE_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.env`
- [ ] `STATE_LOCK_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.state.lock`
- [ ] `REPORT_FILE=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-relayer-20260214.md`
- [ ] `REPACK_BRANCH=glossary-single-source-phase1-repack-upstream-main`
- [ ] `UPSTREAM_MAIN_PIN=fb8a46795eda1f1db5e3232002fd94a270bfbffd`
- [ ] `COMMIT3_SHA=7fdb35552db16ed107be39f57142f54a8a56412b`
- [ ] `OLD_COMMIT4_SHA=0d81919732c5040ace6a2e947e5adaab30e2385f`

## Hard Boundaries
- [ ] Any history rewrite is restricted to `origin/$REPACK_BRANCH` with `--force-with-lease`.
- [ ] All temporary and recovery artifacts go under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] If invariants do not hold, stop and do not improvise the stack shape.

## Recovery Run Artifacts
- [ ] Create a run identifier and isolated recovery root.
  - [ ] `RECOVERY_RUN_ID=$(date -u +%Y%m%dT%H%M%SZ)`
  - [ ] `RECOVERY_ROOT=$OPENCODE_CONFIG_DIR/reports/glossary-single-source-phase1-phase8-9-recovery-$RECOVERY_RUN_ID`
  - [ ] `mkdir -p "$RECOVERY_ROOT"`
- [ ] Use a dedicated recovery state/log pair for resumability.
  - [ ] `RECOVERY_STATE_FILE=$RECOVERY_ROOT/recovery.state.env`
  - [ ] `RECOVERY_LOG=$RECOVERY_ROOT/recovery.log`
- [ ] Use dedicated verification artifact paths for this recovery run.
  - [ ] `RECOVERY_ARTIFACT_ROOT=$RECOVERY_ROOT/artifacts`
  - [ ] `mkdir -p "$RECOVERY_ARTIFACT_ROOT"`

## Crash-Resilient Recovery State Model (Mandatory)
- [ ] Treat `RECOVERY_STATE_FILE` as the source of truth for recovery progress.
  - [ ] Initialize on first entry with immutable keys: `RECOVERY_RUN_ID`, `RECOVERY_ROOT`, `REPACK_BRANCH`, `OLD_COMMIT4_SHA`.
  - [ ] On resume, load and validate immutable keys before any mutation.
  - [ ] If immutable keys mismatch current session intent, stop and open a new recovery run.
- [ ] Persist required checkpoint keys.
  - [ ] Stage completion flags: `R0_DONE`, `R1_DONE`, `R1B_DONE`, `R2_DONE`, `R3_DONE`, `R4_DONE`, `R5_DONE`, `R6_DONE`, `R7_DONE`, `R8_DONE`, `R9_DONE`, `R9B_DONE`, `R10_DONE`.
  - [ ] Runtime pointer: `CURRENT_STAGE`.
  - [ ] Critical values: `OLD_REMOTE_SHA`, `NEW_COMMIT4_SHA`, `REPACK_REMOTE_SHA`.
  - [ ] Push/finalization status: `PUSH_ATTEMPTED`, `PUSH_CONFIRMED`, `CANONICAL_STATE_UPDATED`, `REPORT_APPENDED`.
- [ ] Enforce atomic write discipline for `RECOVERY_STATE_FILE`.
  - [ ] Write candidate updates to `"$RECOVERY_STATE_FILE.tmp"`.
  - [ ] Validate parseability of temp state before replace.
  - [ ] Replace with atomic rename (`mv`) only after validation passes.
  - [ ] Never partially edit `RECOVERY_STATE_FILE` in place.
- [ ] Enforce idempotent report and state finalization.
  - [ ] Recovery report append block includes `RECOVERY_RUN_ID` marker.
  - [ ] On resume, if marker already exists, skip duplicate append.

## Stage R0 - Fresh Session Bootstrap, Lock Safety, and Recovery-State Init
- [ ] Stage checkpointing.
  - [ ] After recovery-state bootstrap, set `CURRENT_STAGE=R0` and atomically persist to `RECOVERY_STATE_FILE`.
  - [ ] On successful completion of Stage R0, set `R0_DONE=1` and atomically persist.
- [ ] Environment and toolchain sanity.
  - [ ] `printenv OPENCODE_CONFIG_DIR` is non-empty and equals expected path.
  - [ ] `test -d "$OPENCODE_CONFIG_DIR/plans"`
  - [ ] `test -d "$OPENCODE_CONFIG_DIR/reports"`
  - [ ] `command -v git`
  - [ ] `command -v uv`
  - [ ] `command -v python3`
  - [ ] `command -v sphinx-build`
  - [ ] `uv sync --frozen`
- [ ] Deterministic env for proof phases.
  - [ ] `TZ=UTC`
  - [ ] `LANG=C.UTF-8`
  - [ ] `LC_ALL=C.UTF-8`
  - [ ] `PYTHONHASHSEED=0`
  - [ ] `umask 022`
- [ ] Lock-file handling (single active writer).
  - [ ] If `STATE_LOCK_FILE` exists, parse `PID`, `HOST`, and `CREATED_AT` from file.
  - [ ] Validate active-lock semantics with PID reuse protection.
    - [ ] `HOST` matches current host name.
    - [ ] `PID` exists.
    - [ ] `PID` owner matches current user.
    - [ ] `PID` command line still matches expected OpenCode session process (not unrelated PID reuse).
  - [ ] If all active-lock checks pass, stop immediately (concurrent writer protection).
  - [ ] If any active-lock check fails, treat lock as stale, archive stale lock content in `RECOVERY_LOG`, then replace lock.
  - [ ] Write fresh lock with current PID/host/time.
  - [ ] Set cleanup trap to remove lock on normal exit and failure exit.
- [ ] Recovery-state bootstrap.
  - [ ] If `RECOVERY_STATE_FILE` does not exist, create it with default flags.
    - [ ] Set immutable keys and `CURRENT_STAGE=R0`.
    - [ ] Set all stage flags (`R0_DONE`, `R1_DONE`, `R1B_DONE`, `R2_DONE`, `R3_DONE`, `R4_DONE`, `R5_DONE`, `R6_DONE`, `R7_DONE`, `R8_DONE`, `R9_DONE`, `R9B_DONE`, `R10_DONE`) to `0`.
    - [ ] Set `PUSH_ATTEMPTED=0`, `PUSH_CONFIRMED=0`, `CANONICAL_STATE_UPDATED=0`, `REPORT_APPENDED=0`.
  - [ ] If `RECOVERY_STATE_FILE` exists, source and validate immutable keys.
    - [ ] `RECOVERY_RUN_ID` matches current run.
    - [ ] `RECOVERY_ROOT` exists and matches current run root.
    - [ ] `OLD_COMMIT4_SHA` and `REPACK_BRANCH` match intended recovery target.
    - [ ] Keep existing stage/progress flags intact; do not reset completed flags on resume.

## Stage R1 - Load Canonical State and Validate Invariants
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R1` and atomically persist.
  - [ ] On successful completion of Stage R1, set `R1_DONE=1` and atomically persist.
- [ ] Load canonical state safely.
  - [ ] `test -f "$STATE_FILE"`
  - [ ] `source "$STATE_FILE"`
  - [ ] Required keys exist and are non-empty (`UPSTREAM_MAIN_PIN`, `COMMIT1_SHA`..`COMMIT4_SHA`, `REPACK_BRANCH`).
- [ ] Validate expected phase checkpoint.
  - [ ] `PHASE_7_COMMIT3_DONE=1`
  - [ ] `PHASE_8_COMMIT4_DONE=1`
  - [ ] `PHASE_10_STOP_POINT_DONE=1`
  - [ ] `COMMIT4_SHA` from state equals `OLD_COMMIT4_SHA`.
- [ ] Validate commit objects and ancestry.
  - [ ] `git cat-file -e "$UPSTREAM_MAIN_PIN^{commit}"`
  - [ ] `git cat-file -e "$COMMIT1_SHA^{commit}"`
  - [ ] `git cat-file -e "$COMMIT2_SHA^{commit}"`
  - [ ] `git cat-file -e "$COMMIT3_SHA^{commit}"`
  - [ ] `git cat-file -e "$OLD_COMMIT4_SHA^{commit}"`
  - [ ] `test "$(git rev-parse "$OLD_COMMIT4_SHA^")" = "$COMMIT3_SHA"`
  - [ ] `git merge-base --is-ancestor "$UPSTREAM_MAIN_PIN" "$COMMIT3_SHA"`
- [ ] Validate branch and remote preconditions.
  - [ ] `git fetch --prune origin`
  - [ ] `git rev-parse --verify "origin/$REPACK_BRANCH"`
  - [ ] Ensure local branch exists.
    - [ ] If local `"$REPACK_BRANCH"` exists, `git switch "$REPACK_BRANCH"`.
    - [ ] If local `"$REPACK_BRANCH"` does not exist, `git switch -c "$REPACK_BRANCH" --track "origin/$REPACK_BRANCH"`.
  - [ ] `OLD_REMOTE_SHA=$(git rev-parse "origin/$REPACK_BRANCH")`
  - [ ] `test "$OLD_REMOTE_SHA" = "$OLD_COMMIT4_SHA"` (remote start point pin).
  - [ ] `test "$(git rev-parse HEAD)" = "$OLD_COMMIT4_SHA"` (local start point pin).
  - [ ] `test "$(git rev-parse HEAD)" = "$OLD_REMOTE_SHA"` (no local divergence before rewrite).
  - [ ] `git rev-list --count "$UPSTREAM_MAIN_PIN"..HEAD` equals `4`.
- [ ] Validate no in-progress git operations.
  - [ ] No `.git/rebase-merge`.
  - [ ] No `.git/rebase-apply`.
  - [ ] No `.git/MERGE_HEAD`.
  - [ ] No `.git/CHERRY_PICK_HEAD`.

## Stage R1b - Crash Resume Reconciliation
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R1b` and atomically persist.
  - [ ] On successful completion of Stage R1b, set `R1B_DONE=1` and atomically persist.
- [ ] Reconcile resume target from `RECOVERY_STATE_FILE` before executing later stages.
  - [ ] If `PUSH_ATTEMPTED=1` and `PUSH_CONFIRMED=0`, probe remote outcome.
    - [ ] `git fetch --prune origin "$REPACK_BRANCH"`
    - [ ] If `origin/$REPACK_BRANCH == NEW_COMMIT4_SHA`, set `PUSH_CONFIRMED=1` and resume at Stage R9b.
    - [ ] If `origin/$REPACK_BRANCH != NEW_COMMIT4_SHA`, resume at Stage R9 push.
  - [ ] If `R9_DONE=1` and (`CANONICAL_STATE_UPDATED=0` or `REPORT_APPENDED=0`), resume at Stage R9b only.
  - [ ] If `R7_DONE=1` and `R8_DONE=0`, resume at Stage R8.
  - [ ] If `R6_DONE=1` and `R7_DONE=0`, resume at Stage R7.
  - [ ] If `R5_DONE=1` and `R6_DONE=0`, resume at Stage R6.
  - [ ] Otherwise resume at the earliest incomplete stage in order.
- [ ] Record reconciliation decision and evidence.
  - [ ] Append decision line and chosen resume stage to `RECOVERY_LOG`.
  - [ ] Persist `CURRENT_STAGE` target after reconciliation.

## Stage R2 - Capture Forensic Snapshot and Safety Refs (Before Destructive Step)
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R2` and atomically persist.
  - [ ] On successful completion of Stage R2, set `R2_DONE=1` and atomically persist.
- [ ] Capture current workspace evidence.
  - [ ] `git status --short > "$RECOVERY_ROOT/status-before.txt"`
  - [ ] `git diff > "$RECOVERY_ROOT/worktree-before.patch"`
  - [ ] `git diff -- tools/verify-html-diff.py > "$RECOVERY_ROOT/verify-html-diff-unstaged.patch"`
  - [ ] `git hash-object tools/verify-html-diff.py > "$RECOVERY_ROOT/verify-html-diff-worktree.hash"`
  - [ ] `git rev-parse :tools/verify-html-diff.py > "$RECOVERY_ROOT/verify-html-diff-index.hash"`
  - [ ] `git show --no-patch --format='%H %P %s' "$OLD_COMMIT4_SHA" > "$RECOVERY_ROOT/old-capstone.txt"`
- [ ] Guard destructive reset with explicit allowlist check.
  - [ ] Allowed pre-reset unstaged path set is only `tools/verify-html-diff.py`.
  - [ ] If additional unstaged/untracked paths exist, stop and triage before continuing.
- [ ] Create recovery backup refs using run id (idempotence-safe).
  - [ ] `RECOVERY_BACKUP_BRANCH=backup/glossary-single-source-phase1-repack-pre-recovery-$RECOVERY_RUN_ID`
  - [ ] `RECOVERY_BACKUP_TAG=backup-glossary-single-source-phase1-repack-pre-recovery-$RECOVERY_RUN_ID`
  - [ ] Create branch/tag at `OLD_COMMIT4_SHA` if absent.
  - [ ] If either ref already exists, require it to resolve to `OLD_COMMIT4_SHA`; otherwise stop.
  - [ ] Push branch/tag to origin.
  - [ ] If either remote ref already exists, require it to resolve to `OLD_COMMIT4_SHA`; otherwise stop.
  - [ ] Verify remote refs resolve to `OLD_COMMIT4_SHA`.

## Stage R3 - Materialize Intended Verifier Policy Delta
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R3` and atomically persist.
  - [ ] On successful completion of Stage R3, set `R3_DONE=1` and atomically persist.
- [ ] Establish verifier patch source.
  - [ ] Preferred: reuse `"$RECOVERY_ROOT/verify-html-diff-unstaged.patch"` if non-empty.
  - [ ] Fallback: manually edit `tools/verify-html-diff.py` and `tools/README.rst` to satisfy policy checklist below.
- [ ] Policy checklist for `tools/verify-html-diff.py` (must all hold).
  - [ ] Define fixed commit constant for deterministic build commit rendering.
  - [ ] Intercept `git rev-parse HEAD` in verifier subprocess wrapper and return fixed commit.
  - [ ] Exclude `_sources/` entries from comparison path set.
- [ ] Policy checklist for `tools/README.rst`.
  - [ ] Document the deterministic commit handling behavior.
  - [ ] Document `_sources/` exclusion rationale in comparison policy text.
- [ ] Capture explicit verifier-policy marker evidence in recovery artifacts.
  - [ ] Save marker evidence with line numbers to `$RECOVERY_ROOT/verify-policy-markers.txt`.
  - [ ] Evidence file includes markers for fixed commit constant, `rev-parse HEAD` interception, and `_sources/` exclusion.

## Stage R4 - Rebuild Capstone From Commit 3 (Only)
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R4` and atomically persist.
  - [ ] On successful completion of Stage R4, set `R4_DONE=1` and atomically persist.
- [ ] Rewind branch tip to commit 3 after evidence and backup refs are complete.
  - [ ] `git reset --hard "$COMMIT3_SHA"`
- [ ] Rehydrate prior capstone payload without committing.
  - [ ] `git cherry-pick --no-commit "$OLD_COMMIT4_SHA"`
  - [ ] `git restore --staged .` (force explicit restaging discipline)
  - [ ] If cherry-pick conflicts, stop and resolve intentionally before proceeding.
- [ ] Apply intended verifier policy delta.
  - [ ] Apply saved patch if available.
  - [ ] If patch application fails, perform manual edits using Stage R3 checklist.

## Stage R5 - Stage Exact File Set and Enforce Pre-Commit Gates
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R5` and atomically persist.
  - [ ] On successful completion of Stage R5, set `R5_DONE=1` and atomically persist.
- [ ] Stage only the capstone file list.
  - [ ] `.github/workflows/ci.yml`
  - [ ] `README.rst`
  - [ ] `exts/ferrocene_spec/README.rst`
  - [ ] `generate-glossary-entry.py`
  - [ ] `generate-glossary.py`
  - [ ] `make.py`
  - [ ] `src/glossary.rst`
  - [ ] `src/glossary.rst.inc`
  - [ ] `tools/README.rst`
  - [ ] `tools/verify-html-diff.py`
- [ ] Gate 1: staged set must be exact.
  - [ ] `git diff --cached --name-only` equals the 10-file list above (no missing, no extra).
- [ ] Gate 2: no unstaged drift.
  - [ ] `git diff --name-only` is empty.
- [ ] Gate 3: verifier worktree/index parity.
  - [ ] `test "$(git rev-parse :tools/verify-html-diff.py)" = "$(git hash-object tools/verify-html-diff.py)"`
- [ ] Gate 4: verifier policy markers present.
  - [ ] `grep -n "FIXED_BUILD_COMMIT" tools/verify-html-diff.py` returns at least one match.
  - [ ] `grep -n "rev-parse" tools/verify-html-diff.py` and `grep -n "HEAD" tools/verify-html-diff.py` confirm interception logic markers exist.
  - [ ] `grep -n "_sources/" tools/verify-html-diff.py` returns at least one match.
  - [ ] `grep -n "_sources" tools/README.rst` returns at least one match.
- [ ] Gate 5: no unexpected untracked files.
  - [ ] `git status --short` only shows staged files for this commit.

## Stage R6 - Commit and Topology Validation
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R6` and atomically persist.
  - [ ] On successful completion of Stage R6, set `R6_DONE=1` and atomically persist.
- [ ] Commit with the same message.
  - [ ] `refactor(glossary): switch to generated-only glossary source and reproducibility checks`
- [ ] Capture `NEW_COMMIT4_SHA=$(git rev-parse HEAD)`.
- [ ] Validate strict stack shape.
  - [ ] `git rev-list --count "$UPSTREAM_MAIN_PIN"..HEAD` equals `4`.
  - [ ] `test "$(git rev-parse "$NEW_COMMIT4_SHA^")" = "$COMMIT3_SHA"`
  - [ ] First three commit SHAs over base remain `COMMIT1_SHA`, `COMMIT2_SHA`, `COMMIT3_SHA` in order.
- [ ] Validate commit payload scope.
  - [ ] `git diff --name-only "$COMMIT3_SHA".."$NEW_COMMIT4_SHA"` equals expected capstone file list.

## Stage R7 - Re-run Phase 9 Integrity Chain (Clean Refs/Worktrees Only)
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R7` and atomically persist.
  - [ ] On successful completion of Stage R7, set `R7_DONE=1` and atomically persist.
- [ ] Build and compare using explicit report paths under `RECOVERY_ARTIFACT_ROOT`.
  - [ ] `./tools/verify-html-diff.py --mode refs --left-ref "$UPSTREAM_MAIN_PIN" --right-ref "$COMMIT3_SHA" --report "$RECOVERY_ARTIFACT_ROOT/diff-upstream-main-vs-commit3.txt"`
  - [ ] `./tools/verify-html-diff.py --mode refs --left-ref "$COMMIT3_SHA" --right-ref "$NEW_COMMIT4_SHA" --report "$RECOVERY_ARTIFACT_ROOT/diff-commit3-vs-commit4.txt"`
  - [ ] `./tools/verify-html-diff.py --mode refs --left-ref "$UPSTREAM_MAIN_PIN" --right-ref "$NEW_COMMIT4_SHA" --report "$RECOVERY_ARTIFACT_ROOT/diff-upstream-main-vs-commit4.txt"`
  - [ ] `./tools/verify-html-diff.py --mode repro --ref "$NEW_COMMIT4_SHA" --report "$RECOVERY_ROOT/capstone-repro-commit4.txt"`
  - [ ] Capture command exit codes in recovery log/state.
    - [ ] `RC_UPSTREAM_VS_COMMIT3` from `diff-upstream-main-vs-commit3.txt` run.
    - [ ] `RC_COMMIT3_VS_COMMIT4` from `diff-commit3-vs-commit4.txt` run.
    - [ ] `RC_UPSTREAM_VS_COMMIT4` from `diff-upstream-main-vs-commit4.txt` run.
    - [ ] `RC_REPRO_COMMIT4` from `capstone-repro-commit4.txt` run.
- [ ] Acceptance gates for marking Phase 9 done.
  - [ ] All four reports exist and are non-empty.
  - [ ] Required pass/fail gates (must pass).
    - [ ] `RC_COMMIT3_VS_COMMIT4=0` and `diff-commit3-vs-commit4.txt` contains exactly `result: no differences under configured comparison policy.`
    - [ ] `RC_REPRO_COMMIT4=0` and `capstone-repro-commit4.txt` contains exactly `result: no differences under configured comparison policy.`
  - [ ] Informational-only reports (must never fail this recovery run).
    - [ ] `diff-upstream-main-vs-commit3.txt` is archived regardless of whether it contains differences.
    - [ ] `diff-upstream-main-vs-commit4.txt` is archived regardless of whether it contains differences.
    - [ ] `RC_UPSTREAM_VS_COMMIT3` and `RC_UPSTREAM_VS_COMMIT4` may be `0` or `1`; both are non-blocking.
    - [ ] Each upstream report result line is either `result: no differences under configured comparison policy.` or `result: differences found under configured comparison policy.`
    - [ ] Differences in either upstream comparison are explicitly allowed and must not set `PHASE_9_VERIFY_DONE=0`.
  - [ ] Operational/tooling failures still fail Stage R7.
    - [ ] If any run exits with code `2` (or any code outside allowed set), keep `PHASE_9_VERIFY_DONE=0`, record blocker, and stop.
    - [ ] If report generation fails, or required pass/fail reports are missing/invalid, keep `PHASE_9_VERIFY_DONE=0`, record blocker, and stop.

## Stage R8 - Pre-Push Finalization Prep (Recovery-State Only)
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R8` and atomically persist.
  - [ ] On successful completion of Stage R8, set `R8_DONE=1` and atomically persist.
- [ ] Generate integrity-chain report before push.
  - [ ] Write `$RECOVERY_ROOT/integrity-chain.md`.
  - [ ] Include old/new capstone SHAs and `RECOVERY_RUN_ID`.
  - [ ] Include required gate results (`commit3 vs commit4`, `repro`) with exit codes and result lines.
  - [ ] Include informational upstream report results with explicit non-blocking statement.
- [ ] Persist provisional recovery-state values only.
  - [ ] Set `PENDING_CANONICAL_UPDATE=1`.
  - [ ] Set `PROPOSED_COMMIT4_SHA=$NEW_COMMIT4_SHA`.
  - [ ] Do not update canonical `STATE_FILE` in Stage R8.
  - [ ] Do not append to canonical `REPORT_FILE` in Stage R8.

## Stage R9 - Push Corrected Repack Branch Safely
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R9` and atomically persist.
  - [ ] On successful completion of Stage R9, set `R9_DONE=1` and atomically persist.
- [ ] Persist push-attempt marker before push.
  - [ ] Set `PUSH_ATTEMPTED=1` and `PUSH_CONFIRMED=0` in `RECOVERY_STATE_FILE`.
- [ ] Push with explicit lease anchored to pre-recovery remote SHA.
  - [ ] `git push --force-with-lease=refs/heads/$REPACK_BRANCH:$OLD_REMOTE_SHA origin HEAD:refs/heads/$REPACK_BRANCH`
  - [ ] If lease push fails, stop and record blocker.
    - [ ] Do not retry with plain `--force`.
    - [ ] Do not retry with weaker or implicit lease settings.
- [ ] Verify push result.
  - [ ] `git fetch origin "$REPACK_BRANCH"`
  - [ ] `REPACK_REMOTE_SHA=$(git rev-parse "origin/$REPACK_BRANCH")`
  - [ ] `test "$REPACK_REMOTE_SHA" = "$NEW_COMMIT4_SHA"`
- [ ] Persist push-success markers atomically.
  - [ ] Set `PUSH_CONFIRMED=1`.
  - [ ] Set `REPACK_REMOTE_SHA=$NEW_COMMIT4_SHA`.

## Stage R9b - Canonical State/Report Finalization (Post-Push, Atomic)
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R9b` and atomically persist.
  - [ ] On successful completion of Stage R9b, set `R9B_DONE=1` and atomically persist.
- [ ] Enforce post-push preconditions.
  - [ ] `PUSH_CONFIRMED=1` in `RECOVERY_STATE_FILE`.
  - [ ] `REPACK_REMOTE_SHA == NEW_COMMIT4_SHA`.
  - [ ] `PENDING_CANONICAL_UPDATE=1`.
- [ ] Update canonical state file atomically.
  - [ ] Write to temp state file, validate content, then replace original with atomic rename.
  - [ ] `COMMIT4_SHA=$NEW_COMMIT4_SHA`
  - [ ] `PHASE_8_COMMIT4_DONE=1`
  - [ ] `PHASE_9_VERIFY_DONE=1` only after Stage R7 required pass/fail gates pass.
  - [ ] Upstream comparison reports are informational only and cannot block `PHASE_9_VERIFY_DONE=1`.
  - [ ] `ARTIFACT_ROOT=$RECOVERY_ARTIFACT_ROOT`
  - [ ] `INTEGRITY_CHAIN_REPORT=$RECOVERY_ROOT/integrity-chain.md`
  - [ ] `REPACK_REMOTE_SHA=$NEW_COMMIT4_SHA`
  - [ ] `PHASE_10_STOP_POINT_DONE=1`
- [ ] Append structured recovery narrative to `REPORT_FILE` atomically and idempotently.
  - [ ] Root cause: index/worktree drift from `reset --soft` + commit-from-index flow.
  - [ ] Mitigation used: explicit restaging, pre-commit drift gates, clean-ref proof runs.
  - [ ] Explicitly note that `UPSTREAM_MAIN vs COMMIT3/NEW_COMMIT4` reports are informational-only and non-blocking.
  - [ ] Record old/new capstone SHAs and report paths.
  - [ ] Include `RECOVERY_RUN_ID` marker and skip duplicate append if marker already exists.
- [ ] Persist finalization markers.
  - [ ] Set `CANONICAL_STATE_UPDATED=1`.
  - [ ] Set `REPORT_APPENDED=1`.

## Stage R10 - Exit and Rollback Preparedness
- [ ] Stage checkpointing.
  - [ ] Set `CURRENT_STAGE=R10` and atomically persist.
  - [ ] On successful completion of Stage R10, set `R10_DONE=1` and atomically persist.
- [ ] Final cleanliness checks.
  - [ ] `git status --short` is clean.
  - [ ] No active lock remains after session exit.
- [ ] Verify recovery safety refs still exist locally and on origin.
  - [ ] `RECOVERY_BACKUP_BRANCH` resolves to `OLD_COMMIT4_SHA`.
  - [ ] `RECOVERY_BACKUP_TAG` resolves to `OLD_COMMIT4_SHA`.
- [ ] Rollback path is documented in `RECOVERY_LOG`.
  - [ ] Hard rollback target: `OLD_COMMIT4_SHA`.
  - [ ] Safety rollback targets: `RECOVERY_BACKUP_BRANCH` and `RECOVERY_BACKUP_TAG`.

## Crash Window Reconciliation Rules (Mandatory on Resume)
- [ ] Window A: crash after `R6_DONE=1` and before `R7_DONE=1`.
  - [ ] Verify `HEAD == NEW_COMMIT4_SHA`.
  - [ ] Resume at Stage R7.
- [ ] Window B: crash after `R7_DONE=1` and before `PUSH_ATTEMPTED=1`.
  - [ ] Verify required reports exist.
  - [ ] Resume at Stage R8 then Stage R9.
- [ ] Window C: crash after `PUSH_ATTEMPTED=1` with unknown push outcome.
  - [ ] Fetch `origin/$REPACK_BRANCH` and compare to `NEW_COMMIT4_SHA`.
  - [ ] If equal, set `PUSH_CONFIRMED=1` and resume at Stage R9b.
  - [ ] If not equal, keep `PUSH_CONFIRMED=0` and resume at Stage R9.
- [ ] Window D: crash after push success but before canonical state/report finalization.
  - [ ] Verify `origin/$REPACK_BRANCH == NEW_COMMIT4_SHA`.
  - [ ] Resume at Stage R9b only (do not rebuild/reverify/push again).
- [ ] Window E: crash after canonical state update but before report append (or inverse).
  - [ ] Reconcile idempotently using `CANONICAL_STATE_UPDATED` and `REPORT_APPENDED` flags.
  - [ ] Complete only missing finalization sub-step and then continue to Stage R10.

## Mandatory Stop Conditions
- [ ] Stop immediately if branch is not at expected four-commit topology over `UPSTREAM_MAIN_PIN`.
- [ ] Stop immediately if staged set is not exact for capstone.
- [ ] Stop immediately if verifier policy markers are missing after edits.
- [ ] Stop immediately if `diff-commit3-vs-commit4.txt` reports differences under configured policy.
- [ ] Stop immediately if `capstone-repro-commit4.txt` reports differences under configured policy.
- [ ] Do not stop due solely to differences reported in `diff-upstream-main-vs-commit3.txt`.
- [ ] Do not stop due solely to differences reported in `diff-upstream-main-vs-commit4.txt`.
- [ ] Stop immediately if `--force-with-lease` cannot prove expected remote SHA.
- [ ] Stop immediately if any attempt is made to push with plain `--force` or with no explicit lease target.
- [ ] Stop immediately if `RECOVERY_STATE_FILE` is missing required immutable keys or cannot be parsed.
- [ ] Stop immediately if `PUSH_CONFIRMED=1` but `origin/$REPACK_BRANCH != NEW_COMMIT4_SHA`.
- [ ] Stop immediately if canonical `STATE_FILE` was updated before push confirmation.
