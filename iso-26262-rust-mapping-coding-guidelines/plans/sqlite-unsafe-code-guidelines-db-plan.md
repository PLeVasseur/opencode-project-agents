# SQLite Plan: Unsafe Code Guidelines (`unsafe_code_guidelines.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a local SQLite knowledge base for Unsafe Code Guidelines (UCG) invariants and constraints.
  - [ ] Capture unsafe invariants and UB-related guidance with source anchors.
  - [ ] Classify authority level and stability for each extracted rule fragment.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for invariant/UB condition retrieval.
  - [ ] Define helper views for unsafe tuple evidence joins.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/unsafe_code_guidelines.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/unsafe_code_guidelines/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/unsafe_code_guidelines/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_unsafe_code_guidelines.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_unsafe_code_guidelines.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_unsafe_code_guidelines.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/unsafe_code_guidelines.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_unsafe_code_guidelines.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_unsafe_code_guidelines.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest UCG sources from pinned revision.
  - [ ] Record commit SHA and source hash manifest.
  - [ ] Preserve chapter ordering and anchor metadata.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, commit_sha, source_url, fetched_at, sha256)`
  - [ ] `chapters(chapter_id, title, order_index)`
  - [ ] `sections(section_id, chapter_id, anchor, heading, text)`
  - [ ] `invariants(invariant_id, section_id, invariant_type, text, authority_level, stability)`
  - [ ] `ub_conditions(condition_id, section_id, text, trigger_pattern)`

## Extraction Pipeline

- [ ] Implement section parser and invariant extraction.
  - [ ] Normalize terminology for aliasing, validity, provenance, and layout.
  - [ ] Map extracted invariants to canonical mechanism IDs.
  - [ ] Flag draft or unresolved guidance separately.

## Validation Gates

- [ ] Add safety-focused checks.
  - [ ] Fail on missing anchor IDs for extracted invariants.
  - [ ] Fail if known core topics disappear (aliasing, validity, references, pointers).
  - [ ] Verify stability field is populated for each invariant.

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

- [ ] Use UCG as primary evidence for unsafe-related violation patterns.
  - [ ] Tag mechanisms as `hard` or `review` based on authority and stability.
  - [ ] Require UCG or Rustonomicon linkage for unsafe tuples.

## Deliverables

- [ ] Produce `unsafe_code_guidelines.sqlite` with repeatable loader.
  - [ ] Add extraction script and validation suite.
  - [ ] Add changelog diff report between snapshots.
