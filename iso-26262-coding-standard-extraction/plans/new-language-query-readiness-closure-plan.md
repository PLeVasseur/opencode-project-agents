# New-Language Query Readiness Closure Plan

## Intent

- Convert the current Part 6-strong extraction stack into an authoring-grade query system for drafting language-specific ISO 26262 coding guidelines for new programming languages.
- Close all remaining readiness gaps with explicit, testable completion criteria.
- Keep all planning artifacts in `$OPENCODE_CONFIG_DIR/plans/` and all licensed/extracted artifacts local under `.cache/iso26262/`.

## Baseline Snapshot (Current State)

- Extraction quality gate is green for the latest run (`extraction_quality_report.json`: 19/19 pass).
- Latest ingest run targeted Part 6 only (`--target-part 6`), so full-corpus freshness is not guaranteed.
- Target register contains 35 prioritized references across Parts 2, 6, 8, and 9.
- Gold-reference coverage against target register is currently 7/35:
  - Part 6: 7/20
  - Part 8: 0/9
  - Part 2: 0/4
  - Part 9: 0/2
- Traceability matrix exists, but the evidence paths are still planning placeholders rather than generated artifacts.

## Comprehensive Remaining Work Register

## R1 - Target Coverage Gap (35 target refs vs partial gold/evaluation coverage)

What remains:

- 28 target references are not yet represented as explicit gold references with strict expected outcomes.
- Validation can pass while still missing large sections of P0-P3 target scope.

Why this blocks the goal:

- New-language guideline drafting needs trustworthy retrieval across all target parts, not just a Part 6 subset.

How to resolve:

- Expand `gold_set_expected_results.json` to full 35-target coverage.
- Add per-target expected values: `expected_page_pattern`, `expected_node_type`, parent/anchor expectations where applicable.
- Add coverage check(s) in `validate` that compare target register vs gold references by `part + ref`.

Exit criteria:

- Gold set covers all 35 targets.
- Validation fails if target coverage drops below 100%.

## R2 - Full-Corpus Freshness Gap (latest run only processed Part 6)

What remains:

- Most recent ingest run processed one part only.
- Non-Part-6 data may be stale relative to current parser and schema behavior.

Why this blocks the goal:

- Drafting guidance for new languages must query all relevant governance/process clauses with consistent parser behavior.

How to resolve:

- Add a full refresh runbook mode for Parts 2, 6, 8, and 9 minimum.
- Add freshness metadata to ingest/validate outputs:
  - processed parts in run,
  - latest run ID by part,
  - stale-part detection based on parser/schema version and source hash set.

Exit criteria:

- A single validated run exists with all target parts freshly ingested.
- `validate` reports per-part freshness status and fails on stale target parts.

## R3 - Extraction Backend and Fidelity Gaps (idea-doc requirements still open)

What remains:

- OCR fallback policy is not implemented as a first-class optional path.
- Header/footer and de-hyphenation quality loop is not fully formalized per part.
- Printed-page mapping fields exist in schema but are not populated.
- Long-clause chunk splitting with overlap is not implemented.

Why this blocks the goal:

- New-language authors need citation-accurate retrieval under mixed PDF conditions and stable chunk semantics.

How to resolve:

- Implement optional OCR mode gated by CLI flag and manifested per page.
- Add extraction-backend provenance fields in ingest manifest (`text_layer`, `ocr`, fallback reason).
- Populate printed-page mappings when detectable.
- Implement semantic split rules for long clauses with deterministic `chunk_seq` and overlap.

Exit criteria:

- OCR pages are explicitly counted and attributable.
- Printed-page mapping is populated for references where page labels are available.
- Long-clause split behavior is deterministic and validated in tests.

## R4 - Hierarchy Semantics Gaps (nested list and richer table-cell contracts)

What remains:

- Nested list/sub-item model is not complete.
- List depth and marker-style metadata are not fully materialized.
- Table-cell structural metadata (header/span semantics) is not fully represented.
- ASIL-style table column alignment still needs a stronger acceptance gate.

Why this blocks the goal:

- Many language-guideline rules derive from fine-grained table/list semantics; flattened structure reduces trust in rule extraction.

How to resolve:

- Extend node model for nested list hierarchy and item depth.
- Extend table cell model for `row_idx`, `col_idx`, `is_header`, `row_span`, `col_span`.
- Add alignment-focused checks for ASIL ratings and marker/description consistency at row level.

Exit criteria:

- Hierarchy checks include nested list contracts and table-cell semantic fields.
- Gold references cover representative nested-list and ASIL-style table cases.

## R5 - Query Contract Hardening Gaps

What remains:

- `query --json` schema contract is not explicitly validated in CI/gates.
- Latency baseline tracking is not implemented.
- Open-at-page helper output is not implemented.

Why this blocks the goal:

- Authoring tooling for new-language guidelines needs stable machine contracts and predictable query performance.

How to resolve:

- Define and version a JSON schema for query output.
- Add schema validation tests and gate checks.
- Add local latency benchmark artifact (query set + p50/p95).
- Add deterministic open-at-page helper output format.

Exit criteria:

- Schema validation passes in gate runs.
- Latency baseline recorded and tracked for regressions.
- Open helper is available for every query hit with page info.

## R6 - Authoring-Synthesis Gap (core underlying goal)

What remains:

- No first-class output that transforms retrieved ISO references into language-guideline drafting units.
- No reusable rule-template package for new-language onboarding.

Why this blocks the goal:

- Querying alone is not enough; the target outcome is writing coding guidelines for new languages with traceable ISO support.

How to resolve:

- Add an authoring synthesis layer that outputs rule-ready units from target references.
- For each target reference, generate structured rule seeds:
  - rule intent,
  - ISO citation set,
  - language concern area,
  - recommended rule form (`shall`, `shall not`, advisory),
  - enforcement method(s),
  - evidence expectations.
- Add a language-profile input (e.g., language features: memory model, typing, concurrency model, unsafe/FFI support).
- Generate language-specific drafting packs from the same ISO core map.

Exit criteria:

- A repeatable command produces a language-specific guideline seed pack with full citations.
- Seed pack covers all P0/P1 areas and links to P2/P3 governance evidence.

## R7 - Traceability Materialization Gap

What remains:

- `traceability_matrix.csv` is present but points to planned artifacts not generated by this workflow.
- Mapping status is not tied to real generated outputs and run IDs.

Why this blocks the goal:

- New-language guideline authoring must be auditable with concrete evidence links, not placeholders.

How to resolve:

- Add deterministic generation of traceability evidence manifests from query/validate/synthesis outputs.
- Add run-linked evidence IDs and artifact paths for each target mapping row.
- Introduce status transitions enforced by checks (`planned -> indexed -> validated -> mapped -> evidenced`).

Exit criteria:

- Every traceability row references an existing generated artifact.
- Status transitions are machine-validated.

## R8 - Idea-to-Implementation Mapping Gap

What remains:

- No explicit requirement map tracking `idea_source -> phase -> implementation_status -> validation_status`.

Why this blocks the goal:

- Harder to prove the implementation still serves the original objective from idea docs.

How to resolve:

- Add `idea_requirements_map.json` under manifests.
- Include one row per requirement derived from:
  - `ideas/iso-26262-query-engine-concept.md`
  - `ideas/iso-26262-parts-that-are-important.md`
- Update map automatically during `validate` or via a dedicated command.

Exit criteria:

- Requirement map exists and is current.
- No requirement stays in unknown state.

## R9 - Final Runbook and Governance Closure

What remains:

- Some plan-level phase checkpoint/governance items remain open.
- Decision-log updates are not consistently tied to all material quality/gold-set changes.

Why this blocks the goal:

- Final handoff for repeated new-language onboarding needs deterministic operational discipline.

How to resolve:

- Finalize runbook gates for full-corpus mode.
- Require decisions-log entries for gold-set mutations, threshold changes, and parser heuristic changes.
- Add a final sign-off checklist specifically for "new-language authoring readiness."

Exit criteria:

- Full runbook can be executed end-to-end without manual state patching.
- Governance artifacts fully explain state transitions and rationale.

## Resolution Program (Execution Plan)

## WP1 - Coverage and Freshness Closure

- Detailed implementation plan: `plans/wp1-coverage-and-freshness-implementation-plan.md`.

- [x] Expand gold references to 35/35 target coverage.
- [x] Add target-vs-gold coverage checks in `validate`.
- [x] Run full ingest for Parts 2, 6, 8, 9 and refresh quality artifacts.
- [x] Add stale-target detection in report.

Outputs:

- [x] Updated `gold_set_expected_results.json`.
- [x] Updated `extraction_quality_report.json` with coverage/freshness sections.

## WP2 - Extraction and Hierarchy Hardening

- Detailed implementation plan: `plans/wp2-extraction-and-hierarchy-hardening-implementation-plan.md`.

- [ ] Implement OCR flag and per-page backend provenance.
- [ ] Implement/verify normalization enhancements (headers/footers, de-hyphenation).
- [ ] Populate printed-page mapping when available.
- [ ] Implement long-clause split with overlap.
- [ ] Complete nested-list and richer table-cell semantics.
- [ ] Add citation-parity non-regression gate for target-linked references.

Outputs:

- [ ] Updated ingest schema/manifest fields.
- [ ] Parser tests covering OCR fallback and split/overlap determinism.
- [ ] Citation parity baseline/report artifacts and pass thresholds.

## WP3 - Query Contract Hardening

- [ ] Define and version `query --json` schema.
- [ ] Add schema-validation tests/gates.
- [ ] Add query latency baseline artifact.
- [ ] Add open-at-page helper output mode.

Outputs:

- [ ] Query schema file and passing schema tests.
- [ ] Query latency baseline report.

## WP4 - Authoring Synthesis for New Languages

- [ ] Define language-profile input contract.
- [ ] Define rule-seed output contract with mandatory citation/evidence fields.
- [ ] Implement synthesis command/workflow to generate language-specific draft packs.
- [ ] Add validation checks for synthesis completeness across P0/P1/P2/P3 coverage.

Outputs:

- [ ] Language-specific guideline seed pack artifact(s).
- [ ] Synthesis quality summary linked to run ID.

## WP5 - Traceability and Idea-Map Finalization

- [ ] Replace traceability placeholders with generated evidence artifact links.
- [ ] Add `idea_requirements_map.json` and keep it synchronized.
- [ ] Add final sign-off checklist for authoring readiness.

Outputs:

- [ ] Updated `traceability_matrix.csv` with evidence-realized rows.
- [ ] `idea_requirements_map.json` in manifests.
- [ ] Final readiness report.

## Definition of Done for "New-Language Query Authoring Readiness"

- [ ] 35/35 target references are gold-covered and validated.
- [ ] Full-corpus freshness confirmed for Parts 2, 6, 8, and 9 in latest run.
- [ ] Query JSON contract is schema-validated and stable.
- [ ] Query latency baseline is recorded and within agreed threshold.
- [ ] Marker/paragraph/table hierarchy quality gates remain green.
- [ ] Authoring synthesis generates citation-complete rule seed packs for a new language profile.
- [ ] Traceability matrix rows link to real generated evidence artifacts.
- [ ] Idea requirement map is complete and up to date.
- [ ] Runbook executes deterministically end-to-end with auditable decision logging.

## Suggested Execution Order

1. WP1 (coverage + freshness)
2. WP2 (extraction + hierarchy)
3. WP3 (query contract)
4. WP4 (authoring synthesis)
5. WP5 (traceability + final sign-off)

## Notes

- This plan intentionally centers the underlying goal: enable effective, auditable authoring of ISO 26262-aligned coding guidelines for new languages.
- Prioritize closure of WP1 before deep parser optimization; coverage/freshness gaps are the highest current risk.
