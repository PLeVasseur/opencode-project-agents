# SQLite Plan: Core Library Docs (`core_docs.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a local SQLite catalog of `core` library API semantics for no-std and foundational mechanisms.
  - [ ] Capture item signatures, stability, safety contracts, panic conditions, and examples.
  - [ ] Normalize links to canonical mechanism IDs.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for API/contract retrieval.
  - [ ] Define helper views for mechanism-family lookups from `core` symbols.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/core_docs.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/core_docs/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/core_docs/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_core_docs.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_core_docs.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_core_docs.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/core_docs.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_core_docs.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_core_docs.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest `library/core` docs from pinned Rust revision.
  - [ ] Record commit SHA, doc generator version, and source hash manifest.
  - [ ] Preserve module/type/function hierarchy.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, commit_sha, fetched_at, sha256)`
  - [ ] `modules(module_id, path, title)`
  - [ ] `items(item_id, module_id, fq_path, item_kind, signature, stability)`
  - [ ] `contracts(contract_id, item_id, contract_kind, text)`
  - [ ] `examples(example_id, item_id, example_kind, code, notes)`

## Extraction Pipeline

- [ ] Implement parser for rustdoc or source markdown artifacts.
  - [ ] Extract safety and panic sections into structured contracts.
  - [ ] Normalize method/trait paths and generic signatures.
  - [ ] Link items to mechanism families (`typing`, `conversion`, `memory`, `sync`).

## Validation Gates

- [ ] Add API integrity checks.
  - [ ] Fail on duplicate fully qualified paths.
  - [ ] Verify critical items exist (`TryFrom`, `Option`, `Result`, atomics).
  - [ ] Detect unexpected API count drops per module.

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

- [ ] Use `core` docs as primary mechanism source for no-std compatible tuples.
  - [ ] Prefer `core` mechanisms when both `core` and `std` alternatives exist.
  - [ ] Require contract evidence link for each selected mechanism.

## Deliverables

- [ ] Produce `core_docs.sqlite` and refresh automation.
  - [ ] Add extraction script with snapshot manifest output.
  - [ ] Add validation report consumable by row-closure pipeline.
