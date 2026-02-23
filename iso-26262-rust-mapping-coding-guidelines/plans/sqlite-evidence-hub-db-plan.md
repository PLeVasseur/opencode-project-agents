# SQLite Plan: Unified Evidence Hub (`rust_iso_evidence_hub.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a normalized integration SQLite DB that federates all resource DBs for tuple closure.
  - [ ] Keep source DBs immutable and provenance-preserving.
  - [ ] Provide one query surface for row-lane mechanism discovery and validation.

## Phase 0 - Queryability Discovery

- [ ] Discover integration query contract before schema freeze.
  - [ ] Define top controller queries for row closure (`row_node_id`, `violation_pattern`, `rust_mechanism`, evidence strength).
  - [ ] Define canonical join contract with source DB IDs and aliases.
- [ ] Design query strategy for high-volume autonomous iterations.
  - [ ] Define required indexes and FTS strategy for evidence search and joins.
  - [ ] Define precomputed views for closure checks and gap reports.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract query suite with expected outputs.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/rust_iso_evidence_hub.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/rust_iso_evidence_hub/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/rust_iso_evidence_hub/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_rust_iso_evidence_hub.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_rust_iso_evidence_hub.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_rust_iso_evidence_hub.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/rust_iso_evidence_hub.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_rust_iso_evidence_hub.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_rust_iso_evidence_hub.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Integration Scope

- [ ] Integrate all required resource databases.
  - [ ] Include user-requested DBs and additional must-have compiler/process DBs.
  - [ ] Track per-source snapshot IDs and freshness state.

## Schema

- [ ] Define normalized integration tables.
  - [ ] `sources(source_id, db_name, snapshot_id, imported_at, freshness_state)`
  - [ ] `mechanisms(mechanism_id, canonical_symbol, family, enforcement_kind, stability)`
  - [ ] `evidence(evidence_id, source_id, source_anchor, evidence_kind, text, confidence)`
  - [ ] `mechanism_evidence(mechanism_id, evidence_id, relation_kind)`
  - [ ] `row_tuple_coverage(row_node_id, violation_pattern_id, mechanism_id, status, rationale)`

## Build Pipeline

- [ ] Implement deterministic importers for each resource DB.
  - [ ] Normalize IDs and collapse aliases to canonical mechanism IDs.
  - [ ] Preserve source provenance and confidence values.
  - [ ] Rebuild hub idempotently from source snapshots.

## Validation Gates

- [ ] Add integration integrity checks.
  - [ ] Fail on orphan mechanisms without evidence links.
  - [ ] Fail on row-tuple entries missing canonical row identity.
  - [ ] Verify all Table 1 row lanes have discoverable mechanism candidates.

## Definition of Done - Table 1 Row Queryability Gate

- [ ] Pass a hard row queryability gate for all ISO 26262 Part 6 Table 1 rows (`1a`..`1i`).
  - [ ] Run deterministic contract queries keyed by canonical `row_node_id`.
  - [ ] Return a verdict for every row: `applicable` or `not_applicable` only.
  - [ ] Reject unresolved `unknown` row outcomes.
- [ ] Enforce mandatory rationale for non-applicable rows.
  - [ ] Every `not_applicable` verdict includes source-backed rationale text.
  - [ ] Every `not_applicable` verdict includes stable evidence anchors and joinable IDs.
- [ ] Verify integration readiness and performance.
  - [ ] Applicable rows return ranked `rust_mechanism` IDs with deterministic ordering.
  - [ ] Results remain fully joinable to source DB evidence anchors.
  - [ ] If latency or joinability fails, rework schema/index/query strategy before signoff.

## Integration with Row-First Tuple Closure

- [ ] Use hub queries as single mechanism discovery API.
  - [ ] Generate exhaustive mechanism sets per (`row`, `violation_pattern`).
  - [ ] Emit explicit missing/evidence-weak reports for closure gating.
  - [ ] Feed materialization only after closure green across rows.

## Deliverables

- [ ] Produce `rust_iso_evidence_hub.sqlite` and refresh workflow.
  - [ ] Add import orchestration script and validation script.
  - [ ] Add closure-view SQL templates for controller iterations.
