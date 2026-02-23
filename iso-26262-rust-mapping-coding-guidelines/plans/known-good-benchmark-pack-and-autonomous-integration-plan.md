# Known-Good Benchmark Pack and Autonomous Loop Integration Plan

This plan defines a complete, auditable process to:

1) harvest high-quality completed guidelines from the upstream Rust Foundation repo,
2) translate rST to Markdown + canonical JSON,
3) derive quality/granularity baselines,
4) compare local draft guidelines against those baselines,
5) integrate the alignment signal into the autonomous convergence controller.

The intent is to make "good quality" and "right granularity" measurable and enforceable per loop iteration.

## 0) Current baseline (already present)

- [x] Autonomous controller loop with quick/full evaluation and handoff artifacts exists.
- [x] Decomposition, FLS proxy, and guideline quality checks are integrated in orchestration.
- [x] Beam bundle candidate logic exists with compatibility/ranking.
- [x] Handoff recommendation states (`ready|needs_review|blocked`) exist.
- [ ] Known-good benchmark ingestion and comparator are not yet implemented.

## 1) Outcomes and non-goals

### 1.1 Outcomes

- [ ] Produce a pinned benchmark pack from upstream completed guidelines.
- [ ] Create deterministic rST -> Markdown + canonical JSON conversion.
- [ ] Build deterministic quality/granularity alignment scoring.
- [ ] Feed alignment deficits into controller candidate generation and acceptance logic.
- [ ] Require benchmark alignment in handoff recommendation and convergence stop criteria.

### 1.2 Non-goals (initial)

- [ ] No upstream auto-push or auto-PR behavior.
- [ ] No model fine-tuning requirement for first release.
- [ ] No replacement of deterministic gates with LLM-only judgment.

## 2) Benchmark source policy (selection rules)

- [ ] Define a reproducible selector over upstream files (`gui_*.rst`, `gui_*.rst.inc`).
- [ ] Tier benchmark entries:
  - [ ] `strict`: rationale + compliant + non-compliant + citation/bibliography signal + no TODO/release-unknown signal.
  - [ ] `extended`: rationale + compliant + non-compliant + no TODO/release-unknown signal.
- [ ] Store provenance per entry:
  - [ ] `source_repo`, `source_sha`, `source_path`, `source_license`, `tier`, `harvested_at`.
- [ ] Freeze the pack as immutable snapshot by `pack_id` + `source_sha`.

## 3) Artifacts and directory layout

- [ ] Add benchmark root in repo:
  - [ ] `benchmarks/known-good/manifest.yaml`
  - [ ] `benchmarks/known-good/upstream-rst/<chapter>/<guideline_id>.rst`
  - [ ] `benchmarks/known-good/markdown/<chapter>/<guideline_id>.md`
  - [ ] `benchmarks/known-good/canonical/<guideline_id>.json`
  - [ ] `benchmarks/known-good/features/per_guideline.jsonl`
  - [ ] `benchmarks/known-good/features/baseline.json`
  - [ ] `benchmarks/known-good/reports/harvest_report.json`

- [ ] Add policy/config files:
  - [ ] `config/known_good_policy.yaml`
  - [ ] `config/alignment_policy.yaml`

- [ ] Add schemas:
  - [ ] `schemas/known_good_manifest.schema.json`
  - [ ] `schemas/known_good_canonical.schema.json`
  - [ ] `schemas/known_good_features.schema.json`
  - [ ] `schemas/known_good_alignment_report.schema.json`
  - [ ] `schemas/known_good_policy.schema.json`
  - [ ] `schemas/alignment_policy.schema.json`

## 4) Script inventory (new)

- [ ] `scripts/harvest_known_good_guidelines.py`
- [ ] `scripts/translate_known_good_rst_to_md.py`
- [ ] `scripts/build_known_good_canonical.py`
- [ ] `scripts/build_known_good_feature_baseline.py`
- [ ] `scripts/check_known_good_alignment.py`
- [ ] `scripts/refresh_known_good_pack.py`

## 5) Detailed algorithm design

### 5.1 Harvest algorithm

- [ ] Input:
  - [ ] `--source-repo` (default upstream repo)
  - [ ] `--source-sha`
  - [ ] `--tier strict|extended|all`
- [ ] Steps:
  - [ ] enumerate guideline files from pinned tree.
  - [ ] compute completion signals per file.
  - [ ] apply tier selector.
  - [ ] fetch and persist raw rST source snapshot.
  - [ ] emit manifest and harvest report.
- [ ] Output:
  - [ ] immutable snapshot folder + `manifest.yaml`.

### 5.2 rST -> Markdown translator algorithm

- [ ] Use directive-aware parser (not plain generic converter) with explicit states:
  - [ ] `title`
  - [ ] `guideline metadata`
  - [ ] `rule body`
  - [ ] `rationale`
  - [ ] `example blocks`
  - [ ] `bibliography`
- [ ] Directive mapping rules:
  - [ ] `.. guideline::` -> metadata header table/front-matter.
  - [ ] `.. rationale::` -> `## Rationale`.
  - [ ] `.. non_compliant_example::` -> `## Non-Compliant Example N`.
  - [ ] `.. compliant_example::` -> `## Compliant Example N`.
  - [ ] `.. rust-example::` + options -> fenced Rust block + option annotations.
  - [ ] `.. bibliography::` -> `## References` with normalized entries.
- [ ] Preserve:
  - [ ] code body exactly,
  - [ ] citation markers,
  - [ ] explanatory prose,
  - [ ] directive ordering.

### 5.3 Canonicalizer algorithm

- [ ] Transform Markdown into canonical JSON shape:
  - [ ] `id`, `title`, `metadata`, `rule_text`, `rationale_text`
  - [ ] `non_compliant_examples[]`, `compliant_examples[]`
  - [ ] `references[]`, `tags[]`, `scope`, `decidability`
- [ ] Normalize whitespace and stable ordering.
- [ ] Include hashes for source reproducibility (`content_sha256`).

### 5.4 Feature extraction algorithm

- [ ] Compute per-guideline deterministic features:
  - [ ] **Structure**:
    - [ ] section coverage ratio
    - [ ] compliant/non-compliant counts
    - [ ] rationale presence
  - [ ] **Specificity**:
    - [ ] Rust API/type token density
    - [ ] actionable constraint phrase density
  - [ ] **Evidence richness**:
    - [ ] average explanation length
    - [ ] code block count and token count
    - [ ] example diversity indicator
  - [ ] **Citation quality**:
    - [ ] citation count
    - [ ] bibliography presence
  - [ ] **Granularity fit proxies**:
    - [ ] concepts-per-rule score
    - [ ] conditions-per-rule score
    - [ ] examples-per-concept ratio

- [ ] Build baseline stats by tier:
  - [ ] median, IQR, P10/P25/P50/P75/P90 for each feature.
  - [ ] store baseline + recommended bounds in `baseline.json`.

### 5.5 Alignment scoring algorithm

- [ ] Compare local guideline features to baseline bounds.
- [ ] Compute per-dimension normalized score in `[0,1]`.
- [ ] Composite score:
  - [ ] `alignment = 0.30 structure + 0.20 specificity + 0.20 evidence + 0.15 citations + 0.15 granularity`.
- [ ] Emit explicit flags:
  - [ ] `known_good_alignment_gap`
  - [ ] `granularity_too_coarse`
  - [ ] `granularity_too_fine`
  - [ ] `example_depth_too_shallow`
  - [ ] `citation_coverage_low`

### 5.6 Optional retrieval/LLM layer (advisory initially)

- [ ] Build embeddings for benchmark canonical corpus.
- [ ] Retrieve top-k nearest known-good neighbors for each local guideline.
- [ ] Run rubric LLM judgment against nearest neighbors:
  - [ ] granularity fit,
  - [ ] enforceability clarity,
  - [ ] rationale quality,
  - [ ] example relevance.
- [ ] Aggregate via multi-judge median.
- [ ] Keep this advisory until stable calibration windows are achieved.

## 6) Integration into autonomous looper

### 6.1 Observer integration

- [ ] Extend `scripts/controller_observe.py` to run `check_known_good_alignment.py`.
- [ ] Parse alignment report and emit new deficits:
  - [ ] `known_good_alignment_gap`
  - [ ] `granularity_too_coarse`
  - [ ] `granularity_too_fine`
  - [ ] `benchmark_similarity_gap` (if retrieval enabled)

### 6.2 Candidate generation integration

- [ ] Extend `scripts/controller_actions.py` mapping:
  - [ ] coarse granularity -> split/spawn actions.
  - [ ] fine granularity -> coarsen/merge action (new action type).
  - [ ] weak alignment -> rewrite actions (`rule_statement`, `amplification`, `examples`, citations enrichment).
- [ ] Extend bundle compatibility matrix:
  - [ ] block conflicting split+merge of same family in one bundle.
  - [ ] block duplicate rewrite of same field in same bundle.

### 6.3 Scoring + acceptance integration

- [ ] Extend `scripts/controller_scoring.py` lexicographic vector to include alignment dimensions after hard lane checks.
- [ ] Add non-regression rule:
  - [ ] reject any candidate that worsens alignment on currently passing guidelines.
- [ ] Include alignment delta in weighted score and tie-break ordering.

### 6.4 Two-pass evaluation integration

- [ ] Evaluate alignment in quick pass for all beam candidates.
- [ ] Re-evaluate alignment in full pass for top-k rerank candidates.
- [ ] Accept only if alignment is non-regressing and net-improving.

### 6.5 Handoff integration

- [ ] Extend handoff artifacts under `.cache/controller/<session>/handoff/`:
  - [ ] `alignment_summary.json`
  - [ ] `alignment_outliers.json`
  - [ ] `alignment_examples.md`
- [ ] Update recommendation logic:
  - [ ] `ready` requires alignment thresholds + zero forbidden outliers.

## 7) Convergence and stopping updates

- [ ] Add alignment to convergence gates:
  - [ ] changed-guideline alignment above threshold.
  - [ ] no granularity outliers over `K` consecutive full passes.
  - [ ] no oscillation (split/merge flip-flop) over policy window.
- [ ] Add alignment stall diagnostics:
  - [ ] classify stalls as decomposition-limited, evidence-limited, citation-limited, or granularity-limited.

## 8) Governance and refresh lifecycle

- [ ] Add refresh workflow:
  - [ ] `scripts/refresh_known_good_pack.py --source-sha <sha>`
- [ ] Emit refresh diff report:
  - [ ] added/removed entries,
  - [ ] feature baseline shifts,
  - [ ] expected quality gate impact.
- [ ] Require explicit reviewer sign-off before switching active benchmark pack.

## 9) Testing strategy

### 9.1 Unit tests

- [ ] translator directive mapping correctness.
- [ ] canonicalizer stability and field completeness.
- [ ] feature extractor determinism.
- [ ] alignment scorer monotonicity and outlier classification.
- [ ] controller deficit mapping for new alignment deficits.

### 9.2 Integration tests

- [ ] end-to-end benchmark build from pinned fixture snapshot.
- [ ] controller behavior on synthetic coarse/fine guideline scenarios.
- [ ] handoff recommendation transitions when alignment passes/fails.

## 10) Rollout phases with entry/exit criteria

### Phase A - Ingest and translate

- [ ] Entry: benchmark schemas and harvest script scaffolded.
- [ ] Deliver:
  - [ ] first pinned known-good pack,
  - [ ] translated markdown,
  - [ ] canonical JSON.
- [ ] Exit: schema validation + snapshot reproducibility pass.

### Phase B - Deterministic alignment checker

- [ ] Entry: canonical corpus + baseline features available.
- [ ] Deliver:
  - [ ] `check_known_good_alignment.py` in `warn` mode,
  - [ ] alignment report schema + reports.
- [ ] Exit: stable repeated outputs over same input.

### Phase C - Controller integration

- [ ] Entry: alignment checker stable.
- [ ] Deliver:
  - [ ] observer deficits,
  - [ ] action mappings,
  - [ ] scoring + two-pass alignment acceptance.
- [ ] Exit: controller demonstrably improves alignment metrics in simulation fixtures.

### Phase D - Handoff enforcement

- [ ] Entry: controller emits alignment metrics.
- [ ] Deliver:
  - [ ] alignment handoff artifacts,
  - [ ] recommendation logic includes alignment criteria.
- [ ] Exit: `ready` cannot be produced when alignment policy fails.

### Phase E - Optional AI-assisted layer

- [ ] Entry: deterministic alignment gate operating in production loop.
- [ ] Deliver:
  - [ ] retrieval neighbor diagnostics,
  - [ ] rubric-based advisory scoring.
- [ ] Exit: measured calibration quality and no adverse false-positive spikes.

## 11) Initial policy values

- [ ] `alignment_min_score_global: 0.75`
- [ ] `alignment_min_score_changed_guidelines: 0.80`
- [ ] `granularity_outliers_allowed: 0`
- [ ] `benchmark_similarity_min_cosine: 0.70` (advisory initially)
- [ ] `consecutive_full_passes_with_alignment: 3`

## 12) Integration patch map (exact files to touch)

- [ ] `scripts/validate_schemas.py` (new schemas)
- [ ] `scripts/controller_observe.py` (new checker + deficits)
- [ ] `scripts/controller_actions.py` (granularity actions + mappings)
- [ ] `scripts/controller_scoring.py` (alignment dimensions)
- [ ] `scripts/autonomous_controller.py` (alignment-aware acceptance + handoff)
- [ ] `README.md` and workflow docs (new commands + interpretation)

## 13) Deliverable checklist for "done"

- [ ] Known-good benchmark pack generated and pinned.
- [ ] rST->Markdown translator + canonicalizer validated.
- [ ] Deterministic alignment checker integrated in controller loop.
- [ ] Alignment deficits actively drive candidate selection and mutation.
- [ ] Handoff includes alignment evidence and blocks `ready` when misaligned.
- [ ] End-to-end tests green and repeatable.

## 14) Immediate next implementation slice

- [ ] Implement Phase A + B first:
  - [ ] schemas,
  - [ ] harvest script,
  - [ ] translator,
  - [ ] canonicalizer,
  - [ ] baseline extractor,
  - [ ] checker in advisory mode.
