# SQLite Plan: Cargo Book (`cargo_book.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a SQLite corpus of Cargo configuration and workflow semantics relevant to enforcement.
  - [ ] Capture profiles, lint config patterns, target settings, and policy-relevant knobs.
  - [ ] Support enforcement-mode evidence for AUTO/HYBRID tuple decisions.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for config key/policy lookups.
  - [ ] Define helper views for enforcement configuration retrieval by mechanism.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/cargo_book.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/cargo_book/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/cargo_book/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_cargo_book.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_cargo_book.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_cargo_book.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/cargo_book.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_cargo_book.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_cargo_book.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest Cargo Book docs from pinned revision/toolchain.
  - [ ] Record commit/toolchain version and content hashes.
  - [ ] Preserve chapter and anchor hierarchy.

## Schema

- [ ] Define normalized tables.
  - [ ] `snapshots(snapshot_id, version_tag, fetched_at, sha256)`
  - [ ] `chapters(chapter_id, title, order_index)`
  - [ ] `sections(section_id, chapter_id, anchor, heading, text)`
  - [ ] `config_keys(key_id, key_path, value_type, default_value, docs_anchor)`
  - [ ] `policy_impacts(impact_id, key_id, impact_kind, rationale)`

## Extraction Pipeline

- [ ] Implement section + key extraction.
  - [ ] Parse code blocks and TOML key definitions.
  - [ ] Normalize key paths and map to enforcement concerns.
  - [ ] Link key-level guidance to mechanism IDs where relevant.

## Validation Gates

- [ ] Add configuration integrity checks.
  - [ ] Fail on duplicate key paths.
  - [ ] Verify expected keys are present (`profile`, `lints`, target-related settings).
  - [ ] Flag major key taxonomy changes between snapshots.

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

- [ ] Use Cargo evidence for operational enforcement mechanics.
  - [ ] Map tuple enforcement recommendations to concrete Cargo configuration anchors.
  - [ ] Add provenance linking for build/lint policy tuples.

## Deliverables

- [ ] Produce `cargo_book.sqlite` and parser scripts.
  - [ ] Add validation report and key-drift summary artifact.
  - [ ] Add query helpers for enforcement policy generation.
