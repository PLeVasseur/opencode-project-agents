# SQLite Plan: Rust Release Notes (`rust_release_notes.sqlite`)

## Objective

## Context Hygiene

- [ ] Prevent context pollution while executing this plan.
  - [ ] Read only files needed for this DB plus shared SQLite query-contract/guardrail files.
  - [ ] Do not read unrelated repository code while implementing this DB.
  - [ ] If additional files are required, record the reason first.

- [ ] Build a SQLite database of Rust release-note changes affecting mechanism availability and behavior.
  - [ ] Track language, std/core, rustc, and Clippy changes with version anchors.
  - [ ] Support drift detection for tuple validity over time.

## Phase 0 - Queryability Discovery

- [ ] Discover the query contract before schema freeze.
  - [ ] Define high-priority questions this DB must answer for (`row_node_id`, `violation_pattern`, `rust_mechanism`).
  - [ ] Define canonical IDs and join keys exported to `rust_iso_evidence_hub.sqlite`.
- [ ] Design query strategy for controller workloads.
  - [ ] Define required indexes and FTS strategy for change impact retrieval.
  - [ ] Define helper views for mechanism drift and deprecation lookup.
- [ ] Validate queryability with benchmarks.
  - [ ] Add deterministic contract queries and expected result fixtures.
  - [ ] Set latency targets and fail completion if query contract is unmet.

## Implementation Footprint (Paths and Interfaces)

- [ ] Pin canonical filesystem paths for this DB.
  - [ ] Active DB: `.cache/sqlite_kb/current/rust_release_notes.sqlite`
  - [ ] Snapshot DBs: `.cache/sqlite_kb/snapshots/rust_release_notes/<snapshot_id>.sqlite`
  - [ ] Query logs: `.cache/sqlite_kb/query_logs/rust_release_notes/`
- [ ] Pin builder and query scripts.
  - [ ] Builder: `scripts/sqlite_build_rust_release_notes.py`
  - [ ] Read-only wrapper: `scripts/sqlite_query_rust_release_notes.py`
  - [ ] Smoke runner: `scripts/sqlite_smoke_rust_release_notes.py`
- [ ] Pin query contract and tests.
  - [ ] Query contract: `config/sqlite_query_contracts/rust_release_notes.yaml`
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_rust_release_notes.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_rust_release_notes.py`
  - [ ] Include in cross-DB contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`

## Source Acquisition

- [ ] Ingest release notes from pinned official sources.
  - [ ] Record release version, date, and source hash.
  - [ ] Preserve section hierarchy and linked issues/PRs.

## Schema

- [ ] Define normalized tables.
  - [ ] `releases(release_id, version, released_at, source_url, sha256)`
  - [ ] `notes(note_id, release_id, component, heading, text)`
  - [ ] `changes(change_id, note_id, change_kind, impact_level, stability)`
  - [ ] `change_links(change_id, mechanism_id, lint_id, diagnostic_code)`
  - [ ] `deprecations(item_id, item_kind, replacement, release_id)`

## Extraction Pipeline

- [ ] Implement note parsing and impact tagging.
  - [ ] Extract component tags (`language`, `std`, `rustc`, `clippy`, `cargo`).
  - [ ] Identify changes likely to affect safety tuple assumptions.
  - [ ] Link changes to canonical mechanism IDs and lint/diagnostic IDs.

## Validation Gates

- [ ] Add release continuity checks.
  - [ ] Fail when release sequence has missing versions in configured window.
  - [ ] Fail on duplicate version rows.
  - [ ] Verify high-impact change entries include component and impact tags.

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

- [ ] Use release data to guard tuple staleness.
  - [ ] Flag tuples impacted by changed/deprecated mechanisms.
  - [ ] Trigger row-lane revalidation when high-impact changes are detected.

## Deliverables

- [ ] Produce `rust_release_notes.sqlite` and drift-check tooling.
  - [ ] Add extraction script and impact classifier.
  - [ ] Add per-release delta report for controller consumption.
