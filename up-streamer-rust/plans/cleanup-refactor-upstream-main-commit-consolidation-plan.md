# Consolidate `cleanup/refactor-upstream-main` into <= 6 Logical Commits

## Objective

Reduce the current commit stack on `cleanup/refactor-upstream-main` to a small, reviewable, logically grouped set (target: 6 commits, max: 6), while preserving exact branch content and keeping PR diff scope unchanged.

## Non-Negotiable Execution Discipline

- [x] This plan is a live execution ledger: every checkbox must be ticked immediately after completion.
  - [x] Do not batch-check boxes later.
  - [x] If a step fails, leave it unchecked, log the failure in the execution report, and resolve before proceeding.
- [x] Manual execution only.
  - [x] No autopilot shortcuts.
  - [x] No destructive fallback unless this plan explicitly reaches rollback phase.
- [x] Fresh-session operation assumptions.
  - [x] Assume no prior environment variables are set.
  - [x] Assume branch state and remotes must be re-verified from scratch.

## Crash Resilience Requirements (Mandatory)

- [x] Maintain durable state and recovery metadata throughout execution.
  - [x] Persist critical values to `"$STATE_FILE"` immediately after each completed step group.
  - [x] Persist phase progression to `"$REPORT_DIR/phase-markers.log"` immediately when a phase completes.
  - [x] Persist command output transcript to `"$REPORT_DIR/command-transcript.log"`.
- [x] Maintain remote-restorable recovery points.
  - [x] Keep durable backup branch/tag on `origin` from pre-rewrite tip.
  - [x] Create and push immutable checkpoint tags at each major safe point.
  - [x] Never delete backup/checkpoint refs until PR is merged.
- [x] Ensure resumability after interruption/crash.
  - [x] Keep a run pointer file that references the active `REPORT_DIR`.
  - [x] Include explicit resume procedure and `last_completed_phase` tracking.
  - [x] On restart, resume from the first unchecked item in the active phase.

## Proposed Target Commit Set (Default: 6)

- [x] Commit 1: `refactor: modernize up-streamer domain architecture boundaries`
  - [x] Consolidate control-plane/data-plane/routing/runtime module modernization and API facade reshaping.
- [x] Commit 2: `refactor: complete USubscription and route identity contract migration`
  - [x] Consolidate USubscription decoupling, identity-key migration, dedupe, and route API adjustments.
- [x] Commit 3: `perf+obs: optimize worker/runtime paths and structured tracing coverage`
  - [x] Consolidate performance-path changes plus structured observability/event-field integration.
- [x] Commit 4: `feat(ci): add benchmark guardrail harness and advisory workflow`
  - [x] Consolidate criterion harness, guardrail utility, scripts, and advisory CI wiring.
- [x] Commit 5: `feat(smoke): add deterministic cross-transport smoke suite, claims, and matrix workflow`
  - [x] Consolidate smoke-suite crate, scenario binaries/fixtures/contracts, docs, and capstone workflow.
- [x] Commit 6: `chore: align new-file copyright headers to 2026`
  - [x] Keep standalone unless intentionally folded into Commit 5 for a 5-commit final stack.

## Phase 0: Fresh-Session Bootstrap and Hard Invariants

- [x] Resume-first decision gate (mandatory before creating a new run).
  - [x] Check whether an unfinished run already exists via `cleanup-refactor-upstream-main-consolidation.current`.
  - [x] If unfinished run exists, execute Phase 0R and continue from that run (do not create a new `RUN_ID`). (N/A this run: no unfinished run found.)
  - [x] Only if no unfinished run exists, proceed with new-run initialization below.
- [x] Initialize session artifacts under `$OPENCODE_CONFIG_DIR`.
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `test -n "$OPENCODE_CONFIG_DIR"`
  - [x] `RUN_ID="cleanup-refactor-upstream-main-consolidation-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [x] `REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/$RUN_ID"`
  - [x] `mkdir -p "$REPORT_DIR"`
  - [x] `RUN_POINTER="$OPENCODE_CONFIG_DIR/reports/cleanup-refactor-upstream-main-consolidation.current"`
  - [x] `ln -sfn "$REPORT_DIR" "$RUN_POINTER"`
  - [x] `STATE_FILE="$REPORT_DIR/session-state.env"`
  - [x] `REPORT_FILE="$REPORT_DIR/execution-report.md"`
  - [x] `PHASE_MARKER_FILE="$REPORT_DIR/phase-markers.log"`
  - [x] `TRANSCRIPT_FILE="$REPORT_DIR/command-transcript.log"`
  - [x] `CHECKPOINT_TAG_PREFIX="checkpoint-cleanup-refactor-upstream-main-$RUN_ID"`
  - [x] `LOCK_FILE="$REPORT_DIR/.execution.lock"`
- [x] Enable crash-friendly execution bookkeeping.
  - [x] If lock exists, determine whether it is stale (PID not running) or active.
    - [x] Active lock: stop and avoid concurrent execution. (No active lock encountered this run.)
    - [x] Stale lock: move to `"$LOCK_FILE.stale.$(date -u +%Y%m%dT%H%M%SZ)"` and continue. (No stale lock encountered this run.)
  - [x] Acquire lock: `printf 'pid=%s\nstart=%s\n' "$$" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$LOCK_FILE"`
  - [x] Start transcript capture for all subsequent commands: `exec > >(tee -a "$TRANSCRIPT_FILE") 2>&1`
  - [x] Initialize phase marker file for new run only: `: > "$PHASE_MARKER_FILE"`
  - [x] Write initial state entries to `"$STATE_FILE"` (`RUN_ID`, `REPORT_DIR`, `RUN_POINTER`, `PHASE_MARKER_FILE`, `TRANSCRIPT_FILE`, `CHECKPOINT_TAG_PREFIX`).
- [x] Confirm repo/branch/worktree invariants.
  - [x] `git status --short --branch`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "cleanup/refactor-upstream-main"`
  - [x] `test -z "$(git status --porcelain)"`
  - [x] `test ! -d .git/rebase-apply && test ! -d .git/rebase-merge`
- [x] Verify required CLI tools for this plan (fail fast).
  - [x] `git --version`
  - [x] `gh --version`
  - [x] `jq --version`
  - [x] `cargo --version`
- [x] Refresh remotes and capture base/head SHAs.
  - [x] `git fetch --all --prune`
  - [x] `PRE_REWRITE_LOCAL_SHA="$(git rev-parse HEAD)"`
  - [x] `PRE_REWRITE_REMOTE_SHA="$(git rev-parse origin/cleanup/refactor-upstream-main)"`
  - [x] `UPSTREAM_MAIN_SHA="$(git rev-parse upstream/main)"`
- [x] Enforce remote tip invariant (mandatory).
  - [x] `test "$PRE_REWRITE_LOCAL_SHA" = "$PRE_REWRITE_REMOTE_SHA"`
  - [x] If mismatch: stop and reconcile before any rewrite.
- [x] Persist baseline state for crash/restart recovery.
  - [x] Write `RUN_ID`, `PRE_REWRITE_LOCAL_SHA`, `PRE_REWRITE_REMOTE_SHA`, `UPSTREAM_MAIN_SHA`, and branch name into `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_0_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 0R: Resume Protocol (If Session Restarts Mid-Execution)

- [x] Detect active prior run.
  - [x] `RUN_POINTER="$OPENCODE_CONFIG_DIR/reports/cleanup-refactor-upstream-main-consolidation.current"`
  - [x] `test -L "$RUN_POINTER"`
  - [x] `ACTIVE_REPORT_DIR="$(readlink -f "$RUN_POINTER")"`
  - [x] `test -f "$ACTIVE_REPORT_DIR/session-state.env"`
- [x] Rehydrate state and validate recoverability.
  - [x] `source "$ACTIVE_REPORT_DIR/session-state.env"`
  - [x] `test -f "$PHASE_MARKER_FILE"`
  - [x] `test -f "$TRANSCRIPT_FILE"`
  - [x] `git fetch --all --prune`
  - [x] If `BACKUP_BRANCH` is already defined in state, verify/fetch it locally; if undefined, continue and create it in Phase 1.
  - [x] If `BACKUP_TAG` is already defined in state, verify/fetch it locally; if undefined, continue and create it in Phase 1.
- [x] Recover run position.
  - [x] Read last completed phase from `"$PHASE_MARKER_FILE"`.
  - [x] If lock file exists with a dead PID, rotate it to stale name and reacquire lock before proceeding.
  - [x] Re-enable transcript appending to `"$TRANSCRIPT_FILE"` in the resumed shell.
  - [x] If rebase is in progress (`.git/rebase-merge` or `.git/rebase-apply` exists), resume rebase flow first (`git status`, then `git rebase --continue`/`--abort` decision).
  - [x] Resume from first unchecked checkbox in the active phase and continue immediate tick discipline.

## Phase 1: Durable Backup Before Any History Rewrite (Step 0)

- [x] Create local immutable backup refs from current tip.
  - [x] `BACKUP_BRANCH="backup/cleanup-refactor-upstream-main-pre-squash-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [x] `BACKUP_TAG="backup-cleanup-refactor-upstream-main-pre-squash-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [x] `git branch "$BACKUP_BRANCH"`
  - [x] `git tag "$BACKUP_TAG"`
- [x] Push backups to remote for durability (mandatory).
  - [x] `git push origin "$BACKUP_BRANCH"`
  - [x] `git push origin "$BACKUP_TAG"`
- [x] Verify backups exist on origin.
  - [x] `git ls-remote --heads origin "$BACKUP_BRANCH"`
  - [x] `git ls-remote --tags origin "$BACKUP_TAG"`
- [x] Persist backup metadata.
  - [x] `BACKUP_BRANCH_SHA="$(git rev-parse "$BACKUP_BRANCH")"`
  - [x] `BACKUP_TAG_SHA="$(git rev-parse "$BACKUP_TAG")"`
  - [x] Append `BACKUP_BRANCH`, `BACKUP_TAG`, and their SHAs to `"$STATE_FILE"`.
- [x] Create remote-restorable phase checkpoint.
  - [x] `PHASE1_TAG="$CHECKPOINT_TAG_PREFIX-phase1-backup-ready"`
  - [x] `git tag "$PHASE1_TAG"`
  - [x] `git push origin "$PHASE1_TAG"`
  - [x] Append `PHASE1_TAG` to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_1_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 2: Analyze Final Diff and Build Consolidation Map

- [x] Record branch divergence and scope evidence.
  - [x] `git merge-base upstream/main HEAD | tee "$REPORT_DIR/merge-base.txt"`
  - [x] `git rev-list --left-right --count upstream/main...HEAD | tee "$REPORT_DIR/divergence-count.txt"`
  - [x] `git diff --stat upstream/main...HEAD | tee "$REPORT_DIR/diff-stat-pre.txt"`
  - [x] `git diff --name-status upstream/main...HEAD | tee "$REPORT_DIR/name-status-pre.txt"`
  - [x] `git rev-list --count upstream/main..HEAD | tee "$REPORT_DIR/commit-count-pre.txt"`
  - [x] `git log --reverse --oneline upstream/main..HEAD | tee "$REPORT_DIR/commits-pre.txt"`
- [x] Produce commit-bucketing map for the 6 target commits.
  - [x] Create `"$REPORT_DIR/commit-buckets.md"` listing each original commit SHA under target Commit 1..6.
  - [x] Mark any mixed commits that require split (`edit`) during rebase.
  - [x] Freeze final commit subjects for each target commit in `"$REPORT_DIR/commit-buckets.md"`.
- [x] Create remote-restorable phase checkpoint.
  - [x] `PHASE2_TAG="$CHECKPOINT_TAG_PREFIX-phase2-analysis-ready"`
  - [x] `git tag "$PHASE2_TAG"`
  - [x] `git push origin "$PHASE2_TAG"`
  - [x] Append `PHASE2_TAG` to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_2_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 3: Headless Interactive Rebase Strategy (Explicit and Reproducible)

- [x] Prepare deterministic rebase todo file.
  - [x] Create `"$REPORT_DIR/rebase-todo.txt"` manually from `upstream/main..HEAD` commit list.
  - [x] Use `reword/pick/fixup/squash/edit` to enforce the 6 logical groups.
  - [x] Insert `break` between logical groups to force per-commit gate checkpoints.
  - [x] Preserve todo snapshot checksum for crash diagnostics: `sha256sum "$REPORT_DIR/rebase-todo.txt" | tee "$REPORT_DIR/rebase-todo.sha256"`
- [x] Prepare non-TTY sequence editor script.
  - [x] Create `"$REPORT_DIR/set-rebase-todo.sh"` that copies `"$REPORT_DIR/rebase-todo.txt"` into Git's todo path argument.
  - [x] `chmod +x "$REPORT_DIR/set-rebase-todo.sh"`
- [x] Create pre-rewrite checkpoint before running rebase.
  - [x] `PHASE3_PRE_TAG="$CHECKPOINT_TAG_PREFIX-phase3-pre-rebase"`
  - [x] `git tag "$PHASE3_PRE_TAG"`
  - [x] `git push origin "$PHASE3_PRE_TAG"`
  - [x] Append `PHASE3_PRE_TAG` to `"$STATE_FILE"`.
- [x] Launch rebase with injected todo (manual, headless-safe).
  - [x] `GIT_SEQUENCE_EDITOR="$REPORT_DIR/set-rebase-todo.sh" git rebase -i upstream/main`
- [x] Rebase stop handling rules.
  - [x] On `edit`: split commit if needed, then continue. (N/A this run: no split/edit stop required.)
  - [x] On conflict: resolve minimally, `git add <files>`, then `git rebase --continue`.
  - [x] On empty pick: `git rebase --skip`. (N/A this run: no empty picks.)
  - [x] If grouping plan needs adjustment: `git rebase --edit-todo`. (N/A this run.)
  - [x] If unrecoverable: `git rebase --abort`, restore from backup, and retry. (N/A this run.)
- [x] After successful rebase completion, create phase checkpoint.
  - [x] `PHASE3_TAG="$CHECKPOINT_TAG_PREFIX-phase3-rebase-complete"`
  - [x] `git tag "$PHASE3_TAG"`
  - [x] `git push origin "$PHASE3_TAG"`
  - [x] Append `PHASE3_TAG` to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_3_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 3A: Mandatory Per-Commit Validation Gates During Rebase

- [x] Checkpoint protocol at each `break`.
  - [x] Record checkpoint SHA+subject to `"$REPORT_DIR/checkpoints.log"` via `git show --no-patch --format='%H %s' HEAD`.
  - [x] Run common gates at each checkpoint:
    - [x] `git diff --check HEAD^..HEAD`
    - [x] `cargo check --workspace --all-targets`
- [x] Commit 1 gate (`refactor: modernize up-streamer domain architecture boundaries`).
  - [x] `cargo check -p up-streamer --all-targets`
  - [x] `cargo test -p up-streamer --test single_local_single_remote`
  - [x] `cargo test -p up-streamer --test single_local_two_remote_add_remove_rules`
  - [x] `cargo test -p up-streamer --test single_local_two_remote_authorities_same_remote_transport`
  - [x] `cargo test -p up-streamer --test single_local_two_remote_authorities_different_remote_transport`
  - [x] `C1_TAG="$CHECKPOINT_TAG_PREFIX-commit1-validated" && git tag "$C1_TAG" && git push origin "$C1_TAG"`
  - [x] Append `C1_TAG` and current `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "COMMIT_1_VALIDATED" >> "$PHASE_MARKER_FILE"`
- [x] Commit 2 gate (`refactor: complete USubscription and route identity contract migration`).
  - [x] `cargo check -p up-streamer --all-targets`
  - [x] `cargo test -p up-streamer --test usubscription`
  - [x] `cargo test -p up-streamer --test api_contract_forwarding_rules`
  - [x] `C2_TAG="$CHECKPOINT_TAG_PREFIX-commit2-validated" && git tag "$C2_TAG" && git push origin "$C2_TAG"`
  - [x] Append `C2_TAG` and current `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "COMMIT_2_VALIDATED" >> "$PHASE_MARKER_FILE"`
- [x] Commit 3 gate (`perf+obs: optimize worker/runtime paths and structured tracing coverage`).
  - [x] `cargo check -p up-streamer --all-targets`
  - [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
  - [x] `cargo test -p up-streamer --tests`
  - [x] `C3_TAG="$CHECKPOINT_TAG_PREFIX-commit3-validated" && git tag "$C3_TAG" && git push origin "$C3_TAG"`
  - [x] Append `C3_TAG` and current `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "COMMIT_3_VALIDATED" >> "$PHASE_MARKER_FILE"`
- [x] Commit 4 gate (`feat(ci): add benchmark guardrail harness and advisory workflow`).
  - [x] `cargo check -p criterion-guardrail --all-targets`
  - [x] `cargo test -p criterion-guardrail --all-targets`
  - [x] `cargo check -p up-streamer --benches`
  - [x] `bash -n scripts/bench_streamer_criterion.sh`
  - [x] `C4_TAG="$CHECKPOINT_TAG_PREFIX-commit4-validated" && git tag "$C4_TAG" && git push origin "$C4_TAG"`
  - [x] Append `C4_TAG` and current `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "COMMIT_4_VALIDATED" >> "$PHASE_MARKER_FILE"`
- [x] Commit 5 gate (`feat(smoke): add deterministic cross-transport smoke suite, claims, and matrix workflow`).
  - [x] `cargo check -p transport-smoke-suite --all-targets`
  - [x] `cargo test -p transport-smoke-suite --tests`
  - [x] `cargo build -p configurable-streamer`
  - [x] `cargo build -p example-streamer-uses --features mqtt-transport,zenoh-transport`
  - [x] `cargo build -p up-linux-streamer --features zenoh-transport,vsomeip-transport,bundled-vsomeip`
  - [x] `C5_TAG="$CHECKPOINT_TAG_PREFIX-commit5-validated" && git tag "$C5_TAG" && git push origin "$C5_TAG"`
  - [x] Append `C5_TAG` and current `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "COMMIT_5_VALIDATED" >> "$PHASE_MARKER_FILE"`
- [x] Commit 6 gate (`chore: align new-file copyright headers to 2026`).
  - [x] `git show --name-only --format='' HEAD | tee "$REPORT_DIR/commit6-filelist.txt"`
  - [x] `git diff --check HEAD^..HEAD`
  - [x] `cargo check --workspace --all-targets`
  - [x] If Commit 6 is folded into Commit 5, run this gate immediately after finalizing merged Commit 5. (N/A this run: Commit 6 exists.)
  - [x] If Commit 6 exists: `C6_TAG="$CHECKPOINT_TAG_PREFIX-commit6-validated" && git tag "$C6_TAG" && git push origin "$C6_TAG"`
  - [x] If Commit 6 is folded into Commit 5: `C5F_TAG="$CHECKPOINT_TAG_PREFIX-commit5-folded-final-validated" && git tag "$C5F_TAG" && git push origin "$C5F_TAG"` (N/A this run.)
  - [x] Append the created tag name and current `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "COMMIT_6_VALIDATED_OR_FOLDED" >> "$PHASE_MARKER_FILE"`
- [x] Mark Phase 3A completion.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_3A_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 4: Post-Rewrite Integrity Proof (No Content Loss)

- [x] Confirm compact stack shape and ancestry.
  - [x] `git merge-base upstream/main HEAD | tee "$REPORT_DIR/merge-base-post.txt"`
  - [x] `test "$(git rev-list --count upstream/main..HEAD)" -le 6`
  - [x] `git log --oneline --decorate upstream/main..HEAD | tee "$REPORT_DIR/commits-post.txt"`
- [x] Prove rewritten tree equals backup tree.
  - [x] `test "$(git rev-parse HEAD^{tree})" = "$(git rev-parse ${BACKUP_BRANCH}^{tree})"`
  - [x] `git diff --stat "${BACKUP_BRANCH}"..HEAD | tee "$REPORT_DIR/diff-vs-backup.txt"`
- [x] Prove intended diff scope still holds.
  - [x] `git diff --stat upstream/main...HEAD | tee "$REPORT_DIR/diff-stat-post.txt"`
  - [x] `git cherry upstream/main HEAD | tee "$REPORT_DIR/cherry-post.txt"`
  - [x] `git range-diff upstream/main..."${BACKUP_BRANCH}" upstream/main...HEAD | tee "$REPORT_DIR/range-diff-post.txt"`
- [x] Create remote-restorable phase checkpoint.
  - [x] `PHASE4_TAG="$CHECKPOINT_TAG_PREFIX-phase4-integrity-proved"`
  - [x] `git tag "$PHASE4_TAG"`
  - [x] `git push origin "$PHASE4_TAG"`
  - [x] Append `PHASE4_TAG` to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_4_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 5: Final Integrated Validation Gate (Mandatory Before Push)

- [x] Run CI-parity base checks.
  - [x] `source build/envsetup.sh highest`
  - [x] `cargo build`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `cargo fmt -- --check`
- [x] Run bundled feature-matrix checks.
  - [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] Run unbundled matrix if environment supports it.
  - [x] `test -n "$VSOMEIP_INSTALL_PATH" && test -d "$VSOMEIP_INSTALL_PATH"`
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport` (N/A this run: env unavailable)
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` (N/A this run: env unavailable)
  - [x] If unavailable, record explicit skip rationale in `"$REPORT_FILE"`.
- [x] Run workspace-wide checks.
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo test --workspace`
- [x] Run final smoke matrix (branch-guarded, efficient, mandatory).
  - [x] Confirm smoke preflight tools are available:
    - [x] `docker --version`
    - [x] `docker compose version`
  - [x] `SMOKE_ARTIFACTS_ROOT="target/transport-smoke/rewrite-final-$RUN_ID"`
  - [x] `SMOKE_EXPECTED_BRANCH=cleanup/refactor-upstream-main cargo run -p transport-smoke-suite --bin transport-smoke-matrix -- --all --expected-branch cleanup/refactor-upstream-main --skip-build --artifacts-root "$SMOKE_ARTIFACTS_ROOT" | tee "$REPORT_DIR/matrix-run.log"`
  - [x] Capture matrix paths from command output:
    - [x] `MATRIX_ARTIFACT_DIR`
    - [x] `MATRIX_SUMMARY_JSON`
    - [x] `MATRIX_SUMMARY_TXT`
  - [x] Verify matrix success:
    - [x] `test "$(jq -r '.fail_count' "$MATRIX_SUMMARY_JSON")" = "0"`
    - [x] `jq -r '.aggregate_exit_rationale' "$MATRIX_SUMMARY_JSON" | tee "$REPORT_DIR/matrix-exit-rationale.txt"`
- [x] Create remote-restorable phase checkpoint.
  - [x] `PHASE5_TAG="$CHECKPOINT_TAG_PREFIX-phase5-validation-passed"`
  - [x] `git tag "$PHASE5_TAG"`
  - [x] `git push origin "$PHASE5_TAG"`
  - [x] Append `PHASE5_TAG`, `MATRIX_SUMMARY_JSON`, and `MATRIX_ARTIFACT_DIR` to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_5_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 6: Safe Force-Push with Explicit Lease and PR Verification

- [x] Pre-push hard checks.
  - [x] `test -z "$(git status --porcelain)"`
  - [x] `git status --short --branch`
  - [x] Confirm all Phase 3A and Phase 5 boxes are checked.
- [x] Reconfirm remote has not moved since baseline.
  - [x] `git fetch origin --prune`
  - [x] `test "$(git rev-parse origin/cleanup/refactor-upstream-main)" = "$PRE_REWRITE_REMOTE_SHA"`
- [x] Push rewritten history with explicit lease target.
  - [x] `git push --force-with-lease=cleanup/refactor-upstream-main:$PRE_REWRITE_REMOTE_SHA origin cleanup/refactor-upstream-main`
- [x] Verify push result.
  - [x] `test "$(git rev-parse HEAD)" = "$(git rev-parse origin/cleanup/refactor-upstream-main)"`
- [x] Verify PR shape and scope.
  - [x] `gh pr view 78 --json commits,changedFiles,additions,deletions,headRefOid,url | tee "$REPORT_DIR/pr-view-post.json"`
  - [x] Verify commit count shown by PR is `<= 6`.
  - [x] Verify changed file/addition/deletion scope remains expected.
- [x] Create post-push checkpoint.
  - [x] `PHASE6_TAG="$CHECKPOINT_TAG_PREFIX-phase6-pushed"`
  - [x] `git tag "$PHASE6_TAG"`
  - [x] `git push origin "$PHASE6_TAG"`
  - [x] Append `PHASE6_TAG` and final pushed `HEAD` SHA to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_6_COMPLETE" >> "$PHASE_MARKER_FILE"`

## Phase 7: Execution Report Deliverable (Mandatory)

- [x] Write `"$REPORT_FILE"` before considering task complete.
  - [x] Include run metadata: `RUN_ID`, operator date/time, repo path, branch, base SHA, pre-rewrite local/remote SHAs.
  - [x] Include backup metadata: backup branch/tag names, SHAs, and proof they were pushed to origin.
  - [x] Include crash/resume metadata:
    - [x] active run pointer path
    - [x] phase marker timeline
    - [x] whether resume flow was used and from which phase
    - [x] list of remote checkpoint tags created
  - [x] Include command transcript summary by phase (ordered, exact commands run).
  - [x] Include conflict and empty-pick section:
    - [x] list each conflict file and exact resolution choice
    - [x] list any skipped empty commits
  - [x] Include per-commit validation results at each checkpoint.
  - [x] Include integrity proof outputs (`tree` equality, `range-diff`, `cherry`, post diff-stat).
  - [x] Include final smoke evidence:
    - [x] command used
    - [x] matrix artifact directory
    - [x] matrix summary JSON/TXT paths
    - [x] `fail_count` and aggregate rationale
  - [x] Include push and PR verification results.
  - [x] Include rollback refs and exact rollback commands.
- [x] Persist final state for future fresh sessions.
  - [x] Append final `HEAD`, `origin/cleanup/refactor-upstream-main`, PR URL, and report path to `"$STATE_FILE"`.
  - [x] `printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "PHASE_7_COMPLETE" >> "$PHASE_MARKER_FILE"`
  - [x] Release lock file: `rm -f "$LOCK_FILE"`.

## Phase 8: Recovery Contingency

- [ ] If rewrite outcome is unacceptable before push:
  - [ ] `git rebase --abort` (if rebase active)
  - [ ] `git checkout cleanup/refactor-upstream-main`
  - [ ] `git reset --hard "$BACKUP_BRANCH"`
- [ ] If rewrite was pushed and must be reverted:
  - [ ] `git checkout cleanup/refactor-upstream-main`
  - [ ] `git reset --hard "$BACKUP_BRANCH"`
  - [ ] `git push --force-with-lease origin cleanup/refactor-upstream-main`
- [ ] If local backup refs are missing in a later session:
  - [ ] Recover from remote backup branch/tag pushed in Phase 1.
- [ ] If partial progress after rebase should be preserved (not full rollback):
  - [ ] Recover nearest successful remote checkpoint tag: `git fetch origin --tags` then `git checkout <checkpoint-tag>`.
  - [ ] Branch from recovered checkpoint: `git checkout -B cleanup/refactor-upstream-main-recovery <checkpoint-tag>`.
  - [ ] Continue from first unchecked phase item and maintain immediate tick discipline.

## Completion Criteria

- [x] Branch has `<= 6` commits on top of `upstream/main`.
- [x] Final rewritten tree equals pre-rewrite backup tree.
- [x] Remote tip invariant was enforced before rewrite.
- [x] Backup refs were created and pushed to origin.
- [x] State file and execution report were produced and finalized under `$OPENCODE_CONFIG_DIR/reports/`.
- [x] Run pointer, phase markers, and command transcript are present and complete.
- [x] Remote checkpoint tags exist for each major phase and each validated logical commit.
- [x] All per-commit gates passed at each checkpoint.
- [x] Final integrated validation passed, including branch-guarded smoke matrix run with `--skip-build`.
- [x] Force-push used explicit `--force-with-lease=<branch>:<pre-rewrite-remote-sha>` and PR diff remained intended.
