# Part 6 Table 1 Row-First Tuple-Complete Pilot Rebuild Plan

## Objective

- [ ] Enforce context hygiene while executing this pilot plan.
  - [ ] Read only files required for the active row-lane task and supporting SQLite contract/guardrail artifacts.
  - [ ] Do not read unrelated repository code during row-first implementation.
  - [ ] If additional files are required, record the reason first.

- [ ] Rebuild growth around Table 1 rows using exhaustive tuple coverage before full guideline writing.
  - [ ] Pilot scope is Part 6 Table 1 only.
  - [ ] Canonical tuple shape is (`table_row`, `violation_pattern`, `rust_mechanism`).
  - [ ] If one violation has N valid mitigations, include all N `rust_mechanism` tuples.
  - [ ] Mechanism scope for v1 is language + `core/std` + Clippy only.

## Phase 0 - Scope, Baseline, and Canonical Row Identity

- [ ] Lock pilot to Table 1 rows (`1a`..`1i`) and exclude non-Table-1 acceptance.
  - [ ] Define a row lane per row marker (`1a`, `1b`, ..., `1i`).
  - [ ] Keep non-Table-1 generation disabled for pilot pass/fail.
- [ ] Capture baseline metrics before architecture changes.
  - [ ] Snapshot diversity, quality, examples, alignment, decomposition, completeness reports.
  - [ ] Snapshot existing Table 1 seed/guideline/coverage state.
- [ ] Use SQLite IDs and markers as canonical row identity.
  - [ ] Read `nodes` from extractor index SQLite for `table_row` records under Table 1.
  - [ ] Store `row_node_id` (primary identity), `row_idx`, and row marker from `table_cell col_idx=1`.
  - [ ] Persist canonical row catalog in `data/table1_rows.yaml`.

## Phase 1 - Tuple Bank Data Model (Before Guideline Materialization)

- [ ] Create row-level tuple bank artifacts.
  - [ ] Add `data/table1_violation_patterns.yaml` keyed by `row_node_id`.
  - [ ] Add `data/table1_mechanisms.yaml` keyed by `row_node_id` and mechanism family.
  - [ ] Add `data/table1_tuple_bank.yaml` with one record per `(row, violation, mechanism)`.
- [ ] Define tuple provenance and enforcement metadata.
  - [ ] Include row identity (`row_node_id`, marker, `row_key`) in every tuple.
  - [ ] Include `enforcement_kind` (`hard`, `lint`, `review`).
  - [ ] Include ISO and Rust evidence anchors used to justify tuple validity.
- [ ] Define strict tuple completeness semantics.
  - [ ] For each row + violation pattern, enumerate all applicable mechanisms in v1 scope.
  - [ ] For mechanisms deemed not applicable, require explicit exclusion rationale.
  - [ ] Add closure checks so missing applicable mechanisms fail the row closure gate.

## Phase 2 - Seed and Query Pipeline Corrections (Pilot Prereq)

- [ ] Fix exact-query matching to prevent false positives.
  - [ ] `Table 1` exact queries must not accept `Table 10`/`Table 11` by substring.
  - [ ] Use strict normalized reference equality for exact table matching.
- [ ] Preserve row-level obligations completely.
  - [ ] Stop using first pinpoint row only; ingest all relevant pinpoint rows.
  - [ ] Deduplicate at row identity level (`row_node_id`/`row_key`), not table anchor only.
- [ ] Ensure query profile supports full Table 1 row extraction.
  - [ ] Add pilot query profile that captures all Table 1 rows, not a partial top-k.
  - [ ] Keep concept lanes needed for strong typing, defensive techniques, and concurrency.

## Phase 3 - Row-First Execution Strategy

- [ ] Execute one row at a time to tuple closure.
  - [ ] Start with row `1c` (strong typing) as the first lane.
  - [ ] For current row: enumerate violation patterns, then enumerate all v1 mechanisms.
  - [ ] Build full applicability matrix and close all gaps before moving to next row.
- [ ] Require tuple closure gate before advancing rows.
  - [ ] Row fails closure if any applicable mechanism is missing for a violation.
  - [ ] Row fails closure if provenance is missing row ID/marker or evidence anchors.
  - [ ] Row passes only when tuple bank completeness report is green.
- [ ] Add early integration smoke checks without full rollout.
  - [ ] Materialize a small sample from the first closed row to verify schema/tooling compatibility.
  - [ ] Keep smoke outputs isolated from full corpus decisions.

## Phase 4 - Deferred Guideline Materialization

- [ ] Do not fully write final guidelines until tuple banks are complete across all Table 1 rows.
  - [ ] Keep tuple-bank growth and validation as the primary loop artifact.
  - [ ] Materialize full `data/todo_guidelines.yaml` only after all row lanes close.
- [ ] Generate guidelines from tuples deterministically.
  - [ ] Derive `rule_statement`, `amplification`, `exceptions`, `rationale` from tuple semantics.
  - [ ] Preserve required record shape and lifecycle fields in guideline spec.
  - [ ] Maintain per-rule traceability to row ID/marker and tuple IDs.
- [ ] Generate paired examples from tuple scenarios.
  - [ ] Always produce at least one compliant and one non-compliant example per guideline.
  - [ ] Non-compliant case must represent the exact violation pattern from the tuple.
  - [ ] Include outcomes/signals/assertions required by example-quality policy.

## Phase 5 - Autonomous Loop and Refresh Semantics

- [ ] Rework controller to row-lane tuple closure workflow.
  - [ ] Scheduler selects one row lane (or tightly bounded row batch) per iteration.
  - [ ] Action space prioritizes tuple discovery, tuple validation, and row closure.
  - [ ] Advance to next row only after closure gate passes.
- [ ] Prevent generic refresh from erasing accepted tuple-grounded results.
  - [ ] Restrict refresh to touched row lanes.
  - [ ] Preserve accepted tuple-proven fields unless superseded by stronger evidence.
  - [ ] Disable broad template rewrites for pilot row lanes.

## Phase 6 - Gates and Acceptance Criteria

- [ ] Add tuple-bank gates for pilot.
  - [ ] Row identity integrity gate (`row_node_id` + marker required).
  - [ ] Tuple closure gate (all applicable mechanisms present per violation).
  - [ ] Provenance gate (ISO + Rust evidence anchors required).
- [ ] Tighten existing quality gates for pilot materialization runs.
  - [ ] Hard-fail duplicate and near-duplicate diversity violations.
  - [ ] Hard-fail severe example-signature repetition and weak negative evidence.
  - [ ] Hard-fail low guideline-quality scores for newly materialized pilot rules.
- [ ] Pilot completion criteria.
  - [ ] All Table 1 rows (`1a`..`1i`) reach tuple closure.
  - [ ] Full materialization produces schema-valid, non-generic guidelines with paired examples.
  - [ ] Autonomous loop converges for multiple consecutive iterations without regression.

## Phase 7 - Expansion After Pilot

- [ ] Reuse row-first tuple-closure architecture for other Part 6 sources.
  - [ ] Add new source registries incrementally (no big-bang migration).
  - [ ] Keep mechanism scope explicit per source group.
- [ ] Preserve incremental rollout safety.
  - [ ] Expand one source group at a time with explicit closure and quality gates.
  - [ ] Track rollback triggers for quality/diversity/example regressions.

## Implementation Sequence

- [ ] Step 1: Build canonical Table 1 row catalog from SQLite.
  - [ ] Persist row IDs, markers, row indices, and compatible row keys.
  - [ ] Add validation checks for row catalog consistency.
- [ ] Step 2: Implement tuple-bank schema and closure checker.
  - [ ] Add violation-pattern and mechanism inventories.
  - [ ] Add closure report artifact and enforce missing-mechanism failures.
- [ ] Step 3: Complete first row (`1c`) to exhaustive tuple closure.
  - [ ] Enumerate all applicable language/core/std/Clippy mechanisms.
  - [ ] Verify all N mechanisms are captured for each violation pattern.
- [ ] Step 4: Run limited materialization smoke for `1c`.
  - [ ] Generate a small set of guidelines/examples from closed tuples.
  - [ ] Confirm compatibility with existing validators.
- [ ] Step 5: Iterate row-by-row (`1a`..`1i`) to closure.
  - [ ] Do not advance a row lane without passing closure gate.
  - [ ] Keep tuple completeness and provenance reports green.
- [ ] Step 6: Materialize full Table 1 guideline corpus and run convergence loop.
  - [ ] Generate full guidelines and examples from closed tuple banks.
  - [ ] Run full gate suite and prepare expansion recommendation.
