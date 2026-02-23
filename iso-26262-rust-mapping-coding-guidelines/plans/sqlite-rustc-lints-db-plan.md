# SQLite Plan: rustc Lints (`rustc_lints.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a SQLite catalog of built-in compiler lints to complement Clippy evidence.
  - [ ] Capture lint IDs, default levels, lint groups, and edition/toolchain behavior.
  - [ ] Support `compiler`-class enforcement mapping in tuple closure.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for lint and group retrieval.
  - [ ] Define helper views for compiler-enforceable mechanism lookups.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/rustc_lints.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/rustc_lints/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/rustc_lints/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_rustc_lints.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_rustc_lints.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_rustc_lints.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/rustc_lints.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_rustc_lints.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_rustc_lints.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest rustc lint listings from pinned toolchain documentation.
  - [ ] Record source revision, URL, and content hash.
  - [ ] Preserve grouping and default-level metadata.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, toolchain, fetched_at, sha256)`
  - [ ] `lints(lint_id, group_name, default_level, docs_url, summary)`
  - [ ] `lint_levels(lint_id, edition, level, notes)`
  - [ ] `lint_examples(example_id, lint_id, code, outcome)`
  - [ ] `lint_mechanisms(lint_id, mechanism_id, enforcement_kind)`

## Extraction Pipeline

- [ ] Implement lint docs parser and normalizer.
  - [ ] Normalize lint naming and deprecated aliases.
  - [ ] Track edition-specific differences where documented.
  - [ ] Link to mechanism ontology IDs.

## Validation Gates

- [ ] Add compiler-lint data checks.
  - [ ] Fail on duplicate lint IDs.
  - [ ] Verify presence of expected safety-relevant lints.
  - [ ] Detect suspicious count regressions between snapshots.

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

- [ ] Use rustc lints as top-priority enforcement evidence where available.
  - [ ] Mark matching tuples as `hard`/`compiler` when applicable.
  - [ ] Prefer rustc-backed tuples over lint-only tuples when equivalent.

## Deliverables

- [ ] Produce `rustc_lints.sqlite` and validation scripts.
  - [ ] Add snapshot diff report to flag lint drift.
  - [ ] Add mapping export consumed by tuple closure checker.
