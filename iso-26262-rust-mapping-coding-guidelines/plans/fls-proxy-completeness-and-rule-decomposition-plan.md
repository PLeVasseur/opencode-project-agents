# FLS-Proxy Completeness and ISO Rule-Decomposition Plan

This plan upgrades completion criteria from a weak `>=1 guideline per ISO target` check to a multi-lane model that supports deep decomposition (for example, one ISO clause/table spawning 15-20 Rust guidelines) while using FLS coverage as an imperfect but useful proxy for Rust-surface completeness.

## 0) Core design principles

- [ ] Treat ISO completeness and Rust completeness as separate lanes with separate metrics.
- [ ] Allow one-to-many decomposition: one ISO target can map to many guidelines.
- [ ] Use FLS coverage as a proxy signal, not as a sole acceptance criterion.
- [ ] Preserve deterministic generation, but avoid destructive overwrites of curated guideline content.
- [ ] Keep quality gates strict on non-generic prose/examples before promoting to accepted baselines.

## 1) Completeness model (new definition of done)

### Lane A: ISO obligation coverage

- [ ] Define a stable `obligation_unit_id` for each normalized seed row:
  - [ ] Use `target_id + row_key` when `row_key` exists.
  - [ ] Use `target_id + clause-anchor` fallback when `row_key` is empty.
- [ ] Require 100% obligation-unit coverage: each in-scope `obligation_unit_id` linked to at least one non-generic guideline.
- [ ] Keep clause-level and row-level obligations distinct in metrics.

### Lane B: Decomposition adequacy

- [ ] Add fanout metrics per ISO target:
  - [ ] `target_fanout = count(distinct guideline_id mapped to target_id)`
  - [ ] `obligation_fanout = count(distinct guideline_id mapped to obligation_unit_id)`
- [ ] Add policy floor for broad targets (tables/annexes) so one-rule collapse is blocked.
- [ ] Gate on minimum fanout floor by target class:
  - [ ] Clause targets: low floor (often 1-3).
  - [ ] Table/annex targets: higher floor (for example 4+ or row-proportional).

### Lane C: Rust-surface proxy (FLS)

- [ ] Require every guideline to declare `fls_refs` (`1..n`, may span multiple paragraphs).
- [ ] Build per-target candidate FLS set and compute span:
  - [ ] `fls_span(target) = covered_fls_refs(target) / candidate_fls_refs(target)`
- [ ] Compute global Rust proxy coverage:
  - [ ] `fls_chapter_coverage = covered_fls_chapters / in_scope_fls_chapters`
- [ ] Use thresholds for acceptance, with target-class-specific floors.

## 2) Data model changes

## 2.1 `data/todo_guidelines.yaml` (schema v3)

- [ ] Add required field: `fls_refs`.
- [ ] Shape:
  - [ ] `fls_refs: ["fls_xxxxx", "fls_yyyyy"]` (minItems: 1 for active guidelines)
- [ ] Add optional decomposition fields:
  - [ ] `rule_family_id` (stable per ISO target family)
  - [ ] `decomposition_parent` (if derived/split from another rule)
  - [ ] `obligation_units` (`obligation_unit_id[]` resolved from seeds)

## 2.2 `data/seed_topics.yaml`

- [ ] Add normalized `obligation_unit_id` per seed.
- [ ] Preserve `target_id` and `row_key` for traceability/debug.

## 2.3 Coverage matrix v2

- [ ] Evolve `data/coverage_matrix.csv` columns (or introduce `data/coverage_matrix_v2.csv`):
  - [ ] `target_id`
  - [ ] `obligation_unit_id`
  - [ ] `seed_id`
  - [ ] `guideline_id`
  - [ ] `fls_ref`
  - [ ] `evidence_path`

## 2.4 New proxy artifacts

- [ ] Add `data/fls_inventory.yaml` (FLS paragraph + chapter index).
- [ ] Add `data/fls_target_candidates.yaml` (target/obligation -> candidate `fls_refs` with confidence metadata).
- [ ] Add `config/completeness_policy.yaml` (proxy thresholds and fanout floors).

## 3) Script and pipeline architecture

## 3.1 Seed normalization

- [ ] Update `scripts/build_seed_topics.py`:
  - [ ] Compute and emit `obligation_unit_id`.
  - [ ] Keep deterministic ID generation and dedup behavior.

## 3.2 FLS inventory pipeline

- [ ] Add `scripts/build_fls_inventory.py`:
  - [ ] Parse FLS source snapshot into paragraph/chapter records.
  - [ ] Emit stable `data/fls_inventory.yaml`.
- [ ] Add `scripts/build_fls_target_candidates.py`:
  - [ ] Generate candidate FLS refs per `target_id` and `obligation_unit_id`.
  - [ ] Record confidence and matching evidence (keywords/chapter overlap).

## 3.3 Guideline decomposition engine

- [ ] Add `scripts/decompose_guidelines.py` (new stage before artifact generation):
  - [ ] Produce multiple guideline candidates per target family.
  - [ ] Assign `rule_family_id` and initial `fls_refs` proposals.
  - [ ] Preserve manually curated rules; only scaffold missing siblings.
- [ ] Update `scripts/generate_guideline_artifacts.py`:
  - [ ] Stop full overwrite behavior for curated guideline records.
  - [ ] Merge generated scaffolds with existing curated content.

## 3.4 Gate scripts

- [ ] Extend `scripts/check_guideline_completeness.py`:
  - [ ] Require `fls_refs` for non-deprecated/non-disapplied rules.
  - [ ] Validate each `fls_ref` exists in `data/fls_inventory.yaml`.
- [ ] Add `scripts/check_rule_decomposition.py`:
  - [ ] Enforce fanout floors from `config/completeness_policy.yaml`.
- [ ] Add `scripts/check_fls_proxy_coverage.py`:
  - [ ] Compute per-target `fls_span` and global chapter coverage.
  - [ ] Fail/warn based on policy thresholds.
- [ ] Add `scripts/check_guideline_quality.py`:
  - [ ] Fail on generic/template/placeholder language.
  - [ ] Fail when example prose/code is still placeholder-level.

## 3.5 Orchestration integration

- [ ] Update `scripts/orchestrate.py` step sequence:
  - [ ] `build_seed_topics`
  - [ ] `build_fls_inventory`
  - [ ] `build_fls_target_candidates`
  - [ ] `decompose_guidelines`
  - [ ] `generate_guideline_artifacts`
  - [ ] existing schema/completeness/examples/traceability/licensing gates
  - [ ] `check_rule_decomposition`
  - [ ] `check_fls_proxy_coverage`
  - [ ] `check_guideline_quality`
- [ ] Include new metrics in run outputs under `.cache/ops/runs/<run_id>/metrics.json`.

## 4) Policy thresholds (initial defaults)

- [ ] Add `config/completeness_policy.yaml` with baseline values:
  - [ ] `iso_obligation_coverage_required: 1.0`
  - [ ] `fls_chapter_coverage_min: 0.90`
  - [ ] `fls_span_min_by_target_class`:
    - [ ] `clause: 0.70`
    - [ ] `table: 0.85`
    - [ ] `annex: 0.85`
  - [ ] `target_fanout_min_by_target_class`:
    - [ ] `clause: 1`
    - [ ] `table: 4`
    - [ ] `annex: 4`
  - [ ] `obligation_fanout_min_default: 1`

## 5) Quality threshold calibration against upstream guidelines

- [ ] Use upstream (`rustfoundation/safety-critical-rust-coding-guidelines`) as style/depth benchmark for:
  - [ ] concrete rule statements,
  - [ ] rationale quality,
  - [ ] compliant/non-compliant example quality,
  - [ ] citation hygiene.
- [ ] Define local stricter threshold than "minimum pass":
  - [ ] no generic seed boilerplate in promoted records,
  - [ ] no placeholder examples in promoted records,
  - [ ] explicit `fls_refs` coverage and traceability per guideline.

## 6) Migration strategy (non-breaking rollout)

## Phase 1: Additive fields and soft gates

- [ ] Introduce `fls_refs` as optional in schema v3 initially.
- [ ] Generate candidate `fls_refs` and report coverage as warnings.
- [ ] Add decomposition/fanout reports without hard-failing.

## Phase 2: Backfill and curation

- [ ] Backfill all existing guidelines with curated `fls_refs`.
- [ ] Split broad ISO-derived generic rules into rule families.
- [ ] Replace placeholder fixtures/examples with rule-specific evidence.

## Phase 3: Hard gating

- [ ] Make `fls_refs` required for active guidelines.
- [ ] Enable hard fail for decomposition and proxy thresholds.
- [ ] Block promotion when any lane fails (ISO coverage, decomposition, FLS proxy, quality).

## 7) Autonomous completion criteria

- [ ] Completion requires all of:
  - [ ] ISO lane passes (100% obligation-unit coverage),
  - [ ] decomposition lane passes (fanout floors met),
  - [ ] FLS proxy lane passes (target-span + chapter coverage floors),
  - [ ] quality lane passes (no generic placeholders),
  - [ ] diffset/reviewer gate passes (no unresolved blockers).
- [ ] Add convergence condition to avoid endless churn:
  - [ ] if coverage deltas are below policy threshold across N successive runs and all lanes pass, mark run promotable.

## 8) Risks and guardrails

- [ ] Risk: FLS proxy over-weights lexical matches.
  - [ ] Guardrail: confidence scoring + manual review for low-confidence mappings.
- [ ] Risk: metric gaming via shallow many-rule decomposition.
  - [ ] Guardrail: rule-quality checks and example-specificity checks.
- [ ] Risk: destructive regeneration erases curated splits.
  - [ ] Guardrail: merge-first generator behavior and stable rule-family IDs.

## 9) Implementation slices (recommended order)

- [ ] Slice A: schema/docs update for `fls_refs` and `obligation_unit_id`.
- [ ] Slice B: FLS inventory + candidate mapping artifacts.
- [ ] Slice C: decomposition engine and non-destructive generation.
- [ ] Slice D: coverage matrix v2 and traceability updates.
- [ ] Slice E: decomposition + FLS proxy gates integrated into orchestration.
- [ ] Slice F: quality hardening and promotion policy activation.

## 10) Immediate next action

- [ ] Implement Slice A first: add `fls_refs` to spec/schema/checkers with warning mode, then backfill current guideline backlog so subsequent decomposition work has stable anchors.
