# Execute ISO 26262 PDF Extraction Quality Remediation Plan (Resumable + Metrics-First)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-16-pdf-extraction-quality-and-unitization-remediation-plan.md`

with resumable behavior aligned to:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`
- `$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py`

## Inputs

- Optional `RUN_ID` (default `pr1-20260215T221903Z`; use this run unless explicitly overridden with another `pr1-*` id).
- Optional `MAX_STAGES` throttle (default `all` for run-to-completion).
- Optional `START_STAGE` (default: earliest incomplete safe stage).
- Optional `BASELINE_RUN_ID` (default: newest completed `iso26262-mining-verbatim-*` run).
- Optional `PR_NUMBER` (default `1`).
- Optional `PR_URL` (default `https://github.com/PLeVasseur/iso-26262-rust-mapping/pull/1`).
- Optional `PDF_ROOT` (default `$REPO_ROOT/.cache/iso26262`).
- Optional `MODE` (`fixture_ci` or `licensed_local`, default `licensed_local`).
- Optional quality-threshold overrides for controlled experiments:
  - `THRESHOLD_PARAGRAPH_LICENSE_MAX_PCT`
  - `THRESHOLD_LIST_LICENSE_MAX_PCT`
  - `THRESHOLD_TABLE_LICENSE_MAX_PCT`
  - `THRESHOLD_PARAGRAPH_MEANINGFUL_MIN_PCT`
  - `THRESHOLD_LIST_MEANINGFUL_MIN_PCT`
  - `THRESHOLD_TABLE_MEANINGFUL_MIN_PCT`
  - `THRESHOLD_PARAGRAPH_PATTERN_CONFORMANCE_MIN_PCT`
  - `THRESHOLD_LIST_MARKER_VALIDITY_MIN_PCT`
  - `THRESHOLD_LIST_CONTINUATION_CAPTURE_MIN_PCT`
  - `THRESHOLD_TABLE_STRUCTURAL_VALIDITY_MIN_PCT`
  - `THRESHOLD_TABLE_PATTERN_CONFORMANCE_MIN_PCT`
  - `THRESHOLD_LINE_WRAP_PRECISION_MIN_PCT`
  - `THRESHOLD_DEHYPHENATION_PRECISION_MIN_PCT`
  - `THRESHOLD_SECTION_BOUNDARY_F1_MIN`
  - `THRESHOLD_CLAUSE_BOUNDARY_F1_MIN`
  - `THRESHOLD_TABLE_SCOPE_RECALL_MIN_PCT`
  - `THRESHOLD_SUPERSCRIPT_RETENTION_MIN_PCT`
  - `THRESHOLD_SUBSCRIPT_RETENTION_MIN_PCT`
  - `THRESHOLD_FOOTNOTE_MARKER_RETENTION_MIN_PCT`
  - `THRESHOLD_SECTION_ANCHOR_RESOLUTION_MIN_PCT`
  - `THRESHOLD_CLAUSE_ANCHOR_RESOLUTION_MIN_PCT`
  - `THRESHOLD_TABLE_ANCHOR_RESOLUTION_MIN_PCT`
  - `THRESHOLD_UNIT_PARENT_SCOPE_LINKAGE_MIN_PCT`
  - `THRESHOLD_UNIT_ANCHOR_LINKAGE_MIN_PCT`
  - `THRESHOLD_REPLAY_SIGNATURE_MATCH_MIN_PCT`

## Operating modes

- `kickoff-default-pr1`: no `RUN_ID`; force `RUN_ID=pr1-20260215T221903Z`.
- `kickoff-explicit-pr1`: `RUN_ID` provided, starts with `pr1-`, and control run root does not exist yet.
- `resume-explicit-pr1`: explicit/default `RUN_ID` control run root already exists.
- `invalid-run-id`: `RUN_ID` does not start with `pr1-` for this remediation wave (stop).

Mode must be auto-detected and reported.

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Resolve PR #1 metadata (`PR_URL`, `PR_NUMBER`, `PR_HEAD_BRANCH`, `PR_BASE_BRANCH`) and lock execution to `PR_HEAD_BRANCH`.
3. Resolve run identity:
   - if `RUN_ID` is not provided, force `RUN_ID=pr1-20260215T221903Z`,
   - if provided, require prefix `pr1-` or stop with `invalid-run-id`.
4. Resolve deterministic roots:
   - `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-extraction-quality-pr1-$RUN_ID"`
   - `QUALITY_DATA_ROOT="$REPO_ROOT/.cache/iso26262/mining/quality-runs/$RUN_ID"`
   - `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`
5. Resolve baseline run:
   - If `BASELINE_RUN_ID` provided, use that run.
   - Else choose newest completed `$OPENCODE_CONFIG_DIR/reports/iso26262-mining-verbatim-*` with `S_FINALIZE_DONE=1`.
6. Kickoff bootstrap for new runs:
   - run `uv sync` in repo root,
   - checkout `PR_HEAD_BRANCH` and verify current branch equals `PR_HEAD_BRANCH`,
   - create control/data directories and stage artifact directories,
   - initialize `state.env` and `checklist.state.env` atomically via `state_tool.py`,
   - persist immutable PR contract keys and baseline gate policy (`BASELINE_GATE_MODE=report_only`, `QUALITY_HARD_GATE_STAGE=EQ12`).
7. Resume bootstrap for existing runs:
   - ensure `state.env`, `checklist.state.env`, `run.log`, `artifacts/`, `lock/` exist,
   - verify immutable PR/branch contract in state matches resolved PR metadata,
   - checkout `PR_HEAD_BRANCH` and fail if current branch differs.
8. Enforce lock discipline with `LOCK_FILE` in run state:
   - stop on active valid lock,
   - replace stale lock only after appending stale payload to `run.log`,
   - release lock on all exits (success/failure/interruption).
9. Validate immutable contract before mutation:
   - run identity, roots, baseline run pointers,
   - PR contract keys (`PR_URL`, `PR_NUMBER`, `PR_HEAD_BRANCH`, `PR_BASE_BRANCH`),
   - threshold profile values and gate policy keys (`BASELINE_GATE_MODE`, `QUALITY_HARD_GATE_STAGE`),
   - branch/base pin and plan path,
   - pattern/scope contract paths (`UNIT_PATTERN_SPEC_PATH`, `SCOPE_PATTERN_SPEC_PATH`),
   - fixture/audit contract paths (`SCOPE_FIXTURE_MANIFEST_PATH`, `HIERARCHICAL_ANCHOR_AUDIT_PATH`).
10. Enforce canonical stage model and checklist model:
    - stages: `EQ0..EQ13`,
    - one explicit done flag per stage,
    - required checklist keys must be explicit `0|1`.
10A. Enforce per-stage implementation evidence (hard gate at every stage):
    - write `artifacts/evidence/EQx.implementation-evidence.json` for every stage,
    - for `EQ2..EQ11`, require stage-tagged Conventional Commit(s) containing `[EQx]` before setting `S_EQx_DONE=1`,
    - forbid stage completion from placeholder/scaffold artifacts,
    - checkpoint must include commit SHA(s), changed files, tests run, targeted metric deltas.
10B. Enforce commit chunk map from plan section `8C`:
    - execute chunk sequence `EQx-C1`, `EQx-C2`, ... in order,
    - do not merge unrelated stage chunks into a single commit,
    - append chunk evidence and commit SHA(s) to `artifacts/evidence/stage-commit-ledger.json`.
11. Enforce crash-resume reconciliation windows:
    - stage done but artifacts/checklist missing => reopen stage,
    - checkpoint/commit mismatch => stop and reconcile,
   - scorecard exists but inputs changed => invalidate stage and reopen,
   - open transaction markers without commit markers => reconcile or stop.
12. Enforce content-policy boundaries:
    - verbatim stays in data-plane,
    - control-plane metadata-only,
    - fail if control-plane contains raw text payload fields,
    - fail if `.cache` artifacts are staged/committed.
13. Execute non-interactively and run through all stages by default:
    - do not pause for manual confirmation between stages,
    - proceed automatically whenever stage gates pass,
    - treat unspecified `MAX_STAGES` as `all`.
14. Execute stages in order with stage gates:
    - `EQ0` Bootstrap + PR branch lock + baseline contract
    - `EQ1` Baseline grading + failure inventory (`report_only`)
    - `EQ2` Header/footer and boilerplate suppression
    - `EQ3` Wrap/dehyphenation reconstruction hardening
    - `EQ4` Sup/sub/footnote retention handling
    - `EQ5` Paragraph pattern spec + segmentation
    - `EQ6` List-bullet pattern spec + continuation/hierarchy
    - `EQ7` Table scope detection + cell pattern hardening
    - `EQ8` Section/clause/table scope extraction + hierarchical anchors
    - `EQ9` Unit selector rewrite + parent-scope linkage enforcement
    - `EQ10` Quality harness + fixtures + scoring
    - `EQ11` End-to-end rerun + linkage/replay checks
    - `EQ12` Acceptance audit and evidence report (hard-threshold enforcement)
    - `EQ13` Finalize
15. Gate promotion with hard metrics from plan section 5 at `EQ12`, including:
    - contamination (`paragraph/list_bullet/table_cell`),
    - semantic quality + pattern conformance,
    - wrap/dehyphenation + paragraph boundaries,
    - scope extraction (`section/clause/table`),
    - sup/sub/footnote retention,
    - lineage completeness (`unit->anchor`, `unit->parent_scope`),
    - scope anchor resolution (`section/clause/table`),
    - replay signature match.
16. Stop behavior:
    - default: continue until all stages complete,
    - if `MAX_STAGES` is numeric: stop after that many completed stages,
    - always stop immediately on a mandatory stop condition.

## Mandatory stop conditions

- Active non-stale lock by another process.
- Immutable contract drift at resume boundary.
- Branch drift from locked `PR_HEAD_BRANCH` / `TARGET_BRANCH`.
- `RUN_ID` not scoped to `pr1-*` for this remediation wave.
- Missing/unparsable state or checklist files.
- Stage marked done without `artifacts/evidence/EQx.implementation-evidence.json`.
- `EQ2..EQ11` stage marked done with zero qualifying implementation commits.
- Stage commit missing `[EQx]` tag or not reachable from `TARGET_BRANCH` HEAD.
- Stage evidence indicates only control/report artifacts changed (no required implementation paths).
- Placeholder/scaffold evidence used as completion proof.
- Stage marked done with missing required artifacts/checklist keys.
- Any hard quality threshold fails at `EQ12` acceptance.
- Any required-part completeness/linkage gate fails.
- Any required `section/clause/table` anchor resolution gate fails.
- Replay signature mismatch.
- Control-plane anti-leak policy violation.
- Attempted `.cache` artifact commit.

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
- `BASELINE_GATE_MODE`
- `QUALITY_HARD_GATE_STAGE`
- `CURRENT_STAGE` before/after
- stages completed this invocation
- checkpoints written this invocation
- baseline score summary (key metrics)
- current score summary (key metrics)
- threshold profile (effective values)
- pass/fail by metric (contamination/semantic/pattern/scope/wrap/supsub/lineage/replay)
- representative evidence paths for paragraph/list/table + section/clause/table anchor improvements
- blockers/stop conditions (if any)
- `STOP_REASON` (`completed_all_stages`, `blocked_by_stop_condition`, `throttled_by_MAX_STAGES`)
- exact resume command or prompt invocation hint
