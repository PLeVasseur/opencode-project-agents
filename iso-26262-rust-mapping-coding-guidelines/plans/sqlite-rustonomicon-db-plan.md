# SQLite Plan: Rustonomicon (`rustonomicon.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a SQLite corpus of Rustonomicon unsafe and advanced semantic guidance.
  - [ ] Capture unsafe invariants, caveats, and examples with stable anchors.
  - [ ] Distinguish cautionary guidance from normative language rules.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for unsafe guidance retrieval.
  - [ ] Define helper views for unsafe pattern to mechanism joins.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/rustonomicon.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/rustonomicon/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/rustonomicon/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_rustonomicon.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_rustonomicon.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_rustonomicon.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/rustonomicon.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_rustonomicon.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_rustonomicon.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest Rustonomicon content from pinned revision.
  - [ ] Record commit SHA, source URL, and content hash.
  - [ ] Preserve chapter hierarchy and anchor mapping.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, commit_sha, fetched_at, sha256)`
  - [ ] `chapters(chapter_id, title, order_index)`
  - [ ] `sections(section_id, chapter_id, anchor, heading, text)`
  - [ ] `guidance(guidance_id, section_id, guidance_kind, text, confidence)`
  - [ ] `unsafe_patterns(pattern_id, section_id, pattern_name, risk_level)`

## Extraction Pipeline

- [ ] Implement parser and guidance extraction.
  - [ ] Tag sections related to aliasing, lifetimes, FFI, and concurrency.
  - [ ] Normalize mechanism IDs from referenced APIs/features.
  - [ ] Mark low-confidence statements requiring corroboration.

## Validation Gates

- [ ] Add content integrity checks.
  - [ ] Fail on missing chapter anchors.
  - [ ] Verify extraction includes known unsafe cornerstone topics.
  - [ ] Detect large chapter-level drift between snapshots.

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

- [ ] Use Rustonomicon as supporting evidence for unsafe tuple design.
  - [ ] Require normative corroboration for `hard` claims.
  - [ ] Use cautionary patterns to expand violation-pattern catalogs.

## Deliverables

- [ ] Produce `rustonomicon.sqlite` and extraction docs.
  - [ ] Add validation script and snapshot diff report.
  - [ ] Add query helpers for unsafe-related row lanes.
