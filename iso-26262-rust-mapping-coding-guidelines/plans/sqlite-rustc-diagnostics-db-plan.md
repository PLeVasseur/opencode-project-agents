# SQLite Plan: rustc Diagnostics (`rustc_diagnostics.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a SQLite corpus of rustc diagnostics and error index entries.
  - [ ] Capture error codes, messages, explanations, and examples.
  - [ ] Enable mapping from violation patterns to compiler feedback.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for diagnostic code and text lookup.
  - [ ] Define helper views for compile-fail evidence retrieval by mechanism.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/rustc_diagnostics.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/rustc_diagnostics/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/rustc_diagnostics/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_rustc_diagnostics.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_rustc_diagnostics.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_rustc_diagnostics.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/rustc_diagnostics.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_rustc_diagnostics.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_rustc_diagnostics.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest rustc error index and diagnostics references from pinned toolchain.
  - [ ] Record toolchain version and source hash.
  - [ ] Preserve links to canonical docs pages.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, toolchain, fetched_at, sha256)`
  - [ ] `diagnostics(diag_id, code, title, level, docs_url, summary)`
  - [ ] `diagnostic_details(detail_id, diag_id, section_kind, text)`
  - [ ] `diagnostic_examples(example_id, diag_id, code, expected_outcome)`
  - [ ] `diagnostic_mechanisms(diag_id, mechanism_id, confidence)`

## Extraction Pipeline

- [ ] Implement extraction and normalization.
  - [ ] Parse structured diagnostic entries and section text.
  - [ ] Normalize error code format and edition metadata.
  - [ ] Link diagnostics to mechanism IDs and violation patterns.

## Validation Gates

- [ ] Add diagnostics integrity checks.
  - [ ] Fail on duplicate diagnostic codes.
  - [ ] Fail if high-priority codes disappear without explicit allowlist.
  - [ ] Verify parsability of examples for regression testing.

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

- [ ] Use diagnostics as executable evidence for non-compliant outcomes.
  - [ ] Prefer tuples with deterministic compile-time failure when available.
  - [ ] Attach diagnostic anchors to example expectations.

## Deliverables

- [ ] Produce `rustc_diagnostics.sqlite` and query helpers.
  - [ ] Add extraction script and validator.
  - [ ] Add report summarizing row-lane relevant diagnostics.
