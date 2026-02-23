# SQLite Plan: Clippy Lints (`clippy_lints.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a local, versioned SQLite catalog of Clippy lints for tuple-level enforcement evidence.
  - [ ] Capture lint identity, category, default level, applicability, and docs URL.
  - [ ] Preserve version snapshots by Rust toolchain.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for lint lookup and evidence joins.
  - [ ] Define helper views for per-row mechanism enumeration.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/clippy_lints.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/clippy_lints/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/clippy_lints/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_clippy_lints.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_clippy_lints.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_clippy_lints.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/clippy_lints.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_clippy_lints.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_clippy_lints.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest stable Clippy lint index from pinned toolchain docs.
  - [ ] Record source URL, toolchain version, and content hash.
  - [ ] Store fetch manifest for reproducibility.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, toolchain, source_url, fetched_at, sha256)`
  - [ ] `lints(lint_id, group_name, default_level, docs_url, summary, is_restriction)`
  - [ ] `lint_aliases(alias, lint_id)`
  - [ ] `lint_examples(lint_id, example_kind, code_snippet, notes)`
  - [ ] `lint_mechanisms(lint_id, mechanism_id, enforcement_kind)`

## Extraction Pipeline

- [ ] Implement parser and loader.
  - [ ] Parse lints from source index and normalize lint IDs.
  - [ ] Validate uniqueness and referential integrity before insert.
  - [ ] Keep full snapshot history, not overwrite-only updates.

## Validation Gates

- [ ] Add data-quality checks.
  - [ ] Fail on duplicate lint IDs or missing docs URLs.
  - [ ] Fail if lint count drops unexpectedly beyond configured threshold.
  - [ ] Verify selected high-value lints exist (`unwrap_used`, `expect_used`, `await_holding_lock`).

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

- [ ] Bind Clippy lints to row-level mechanism discovery.
  - [ ] Map lint IDs to candidate `rust_mechanism` entries.
  - [ ] Tag as `lint` enforcement for tuple completeness accounting.

## Deliverables

- [ ] Produce `clippy_lints.sqlite` and update metadata manifest.
  - [ ] Add ingestion script and validation script.
  - [ ] Document refresh cadence aligned with toolchain updates.
