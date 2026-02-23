# ISO 26262 Unit Boundary Pathology Diagnosis and Remediation Plan (Hardened)

Date: 2026-02-16
Status: Draft execution plan
Priority: Critical
Plan type: Deep diagnosis + corrective remediation + run-contract hardening

## 0) Objective
- [ ] Diagnose and resolve persistent unit-quality pathologies for required parts `P06`, `P08`, `P09`.
- [ ] Eliminate clumping/fragmentation behaviors and residual contamination leakage.
- [ ] Ensure a fresh session can execute this plan end-to-end with deterministic resumability and hard gates.

## 1) Locked decisions (non-negotiable)
- [ ] Branch lock: PR #1 head branch `docs/iso26262-sphinx-traceability-migration-20260214T184350Z`.
- [ ] Run-id scope: only `pr1-*` IDs for this wave.
- [ ] Stage model lock: execution stages are canonical `EQ0..EQ13` only.
- [ ] Control-plane remains metadata-only; verbatim text remains data-plane only.
- [ ] Baseline gate remains report-only at `EQ1`; hard acceptance remains `EQ12`.
- [ ] No stage may complete without implementation evidence and checkpoint artifacts.

## 2) Execution entrypoint alignment
- [ ] Canonical plan path:
  - [ ] `$OPENCODE_CONFIG_DIR/plans/2026-02-16-unit-boundary-pathology-diagnosis-and-remediation-plan.md`
- [ ] Canonical prompt path (must reference this plan before kickoff):
  - [ ] `$OPENCODE_CONFIG_DIR/prompts/execute-iso26262-unit-boundary-pathology-remediation-resumable.md`
- [ ] Canonical runner:
  - [ ] `tools/traceability/mining/execute_quality_remediation.py`
- [ ] Hard preflight rule:
  - [ ] Stop if prompt-plan linkage is stale or points to a different execution plan.

## 3) Inputs, defaults, and modes

### 3A) Required input
- [ ] `OPENCODE_CONFIG_DIR`

### 3B) Optional inputs with defaults
- [ ] `RUN_ID=pr1-<UTC timestamp>`
- [ ] `BASELINE_RUN_ID=pr1-20260215T221903Z`
- [ ] `MAX_STAGES=all`
- [ ] `START_STAGE` unset (earliest incomplete safe stage)
- [ ] `MODE=licensed_local`

### 3C) Threshold override inputs (must be recognized when provided)
- [ ] Existing threshold keys from current remediation prompt.
- [ ] New contamination keys:
  - [ ] `THRESHOLD_PARAGRAPH_BOILERPLATE_MAX_PCT`
  - [ ] `THRESHOLD_LIST_BOILERPLATE_MAX_PCT`
  - [ ] `THRESHOLD_TABLE_BOILERPLATE_MAX_PCT`
- [ ] New pathology keys:
  - [ ] `THRESHOLD_TRIAD_SOURCE_SET_IDENTITY_MAX_PCT`
  - [ ] `THRESHOLD_PARAGRAPH_FRAGMENT_START_MAX_PCT`
  - [ ] `THRESHOLD_PARAGRAPH_FRAGMENT_END_MAX_PCT`
  - [ ] `THRESHOLD_PARAGRAPH_SINGLETON_PAGE_MAX_PCT`
  - [ ] `THRESHOLD_OVERSIZED_PARAGRAPH_MAX_PCT`
  - [ ] `THRESHOLD_UNIT_TYPE_PROVENANCE_OVERLAP_MAX_PCT`

### 3D) Mode detection
- [ ] `kickoff-explicit-pr1`: run root absent.
- [ ] `resume-explicit-pr1`: run root present.
- [ ] `invalid-run-id`: run ID missing `pr1-` prefix.

## 4) Deterministic roots and immutable contract

### 4A) Deterministic roots
- [ ] `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-extraction-quality-pr1-$RUN_ID"`
- [ ] `QUALITY_DATA_ROOT="$REPO_ROOT/.cache/iso26262/mining/quality-runs/$RUN_ID"`
- [ ] `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`

### 4B) Immutable contract keys (must persist + validate at resume)
- [ ] Run identity and roots: `RUN_ID`, `CONTROL_RUN_ROOT`, `QUALITY_DATA_ROOT`, `PDF_ROOT`, `REPO_ROOT`.
- [ ] PR contract: `PR_URL`, `PR_NUMBER`, `PR_HEAD_BRANCH`, `PR_BASE_BRANCH`, `TARGET_BRANCH`.
- [ ] Baseline contract: `BASELINE_RUN_ID`, baseline control/data roots.
- [ ] Stage model contract: `EQ0..EQ13`.
- [ ] Plan/prompt contract: plan path, prompt path, contract hashes.
- [ ] Threshold profile contract: effective threshold values + profile hash.
- [ ] Pattern/spec contract paths and fixture manifest paths.

## 5) New-session preflight gate (mandatory)
- [ ] Environment and branch checks:
  - [ ] `OPENCODE_CONFIG_DIR` exists and is readable.
  - [ ] current branch equals locked PR head branch.
- [ ] Baseline checks:
  - [ ] `BASELINE_RUN_ID` exists and is complete enough for baseline scoring.
- [ ] Prompt-runner compatibility checks:
  - [ ] runner accepts `EQ0..EQ13` with `START_STAGE`/`MAX_STAGES`.
  - [ ] runner/prompt support new threshold keys.
  - [ ] scorecard supports all required new metric keys.
- [ ] Artifact contract checks:
  - [ ] required directories can be created.
  - [ ] state/checklist templates are present and parseable.
- [ ] Stop if any preflight check fails.

## 6) Confirmed pathology signals to resolve
- [ ] Over-clumping:
  - [ ] same page-level block pools reused across multiple unit types.
- [ ] Fragmentation:
  - [ ] paragraph starts at lowercase/connectors and truncated endings.
- [ ] Coarse paragraph granularity:
  - [ ] near one-paragraph-per-page behavior in many regions.
- [ ] Residual legal/header/footer contamination leakage.
- [ ] Metric trust gap:
  - [ ] percent metrics can become out of range without a hard bounds stop.

## 7) Diagnosis hypotheses
- [ ] H1: Candidate pools are built page-wide before type-local filtering.
- [ ] H2: Paragraph boundary cues are underweighted vs broad span continuity.
- [ ] H3: Type assignment lacks strict mutual-exclusion and locality rules.
- [ ] H4: Contamination suppression is incomplete and/or applied too late.
- [ ] H5: Metric formulas/denominators are not fully contract-enforced.

## 8) EQ-stage execution map (diagnose + fix)

### EQ0: Bootstrap and contract lock
- [ ] Resolve inputs, detect mode, validate contract, acquire lock.
- [ ] Initialize or reconcile state/checklist/run log.

### EQ1: Baseline pathology inventory (report-only)
- [ ] Compute baseline pathology + quality inventory from `BASELINE_RUN_ID`.
- [ ] Emit artifacts:
  - [ ] `artifacts/baseline/pathology-baseline.json`
  - [ ] `artifacts/baseline/pathology-exemplars.md`

### EQ2: Instrument decision trace
- [ ] Emit candidate pools, boundary decisions, accepted/rejected candidate traces, provenance-locality traces.
- [ ] Required artifacts:
  - [ ] `artifacts/diagnostics/candidate-pools.jsonl`
  - [ ] `artifacts/diagnostics/boundary-decisions.jsonl`
  - [ ] `artifacts/diagnostics/unit-provenance-locality.jsonl`

### EQ3: Build and pin boundary goldset
- [ ] Create fixed goldset page list: minimum 40 pages (`P06:15`, `P08:15`, `P09:10`).
- [ ] Include archetypes: prose, list-dense, table-dense, mixed, known contamination pages.
- [ ] Emit:
  - [ ] `artifacts/fixtures/boundary-goldset-manifest.json`
  - [ ] `artifacts/fixtures/boundary-goldset.jsonl`

### EQ4: Root-cause classification and metric-contract freeze
- [ ] Classify failures: `over_merge`, `over_split`, `mis_type`, `contamination_bleed`, `provenance_overlap`.
- [ ] Freeze metric formulas and denominator rules in versioned contract.
- [ ] Emit:
  - [ ] `artifacts/diagnostics/root-cause-classification.json`
  - [ ] `artifacts/quality/metric-contract-v2.json`

### EQ5: Paragraph boundary remediation
- [ ] Strengthen paragraph segmentation + continuation logic.
- [ ] Add explicit exclusion for list/table/header/footer signatures.
- [ ] Reject paragraph candidates dominated by contamination/table/list patterns.

### EQ6: List marker and continuation remediation
- [ ] Improve marker grammar and continuation capture.
- [ ] Enforce list-local provenance locality (no default full-page candidate origin).

### EQ7: Table scope/cell remediation and shard hygiene
- [ ] Tighten table region detection and row/column segmentation.
- [ ] Enforce table-local candidate pools for `table_cell`.
- [ ] Enforce manifest-only active shard set; remove/archive undeclared active shards.

### EQ8: Scope and anchor strictness
- [ ] Preserve/improve section/clause/table scope extraction.
- [ ] Enforce strict `unit -> parent_scope -> anchor` completeness.
- [ ] Prepare active-corpus anchor set for strict verify equality.

### EQ9: Selector isolation and early contamination suppression
- [ ] Enforce per-type selector isolation and cross-type provenance limits.
- [ ] Apply contamination suppression prior to final candidate commit.

### EQ10: Harness and gate wiring hardening
- [ ] Add pathology metrics and boilerplate thresholds to scorecard and threshold evaluator.
- [ ] Add prompt/env parsing support for new threshold keys.
- [ ] Add bounds invariant checks for all percent metrics.

### EQ11: End-to-end rerun and strict audits
- [ ] Rerun full pipeline `ingest -> extract -> normalize -> anchor -> publish -> verify`.
- [ ] Run goldset scorer and full-run pathology checks.
- [ ] Enforce strict integrity checks:
  - [ ] no undeclared active shards,
  - [ ] anchor registry equality with active manifest-listed corpus anchors,
  - [ ] no out-of-range metrics.

### EQ12: Hard acceptance gate
- [ ] Legacy hard gates pass.
- [ ] New pathology hard gates pass (per part + overall):
  - [ ] `RESIDUAL_LEGAL_BOILERPLATE_HIT_COUNT == 0`
  - [ ] `triad_source_set_identity_rate_pct <= 5`
  - [ ] `paragraph_fragment_start_rate_pct <= 10`
  - [ ] `paragraph_fragment_end_rate_pct <= 10`
  - [ ] `paragraph_singleton_page_rate_pct <= 85`
  - [ ] `oversized_paragraph_rate_pct <= 20`
  - [ ] `unit_type_provenance_overlap_rate_pct <= 10`
  - [ ] all percent metrics in `[0,100]`.
- [ ] Goldset quality gates pass:
  - [ ] `paragraph_boundary_f1 >= 0.90`
  - [ ] `list_boundary_f1 >= 0.92`
  - [ ] `table_cell_boundary_f1 >= 0.92`

### EQ13: Finalize and handoff
- [ ] Validate every final summary evidence path exists.
- [ ] Finalize state/checklist and release lock.

## 9) Stage evidence and commit contract (hardened)

### 9A) Required for every stage `EQx`
- [ ] `artifacts/evidence/EQx.implementation-evidence.json`
- [ ] `artifacts/checkpoints/EQx.done.json`
- [ ] Evidence includes:
  - [ ] `run_id`, `stage`, `timestamp_utc`, `target_branch`,
  - [ ] `commit_shas[]`, `changed_files[]`,
  - [ ] `tests_run[]` with command/exit code/output path,
  - [ ] `metrics_before`, `metrics_after`, `metrics_delta`,
  - [ ] `artifacts_written[]`, `blocking_issues[]`.

### 9B) Implementation-stage rules (`EQ2..EQ11`)
- [ ] At least one qualifying implementation commit per stage.
- [ ] Commit message contains stage tag `[EQx]` and follows Conventional Commits.
- [ ] Commit must touch stage-required implementation paths (not reports-only).
- [ ] Commits that only touch control-plane/report files are invalid.
- [ ] Stage completion blocked if tests/metrics evidence is missing.

### 9C) Ledger
- [ ] Maintain `artifacts/evidence/stage-commit-ledger.json` mapping stage -> commits -> tests -> metric deltas.

## 10) Stage-to-path and test matrix (minimum)
- [ ] EQ2-EQ3: `tools/traceability/mining/normalize.py`, extraction/diagnostics paths, unit tests/fixtures.
- [ ] EQ4: scorer and metric contract code, metric sanity tests.
- [ ] EQ5-EQ7: normalization/selection/table logic and fixture tests.
- [ ] EQ8-EQ9: anchor/linkage/selector code and linkage audits.
- [ ] EQ10: scoring + threshold evaluation + prompt env parsing.
- [ ] EQ11: pipeline execution wiring + strict verify checks.
- [ ] Required command evidence by stage (as applicable):
  - [ ] `uvx black . --check --diff --color`
  - [ ] `uvx flake8 . --exclude .venv`
  - [ ] targeted fixture test commands
  - [ ] end-to-end run command

## 11) Metric and threshold contract

### 11A) New metrics to add to scorecard
- [ ] `triad_source_set_identity_rate_pct`
- [ ] `paragraph_fragment_start_rate_pct`
- [ ] `paragraph_fragment_end_rate_pct`
- [ ] `paragraph_singleton_page_rate_pct`
- [ ] `oversized_paragraph_rate_pct`
- [ ] `unit_type_provenance_overlap_rate_pct`

### 11B) Definition constraints
- [ ] Every metric definition includes numerator, denominator, filters, and edge-case behavior.
- [ ] Percent metric outputs are bounded to `[0,100]` or stage fails.
- [ ] Denominator zero behavior is explicit and deterministic.

### 11C) Unit-volume guardrails (anti-over-pruning)
- [ ] For each required part and unit type:
  - [ ] unit count must be `>= 85%` of baseline count unless justified blocker approved.
  - [ ] unit count inflation `> 300%` of baseline requires blocker review.

### 11D) Gate granularity
- [ ] EQ12 gates are evaluated both:
  - [ ] per part (`P06`, `P08`, `P09`), and
  - [ ] overall aggregate.

## 12) Contamination dictionary governance
- [ ] Maintain versioned contamination dictionary artifact:
  - [ ] `artifacts/patterns/contamination-dictionary-v2.json`
- [ ] Dictionary includes:
  - [ ] term families, regex patterns, exclusions, examples, version hash.
- [ ] Scorecard and audits record dictionary version/hash used.

## 13) Sentinel acceptance exemplars
- [ ] Maintain mandatory sentinel case manifest:
  - [ ] `artifacts/fixtures/sentinel-cases.json`
- [ ] Include at minimum:
  - [ ] known fragmented paragraph case (example: `p06-p0014-par-001`),
  - [ ] known contamination-prone pages in each required part,
  - [ ] mixed list/table/prose pages previously showing full-pool provenance reuse.
- [ ] EQ12 fails if sentinel expected outcomes do not pass.

## 14) Required artifacts
- [ ] Baseline:
  - [ ] `artifacts/baseline/pathology-baseline.json`
  - [ ] `artifacts/baseline/pathology-exemplars.md`
- [ ] Diagnostics:
  - [ ] `artifacts/diagnostics/candidate-pools.jsonl`
  - [ ] `artifacts/diagnostics/boundary-decisions.jsonl`
  - [ ] `artifacts/diagnostics/unit-provenance-locality.jsonl`
  - [ ] `artifacts/diagnostics/root-cause-classification.json`
- [ ] Fixtures/specs:
  - [ ] `artifacts/fixtures/boundary-goldset-manifest.json`
  - [ ] `artifacts/fixtures/boundary-goldset.jsonl`
  - [ ] `artifacts/fixtures/sentinel-cases.json`
  - [ ] `artifacts/patterns/contamination-dictionary-v2.json`
  - [ ] `artifacts/quality/metric-contract-v2.json`
- [ ] Quality/reports:
  - [ ] `artifacts/quality/quality-scorecard.json`
  - [ ] `artifacts/checkpoints/EQ12.acceptance-audit.json`
  - [ ] `artifacts/pipeline-control/artifacts/verify/verify-summary.json`
  - [ ] `artifacts/final/quality-remediation-summary.json`

## 15) Mandatory stop conditions
- [ ] Active lock owned by another process.
- [ ] Branch drift from locked PR head branch.
- [ ] Invalid run-id scope (not `pr1-*`).
- [ ] Stage model mismatch (anything outside `EQ0..EQ13`).
- [ ] Prompt-plan linkage mismatch.
- [ ] Missing/unparsable state or checklist.
- [ ] Immutable contract drift.
- [ ] Missing stage evidence/checkpoint for done stage.
- [ ] Missing required artifact for active stage.
- [ ] Control-plane anti-leak violation.
- [ ] Any percent metric outside `[0,100]`.
- [ ] Residual legal contamination count > 0 at EQ12.
- [ ] Active shard set mismatch with manifests.
- [ ] Anchor set mismatch (active corpus vs registry).
- [ ] Final summary references non-existent evidence path.

## 16) New-session runbook

### 16A) Kickoff fresh run
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="pr1-$(date -u +%Y%m%dT%H%M%SZ)" \
BASELINE_RUN_ID="pr1-20260215T221903Z" \
MAX_STAGES="all" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

### 16B) Resume
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="<existing-pr1-run-id>" \
START_STAGE="<EQ0..EQ13>" \
MAX_STAGES="all" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

### 16C) Debug window
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="<existing-pr1-run-id>" \
START_STAGE="EQ10" \
MAX_STAGES="2" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

## 17) Definition of done
- [ ] All stages `EQ0..EQ13` complete with valid evidence and checkpoints.
- [ ] Legacy + pathology hard gates pass at `EQ12` for each required part and overall.
- [ ] Goldset boundary F1 gates pass.
- [ ] Residual legal contamination count is zero in normalize/query outputs.
- [ ] Active shard integrity and anchor-set equality checks pass.
- [ ] Final summary evidence paths all resolve.
- [ ] Touched Python files pass black and flake8 checks.
