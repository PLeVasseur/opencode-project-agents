---
name: resumable-execution
description: Execute multi-stage plans with durable state, crash-safe resume, and idempotent closeout.
compatibility: opencode
metadata:
  audience: maintainers
  category: process
  workflow: durable-run
---

## What I do

- Provide a reusable workflow for long-running or high-risk tasks that may span multiple sessions.
- Enforce a transaction-like model: immutable contract, stage gates, atomic state persistence, resume reconciliation, and idempotent finalization.
- Reduce drift during multi-phase execution by requiring explicit completion checks and artifact capture.

## When to use me

- Multi-stage plans where interruption is likely.
- Tasks with strict stop conditions and non-trivial verification gates.
- Any run where progress must be recoverable without redoing completed steps.

## Run layout

- Create one run root per execution:
  - `$OPENCODE_CONFIG_DIR/reports/<task>-<run-id>/`
- Keep durable files inside the run root:
  - `state.env` (machine state)
  - `checklist.state.env` (required child checks)
  - `run.log` (human-readable timeline)
  - `artifacts/` (reports, diffs, evidence)
- Keep temporary files under `$OPENCODE_CONFIG_DIR/`, never in the repo.

## Starter templates

- Bootstrap run files from:
  - `$OPENCODE_CONFIG_DIR/skills/resumable-execution/run-state.template.env`
  - `$OPENCODE_CONFIG_DIR/skills/resumable-execution/checklist-state.template.env`
- Fill immutable contract keys before any mutating action.
- Add task-specific `CB_<STAGE>_<ITEM>` keys before executing each stage.
- Keep keys explicit (`0` or `1`); never infer completion from missing keys.

## Quick bootstrap (3 commands)

```bash
TASK=<task>
RUN_ID=$(date -u +%Y%m%dT%H%M%SZ)
RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/${TASK}-${RUN_ID}"
mkdir -p "$RUN_ROOT/artifacts" && cp "$OPENCODE_CONFIG_DIR/skills/resumable-execution/run-state.template.env" "$RUN_ROOT/state.env" && cp "$OPENCODE_CONFIG_DIR/skills/resumable-execution/checklist-state.template.env" "$RUN_ROOT/checklist.state.env"
```

- In `state.env`, set at minimum: `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`, `ARTIFACT_ROOT`, and `LOCK_FILE`.
- In `checklist.state.env`, add required task-specific gates for each stage.

## Single-writer discipline

- Use a lock file with `pid`, `host`, `user`, and timestamp metadata.
- If lock is active and valid, stop immediately.
- If lock is stale, append lock contents to `run.log`, then replace lock.
- Remove lock on normal and failure exit.

## Immutable contract first

- Persist immutable intent before stage mutations:
  - repo root, branch, base pin, expected old SHA, plan path, and report targets
- Validate immutable contract on resume.
- If immutable values drift, stop and start a new run.

## Atomic state persistence

- Never edit state files in place.
- Write to `*.tmp`, parse-check, then atomically rename.
- Track both stage state and checklist state.
- Use explicit schema keys:
  - `STATE_SCHEMA_VERSION`
  - `CHECKLIST_SCHEMA_VERSION`

## Stage and checklist gates

- Maintain one stage pointer (`CURRENT_STAGE`) and per-stage done flags (`S*_DONE=1`).
- Mirror required child checks with explicit keys (`CB_<STAGE>_<ITEM>=1`).
- A stage is complete only when all required child checks are complete.
- Forbid setting `S*_DONE=1` when required checklist keys are incomplete.

## Crash-resume reconciliation

- Define resume windows before execution starts:
  - before mutation
  - after mutation, before verification
  - push attempted with unknown outcome
  - push confirmed, finalization incomplete
- Reconcile by observing real state (HEAD, remote SHA, artifacts), then continue from the earliest incomplete safe stage.
- Never rerun completed destructive stages unless reconciliation proves it is necessary.

## Idempotent finalization

- Finalization updates are post-confirmation only.
- Append summary blocks with a unique run marker (`RUN_ID`) and skip duplicates on resume.
- Track finalization flags explicitly:
  - `CANONICAL_STATE_UPDATED=1`
  - `REPORT_APPENDED=1`
  - `RUN_SUMMARY_UPDATED=1`

## Mandatory stop conditions

- Dirty worktree at a mutation boundary.
- Remote drift from expected lease target.
- Missing or unparsable state/checklist files.
- Stage marked done while required checklist keys are incomplete.
- Missing required artifacts for the current stage gate.

## Recommended execution flow

1. Bootstrap run root and acquire lock.
2. Initialize or resume durable state.
3. Validate immutable contract and stop conditions.
4. Execute stage-by-stage with checklist gates.
5. Verify outputs and capture artifacts.
6. Push with explicit lease where required.
7. Finalize idempotently and release lock.
