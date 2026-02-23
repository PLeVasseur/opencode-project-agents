# Execute ISO 26262 Unit Boundary Pathology Remediation Repair (Resumable + One-Shot)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-16-unit-boundary-pathology-remediation-repair-plan.md`

with resumable discipline aligned to:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`
- `$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py`

## Intent

- This prompt is designed to work for both:
  - kickoff from scratch, and
  - deterministic resume of an existing run.
- If pasted with no optional inputs, it must generate a fresh `RUN_ID` and run one-shot through `EQ13` unless a mandatory stop condition triggers.

## Inputs

- Required:
  - `OPENCODE_CONFIG_DIR`

- Optional identity/run inputs:
  - `RUN_ID` (default: generate `pr1-<UTC timestamp>`)
  - `BASELINE_RUN_ID` (default: `pr1-20260215T221903Z`)
  - `MAX_STAGES` (default: `all`)
  - `START_STAGE` (default: earliest incomplete safe stage)
  - `MODE` (default: `licensed_local`; allowed: `licensed_local`, `fixture_ci`)
  - `PR_NUMBER` (default: `1`)
  - `PR_URL` (default: `https://github.com/PLeVasseur/iso-26262-rust-mapping/pull/1`)
  - `PDF_ROOT` (default: `$REPO_ROOT/.cache/iso26262`)
  - `AUTO_STAGE_COMMITS` (default: `1`)

- Optional path overrides:
  - `PLAN_PATH_OVERRIDE` (absolute path or `$OPENCODE_CONFIG_DIR`-relative)
  - `PROMPT_PATH_OVERRIDE` (absolute path or `$OPENCODE_CONFIG_DIR`-relative)

- Optional threshold overrides (existing + repair-wave keys):
  - `THRESHOLD_PARAGRAPH_BOILERPLATE_MAX_PCT` (default `5`)
  - `THRESHOLD_LIST_BOILERPLATE_MAX_PCT` (default `5`)
  - `THRESHOLD_TABLE_BOILERPLATE_MAX_PCT` (default `10`)
  - `THRESHOLD_TRIAD_SOURCE_SET_IDENTITY_MAX_PCT` (default `5`)
  - `THRESHOLD_PARAGRAPH_FRAGMENT_START_MAX_PCT` (default `10`)
  - `THRESHOLD_PARAGRAPH_FRAGMENT_END_MAX_PCT` (default `10`)
  - `THRESHOLD_PARAGRAPH_SINGLETON_PAGE_MAX_PCT` (default `85`)
  - `THRESHOLD_OVERSIZED_PARAGRAPH_MAX_PCT` (default `20`)
  - `THRESHOLD_UNIT_TYPE_PROVENANCE_OVERLAP_MAX_PCT` (default `10`)

## One-shot behavior

- Execute non-interactively from kickoff/resume through `EQ13` by default.
- Do not pause between stages when gates pass.
- Auto-detect kickoff/resume mode.
- If compatibility gaps are discovered in preflight (prompt/runner/metric/threshold wiring), implement required compatibility fixes in the same invocation and continue.

## Operating modes

- `kickoff-auto-pr1`: no `RUN_ID`; generate fresh `pr1-<UTC timestamp>`.
- `kickoff-explicit-pr1`: explicit `RUN_ID` provided, `pr1-*`, run root absent.
- `resume-explicit-pr1`: explicit/generated `RUN_ID`, run root present.
- `invalid-run-id`: `RUN_ID` does not start with `pr1-` (stop).

Mode must be auto-detected and reported.

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Resolve plan/prompt paths:
   - default plan path: `$OPENCODE_CONFIG_DIR/plans/2026-02-16-unit-boundary-pathology-remediation-repair-plan.md`
   - default prompt path: `$OPENCODE_CONFIG_DIR/prompts/execute-iso26262-unit-boundary-pathology-remediation-resumable.md`
   - if overrides are provided, resolve and use them.
3. Resolve and validate execution assets:
   - resolved plan path exists and matches this workflow,
   - resolved prompt path is recorded in immutable contract,
   - skill path and `state_tool.py` are readable.
4. Validate prompt/runner/plan linkage triad:
   - prompt references resolved plan,
   - runner resolves same plan/prompt pair,
   - stop on mismatch.
5. Resolve PR metadata and lock execution to PR #1 head branch.
6. Resolve `RUN_ID`:
   - if missing, generate `pr1-<UTC timestamp>`,
   - if present, require `pr1-*` prefix.
7. Resolve deterministic roots:
   - `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-extraction-quality-pr1-$RUN_ID"`
   - `QUALITY_DATA_ROOT="$REPO_ROOT/.cache/iso26262/mining/quality-runs/$RUN_ID"`
   - `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`
8. Resolve baseline:
   - use provided `BASELINE_RUN_ID`, else default `pr1-20260215T221903Z`.
9. Run mandatory preflight gate before stage mutation:
   - branch lock and PR contract checks,
   - immutable contract key checks,
   - stage model compatibility (`EQ0..EQ13`),
   - state/checklist template availability,
   - prompt/runner support for required threshold and metric keys,
   - scorecard schema support for pathology metrics,
   - goldset scorer wiring support (no proxy fallback for boundary gates).
10. Compatibility-gap auto-remediation (one-shot requirement):
    - if preflight detects missing threshold/metric/linkage wiring, implement required support before continuing,
    - write evidence artifact under `artifacts/diagnostics/compatibility-gap-remediation.json`,
    - continue in same invocation once fixed.
11. Kickoff bootstrap (new runs):
    - run `uv sync`,
    - checkout locked PR head branch,
    - create run root + artifact directories,
    - initialize `state.env` and `checklist.state.env` atomically.
12. Resume bootstrap (existing runs):
    - verify required files/dirs exist,
    - reconcile incomplete/partial stage writes safely,
    - reopen stage when done flags conflict with missing artifacts.
13. Enforce lock discipline:
    - stop on active non-stale lock,
    - log and replace stale lock,
    - release lock on all exits.
14. Enforce content-policy boundaries:
    - no verbatim in control-plane,
    - no `.cache` artifact commits,
    - fail on anti-leak violations.
15. Enforce stage evidence contract:
    - for each `EQx`, require `artifacts/evidence/EQx.implementation-evidence.json` and `artifacts/checkpoints/EQx.done.json` before done flag,
    - evidence payload includes run/stage metadata, commits/files, tests, metrics before/after/delta, artifacts, blockers.
16. Enforce stage commit contract for implementation stages (`EQ2..EQ11`):
    - require at least one stage-tagged Conventional Commit (`[EQx]`) touching implementation paths,
    - if `AUTO_STAGE_COMMITS=1`, create one qualifying stage commit after stage checks pass,
    - if `AUTO_STAGE_COMMITS=0`, stop when qualifying commit evidence is missing.
17. Execute stage order `EQ0..EQ13`:
    - `EQ0`: bootstrap and immutable contracts,
    - `EQ1`: baseline pathology inventory (report-only),
    - `EQ2`: candidate/boundary/provenance diagnostics,
    - `EQ3`: boundary goldset refresh,
    - `EQ4`: root-cause classification + metric-contract freeze,
    - `EQ5`: paragraph boundary remediation,
    - `EQ6`: list marker/continuation remediation,
    - `EQ7`: table scope/cell remediation + shard hygiene,
    - `EQ8`: scope extraction + anchor strictness,
    - `EQ9`: selector isolation + early contamination suppression,
    - `EQ10`: harness/threshold wiring + metric bounds checks,
    - `EQ11`: end-to-end rerun + strict verify audits,
    - `EQ12`: hard acceptance gate,
    - `EQ13`: finalize.
18. Enforce EQ12 hard gates per part (`P06`,`P08`,`P09`) and overall aggregate:
    - all legacy remediation hard gates,
    - `RESIDUAL_LEGAL_BOILERPLATE_HIT_COUNT == 0`,
    - `triad_source_set_identity_rate_pct <= THRESHOLD_TRIAD_SOURCE_SET_IDENTITY_MAX_PCT`,
    - `paragraph_fragment_start_rate_pct <= THRESHOLD_PARAGRAPH_FRAGMENT_START_MAX_PCT`,
    - `paragraph_fragment_end_rate_pct <= THRESHOLD_PARAGRAPH_FRAGMENT_END_MAX_PCT`,
    - `paragraph_singleton_page_rate_pct <= THRESHOLD_PARAGRAPH_SINGLETON_PAGE_MAX_PCT`,
    - `oversized_paragraph_rate_pct <= THRESHOLD_OVERSIZED_PARAGRAPH_MAX_PCT`,
    - `unit_type_provenance_overlap_rate_pct <= THRESHOLD_UNIT_TYPE_PROVENANCE_OVERLAP_MAX_PCT`,
    - all percent metrics in `[0,100]`.
19. Enforce boundary goldset gates at EQ12 using scorer artifact (not proxies):
    - `paragraph_boundary_f1 >= 0.90`,
    - `list_boundary_f1 >= 0.92`,
    - `table_cell_boundary_f1 >= 0.92`.
20. Enforce integrity gates before finalize:
    - active shard set equals manifest set for required parts,
    - anchor registry set equals active manifest-listed corpus anchor set,
    - final summary evidence paths all exist.
21. Run lint for touched Python files before completion:
    - `uvx black . --check --diff --color`
    - `uvx flake8 . --exclude .venv`
22. Default stop behavior:
    - continue until all stages complete,
    - if `MAX_STAGES` numeric, stop after that many completed stages.
23. On any mandatory stop condition, stop immediately with deterministic resume hint.

## Mandatory stop conditions

- Active lock by another process.
- Invalid run ID scope (`not pr1-*`).
- Branch drift from locked PR head branch.
- Immutable contract drift.
- Prompt/plan linkage mismatch.
- Runner resolved plan/prompt mismatch.
- Stage model mismatch (non-`EQ0..EQ13`).
- Missing/unparsable state/checklist files.
- Missing required stage evidence/checkpoint for stage marked done.
- Stage marked done without qualifying implementation commit (`EQ2..EQ11`).
- Control-plane anti-leak violation.
- Attempted `.cache` artifact commit.
- Any required artifact for active stage missing.
- Any required threshold/metric/linkage wiring still missing after auto-remediation attempt.
- Boundary gate wired to proxy metrics instead of scorer artifact.
- Any percent metric outside `[0,100]`.
- Any EQ12 hard-gate failure.
- Active shard set mismatch with manifests.
- Anchor set mismatch (active corpus vs registry).
- Final summary references non-existent evidence path.

## Required output format

- `MODE`
- `RUN_ID`
- `PR_URL`
- `PR_NUMBER`
- `PR_HEAD_BRANCH`
- `PR_BASE_BRANCH`
- `REPO_ROOT`
- `CONTROL_RUN_ROOT`
- `QUALITY_DATA_ROOT`
- `BASELINE_RUN_ID`
- `CURRENT_STAGE` before/after
- stages completed this invocation
- checkpoints written this invocation
- compatibility gaps found/fixed this invocation
- baseline pathology summary
- current pathology summary
- legacy quality summary
- effective threshold profile
- pass/fail by category (`contamination`, `semantic`, `pattern`, `scope`, `wrap`, `supsub`, `lineage`, `replay`, `pathology`)
- representative evidence paths
- blockers/stop conditions (if any)
- `STOP_REASON` (`completed_all_stages`, `blocked_by_stop_condition`, `throttled_by_MAX_STAGES`)
- exact resume command/prompt hint with resolved `RUN_ID`
