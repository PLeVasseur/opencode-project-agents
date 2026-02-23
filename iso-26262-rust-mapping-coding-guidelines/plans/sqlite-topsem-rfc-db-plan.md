# SQLite Plan: T-opsem RFC Work (`topsem_rfcs.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a local SQLite corpus of RFCs and design work relevant to operational semantics.
  - [ ] Track normative status and implementation maturity.
  - [ ] Surface unresolved semantics that should downgrade tuple confidence.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for RFC claim retrieval and joins.
  - [ ] Define helper views for maturity/stability filtering by mechanism.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/topsem_rfcs.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/topsem_rfcs/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/topsem_rfcs/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_topsem_rfcs.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_topsem_rfcs.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_topsem_rfcs.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/topsem_rfcs.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_topsem_rfcs.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_topsem_rfcs.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest RFCs and linked design artifacts tagged for operational semantics.
  - [ ] Record RFC number, title, status, merge date, and linked tracking issues.
  - [ ] Capture labels and team ownership metadata.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, source_kind, fetched_at, sha256)`
  - [ ] `rfcs(rfc_id, number, title, status, merged_at, url, tracking_issue)`
  - [ ] `rfc_sections(section_id, rfc_id, heading, order_index, text)`
  - [ ] `semantic_claims(claim_id, section_id, claim_type, text, maturity)`
  - [ ] `claim_links(claim_id, mechanism_id, related_resource_id)`

## Extraction Pipeline

- [ ] Implement RFC harvesting and claim extraction.
  - [ ] Normalize statuses (`draft`, `accepted`, `implemented`, `superseded`).
  - [ ] Extract safety-relevant semantics claims and caveats.
  - [ ] Link claims to canonical mechanism IDs where possible.

## Validation Gates

- [ ] Add quality checks.
  - [ ] Fail on missing RFC IDs or duplicate section keys.
  - [ ] Warn when claims lack maturity labels.
  - [ ] Fail if extraction loses known high-priority RFC records.

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

- [ ] Use this DB as context evidence, not sole normative authority.
  - [ ] Annotate tuples with risk flags when semantics are unstable.
  - [ ] Require corroboration from normative sources for `hard` enforcement claims.

## Deliverables

- [ ] Produce `topsem_rfcs.sqlite` and extraction provenance report.
  - [ ] Add ingestion script with deterministic pagination and retries.
  - [ ] Add freshness check for newly merged RFCs.
