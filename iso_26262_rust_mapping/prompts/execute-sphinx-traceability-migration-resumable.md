# Execute Sphinx Traceability Migration (Kickoff + Resume + Crash-Recovery)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-15-sphinx-traceability-migration-plan.md`

with alignment to:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-14-iso26262-traceability-anchor-plan.md`
- `$OPENCODE_CONFIG_DIR/plans/2026-02-14-critique-remediation-plan.md`

using:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`
- `$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py`
- `$OPENCODE_CONFIG_DIR/reports/tooling/bootstrap_sphinx_migration_run.py`
- `$OPENCODE_CONFIG_DIR/reports/tooling/record_phase_commit.py`
- `$OPENCODE_CONFIG_DIR/reports/schemas/paragraph-ids.schema.json`

## Inputs

- Optional `RUN_ID`.
- Optional `MAX_STAGES` (default `1`).
- Optional `START_STAGE`.
- Optional `BASE_BRANCH` (default `main`).

## Operating modes

- `kickoff-new`: no `RUN_ID`, no incomplete run exists.
- `kickoff-explicit`: `RUN_ID` provided but run root does not exist yet.
- `resume-auto`: no `RUN_ID`, newest incomplete run exists.
- `resume-explicit`: `RUN_ID` provided and run root exists.

Mode must be auto-detected and reported in output.

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Resolve run root deterministically:
   - If `RUN_ID` provided, use `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-$RUN_ID`.
   - Else scan `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-*`.
   - Run is incomplete if any of: `M14_DONE!=1`, `M14_CHECKLIST_DONE!=1`, missing `artifacts/summary.md`, missing commit-ledger artifacts, missing required closeout reports.
   - Pick newest incomplete by parsed run-id timestamp; fallback to filesystem `mtime` when parse fails.
   - If none incomplete, create new run id with `date -u +%Y%m%dT%H%M%SZ`.
3. Kickoff bootstrap for new runs:
   - run `uv sync` in repository root,
   - set `BASE_BRANCH="${BASE_BRANCH:-main}"`,
   - set `CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"`,
   - if `CURRENT_BRANCH==BASE_BRANCH`, create/switch `TARGET_BRANCH="docs/iso26262-sphinx-traceability-migration-$RUN_ID"`; else `TARGET_BRANCH="$CURRENT_BRANCH"`,
   - run `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/bootstrap_sphinx_migration_run.py" --repo-root "$REPO_ROOT" --run-id "$RUN_ID" --base-branch "$BASE_BRANCH" --target-branch "$TARGET_BRANCH"`,
   - treat bootstrap helper failure (`TARGET_BRANCH==BASE_BRANCH`) as hard stop,
   - capture emitted `RUN_ROOT` and use it for all state/checklist/log paths.
4. Resume bootstrap for existing runs:
   - ensure `state.env`, `checklist.state.env`, `run.log`, `artifacts/` exist,
   - load `TARGET_BRANCH` from `state.env`,
   - if current branch differs, checkout `TARGET_BRANCH`.
5. Enforce lock discipline with `state.env:LOCK_FILE`:
   - stop on active valid lock,
   - validate lock payload fields: `pid`, `host`, `user`, `run_id`, `acquired_at_utc`,
   - on stale lock, append stale payload to `run.log` before replacement,
   - release lock on all exits (success and failure paths).
6. Validate immutable contract before mutation:
   - `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`,
   - `ARTIFACT_ROOT`, `LOCK_FILE`, `REPORT_FILE`, `TARGET_REMOTE`, `BASE_BRANCH`, `TARGET_BRANCH`, `BASE_PIN_SHA`,
   - `COMMIT_LEDGER_FILE`, `COMMIT_LEDGER_JSON_FILE`,
   - `TRACEABILITY_PLAN_PATH`, `CRITIQUE_PLAN_PATH`,
   - `SOURCE_PDFSET_ID`, `P06_SHA256`, `P08_SHA256`, `P09_SHA256`,
   - `SPHINX_VERSION_PIN`, `MYST_VERSION_PIN`.
7. Reconcile stage/checklist schema:
   - canonical stages are `M0..M14`,
   - all done/checklist keys are explicit `0|1`,
   - remove/ignore legacy `S*` keys,
   - ensure required `CB_M*_*` keys exist.
8. Reconcile crash windows before executing stages:
   - if stage is marked done but required artifact missing, reopen stage,
   - if stage checklist incomplete, reopen stage,
   - if phase commit exists but ledger entry missing, record with `record_phase_commit.py`,
   - choose earliest incomplete safe stage unless `START_STAGE` is valid and not beyond earliest incomplete safe stage.
9. Enforce branch and phased-commit discipline:
   - mutating work runs only on `TARGET_BRANCH`,
   - `TARGET_BRANCH!=BASE_BRANCH` for `M1..M14`,
   - phase commits occur at required checkpoints and are ledgered via `record_phase_commit.py`,
   - commit messages use Conventional Commits and remain logically scoped.
10. Enforce immediate cutover policy:
    - no dual-run mode,
    - no legacy placeholder compatibility,
    - fail if canonical source contains `{{TABLE:`, `{{PAGE_BREAK}}`, `{{BLANK}}`.
11. Enforce FLS-style trace contract:
    - every markdown paragraph/list-item statement unit carries `dp` and `ts`,
    - granularity is paragraph/list-item/cell-entry (not sentence-level),
    - metadata preface is directly above bound markdown statement unit,
    - table cell-entry units satisfy equivalent `_trace` / `cell_trace` metadata requirements (`source_id`, `trace_status`),
    - markdown mapped statements include `a` and `rel`; YAML mapped statements include `anchor_ids[]`.
12. Enforce table schema + semantics:
    - trace-aware schema updates in `table_common` and per-table schemas,
    - `row_id` required for trace-exported rows,
    - traceable mapping tables use `iso-table` (not native MyST table directives),
    - row/cell precedence has no inheritance fallback and no double-count overlap.
13. Enforce strict build/lint/trace gates:
    - warnings-as-errors,
    - `env-check-consistency` lint gate,
    - `uv run python make.py trace-validate` passes,
    - failed `trace-validate` runs write diagnostics to `artifacts/validation/trace-validate.log`,
    - paragraph-ID export uses in-memory preface/trace bindings (not raw line scan),
    - table-derived paragraph-ID records use `<table_label>--r-<row_id>--c-<col_key>`,
    - `paragraph-ids.json` checks run against `reports/schemas/paragraph-ids.schema.json`,
    - no-leak and report-schema checks pass.
14. Use atomic state updates only:
    - `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" write <file> key=value ...`
    - `python3 "$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py" update <file> key=value ...`
15. Stop after `MAX_STAGES` and return deterministic resume details.

## Phase commit checkpoints

- `C01` (`M2`): `build(sphinx): scaffold sphinx project and strict config`
- `C02` (`M3`): `feat(traceability): convert source placeholders to myst directives and metadata preface syntax`
- `C03` (`M4-M5`): `feat(traceability): add fls-style trace domain and statement-unit instrumentation enforcement`
- `C04` (`M6`): `feat(traceability): integrate yaml iso-table directive and table trace validators`
- `C05` (`M7-M8`): `feat(traceability): enforce anchor integrity and strict lint consistency gates`
- `C06` (`M9-M10`): `feat(traceability): add coverage exports and make.py sphinx orchestration contract`
- `C07` (`M11-M12`): `docs(remediation): execute critique-aligned updates with instrumentation freeze`
- `C08` (`M13-M14`): `docs(migration): finalize cutover, closeout reports, and legacy retirement`

## Stage map

- `M0`: bootstrap and contract pinning
- `M1`: baseline capture and migration readiness
- `M2`: Sphinx skeleton and dependency pinning
- `M3`: immediate source conversion to MyST contracts
- `M4`: FLS-style domain, IDs, and role scaffold
- `M5`: statement segmentation and markdown instrumentation enforcement
- `M6`: YAML table traceability and `iso-table` integration
- `M7`: ISO anchor registry and reference integrity
- `M8`: lints and strict consistency gate
- `M9`: report generation and reverse index generation
- `M10`: `make.py` orchestration contract completion
- `M11`: critique remediation execution within Sphinx gates
- `M12`: full-document instrumentation freeze
- `M13`: integrated validation and HTML quality gates
- `M14`: canonical cutover closeout and legacy retirement

## Mandatory closeout outputs

- `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/traceability-statement-coverage.json`
- `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/traceability-statement-coverage.md`
- `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.json`
- `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.md`
- `build/html/paragraph-ids.json`
- `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/artifacts/commits/commit-ledger.md`
- `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/artifacts/commits/commit-ledger.json`
- `$OPENCODE_CONFIG_DIR/reports/sphinx-traceability-migration-<run-id>/artifacts/summary.md`

## Required output format

- `MODE` (`kickoff-new`, `kickoff-explicit`, `resume-auto`, `resume-explicit`)
- `RUN_ID`
- `RUN_ROOT`
- `BASE_BRANCH` and `TARGET_BRANCH`
- `CURRENT_STAGE` before and after
- stages completed this invocation
- phase commits created this invocation (`sha`, `subject`, `stage_checkpoint`)
- statement-level traceability counts (`total`, `mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`)
- statement-unit export counts by source (`markdown_preface_units`, `table_cell_units`, `table_row_units`)
- artifacts created/updated (paths)
- blockers/stop conditions (if any)
- exact next resume command or prompt invocation hint
