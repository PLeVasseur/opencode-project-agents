# Part 6 Table 1 Retrieval Recovery Plan (Phase 1 Reliability, Phase 2 Expansion)

## Decision

We will recover retrieval quality in two stages:

1. **Phase 1 (now):** fix reliability/quality using the current Rust Reference corpus only.
2. **Phase 2 (later):** expand corpus coverage after Phase 1 quality gates pass.

Rationale: this keeps improvements measurable and attributable, avoids conflating
retrieval defects with source-mix changes, and gives us a clean before/after line.

## Why Recovery Is Needed

Based on `feedback/rust-reference/rust-reference-retrieval-feedback.md` and
captured bundle `query-review-handoff-20260222`:

- Row projection is not yet trustworthy for Table 1 mapping (heavy `1i` skew).
- Some prompts are poorly aligned with Rust Reference vocabulary.
- Statement chunk size is inconsistent (very short and very long extremes).
- Score instrumentation is sometimes hard to interpret.
- Hybrid latency is high for interactive work in current settings.

## Scope and Non-Goals

### In scope (Phase 1)

- Retrieval quality and explainability on **current Rust Reference corpus**.
- Row-projection precision and abstain behavior.
- Query rewrite bridge from ISO phrasing to Rust-native terms.
- Chunk/context normalization and latency tuning.

### Out of scope (Phase 1)

- Adding external corpora (Rust Book, Rustonomicon, Clippy docs, style guides, internal policy docs).
- Declaring full Table 1 coverage complete from Rust Reference alone.

### In scope (Phase 2)

- Controlled corpus expansion with source tagging, provenance, and per-source evaluation.

## Baseline Snapshot (Before Recovery)

- Corpus: 2,896 statements.
- Five-query hybrid capture latency: ~23.5s to ~50.1s.
- Row-marker distribution across 40 returned rows in sample: `1i` = 28 (70%).
- Observed row metadata anomaly risk:
  - `table1_rows.requirement_text` for `1i` is abnormally long.
  - suffix/footnote noise appears in some row texts (for example `...f`).

## Recovery Principles

- Keep retrieval statement-first and full-corpus (no mechanism-gated membership).
- Keep row projection as **post-retrieval annotation**, never pre-ranking gate.
- Allow explicit "no-row" when evidence is weak.
- Optimize for human review quality first, then metric gates.
- Keep all runs reproducible with persisted artifacts.

## Phase 1 - Reliability and Quality on Current Corpus

## Workstream A - Baseline Freeze and Diagnostics

- [ ] Freeze baseline artifacts for A/B comparisons.
  - [ ] Preserve current five-query bundle and evaluator reports under timestamped path.
  - [ ] Add a baseline summary file with current row-marker skew and latency stats.
- [ ] Add a repeatable diagnostics command pack.
  - [ ] One command for five-query bundle capture.
  - [ ] One command for metric report generation.
  - [ ] One command for row-marker distribution report.

## Workstream B - Table 1 Row Metadata Repair

- [ ] Repair and validate `table1_rows` requirement text quality.
  - [ ] Rebuild row requirement extraction to avoid footnote bleed and row text concatenation.
  - [ ] Ensure each row (`1a`..`1i`) has clean, bounded requirement text.
  - [ ] Verify row labels and text lengths against sanity bounds.
- [ ] Add hard validation checks during build/migrate.
  - [ ] Fail build if a row requirement exceeds max expected size.
  - [ ] Fail build if row marker labels are malformed or duplicated.
  - [ ] Emit validation report artifact with row text lengths and token counts.
- [ ] Add regression tests for row metadata integrity.

## Workstream C - Row Projection Reliability Redesign

- [ ] Replace lexical-overlap row tagging with calibrated row classification.
  - [ ] Add semantic row-profile scoring (statement vs row profile embedding similarity).
  - [ ] Keep top-k row candidates but require confidence threshold.
  - [ ] Add explicit abstain output when no row passes threshold.
- [ ] Add row-projection provenance fields.
  - [ ] Include classifier version and threshold in response payload.
  - [ ] Include confidence and reason codes for abstain cases.
- [ ] Evaluate row-marker quality on hand-labeled set.
  - [ ] Build labeled set (10-20 prompts per row, minimum 90 prompts total).
  - [ ] Track per-row precision/recall/F1 and abstain rate.

## Workstream D - ISO-to-Rust Query Rewriting Layer

- [ ] Add rewrite pass before retrieval (logged and inspectable).
  - [ ] Define row-aware term map (example: "strong typing" -> type checking/traits/generics/casts/coercions).
  - [ ] Preserve original query and rewritten query in artifacts.
  - [ ] Support no-rewrite toggle for A/B evaluation.
- [ ] Add rewrite quality tests.
  - [ ] Ensure deterministic rewrite output.
  - [ ] Ensure no destructive rewrite for already Rust-native queries.

## Workstream E - Chunking and Context Normalization

- [ ] Normalize text used for embeddings/reranking.
  - [ ] Keep raw text for display/citation.
  - [ ] Add cleaned embedding text view (remove noisy markers/bullets/admonition artifacts).
- [ ] Introduce concept-sized retrieval chunks.
  - [ ] Add chunk splitting for overlong statements.
  - [ ] Merge or contextualize very short fragments where needed.
  - [ ] Keep traceability back to original `statement_id`.
- [ ] Return context windows for review.
  - [ ] Include +/- neighboring statements and section title in output payload.
  - [ ] Keep citation anchor stable and explicit.

## Workstream F - Score Instrumentation Consistency

- [ ] Make scoring fields semantically consistent across modes.
  - [ ] Define exact meaning of `bm25_raw`, `lexical_score`, `semantic_score`, `reranker_score`, `relevance_score`.
  - [ ] Ensure fields not computed in a mode are null or explicitly marked unavailable.
  - [ ] Remove or rename misleading fields.
- [ ] Add score-audit tests for representative lexical/semantic/hybrid cases.

## Workstream G - Interactive Latency Reduction

- [ ] Add interactive performance profile (default for manual querying).
  - [ ] Lower candidate pool defaults for hybrid interactive usage.
  - [ ] Bound rerank set size.
  - [ ] Add optional preflight cache TTL to reduce repeated backend probe cost.
- [ ] Retain deep-eval profile separately for quality runs.
  - [ ] Explicit profile flags in CLI and reports (`interactive` vs `eval`).
- [ ] Add latency tracking in artifacts.
  - [ ] Record median/p95 per mode and profile.

## Workstream H - Evaluation and Quality Gates

- [ ] Extend evaluation suite for recovery outcomes.
  - [ ] Add top-3 evidence usefulness rubric for five representative prompts.
  - [ ] Add row-marker correctness suite with abstain-aware scoring.
  - [ ] Add rewrite on/off A/B comparison suite.
- [ ] Define hard gates for Phase 1 completion.
  - [ ] Row projection macro precision@1 >= 0.75 on labeled row set.
  - [ ] Row abstain behavior present and calibrated (not forced labeling).
  - [ ] Five-query manual review bundle accepted by reviewer as "directionally useful".
  - [ ] Interactive hybrid median latency <= 15s on local baseline for five-query pack.
  - [ ] No regression in retrieval traceability fields (statement_id + anchor + metadata).

## Workstream I - Documentation and Adoption

- [ ] Update process docs and review command docs.
  - [ ] Add "how to interpret outputs" section (evidence first, row projection secondary).
  - [ ] Add troubleshooting for rewrite and abstain behavior.
- [ ] Publish a recovery report.
  - [ ] Baseline vs post-recovery metrics.
  - [ ] Known limitations and unresolved risks.

## Phase 1 Deliverables (Concrete File Targets)

- [ ] Code:
  - [ ] `scripts/sqlite_query_rust_reference.py` (rewrite, row classifier, score cleanup, profile support)
  - [ ] `scripts/sqlite_eval_rust_reference_retrieval.py` (row-classifier metrics, A/B hooks)
  - [ ] `scripts/sqlite_build_rust_reference.py` and/or migration script (row text sanity checks)
  - [ ] optional new script: `scripts/sqlite_report_row_projection_quality.py`
- [ ] Data:
  - [ ] new labeled set for row-marker quality (under `data/query_testsets/`)
  - [ ] rewrite term map config (versioned)
- [ ] Reports:
  - [ ] baseline and post-recovery bundles under `.cache/sqlite_kb/reports/rust_reference/`

## Phase 2 - Controlled Corpus Expansion (After Phase 1 Gates Pass)

Start only after all Phase 1 hard gates pass.

## Workstream J - Source Expansion Design

- [ ] Add source inventory and priority order.
  - [ ] Rustonomicon (unsafe practice depth)
  - [ ] Rust Book (idiomatic error handling and patterns)
  - [ ] Rust API Guidelines (design/naming/style)
  - [ ] Clippy lint docs and rustfmt/style references
  - [ ] Internal coding/modeling guidelines for organization-specific requirements
- [ ] Define source quality and licensing constraints.

## Workstream K - Ingestion and Provenance

- [ ] Build ingestion pipelines per source with provenance fields.
  - [ ] `source_type`, `source_doc`, revision, timestamp, license tag.
  - [ ] Chunking policy per source, harmonized metadata shape.
- [ ] Add source-aware retrieval filtering and reporting.

## Workstream L - Table 1 Coverage Calibration

- [ ] Create row-to-source fit matrix and enforce routing hints.
  - [ ] Rows weak in Rust Reference alone (1a/1e/1f/1g/1h style naming aspects) get expanded-source support.
- [ ] Re-run evaluation with per-source attribution.

## Workstream M - Phase 2 Gates

- [ ] Coverage gain demonstrated on weak rows without harming strong rows.
- [ ] Row-marker quality remains stable or improves.
- [ ] Latency remains within profile budget.
- [ ] Reviewer acceptance on expanded five-query plus row-specific packs.

## Risks and Mitigations

- Risk: Row classifier overfits to labeled set.
  - Mitigation: keep held-out prompts and periodic blind review.
- Risk: Query rewrite introduces false intent drift.
  - Mitigation: always log original and rewritten query; support no-rewrite A/B.
- Risk: Latency improvements reduce quality.
  - Mitigation: maintain separate interactive and deep-eval profiles.
- Risk: Corpus expansion dilutes precision.
  - Mitigation: source tagging, source-aware scoring, per-source diagnostics.

## Execution Order (Recommended)

- [ ] Step 1: Workstreams A + B (baseline freeze + row metadata repair).
- [ ] Step 2: Workstream C (row projection classifier + abstain) with initial labeled set.
- [ ] Step 3: Workstreams D + F (query rewrite + scoring consistency).
- [ ] Step 4: Workstreams E + G (chunk/context normalization + latency profile).
- [ ] Step 5: Workstream H + I (gates, docs, post-recovery report).
- [ ] Step 6: Phase 2 J/K/L/M (only after Phase 1 gate pass).

## Definition of Done

- [ ] Phase 1 hard gates are green and reviewer signs off on usefulness of outputs.
- [ ] Recovery report documents measurable improvement from baseline.
- [ ] Phase 2 plan is approved with explicit source-by-source onboarding sequence.
