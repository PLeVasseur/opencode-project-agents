# SQLite Resource Plan Index (ISO 26262 Rust KB)

## Context Hygiene

- [ ] Enforce context hygiene for all plan execution.
  - [ ] Read only files needed for the active DB rank plus shared SQLite contract/guardrail files.
  - [ ] Do not read unrelated repository code while executing SQLite plan ranks.
  - [ ] If additional files are required, record the reason first.

## Goal

- [ ] Build a consistent local SQLite knowledge base for Rust evidence used by row-first tuple closure.
  - [ ] Keep each resource in its own SQLite DB for provenance and update control.
  - [ ] Use a normalized integration DB to unify cross-resource lookup.
  - [ ] Drive Table 1 tuple completeness from evidence-backed mechanism discovery.

## Filesystem and Tooling Layout (Canonical)

- [ ] Use one canonical storage layout for all SQLite artifacts.
  - [ ] Current active DBs: `.cache/sqlite_kb/current/<db_name>.sqlite`
  - [ ] Immutable snapshots: `.cache/sqlite_kb/snapshots/<db_name>/<snapshot_id>.sqlite`
  - [ ] Query audit logs: `.cache/sqlite_kb/query_logs/<db_name>/`
- [ ] Use one canonical code layout for builders and query wrappers.
  - [ ] DB builders: `scripts/sqlite_build_<db_name>.py`
  - [ ] Read-only query wrappers: `scripts/sqlite_query_<db_name>.py`
  - [ ] DB smoke runners: `scripts/sqlite_smoke_<db_name>.py`
  - [ ] Shared guardrails: `scripts/sqlite_query_guardrails.py`
- [ ] Use one canonical test layout for query and smoke verification.
  - [ ] Wrapper tests: `tests/unit/sqlite_kb/test_query_<db_name>.py`
  - [ ] Smoke tests: `tests/unit/sqlite_kb/test_smoke_<db_name>.py`
  - [ ] Cross-DB Table 1 contract smoke: `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py`
- [ ] Track active snapshots and schema versions in a committed manifest.
  - [ ] Registry file: `data/sqlite_kb_manifest.yaml`
  - [ ] Query contracts: `config/sqlite_query_contracts/<db_name>.yaml`

## Per-Database Implementation Footprint

- [ ] `clippy_lints.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/clippy_lints.sqlite`
  - [ ] Builder: `scripts/sqlite_build_clippy_lints.py`
  - [ ] Wrapper: `scripts/sqlite_query_clippy_lints.py`
  - [ ] Smoke: `scripts/sqlite_smoke_clippy_lints.py`
- [ ] `rust_reference.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/rust_reference.sqlite`
  - [ ] Builder: `scripts/sqlite_build_rust_reference.py`
  - [ ] Wrapper: `scripts/sqlite_query_rust_reference.py`
  - [ ] Smoke: `scripts/sqlite_smoke_rust_reference.py`
- [ ] `topsem_rfcs.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/topsem_rfcs.sqlite`
  - [ ] Builder: `scripts/sqlite_build_topsem_rfcs.py`
  - [ ] Wrapper: `scripts/sqlite_query_topsem_rfcs.py`
  - [ ] Smoke: `scripts/sqlite_smoke_topsem_rfcs.py`
- [ ] `unsafe_code_guidelines.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/unsafe_code_guidelines.sqlite`
  - [ ] Builder: `scripts/sqlite_build_unsafe_code_guidelines.py`
  - [ ] Wrapper: `scripts/sqlite_query_unsafe_code_guidelines.py`
  - [ ] Smoke: `scripts/sqlite_smoke_unsafe_code_guidelines.py`
- [ ] `miri_capabilities.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/miri_capabilities.sqlite`
  - [ ] Builder: `scripts/sqlite_build_miri_capabilities.py`
  - [ ] Wrapper: `scripts/sqlite_query_miri_capabilities.py`
  - [ ] Smoke: `scripts/sqlite_smoke_miri_capabilities.py`
- [ ] `core_docs.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/core_docs.sqlite`
  - [ ] Builder: `scripts/sqlite_build_core_docs.py`
  - [ ] Wrapper: `scripts/sqlite_query_core_docs.py`
  - [ ] Smoke: `scripts/sqlite_smoke_core_docs.py`
- [ ] `std_docs.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/std_docs.sqlite`
  - [ ] Builder: `scripts/sqlite_build_std_docs.py`
  - [ ] Wrapper: `scripts/sqlite_query_std_docs.py`
  - [ ] Smoke: `scripts/sqlite_smoke_std_docs.py`
- [ ] `rustc_lints.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/rustc_lints.sqlite`
  - [ ] Builder: `scripts/sqlite_build_rustc_lints.py`
  - [ ] Wrapper: `scripts/sqlite_query_rustc_lints.py`
  - [ ] Smoke: `scripts/sqlite_smoke_rustc_lints.py`
- [ ] `rustc_diagnostics.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/rustc_diagnostics.sqlite`
  - [ ] Builder: `scripts/sqlite_build_rustc_diagnostics.py`
  - [ ] Wrapper: `scripts/sqlite_query_rustc_diagnostics.py`
  - [ ] Smoke: `scripts/sqlite_smoke_rustc_diagnostics.py`
- [ ] `rustonomicon.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/rustonomicon.sqlite`
  - [ ] Builder: `scripts/sqlite_build_rustonomicon.py`
  - [ ] Wrapper: `scripts/sqlite_query_rustonomicon.py`
  - [ ] Smoke: `scripts/sqlite_smoke_rustonomicon.py`
- [ ] `cargo_book.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/cargo_book.sqlite`
  - [ ] Builder: `scripts/sqlite_build_cargo_book.py`
  - [ ] Wrapper: `scripts/sqlite_query_cargo_book.py`
  - [ ] Smoke: `scripts/sqlite_smoke_cargo_book.py`
- [ ] `rust_release_notes.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/rust_release_notes.sqlite`
  - [ ] Builder: `scripts/sqlite_build_rust_release_notes.py`
  - [ ] Wrapper: `scripts/sqlite_query_rust_release_notes.py`
  - [ ] Smoke: `scripts/sqlite_smoke_rust_release_notes.py`
- [ ] `rust_iso_evidence_hub.sqlite`
  - [ ] DB: `.cache/sqlite_kb/current/rust_iso_evidence_hub.sqlite`
  - [ ] Builder: `scripts/sqlite_build_rust_iso_evidence_hub.py`
  - [ ] Wrapper: `scripts/sqlite_query_rust_iso_evidence_hub.py`
  - [ ] Smoke: `scripts/sqlite_smoke_rust_iso_evidence_hub.py`

## Cross-Cutting Queryability Contract

- [ ] Define queryability requirements before finalizing per-DB schemas.
  - [ ] Plan: `plans/sqlite-queryability-contract-plan.md`
  - [ ] Require every DB plan to complete `Phase 0 - Queryability Discovery`.
  - [ ] Require every DB plan to pass a hard Table 1 row queryability gate.

## Required Resource Databases

- [ ] `clippy_lints.sqlite`
  - [ ] Plan: `plans/sqlite-clippy-lints-db-plan.md`
- [ ] `rust_reference.sqlite`
  - [ ] Plan: `plans/sqlite-rust-reference-db-plan.md`
- [ ] `topsem_rfcs.sqlite`
  - [ ] Plan: `plans/sqlite-topsem-rfc-db-plan.md`
- [ ] `unsafe_code_guidelines.sqlite`
  - [ ] Plan: `plans/sqlite-unsafe-code-guidelines-db-plan.md`
- [ ] `miri_capabilities.sqlite`
  - [ ] Plan: `plans/sqlite-miri-capabilities-db-plan.md`
- [ ] `core_docs.sqlite`
  - [ ] Plan: `plans/sqlite-core-library-docs-db-plan.md`
- [ ] `std_docs.sqlite`
  - [ ] Plan: `plans/sqlite-std-library-docs-db-plan.md`

## Additional Must-Have Resource Databases

- [ ] `rustc_lints.sqlite`
  - [ ] Plan: `plans/sqlite-rustc-lints-db-plan.md`
- [ ] `rustc_diagnostics.sqlite`
  - [ ] Plan: `plans/sqlite-rustc-diagnostics-db-plan.md`
- [ ] `rustonomicon.sqlite`
  - [ ] Plan: `plans/sqlite-rustonomicon-db-plan.md`
- [ ] `cargo_book.sqlite`
  - [ ] Plan: `plans/sqlite-cargo-book-db-plan.md`
- [ ] `rust_release_notes.sqlite`
  - [ ] Plan: `plans/sqlite-rust-release-notes-db-plan.md`

## Integration Database

- [ ] `rust_iso_evidence_hub.sqlite`
  - [ ] Plan: `plans/sqlite-evidence-hub-db-plan.md`

## Execution Order

- [ ] Phase A - Queryability contract discovery
  - [ ] Complete `plans/sqlite-queryability-contract-plan.md` and DB-local queryability phases first.
- [ ] Phase B - Foundation language/library ingestion
  - [ ] Build `rust_reference.sqlite`, `core_docs.sqlite`, `std_docs.sqlite`, `rustc_lints.sqlite`, `clippy_lints.sqlite`, and `rustc_diagnostics.sqlite`.
- [ ] Phase C - Unsafe semantics ingestion
  - [ ] Build `unsafe_code_guidelines.sqlite` and `rustonomicon.sqlite`.
- [ ] Phase D - Process and lifecycle ingestion
  - [ ] Build `cargo_book.sqlite`, `rust_release_notes.sqlite`, and `topsem_rfcs.sqlite`.
- [ ] Phase E - Miri capability baseline (no runtime dependency)
  - [ ] Build `miri_capabilities.sqlite` from documentation/project knowledge first.
- [ ] Phase F - Governance and integration
  - [ ] Materialize `rust_iso_evidence_hub.sqlite` from all source DB snapshots.
- [ ] Optional later phase - dynamic Miri observations
  - [ ] Add curated runtime findings only after capability baseline is stable.

## Exit Criteria

- [ ] All resource DB plans have an implemented extraction pipeline and schema validation.
  - [ ] Each DB has snapshot metadata (`source`, `version`, `fetched_at`, `hash`).
  - [ ] Each DB exposes stable IDs usable in Table 1 tuple provenance.
  - [ ] Each DB passes its queryability contract and latency targets.
  - [ ] Each DB returns `applicable` or `not_applicable` for every Table 1 row (`1a`..`1i`) with evidence.
  - [ ] Each `not_applicable` verdict includes mandatory source-backed rationale and joinable anchors.
  - [ ] Integration DB resolves `row_node_id -> violation_pattern -> rust_mechanism -> evidence` joins.
