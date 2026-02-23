# Execute ISO 26262 Traceability Plan (Resumable)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-14-iso26262-traceability-anchor-plan.md`

using:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`
- `$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py`

## Inputs

- Optional `RUN_ID` (resume exact run root if provided).
- Optional `MAX_STAGES` (default `1`; execute one stage per invocation).
- Optional `START_STAGE` (force start at specific incomplete stage).

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Select run root:
   - If `RUN_ID` is provided, use `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-$RUN_ID`.
   - Else locate newest incomplete `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-*`.
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
   - `SOURCE_PDFSET_ID`, `P06_SHA256`, `P08_SHA256`, `P09_SHA256`
6. Reconcile resume state:
   - if any stage done with incomplete checklist, resume that stage
   - else resume earliest incomplete stage (or `START_STAGE` if valid)
7. Execute stages in order (`S0..S9`) with stage gates and mandatory artifacts.
8. Enforce source-embedded correlation invariants continuously:
   - canonical links stay embedded in source markdown/YAML
   - no manual tracked mapping file set becomes canonical
9. Enforce statement-level anchoring at `S8` and final gate:
   - every statement has `source_id`
   - every statement has `trace_status`
   - mapped statements resolve to valid ISO anchors
10. Enforce final reporting at `S9`:
    - run-scoped JSON/Markdown statement coverage reports
    - latest pointer JSON/Markdown reports under `$OPENCODE_CONFIG_DIR/reports/`
11. Use atomic state updates only:
    - `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" update ...`
12. Stop after `MAX_STAGES` and return deterministic resume details.

## Stage map

- `S0`: bootstrap run and immutable contract
- `S1`: ISO decomposition and baseline inventory
- `S2`: schema and contract finalization
- `S3`: tooling foundation
- `S4`: seed ISO hierarchy
- `S5`: embed source metadata
- `S6`: build reverse indexes and lookup workflows
- `S7`: docgen trace surfacing
- `S8`: full source instrumentation freeze
- `S9`: validation, reporting, and closeout

## Mandatory closeout outputs

- `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-<run-id>/traceability-statement-coverage.json`
- `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-<run-id>/traceability-statement-coverage.md`
- `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.json`
- `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.md`

## Required output format

- `RUN_ID`
- `RUN_ROOT`
- `CURRENT_STAGE` before and after
- stages completed this invocation
- statement-level traceability counts (`total`, `mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`)
- artifacts created/updated (paths)
- blockers/stop conditions (if any)
- exact next resume command or prompt invocation hint
