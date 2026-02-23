# ISO 26262 PDF Extraction Quality Follow-up Hardening Plan

Date: 2026-02-16
Status: Draft implementation plan
Priority: Critical
Plan type: Post-remediation quality hardening and run-contract stabilization

## 0) Goal
- [ ] Close known quality gaps after run `pr1-20260215T221903Z` and make gating trustworthy for required parts `P06`, `P08`, `P09`.
- [ ] Ensure a brand-new session can execute this plan end-to-end without ambiguity, stage drift, or hidden manual steps.
- [ ] Preserve deterministic, resumable behavior with auditable artifacts and no dangling evidence paths.

## 1) Locked decisions (non-negotiable)
- [ ] Branch is locked to PR #1 head branch: `docs/iso26262-sphinx-traceability-migration-20260214T184350Z`.
- [ ] Run IDs for this wave must use `pr1-*` prefix only.
- [ ] Executor stage model remains canonical `EQ0..EQ13`.
  - [ ] This plan must not introduce alternate stage IDs as execution stages.
  - [ ] Follow-up workstream labels (`FQ*`) are descriptive only and map into `EQ*` stages.
- [ ] Control-plane remains metadata-only; verbatim stays in data-plane only.
- [ ] `EQ12` is hard gate; `EQ1` remains report-only baseline gate.
- [ ] No stage may be marked complete without implementation evidence artifact.

## 2) Inputs, defaults, and mode detection for new sessions
- [ ] Required environment:
  - [ ] `OPENCODE_CONFIG_DIR` must resolve and be used for plan/prompt/reports roots.
- [ ] Optional inputs with defaults:
  - [ ] `RUN_ID` default: `pr1-<UTC timestamp>` for follow-up wave.
  - [ ] `BASELINE_RUN_ID` default: `pr1-20260215T221903Z`.
  - [ ] `MAX_STAGES` default: `all`.
  - [ ] `START_STAGE` default: earliest incomplete safe stage.
  - [ ] `MODE` default: `licensed_local`.
- [ ] Mode detection:
  - [ ] `kickoff-explicit-pr1` when new `pr1-*` run root does not exist.
  - [ ] `resume-explicit-pr1` when run root already exists.
  - [ ] `invalid-run-id` when run ID is missing `pr1-` prefix.

## 3) Deterministic roots and immutable contract
- [ ] Roots for a run are deterministic:
  - [ ] `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-extraction-quality-pr1-$RUN_ID"`
  - [ ] `QUALITY_DATA_ROOT="$REPO_ROOT/.cache/iso26262/mining/quality-runs/$RUN_ID"`
  - [ ] `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`
- [ ] Immutable contract keys are persisted and validated on every resume:
  - [ ] run identity and roots (`RUN_ID`, `CONTROL_RUN_ROOT`, `QUALITY_DATA_ROOT`, `PDF_ROOT`),
  - [ ] PR contract (`PR_URL`, `PR_NUMBER`, `PR_HEAD_BRANCH`, `PR_BASE_BRANCH`, `TARGET_BRANCH`),
  - [ ] baseline pointers (`BASELINE_RUN_ID`, baseline roots),
  - [ ] stage model (`EQ0..EQ13`),
  - [ ] threshold profile hash,
  - [ ] plan path and prompt path.
- [ ] Contract drift is a hard stop.

## 4) Bootstrap, resume, and reset protocol (new-session critical)

### 4A) Kickoff bootstrap
- [ ] `uv sync` in `REPO_ROOT`.
- [ ] Checkout and verify locked PR head branch before any mutation.
- [ ] Create run directories and initialize `state.env`, `checklist.state.env`, `run.log`, `artifacts/`.
- [ ] Acquire lock file and record lock metadata.

### 4B) Resume bootstrap
- [ ] Validate required run files/directories exist.
- [ ] Validate immutable contract keys and stage model.
- [ ] Reconcile stage/checkpoint/evidence consistency before continuing.

### 4C) Reset protocol
- [ ] If run state is irreconcilable, archive existing roots with `.reset-<timestamp>` suffix.
- [ ] Do not delete prior evidence unless explicitly instructed.
- [ ] Restart as kickoff for a fresh `pr1-*` run ID.

## 5) Quality issue register and planned resolution

### IQ1: Residual contamination terms remain in extracted text
- [ ] Observed:
  - [ ] Legal boilerplate remains in three known units: `p06-p0002-par-001`, `p08-p0002-par-001`, `p09-p0002-par-001`.
  - [ ] Terms include: `without prior written permission`, `copyright`, `published in switzerland`.
- [ ] Planned resolution:
  - [ ] Expand contamination signatures beyond current narrow license tokens.
  - [ ] Add deterministic exclusion for legal boilerplate paragraphs during normalization/selection.
  - [ ] Add fixture coverage for legal boilerplate positives/negatives.
- [ ] Exit criteria:
  - [ ] `RESIDUAL_LEGAL_BOILERPLATE_HIT_COUNT == 0` for required parts in `unit-slices.jsonl`.
  - [ ] Same count is `0` in `query-source-rows.jsonl`.

### IQ2: EQ12 contamination gate blind spot
- [ ] Observed:
  - [ ] Hard gate checks `license_header_contamination_rate_pct` only.
  - [ ] `boilerplate_phrase_contamination_rate_pct` is computed but not hard-gated.
- [ ] Planned resolution:
  - [ ] Add threshold keys:
    - [ ] `THRESHOLD_PARAGRAPH_BOILERPLATE_MAX_PCT`
    - [ ] `THRESHOLD_LIST_BOILERPLATE_MAX_PCT`
    - [ ] `THRESHOLD_TABLE_BOILERPLATE_MAX_PCT`
  - [ ] Wire these into `evaluate_thresholds`, category pass/fail, and scorecard output.
  - [ ] Add prompt input support for these overrides.
- [ ] Exit criteria:
  - [ ] EQ12 fails when boilerplate contamination exceeds threshold for any required unit type.

### IQ3: Scope recall metric can exceed 100%
- [ ] Observed:
  - [ ] `table_scope_detection_recall_pct` currently can exceed `100`.
- [ ] Planned resolution:
  - [ ] Redefine denominator to true opportunity count.
  - [ ] Add global metric sanity validation: percent metrics must be in `[0, 100]`.
  - [ ] Reject scorecard/finalization if out-of-range metric appears.
- [ ] Exit criteria:
  - [ ] No percent metric in scorecard is outside `[0, 100]`.

### IQ4: Stale legacy shard files coexist with active shards
- [ ] Observed:
  - [ ] Part folders include undeclared `.jsonl` files not listed in active `part-manifest.jsonc`.
- [ ] Planned resolution:
  - [ ] Enforce manifest-only active shard set in publish/verify.
  - [ ] Remove or archive undeclared shards outside active part directories.
  - [ ] Add verify hard check: directory `.jsonl` set must equal manifest `shards[]` set for required parts.
- [ ] Exit criteria:
  - [ ] For each required part, on-disk active shard set exactly matches manifest.

### IQ5: Anchor registry verification is one-way, not bijective
- [ ] Observed:
  - [ ] Verify ensures registry anchors exist in corpus, but does not enforce full set equality.
- [ ] Planned resolution:
  - [ ] Build active corpus anchor set from manifest-listed shards only.
  - [ ] Enforce exact set equality between active corpus anchors and anchor registry anchors.
  - [ ] Emit bounded diagnostics for missing/extra anchor IDs.
- [ ] Exit criteria:
  - [ ] `anchor_registry_count == active_corpus_anchor_count` and zero set mismatches.

### IQ6: Final summary can reference non-existent evidence paths
- [ ] Observed:
  - [ ] Summary may include lineage evidence paths that were not generated.
- [ ] Planned resolution:
  - [ ] Generate missing lineage audit artifacts or update path wiring to actual artifacts.
  - [ ] Add finalize preflight that validates every `evidence_paths` target exists.
- [ ] Exit criteria:
  - [ ] Every referenced evidence path exists at finalize time.

### IQ7: Stage-model mismatch risk for new sessions
- [ ] Observed:
  - [ ] Follow-up naming can drift (`FQ*`) while executor is fixed to `EQ0..EQ13`.
- [ ] Planned resolution:
  - [ ] Keep executor stage IDs strictly `EQ*`.
  - [ ] Maintain explicit mapping table from follow-up workstreams into `EQ` stages.
- [ ] Exit criteria:
  - [ ] No run attempts with undefined/non-EQ stage IDs.

## 6) Workstream to EQ-stage mapping
- [ ] `FQ0` (run setup) -> `EQ0`.
- [ ] `FQ1` (contamination detection/filtering) -> `EQ2`, `EQ5`, `EQ9`.
- [ ] `FQ2` (EQ12 gate wiring) -> `EQ10`, `EQ12`.
- [ ] `FQ3` (metric correctness/bounds) -> `EQ10`, `EQ12`.
- [ ] `FQ4` (shard hygiene) -> `EQ7`, `EQ11`.
- [ ] `FQ5` (anchor bijection) -> `EQ8`, `EQ11`.
- [ ] `FQ6` (evidence path integrity) -> `EQ12`, `EQ13`.
- [ ] `FQ7` (e2e rerun and acceptance) -> `EQ11`, `EQ12`, `EQ13`.

## 7) Stage plan (EQ0..EQ13)

### EQ0: Bootstrap and contract lock
- [ ] Resolve inputs and detect mode.
- [ ] Enforce PR branch lock and immutable contract.
- [ ] Initialize/reconcile run state/checklist/lock.

### EQ1: Baseline inventory (report only)
- [ ] Capture baseline scorecard and issue inventory from `BASELINE_RUN_ID`.
- [ ] Produce explicit baseline issue artifacts for IQ1-IQ6.

### EQ2: Contamination signature hardening
- [ ] Expand contamination token/signature set (license + legal boilerplate).
- [ ] Add deterministic normalization flags for contamination classing.

### EQ3: Line reconstruction confidence hardening
- [ ] Ensure wrap/dehyphenation logic remains deterministic while contamination handling changes.
- [ ] Guard against regressions in text quality metrics.

### EQ4: Typography retention non-regression
- [ ] Ensure sup/sub/footnote logic remains passing after contamination updates.

### EQ5: Paragraph/list contamination exclusion behavior
- [ ] Apply deterministic exclusion to paragraph/list candidate acceptance.
- [ ] Add/extend fixtures for contamination-negative extraction.

### EQ6: List marker and continuation non-regression
- [ ] Confirm list marker validity and continuation capture remain at threshold.

### EQ7: Publish shard hygiene
- [ ] Enforce manifest-only active shard set.
- [ ] Remove/archive undeclared shards from active required-part directories.

### EQ8: Scope and anchor completeness hardening
- [ ] Ensure section/clause/table scope linkage remains complete.
- [ ] Prepare strict active-corpus anchor set extraction.

### EQ9: Selector and linkage strictness
- [ ] Enforce selection/linkage behavior with contamination exclusions and no fallback leakage.

### EQ10: Metric/gate contract updates
- [ ] Add boilerplate thresholds and hard-gate wiring.
- [ ] Add metric sanity checks and `[0,100]` bounds validation.
- [ ] Update prompt input list for new threshold overrides.

### EQ11: End-to-end rerun + strict verify
- [ ] Rerun ingest/extract/normalize/anchor/publish/verify.
- [ ] Enforce anchor registry equality against active manifest-listed corpus anchors.
- [ ] Enforce undeclared-shard failure behavior.

### EQ12: Acceptance audit
- [ ] Run hard thresholds including new boilerplate thresholds.
- [ ] Validate metric sanity constraints and residual contamination count.
- [ ] Validate evidence paths are concrete and existing.

### EQ13: Finalize
- [ ] Write final summary only after evidence-path existence check passes.
- [ ] Release lock and finalize run state.

## 8) Stage evidence contract (required for successful resume)
- [ ] For each stage `EQx`, write:
  - [ ] `artifacts/evidence/EQx.implementation-evidence.json`
  - [ ] `artifacts/checkpoints/EQx.done.json`
- [ ] Evidence payload must include:
  - [ ] `run_id`, `stage`, `timestamp_utc`, `commit_shas`, `changed_files`, `tests_run`, `metrics_before`, `metrics_after`, `metrics_delta`.
- [ ] For implementation stages (`EQ2..EQ11`):
  - [ ] at least one qualifying code commit,
  - [ ] commit references stage tag (`[EQx]`) in message,
  - [ ] commit is reachable from `TARGET_BRANCH` head.

## 9) Validation matrix (must pass before EQ13)

### Functional and completeness checks
- [ ] Required parts completeness remains `3/3`.
- [ ] Required unit types remain present for each required part.
- [ ] Replay signature match remains `100%`.

### Quality checks
- [ ] `RESIDUAL_LEGAL_BOILERPLATE_HIT_COUNT == 0` in both normalize and query source rows.
- [ ] License and boilerplate contamination thresholds pass for each required unit type.
- [ ] No scorecard percent metric outside `[0,100]`.

### Integrity checks
- [ ] Active shard set equals manifest shard set for each required part.
- [ ] Anchor registry set equals active corpus anchor set.
- [ ] All final summary evidence paths exist.

### CI and lint checks for touched Python files
- [ ] `uvx black . --check --diff --color`
- [ ] `uvx flake8 . --exclude .venv`

## 10) Mandatory stop conditions
- [ ] Active lock owned by another process.
- [ ] Immutable contract drift.
- [ ] Branch drift from locked PR head branch.
- [ ] Invalid run ID scope (not `pr1-*`).
- [ ] Stage model mismatch (anything outside `EQ0..EQ13`).
- [ ] Missing/unparsable state or checklist.
- [ ] Missing stage evidence/checkpoint for a stage marked done.
- [ ] EQ12 hard-threshold failure.
- [ ] Any percent metric outside `[0,100]`.
- [ ] Residual legal-boilerplate hit count > 0 for required parts.
- [ ] Undeclared active shard files detected for required parts.
- [ ] Anchor set mismatch between active corpus and registry.
- [ ] Final summary references non-existent evidence artifact.

## 11) Required outputs for handoff
- [ ] `artifacts/quality/quality-scorecard.json`
- [ ] `artifacts/checkpoints/EQ12.acceptance-audit.json`
- [ ] `artifacts/final/quality-remediation-summary.json`
- [ ] `artifacts/pipeline-control/artifacts/verify/verify-summary.json`
- [ ] `artifacts/lineage/*` (if referenced by final summary)
- [ ] A final run report that includes:
  - [ ] mode, run id, branch lock info,
  - [ ] stage before/after and completed stages,
  - [ ] threshold profile and pass/fail by category,
  - [ ] explicit blockers or `STOP_REASON`,
  - [ ] exact resume hint.

## 12) New-session runbook (copy/paste ready)

### Kickoff new follow-up run
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="pr1-$(date -u +%Y%m%dT%H%M%SZ)" \
BASELINE_RUN_ID="pr1-20260215T221903Z" \
MAX_STAGES="all" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

### Resume an existing follow-up run
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="<existing-pr1-run-id>" \
START_STAGE="<EQ0..EQ13>" \
MAX_STAGES="all" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

### Throttled execution for debugging
```bash
OPENCODE_CONFIG_DIR="${OPENCODE_CONFIG_DIR:?}" \
RUN_ID="<existing-pr1-run-id>" \
START_STAGE="EQ10" \
MAX_STAGES="2" \
uv run python tools/traceability/mining/execute_quality_remediation.py
```

## 13) Definition of done
- [ ] All IQ1-IQ7 exit criteria pass in one full rerun.
- [ ] All stages `EQ0..EQ13` complete with valid evidence artifacts.
- [ ] No mandatory stop condition is triggered.
- [ ] Required quality and integrity checks pass.
- [ ] Lint checks pass for touched Python files.
- [ ] Follow-up commits use Conventional Commits and reference this plan path.
