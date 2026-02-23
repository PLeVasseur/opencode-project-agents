# ISO 26262 Unit Boundary Pathology Remediation Repair Plan (Post-EQ12 Failure)

Date: 2026-02-16
Status: Draft implementation plan
Priority: Critical
Plan type: Root-cause repair + deterministic rerun + hard-gate closure
Primary reference run: `pr1-20260216T031732Z`

## 0) Objective
- [ ] Close the hard-gate failures observed at `EQ12` for required parts `P06`, `P08`, `P09`.
- [ ] Convert boundary/pathology behavior from page-level clumping to candidate-local segmentation and provenance.
- [ ] Correct metric math so quality gates are trustworthy (especially per-part and percent-bounds checks).
- [ ] Preserve strict resumable execution discipline (`EQ0..EQ13`, immutable contracts, evidence contracts, lock discipline).
- [ ] Ensure a brand-new session executes this repair plan by default (no stale prompt/runner linkage).

## 0A) New-session readiness gaps from prior draft (must be closed first)
- [ ] Prompt currently points at the older diagnosis/remediation plan; it must point at this repair plan.
- [ ] Runner constants still default to the older plan; default linkage must be moved to this repair plan.
- [ ] Runner must support explicit `PLAN_PATH`/`PROMPT_PATH` overrides for deterministic handoff in fresh sessions.
- [ ] Boundary goldset gates currently rely on proxy metrics; scoring must be wired to real goldset fixtures.
- [ ] Stage commit contract (`EQ2..EQ11`, `[EQx]`) must be explicitly enforceable in one-shot mode.

## 1) Confirmed failure snapshot (must be treated as factual input)

### 1A) Hard gate status
- [ ] `STOP_REASON=blocked_by_stop_condition` in run summary.
- [ ] `overall_pass=false` at `EQ12` acceptance audit.

### 1B) Pathology failures (overall)
- [ ] `residual_legal_boilerplate_hit_count = 3` (required `== 0`).
- [ ] `triad_source_set_identity_rate_pct = 100.0` (required `<= 5`).
- [ ] `paragraph_fragment_start_rate_pct = 51.724...` (required `<= 10`).
- [ ] `paragraph_fragment_end_rate_pct = 25.862...` (required `<= 10`).
- [ ] `paragraph_singleton_page_rate_pct = 100.0` (required `<= 85`).
- [ ] `unit_type_provenance_overlap_rate_pct = 100.0` (required `<= 10`).

### 1C) Boundary and metric-contract failures
- [ ] Per-part paragraph boundary F1 fails:
  - [ ] `P06 = 0.375`
  - [ ] `P08 = 0.3977...`
  - [ ] `P09 = 0.2159...`
  - [ ] required `>= 0.90`.
- [ ] Percent-bounds invariant failure:
  - [ ] `table_scope_detection_recall_pct = 766.666...` (invalid; must remain in `[0,100]`).

## 2) Root-cause diagnosis (code and artifact backed)

### RC1: Single-best candidate selection per type per page
- [ ] `normalize.py` currently takes only `[0]` candidate for paragraph/list/table on each page.
- [ ] Result: near one paragraph per page and collapsed boundary behavior.

### RC2: Page-wide provenance assignment reused across unit types
- [ ] `source_block_refs` currently receives the full page block list for every selected unit.
- [ ] Result: identical source signatures across paragraph/list/table on the same page.
- [ ] This directly drives `triad_source_set_identity_rate_pct=100` and provenance overlap `=100`.

### RC3: Table-line heuristic is too permissive
- [ ] `MULTI_COL_RE` based detection classifies many non-table lines as table-like.
- [ ] Result: table candidates appear on prose pages, reinforcing cross-type contamination.

### RC4: Scope metric denominator/model mismatch
- [ ] Score computation uses global summary signals for by-part scope metrics.
- [ ] `table_scope_detection_recall_pct` uses incompatible numerator/denominator, causing >100 outputs.

### RC5: Legal boilerplate suppression misses known patterns
- [ ] Residual legal text remains in page-2 paragraph units for each required part.
- [ ] Existing suppression tokens do not fully cover observed legal-office boilerplate variants.

## 3) Locked decisions (non-negotiable)
- [ ] Branch lock remains PR #1 head branch: `docs/iso26262-sphinx-traceability-migration-20260214T184350Z`.
- [ ] Run-id scope for this wave remains `pr1-*` only.
- [ ] Stage model remains canonical `EQ0..EQ13` only.
- [ ] Baseline gate remains report-only at `EQ1`; hard acceptance remains `EQ12`.
- [ ] Control-plane remains metadata only; no verbatim text leakage into run-control artifacts.
- [ ] Canonical execution plan for this wave is:
  - [ ] `$OPENCODE_CONFIG_DIR/plans/2026-02-16-unit-boundary-pathology-remediation-repair-plan.md`
- [ ] Canonical execution prompt for this wave is:
  - [ ] `$OPENCODE_CONFIG_DIR/prompts/execute-iso26262-unit-boundary-pathology-remediation-resumable.md`
- [ ] Prompt-plan linkage mismatch is a mandatory stop.
- [ ] No stage completes without both:
  - [ ] `artifacts/evidence/EQx.implementation-evidence.json`
  - [ ] `artifacts/checkpoints/EQx.done.json`.

## 3A) Inputs, defaults, and operating modes (new-session contract)

### 3A.1) Required input
- [ ] `OPENCODE_CONFIG_DIR`.

### 3A.2) Optional inputs with defaults
- [ ] `RUN_ID` default: `pr1-<UTC timestamp>`.
- [ ] `BASELINE_RUN_ID` default: `pr1-20260215T221903Z`.
- [ ] `MAX_STAGES` default: `all`.
- [ ] `START_STAGE` default: earliest incomplete safe stage.
- [ ] `MODE` default: `licensed_local` (allowed: `licensed_local`, `fixture_ci`).
- [ ] `PR_NUMBER` default: `1`.
- [ ] `PR_URL` default: `https://github.com/PLeVasseur/iso-26262-rust-mapping/pull/1`.
- [ ] `PDF_ROOT` default: `$REPO_ROOT/.cache/iso26262`.
- [ ] `AUTO_STAGE_COMMITS` default: `1`.

### 3A.3) Operating mode detection
- [ ] `kickoff-auto-pr1`: no `RUN_ID`; generated run root absent.
- [ ] `kickoff-explicit-pr1`: explicit `RUN_ID` with absent run root.
- [ ] `resume-explicit-pr1`: explicit/generated `RUN_ID` with existing run root.
- [ ] `invalid-run-id`: `RUN_ID` does not start with `pr1-` (hard stop).

### 3A.4) Threshold override contract
- [ ] Accept legacy remediation threshold overrides already supported by runner.
- [ ] Accept new contamination/pathology overrides:
  - [ ] `THRESHOLD_PARAGRAPH_BOILERPLATE_MAX_PCT`
  - [ ] `THRESHOLD_LIST_BOILERPLATE_MAX_PCT`
  - [ ] `THRESHOLD_TABLE_BOILERPLATE_MAX_PCT`
  - [ ] `THRESHOLD_TRIAD_SOURCE_SET_IDENTITY_MAX_PCT`
  - [ ] `THRESHOLD_PARAGRAPH_FRAGMENT_START_MAX_PCT`
  - [ ] `THRESHOLD_PARAGRAPH_FRAGMENT_END_MAX_PCT`
  - [ ] `THRESHOLD_PARAGRAPH_SINGLETON_PAGE_MAX_PCT`
  - [ ] `THRESHOLD_OVERSIZED_PARAGRAPH_MAX_PCT`
  - [ ] `THRESHOLD_UNIT_TYPE_PROVENANCE_OVERLAP_MAX_PCT`

## 3B) Deterministic roots and immutable contract keys

### 3B.1) Deterministic roots
- [ ] `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-extraction-quality-pr1-$RUN_ID"`
- [ ] `QUALITY_DATA_ROOT="$REPO_ROOT/.cache/iso26262/mining/quality-runs/$RUN_ID"`
- [ ] `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`

### 3B.2) Immutable contract keys (must persist and validate on resume)
- [ ] identity/roots: `RUN_ID`, `REPO_ROOT`, `CONTROL_RUN_ROOT`, `QUALITY_DATA_ROOT`, `PDF_ROOT`.
- [ ] PR lock: `PR_URL`, `PR_NUMBER`, `PR_HEAD_BRANCH`, `PR_BASE_BRANCH`, `TARGET_BRANCH`, `BASE_BRANCH`, `BASE_PIN_SHA`.
- [ ] baseline lock: `BASELINE_RUN_ID`, baseline control root, baseline data root, baseline metrics control root.
- [ ] stage model: `EQ0..EQ13` only.
- [ ] entrypoint lock: resolved `PLAN_PATH`, `PROMPT_PATH`, and hashes.
- [ ] threshold lock: effective threshold profile + profile hash.

## 3C) Mandatory preflight gate (before any stage mutation)
- [ ] Verify `OPENCODE_CONFIG_DIR` and `REPO_ROOT` readability.
- [ ] Verify prompt, plan, skill, and `state_tool.py` readability.
- [ ] Verify prompt-plan linkage resolves to this repair plan.
- [ ] Verify branch is locked to PR #1 head branch.
- [ ] Verify immutable contract values do not drift on resume.
- [ ] Verify stage model compatibility (`EQ0..EQ13` only).
- [ ] Verify state/checklist templates are available and parseable.
- [ ] Verify threshold/metric wiring supports all pathology and boilerplate keys.
- [ ] Verify scorecard schema supports required pathology metrics and by-part checks.
- [ ] Verify goldset scorer artifact path contract is wired (not proxy fallback).
- [ ] Compatibility-gap auto-remediation policy:
  - [ ] if preflight detects missing threshold/metric wiring, implement fixes in the same invocation,
  - [ ] record evidence at `artifacts/diagnostics/compatibility-gap-remediation.json`,
  - [ ] hard stop if required wiring is still missing after remediation attempt.
- [ ] On any preflight failure: hard stop with deterministic resume hint.

## 3D) Bootstrap and lock discipline

### 3D.1) Kickoff bootstrap
- [ ] Run `uv sync`.
- [ ] Checkout locked PR head branch before mutation.
- [ ] Create run root and required artifact subdirectories.
- [ ] Initialize `state.env` and `checklist.state.env` atomically.

### 3D.2) Resume bootstrap
- [ ] Validate required run files/dirs exist.
- [ ] Reconcile incomplete/partial stage writes.
- [ ] Reopen stage if done flags conflict with missing evidence/checkpoint artifacts.

### 3D.3) Lock behavior
- [ ] Hard stop on active non-stale lock.
- [ ] Log and replace stale lock.
- [ ] Release lock on all exits (success and failure).

## 4) Repair streams and concrete fixes

### RS0: Entrypoint and run-contract linkage repair (must land before remediation)
- [ ] Update prompt plan reference to this repair plan (new default execution target).
- [ ] Update runner default `PLAN_RELATIVE_PATH` to this repair plan.
- [ ] Add runner support for explicit override inputs:
  - [ ] `PLAN_PATH_OVERRIDE` (absolute or config-relative)
  - [ ] `PROMPT_PATH_OVERRIDE` (absolute or config-relative)
- [ ] Persist resolved plan/prompt paths and hashes into immutable contract keys.
- [ ] Preflight must fail if prompt references a plan path that does not match resolved runner plan path.
- [ ] Exit criteria:
  - [ ] fresh-session invocation without overrides resolves this repair plan.
  - [ ] immutable contract stores/validates the resolved plan/prompt pair.

### RS1: Metric contract and denominator repair (highest priority unblock)
- [ ] Update `tools/traceability/mining/quality_metrics.py` to enforce bounded percent outputs (`[0,100]`) at calculation time.
- [ ] Compute by-part scope metrics from part-local opportunities only.
- [ ] Add deterministic `scope_boundaries_by_part` consumption path.
- [ ] Ensure `table_scope_detection_recall_pct` denominator reflects true table opportunity count, never global part count.
- [ ] Add explicit zero-denominator behavior in code and `metric-contract-v2`.
- [ ] Replace proxy boundary-gate scoring with fixture-backed goldset scorer:
  - [ ] read `artifacts/fixtures/boundary-goldset.jsonl`,
  - [ ] compute boundary precision/recall/F1 against expected segment boundaries,
  - [ ] publish scorer artifact consumed by `EQ12`.
- [ ] Exit criteria:
  - [ ] `percent_metric_violations` is empty overall and per part.
  - [ ] no metric in scorecard exceeds `[0,100]`.
  - [ ] boundary F1 values in EQ12 are sourced from goldset scorer output, not heuristics.

### RS2: Paragraph boundary remediation (real multi-segment extraction)
- [ ] Replace top-1 paragraph selection with multi-segment extraction and acceptance.
- [ ] Split paragraph spans using deterministic boundaries:
  - [ ] heading transitions,
  - [ ] list/table boundaries,
  - [ ] sentence-ending punctuation + next-line casing cues,
  - [ ] TOC/dot-leader separators.
- [ ] Enforce min-content constraints while preserving legitimate short normative clauses.
- [ ] Exit criteria:
  - [ ] paragraph count no longer equals pages for all required parts.
  - [ ] `paragraph_singleton_page_rate_pct <= 85`.
  - [ ] `paragraph_fragment_start/end_rate_pct <= 10`.

### RS3: Candidate-local provenance isolation
- [ ] Carry source line indices through candidate extraction for paragraph/list/table.
- [ ] Build `source_block_refs` from candidate-local line/block mapping, not full-page defaults.
- [ ] Store locality metadata in `selection_meta` (`source_line_indices`, `source_block_ref_count`).
- [ ] Exit criteria:
  - [ ] `triad_source_set_identity_rate_pct <= 5`.
  - [ ] `unit_type_provenance_overlap_rate_pct <= 10`.

### RS4: Table/list type-isolation hardening
- [ ] Tighten `_is_table_line` heuristics to avoid prose and TOC false positives.
- [ ] Require stronger table structure before creating `table_cell` units:
  - [ ] repeated row evidence and column structure,
  - [ ] no one-off pseudo-table extraction from prose lines.
- [ ] Reduce use of `Table-Unknown`; only allow when table context evidence exists.
- [ ] Exit criteria:
  - [ ] table-cell extraction remains high-quality while not contaminating prose pages.
  - [ ] list/table boundary F1 thresholds remain passing.

### RS5: Contamination suppression expansion
- [ ] Extend legal/boilerplate patterns in normalization and scoring dictionaries:
  - [ ] copyright-office phrasing,
  - [ ] publication/footer legal lines,
  - [ ] "without prior written permission" class phrases.
- [ ] Apply suppression before final unit acceptance (not only in post-hoc scoring).
- [ ] Add deterministic exception rules for true normative legal clauses.
- [ ] Exit criteria:
  - [ ] `RESIDUAL_LEGAL_BOILERPLATE_HIT_COUNT == 0` for each required part and overall.

### RS6: Stage contract enforcement gaps in runner
- [ ] Enforce `EQ2..EQ11` stage-tagged Conventional Commit requirement (`[EQx]`) before done flags.
- [ ] Enforce implementation-path touch requirements for qualifying stage commits.
- [ ] Keep `.cache` commit prohibition and anti-leak checks as hard stops.
- [ ] One-shot commit policy (required to avoid deadlock):
  - [ ] default `AUTO_STAGE_COMMITS=1` performs one commit per `EQ2..EQ11` after stage checks pass,
  - [ ] commit message format `fix(mining): [EQx] <stage intent>`,
  - [ ] disable with `AUTO_STAGE_COMMITS=0` for manual workflows.
- [ ] Exit criteria:
  - [ ] stage completion is blocked when commit-contract evidence is missing.
  - [ ] one-shot mode can progress through `EQ2..EQ11` without manual commit intervention.

## 5) File-level implementation map
- [ ] `$OPENCODE_CONFIG_DIR/prompts/execute-iso26262-unit-boundary-pathology-remediation-resumable.md`
  - [ ] point prompt to this repair plan by default
  - [ ] document new optional overrides (`PLAN_PATH_OVERRIDE`, `PROMPT_PATH_OVERRIDE`, `AUTO_STAGE_COMMITS`)
- [ ] `tools/traceability/mining/normalize.py`
  - [ ] multi-segment paragraph extraction
  - [ ] candidate-local block mapping and provenance
  - [ ] tighter table/list discrimination
  - [ ] per-part scope boundary counters for summary output
- [ ] `tools/traceability/mining/quality_metrics.py`
  - [ ] denominator/model corrections
  - [ ] bounded percent helper and contract-safe outputs
  - [ ] by-part scope metric correctness
  - [ ] fixture-backed boundary goldset scorer integration
- [ ] `tools/traceability/mining/execute_quality_remediation.py`
  - [ ] default plan path switch to repair plan
  - [ ] plan/prompt override handling and immutable contract checks
  - [ ] stage commit contract enforcement (`EQ2..EQ11`)
  - [ ] auto-stage commit implementation for one-shot mode
  - [ ] stronger EQ12 validation messaging for metric bounds and denominator anomalies
- [ ] `tools/traceability/mining/config/*` and stage artifacts
  - [ ] update metric contract documentation emitted at `EQ4` and `EQ10`
  - [ ] preserve threshold wiring for pathology metrics and boilerplate thresholds

## 6) EQ-stage execution map for repair run

### EQ0: bootstrap and immutable contract validation
- [ ] Resume or kickoff with lock acquisition, contract validation, and stale-write reconciliation.
- [ ] Validate prompt/runner/plan linkage triad before any stage mutation.

### EQ1: baseline inventory (report-only)
- [ ] Keep baseline inventory for comparability against `pr1-20260215T221903Z`.

### EQ2: instrumentation expansion for locality debugging
- [ ] Emit candidate-level span and provenance diagnostics including local block counts.

### EQ3: boundary goldset refresh (same page quotas, richer assertions)
- [ ] Keep minimum 40-page quota (`P06:15`, `P08:15`, `P09:10`).
- [ ] Add expected split-count annotations for known over-clumped pages.
- [ ] Add fixture schema keys needed by scorer (`expected_paragraph_boundaries`, `expected_list_boundaries`, `expected_table_cell_boundaries`).

### EQ4: metric contract freeze v3
- [ ] Freeze corrected denominator math and bounded-percent behavior.

### EQ5-EQ7: core extraction repairs
- [ ] `EQ5`: paragraph segmentation and fragment suppression.
- [ ] `EQ6`: list continuation non-regression with locality isolation.
- [ ] `EQ7`: table scope/cell precision and shard hygiene non-regression.

### EQ8-EQ9: scope and selector isolation
- [ ] preserve lineage/scope guarantees while enforcing type-local candidate isolation.

### EQ10: harness and threshold wiring validation
- [ ] verify all pathology and boilerplate thresholds are wired and reported.
- [ ] fail immediately on any out-of-range percent metric.
- [ ] verify goldset scorer artifact exists and is wired into EQ12 gate evaluation.

### EQ11: full rerun and strict verify
- [ ] run `ingest -> extract -> normalize -> anchor -> publish -> verify`.
- [ ] run strict integrity audit and anchor/shard equality checks.
- [ ] emit stage commit ledger entries with actual `[EQx]` commit references for this run.

### EQ12: hard acceptance gate
- [ ] require all legacy gates plus all pathology gates plus boundary goldset gates.
- [ ] require zero percent-bounds violations.
- [ ] fail if boundary F1 values are not sourced from goldset scorer artifact.

### EQ13: finalize
- [ ] finalize only when all evidence paths exist and hard gates are green.

## 6A) Stage evidence and commit contract (required for resumability)

### 6A.1) Required per-stage artifacts
- [ ] `artifacts/evidence/EQx.implementation-evidence.json`
- [ ] `artifacts/checkpoints/EQx.done.json`
- [ ] stage marked done only when both exist.

### 6A.2) Required evidence payload fields
- [ ] `run_id`, `stage`, `timestamp_utc`, `target_branch`, `base_branch`, `base_pin_sha`.
- [ ] `commit_shas[]`, `changed_files[]`.
- [ ] `tests_run[]` with command, exit code, and output artifact path.
- [ ] `metrics_before`, `metrics_after`, `metrics_delta`.
- [ ] `artifacts_written[]`, `blocking_issues[]`.

### 6A.3) Implementation stage commit rule (`EQ2..EQ11`)
- [ ] At least one qualifying stage-tagged Conventional Commit (`[EQx]`).
- [ ] Commit touches implementation paths (not reports-only files).
- [ ] Stage completion blocked when commit evidence is missing.
- [ ] Maintain `artifacts/evidence/stage-commit-ledger.json` mapping stage -> commits/tests/metric deltas.

## 7) Validation matrix

### 7A) Pathology and boundary targets (required)
- [ ] `residual_legal_boilerplate_hit_count == 0`
- [ ] `triad_source_set_identity_rate_pct <= 5`
- [ ] `paragraph_fragment_start_rate_pct <= 10`
- [ ] `paragraph_fragment_end_rate_pct <= 10`
- [ ] `paragraph_singleton_page_rate_pct <= 85`
- [ ] `oversized_paragraph_rate_pct <= 20`
- [ ] `unit_type_provenance_overlap_rate_pct <= 10`
- [ ] `paragraph_boundary_f1 >= 0.90`
- [ ] `list_boundary_f1 >= 0.92`
- [ ] `table_cell_boundary_f1 >= 0.92`

### 7B) Metric-contract integrity targets
- [ ] all percent metrics are in `[0,100]` overall and per part.
- [ ] `table_scope_detection_recall_pct` uses corrected denominator and remains bounded.
- [ ] by-part scope metrics are computed from part-local signals only.
- [ ] no by-part metric reuses aggregate counters unless explicitly documented in contract.

### 7C) New-session linkage targets
- [ ] default prompt invocation executes this repair plan without manual file edits.
- [ ] runner output reports resolved plan/prompt paths that match this plan.
- [ ] resume hint uses the same resolved prompt/plan pair.

### 7D) Non-regression targets
- [ ] contamination/semantic/pattern/scope/wrap/supsub/lineage/replay categories remain passing.
- [ ] verify summary remains green for schema/integrity/replay/probe checks.

### 7E) Tooling checks for touched Python files
- [ ] `uvx black . --check --diff --color`
- [ ] `uvx flake8 . --exclude .venv`

## 8) Mandatory stop conditions
- [ ] Active non-stale lock owned by another process.
- [ ] Branch drift from locked PR head branch.
- [ ] Invalid run-id scope (not `pr1-*`).
- [ ] Immutable contract drift.
- [ ] Missing/unparsable state/checklist files.
- [ ] Missing required stage evidence/checkpoint for stage marked done.
- [ ] Missing required artifact for active stage.
- [ ] Missing commit-contract evidence for `EQ2..EQ11`.
- [ ] Control-plane anti-leak violation.
- [ ] Attempted `.cache` artifact commit.
- [ ] Prompt/runner default plan linkage still points to pre-repair plan.
- [ ] Boundary gate uses proxy metrics instead of goldset scorer artifact.
- [ ] Any percent metric outside `[0,100]`.
- [ ] Any EQ12 hard-gate failure.
- [ ] Active shard set mismatch with part manifests.
- [ ] Anchor registry set mismatch vs active corpus anchor set.
- [ ] Final summary references non-existent evidence path.

## 9) Runbook for the next execution

### 9A) Fresh kickoff
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="pr1-$(date -u +%Y%m%dT%H%M%SZ)" \
BASELINE_RUN_ID="pr1-20260215T221903Z" \
MODE="licensed_local" \
PR_NUMBER="1" \
AUTO_STAGE_COMMITS="1" \
MAX_STAGES="all" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

### 9B) Resume
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="<existing-pr1-run-id>" \
START_STAGE="<EQx>" \
MODE="licensed_local" \
AUTO_STAGE_COMMITS="1" \
MAX_STAGES="all" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

## 9C) Required run output contract
- [ ] `MODE`, `RUN_ID`, `PR_URL`, `PR_NUMBER`, `PR_HEAD_BRANCH`, `PR_BASE_BRANCH`.
- [ ] `REPO_ROOT`, `CONTROL_RUN_ROOT`, `QUALITY_DATA_ROOT`, `BASELINE_RUN_ID`.
- [ ] `CURRENT_STAGE` before/after.
- [ ] stages completed this invocation.
- [ ] checkpoints written this invocation.
- [ ] compatibility gaps found/fixed this invocation.
- [ ] baseline pathology summary.
- [ ] current pathology summary.
- [ ] legacy quality summary.
- [ ] effective threshold profile.
- [ ] pass/fail by category (`contamination`, `semantic`, `pattern`, `scope`, `wrap`, `supsub`, `lineage`, `replay`, `pathology`).
- [ ] representative evidence paths.
- [ ] blockers/stop conditions (if any).
- [ ] `STOP_REASON` (`completed_all_stages`, `blocked_by_stop_condition`, `throttled_by_MAX_STAGES`).
- [ ] exact resume command and prompt hint with resolved `RUN_ID`.

## 10) Definition of done
- [ ] `EQ12` passes for each required part and overall with zero blockers.
- [ ] `EQ13` finalize completes and writes valid summary evidence paths.
- [ ] run is resumable from any interruption point without state drift.
- [ ] final quality and pathology metrics show material improvement from `pr1-20260216T031732Z`.
