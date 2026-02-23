# Execute Critique Remediation (Resumable, Traceability-Strict)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-14-critique-remediation-plan.md`

with dependency alignment to:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-14-iso26262-traceability-anchor-plan.md`

using:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`
- `$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py`

## Inputs

- Optional `RUN_ID` (resume exact run root if provided).
- Optional `MAX_STAGES` (default `1`; execute one stage per invocation).
- Optional `START_STAGE` (force start at a specific incomplete stage).

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Select run root:
   - If `RUN_ID` is provided, use `$OPENCODE_CONFIG_DIR/reports/critique-remediation-$RUN_ID`.
   - Else locate newest incomplete `$OPENCODE_CONFIG_DIR/reports/critique-remediation-*`.
   - If none exists, bootstrap from resumable templates.
3. Ensure run files exist:
   - `state.env`
   - `checklist.state.env`
   - `run.log`
   - `artifacts/`
4. Enforce lock discipline with `state.env:LOCK_FILE`:
   - stop on active lock
   - reconcile stale lock and continue
   - release lock on all exits
5. Validate immutable contract before mutation:
   - `REPO_ROOT`, `PLAN_PATH`, `TARGET_BRANCH`, `BASE_PIN_SHA`
   - traceability dependency plan path is present and readable
6. Reconcile stage model:
   - Use canonical remediation stages `CR0..CR12`
   - If legacy `S*` state is detected, migrate to `CR*` stage keys before continuing
   - Resume from earliest incomplete safe stage unless `START_STAGE` is valid
7. Enforce dependency gate before and during execution:
   - Source-embedded correlation remains canonical
   - Statement-level source anchoring invariants remain enforced
8. Execute stages in order with strict gates:
   - Do not mark a stage done until required artifacts exist
   - Do not skip CR8/CR9 statement instrumentation stages
9. Enforce statement-level requirements at CR8 and CR9:
   - every statement has `source_id`
   - every statement has `trace_status`
   - mapped statements resolve to valid anchor IDs
10. Enforce integrated validation at CR10:
   - run traceability validators
   - run `uv run python make.py validate`
   - run `uv run python make.py build`
   - run `uv run python make.py verify`
11. Enforce reporting at CR11:
   - generate run-scoped JSON report
   - generate run-scoped Markdown report
   - update latest JSON/Markdown pointers under `$OPENCODE_CONFIG_DIR/reports/`
12. Use atomic state updates only:
   - `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" update ...`
13. Stop after `MAX_STAGES` and return deterministic resume data.

## Stage map

- `CR0`: bootstrap and contracts
- `CR1`: critique claim normalization
- `CR2`: structural backbone rewrite
- `CR3`: ISO fidelity corrections
- `CR4`: Rust language corrections
- `CR5`: library inventory and hazard taxonomy corrections
- `CR6`: tooling and qualification corrections
- `CR7`: verification/profile coherence
- `CR8`: modified-file traceability reconciliation
- `CR9`: full-document statement instrumentation freeze
- `CR10`: integrated validation gate
- `CR11`: reporting and remediation backlog
- `CR12`: closeout and handoff

## Mandatory closeout outputs

- `$OPENCODE_CONFIG_DIR/reports/critique-remediation-<run-id>/critique-traceability-remediation-report.json`
- `$OPENCODE_CONFIG_DIR/reports/critique-remediation-<run-id>/critique-traceability-remediation-report.md`
- `$OPENCODE_CONFIG_DIR/reports/critique-traceability-remediation-report-latest.json`
- `$OPENCODE_CONFIG_DIR/reports/critique-traceability-remediation-report-latest.md`

## Required output format

- `RUN_ID`
- `RUN_ROOT`
- `CURRENT_STAGE` before and after
- stages completed this invocation
- statement-level traceability counts (`total`, `mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`)
- artifacts created/updated (paths)
- blockers/stop conditions (if any)
- exact next resume command or prompt invocation hint
