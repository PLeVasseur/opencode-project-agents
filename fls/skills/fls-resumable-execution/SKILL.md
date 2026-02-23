---
name: fls-resumable-execution
description: Execute multi-stage, high-risk plans with durable state, crash-safe resume, and rollback readiness.
compatibility: opencode
metadata:
  audience: maintainers
  category: process
  workflow: durable-run
---

## What I do

- Provide a reusable way of work for long-running or high-risk operations that may span multiple sessions.
- Encode a transaction-like execution model: immutable contract, stage gates, atomic state persistence, crash-resume reconciliation, and idempotent finalization.
- Reduce unsafe improvisation during rewrites, restacks, migrations, or multi-step verification runs.

## When to use me

- Branch rewrites, restacks, or other history-mutating operations.
- Multi-stage plans with strict invariants and explicit stop conditions.
- Any task where a session may be interrupted and must resume safely.

## Run layout

- Create one run root per execution:
  - `$OPENCODE_CONFIG_DIR/reports/<task>-<run-id>/`
- Keep durable files inside the run root:
  - `state.env` (machine state)
  - `checklist.state.env` (required child checks)
  - `run.log` (human-readable timeline)
  - `artifacts/` (reports, diffs, manifests)
- Keep temporary files under `$OPENCODE_CONFIG_DIR/`, never in the repo.

## Starter templates

- Bootstrap run files from:
  - `skills/fls-resumable-execution/run-state.template.env`
  - `skills/fls-resumable-execution/checklist-state.template.env`
- Fill immutable contract keys before any mutating action.
- Add task-specific `CB_<STAGE>_<ITEM>` keys before running each stage.
- Keep keys explicit (`0` or `1`); do not infer completion from missing keys.

## Quick bootstrap (3 commands)

```bash
TASK=<task>; RUN_ID=$(date -u +%Y%m%dT%H%M%SZ); RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/${TASK}-${RUN_ID}"
mkdir -p "$RUN_ROOT/artifacts" && cp "$OPENCODE_CONFIG_DIR/skills/fls-resumable-execution/run-state.template.env" "$RUN_ROOT/state.env" && cp "$OPENCODE_CONFIG_DIR/skills/fls-resumable-execution/checklist-state.template.env" "$RUN_ROOT/checklist.state.env"
${EDITOR:-vi} "$RUN_ROOT/state.env" "$RUN_ROOT/checklist.state.env"
```

- In `state.env`, set at minimum: `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `TARGET_BRANCH`, `BASE_PIN_SHA`, `EXPECTED_OLD_REMOTE_SHA`, `LOCK_FILE`, and `ARTIFACT_ROOT`.
- In `checklist.state.env`, add task-specific `CB_<STAGE>_<ITEM>` keys before stage execution begins.

## Single-writer discipline

- Use a lock file with `pid`, `host`, `user`, and timestamp metadata.
- If lock is active and valid, stop immediately.
- If lock is stale, archive lock contents to `run.log`, then replace lock.
- Remove lock on normal exit and failure exit.

## Immutable contract first

- Persist immutable intent before mutation starts:
  - repo root, target branch, remote, base pin, expected old SHA, required commit subjects, report paths
- Validate immutable contract at resume time.
- If immutable values drift, stop and open a new run.

## Atomic state persistence

- Never edit state files in place.
- Write to `*.tmp`, parse-check, then atomically rename.
- Track both stage state and checklist state.
- Use explicit schema version keys to support safe backfills:
  - `STATE_SCHEMA_VERSION`
  - `CHECKLIST_SCHEMA_VERSION`

## Stage and checklist gates

- Maintain one stage pointer (`CURRENT_STAGE`) and per-stage done flags (`S*_DONE=1`).
- Mirror required child checks with explicit keys (`CB_<STAGE>_<ITEM>=1`).
- A stage is complete only when all required child checks are complete.
- Forbid setting `S*_DONE=1` when required checklist keys are incomplete.

## Mutation safety pattern

- Before destructive steps:
  - verify clean tree and no in-progress git operations
  - fetch remotes and re-validate expected remote SHA
  - create and push rollback refs (backup branch + tag)
  - record rollback commands in `run.log`
- For rewrite pushes, use explicit lease with expected old SHA.

## Crash-resume reconciliation

- Define resume windows before execution starts:
  - before mutation
  - after mutation, before push
  - push attempted with unknown outcome
  - push confirmed, finalization incomplete
- Reconcile by observing real world state (local HEAD, remote SHA, artifacts), then continue from the earliest incomplete safe stage.
- Never rerun completed destructive stages unless reconciliation proves it is necessary.

## Idempotent finalization

- Finalization updates are post-confirmation only (for example, after push is confirmed).
- Append summary blocks with a unique run marker (`run_id`) and skip duplicates on resume.
- Mark finalization keys separately, for example:
  - `CANONICAL_STATE_UPDATED=1`
  - `REPORT_APPENDED=1`
  - `RUN_SUMMARY_UPDATED=1`

## Mandatory stop conditions

- Dirty worktree at a mutation boundary.
- Remote SHA drift from expected lease target.
- PR head owner/branch/SHA mismatch (when operating on a PR head).
- Missing or unparsable state/checklist files.
- Stage marked done without required checklist completion.
- Missing required artifacts for the current gate.

## Recommended execution flow

1. Bootstrap tools/env and acquire lock.
2. Initialize or resume durable run state.
3. Validate immutable contract and stop conditions.
4. Execute stage-by-stage with checklist gates.
5. Perform destructive step only after backup refs exist.
6. Verify outputs and capture artifacts.
7. Push with explicit lease where required.
8. Finalize idempotently and release lock.

## References

- `AGENTS.md`
- `skills/fls-resumable-execution/run-state.template.env`
- `skills/fls-resumable-execution/checklist-state.template.env`
- `$OPENCODE_CONFIG_DIR/plans/`
- `$OPENCODE_CONFIG_DIR/reports/`
