# SQLite Plan: Miri Capabilities (`miri_capabilities.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a SQLite knowledge base describing what Miri catches and what it does not catch.
  - [ ] Capture check categories, limitations, prerequisites, and confidence.
  - [ ] Use documentation/project knowledge as primary source, not runtime findings first.
  - [ ] Treat Miri evidence as supporting scope evidence for tuple closure.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for capability and limitation lookups.
  - [ ] Define helper views for `caught_by_miri` and `not_caught_by_miri` gap analysis.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/miri_capabilities.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/miri_capabilities/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/miri_capabilities/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_miri_capabilities.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_miri_capabilities.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_miri_capabilities.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/miri_capabilities.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_miri_capabilities.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_miri_capabilities.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest Miri documentation and authoritative project references.
  - [ ] Record source URLs, revisions, fetched timestamps, and content hashes.
  - [ ] Extract explicit statements of detected UB classes and non-detected classes.
  - [ ] Capture preconditions and caveats (flags, target limitations, model assumptions).

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, source_kind, source_ref, fetched_at, sha256)`
  - [ ] `checks(check_id, category, caught_pattern, source_anchor, confidence)`
  - [ ] `limitations(limit_id, check_id, not_caught_pattern, reason, source_anchor)`
  - [ ] `preconditions(precondition_id, check_id, requirement_kind, requirement_text)`
  - [ ] `examples(example_id, check_id, example_kind, expected_miri_behavior)`
  - [ ] `check_mechanisms(check_id, mechanism_id, relation_kind)`

## Extraction Pipeline

- [ ] Build capability-first extractor.
  - [ ] Parse docs into structured `checks`, `limitations`, and `preconditions`.
  - [ ] Normalize terms to canonical mechanism IDs and violation-pattern aliases.
  - [ ] Preserve traceable source anchors for every extracted claim.

## Validation Gates

- [ ] Add capability coverage checks.
  - [ ] Fail on entries missing either `caught_pattern` or `not_caught_pattern` mapping context.
  - [ ] Fail on orphan checks without source anchors.
  - [ ] Verify known major capability buckets and major limitations are represented.

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
  - [ ] Results join cleanly into `rust_iso_evidence_hub.sqlite`.
  - [ ] If latency or joinability fails, rework schema/index/query strategy before signoff.

## Integration with Tuple Closure

- [ ] Use Miri capabilities to classify dynamic-check coverage boundaries.
  - [ ] Mark tuples where Miri can provide supporting negative evidence.
  - [ ] Mark tuples where Miri cannot validate the violation pattern.
  - [ ] Require normative corroboration for final enforcement claims.

## Optional Later Phase - Observed Runtime Findings

- [ ] Add optional ingestion of curated Miri run outputs after capability baseline is stable.
  - [ ] Store reproducible run metadata and parsed findings in extension tables.
  - [ ] Keep runtime findings separate from capability/limitation authority records.

## Deliverables

- [ ] Produce `miri_capabilities.sqlite` and capability extraction tooling.
  - [ ] Add validation report focused on catch/not-catch coverage.
  - [ ] Add query helpers used by row-lane tuple closure reports.
