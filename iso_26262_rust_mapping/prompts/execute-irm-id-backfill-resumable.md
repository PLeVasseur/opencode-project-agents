# Execute IRM ID Backfill and Extension Decomposition (Resumable)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-15-source-id-full-backfill-and-generator-plan.md`

using:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`

## Inputs

- Optional `RUN_ID`.
- Optional `MAX_STAGES` (default `1`; run one stage per invocation).
- Optional `START_STAGE` (must not skip required earlier incomplete stages).
- Optional `BASE_BRANCH` (default `main`).

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Resolve run root deterministically:
   - If `RUN_ID` provided: `$OPENCODE_CONFIG_DIR/reports/irm-id-full-backfill-$RUN_ID`.
   - Else resume newest incomplete `$OPENCODE_CONFIG_DIR/reports/irm-id-full-backfill-*`.
   - Else create new run id with `date -u +%Y%m%dT%H%M%SZ`.
3. Bootstrap/validate durable run files before mutation:
   - `state.env`, `checklist.state.env`, `run.log`, `artifacts/`.
4. Apply resumable-execution lock discipline:
   - stop on active lock,
   - reconcile stale lock and log details,
   - release lock on all exits.
5. Validate immutable contract before mutating:
   - `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`, `ARTIFACT_ROOT`, `LOCK_FILE`,
   - `BASE_BRANCH`, `TARGET_BRANCH`, expected pre-mutation `HEAD` pin.
6. Enforce terminology policy in all new/changed user-facing text:
   - use `IRM ID` / `ISO 26262 Rust Mapping ID`,
   - treat `source_id` as legacy wording only for explicit migration tasks.
7. Enforce stage semantics exactly:
   - `S1`: safe refactor only (no behavior changes),
   - `S2`: checker implementation in shadow/report mode (no hard fail on legacy),
   - `S3`: tooling introduction (`generate_irm_ids.py`, `backfill_irm_ids.py`),
   - `S4`: one-time cutover apply + strict hard-fail gates.
8. Enforce anchor policy:
   - paragraph/list anchors use exact IRM ID (`irm_...`) strings,
   - duplicate anchors are hard errors.
9. Enforce no wrapper-scope creep:
   - do not add a separate `paragraph-id-check.py` operator wrapper script.
10. Enforce strict-cutover timing:
    - strict rejection of `SRCN-*` and `source_id` schema/runtime keys only turns on at `S4`.
11. Persist required artifacts and stage gates before marking stages done.
12. Use atomic state updates for `state.env` and `checklist.state.env`.
13. Stop after `MAX_STAGES` and return deterministic resume details.

## Stage map

- `S1`: extension decomposition and lint decomposition (safe refactor).
- `S2`: `paragraph_id_check.py` shadow mode + IRM regex/duplicate/ref checks.
- `S3`: implement `generate_irm_ids.py` and `backfill_irm_ids.py` with dry-run mapping artifacts.
- `S4`: apply full backfill, migrate `source_id -> irm_id`, enforce strict gates, docs/schema cutover.

## Mandatory stage artifacts

- `S1`: `artifacts/s1/refactor-manifest.json`, `artifacts/s1/s1-verify.log`
- `S2`: `artifacts/s2/paragraph-id-check-shadow.json`, `artifacts/s2/s2-verify.log`
- `S3`: `artifacts/s3/generator-smoke.log`, `artifacts/s3/backfill-dry-run-summary.json`
- `S4`: `artifacts/s4/id-mapping.json`, `artifacts/s4/rewrite-summary.json`, `artifacts/s4/validation-summary.json`

For every required artifact, log SHA256 and file size in `run.log`.

## Commit strategy (logical and reviewable)

1. `refactor(iso26262-spec): split extension into focused modules with thin __init__ wiring`
2. `refactor(iso26262-spec-lints): split lint checks and add paragraph_id_check shadow mode`
3. `feat(traceability): add IRM ID generator templates for {dp} and {ts}`
4. `feat(traceability): add IRM ID backfill tooling with dry-run mapping artifacts`
5. `chore(traceability): apply one-time IRM ID backfill across markdown, tables, and references`
6. `feat(traceability)!: enable strict IRM cutover and reject legacy SRCN/source_id metadata`
7. `docs(traceability): rename legacy ID terminology to IRM ID and publish migration evidence`

## Required output format

- `RUN_ID`
- `RUN_ROOT`
- `TARGET_BRANCH`
- `CURRENT_STAGE` before and after
- stages completed this invocation
- commits created this invocation (`sha`, `subject`)
- artifact paths created/updated
- strict gate status (`validate`, `build`, `trace-validate`, `black`, `flake8`)
- blockers/stop conditions (if any)
- exact next resume command/prompt invocation
