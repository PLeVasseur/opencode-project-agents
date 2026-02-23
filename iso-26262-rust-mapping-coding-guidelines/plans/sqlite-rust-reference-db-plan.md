# SQLite Plan: Rust Reference (`rust_reference.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a structured SQLite representation of The Rust Reference for normative mechanism grounding.
  - [ ] Capture sections, anchors, and semantic statements that define language behavior.
  - [ ] Preserve stable anchor IDs for tuple provenance.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for section/anchor search and evidence joins.
  - [ ] Define helper views for row-lane mechanism lookup by anchor.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/rust_reference.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/rust_reference/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/rust_reference/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_rust_reference.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_rust_reference.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_rust_reference.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/rust_reference.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_rust_reference.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_rust_reference.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest Rust Reference source from pinned revision.
  - [ ] Record repository commit, fetched timestamp, and hash manifest.
  - [ ] Preserve chapter/section hierarchy from source markdown.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, commit_sha, source_url, fetched_at, sha256)`
  - [ ] `chapters(chapter_id, title, order_index)`
  - [ ] `sections(section_id, chapter_id, anchor, heading, order_index, text)`
  - [ ] `statements(statement_id, section_id, statement_type, text, confidence)`
  - [ ] `mechanisms(mechanism_id, canonical_symbol, mechanism_family, stability)`

## Extraction Pipeline

- [ ] Parse and normalize reference content.
  - [ ] Build deterministic anchor-to-text extraction.
  - [ ] Tag statement types (`definition`, `constraint`, `behavior`).
  - [ ] Link statements to canonical mechanism IDs.

## Validation Gates

- [ ] Add structural and semantic checks.
  - [ ] Fail on missing anchors or duplicate section IDs.
  - [ ] Verify high-safety chapters are present (`types`, `unsafe`, `concurrency`, `traits`).
  - [ ] Detect major content drift between snapshots.

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

- [ ] Use Reference evidence as a primary source for `hard` mechanisms.
  - [ ] Map row violations to language constructs and constraints.
  - [ ] Require at least one Rust Reference anchor for each language-level tuple.

## Deliverables

- [ ] Produce `rust_reference.sqlite` and ingestion docs.
  - [ ] Add extraction script + schema migration script.
  - [ ] Add validation report artifact for each snapshot.
