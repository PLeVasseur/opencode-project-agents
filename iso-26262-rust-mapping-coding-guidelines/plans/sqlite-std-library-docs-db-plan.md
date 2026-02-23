# SQLite Plan: Standard Library Docs (`std_docs.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a local SQLite catalog of `std` API semantics for production mechanism discovery.
  - [ ] Capture signatures, contracts, panic/error behavior, and concurrency primitives.
  - [ ] Link each item to mechanism IDs used in tuple closure.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for API/contract lookup.
  - [ ] Define helper views for `std`-only vs `core`-shared mechanism queries.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/std_docs.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/std_docs/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/std_docs/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_std_docs.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_std_docs.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_std_docs.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/std_docs.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_std_docs.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_std_docs.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest `library/std` docs from pinned Rust revision.
  - [ ] Record commit SHA and generated docs hash.
  - [ ] Preserve crate/module/item hierarchy and stable anchors.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, commit_sha, fetched_at, sha256)`
  - [ ] `modules(module_id, path, title)`
  - [ ] `items(item_id, module_id, fq_path, item_kind, signature, stability)`
  - [ ] `contracts(contract_id, item_id, contract_kind, text)`
  - [ ] `behavior_notes(note_id, item_id, behavior_kind, text)`

## Extraction Pipeline

- [ ] Implement docs parser and normalization.
  - [ ] Extract safety notes, panics, and error sections.
  - [ ] Normalize concurrency APIs (`Mutex`, `RwLock`, `Arc`, atomics).
  - [ ] Map each API item to mechanism families and enforcement kinds.

## Validation Gates

- [ ] Add coverage checks.
  - [ ] Fail on duplicate FQ paths or missing anchors.
  - [ ] Verify presence of high-value APIs (`std::sync`, `std::result::Result`, `std::error::Error`).
  - [ ] Alert on major item count deltas per snapshot.

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

- [ ] Use `std` docs for library-level mechanism completeness.
  - [ ] Require API-contract evidence for tuple selection.
  - [ ] Distinguish `std`-only mechanisms from `core` alternatives.

## Deliverables

- [ ] Produce `std_docs.sqlite` and extraction validator.
  - [ ] Add refresh script and snapshot changelog report.
  - [ ] Expose query helpers for row-lane mechanism enumeration.
