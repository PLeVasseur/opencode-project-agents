# Sequential SQLite DB Execution Checklist

## Goal

- [ ] Build all SQLite knowledge-base databases one-by-one, in ranked order, with hard queryability gates.
  - [ ] Do not start DB rank `N+1` until DB rank `N` passes its full Definition-of-Done gate.
  - [ ] Keep all work on a dedicated implementation branch until the full sequence is complete.

## Context Hygiene Rule

- [ ] Prevent context pollution during sequential execution.
  - [ ] For each DB rank, read only files required for that DB plus shared SQLite contract/guardrail files.
  - [ ] Do not read unrelated repository code while a rank is in progress.
  - [ ] If additional files are required, record the reason first in run notes.

## Branching Setup

- [ ] Fork from the current branch into a new descriptive implementation branch.
  - [ ] Create branch: `feat/table1-sqlite-kb-sequential-build`
  - [ ] Record base commit SHA in the run notes/checklist.
  - [ ] Keep one DB-focused commit set per rank (no mixed multi-DB commits).
- [ ] Reserve autonomous-loop work for a later branch.
  - [ ] After implementation sequence completion, branch from implementation branch to: `feat/table1-sqlite-kb-autoloop`

## Global Prerequisites (Run Once Before Rank 1)

- [ ] Finalize cross-DB query contract and wrapper guardrails first.
  - [ ] `plans/sqlite-queryability-contract-plan.md` accepted.
  - [ ] Wrapper guardrails defined (`read-only`, `query-only`, contract query IDs only).
  - [ ] Canonical filesystem layout accepted (`.cache/sqlite_kb/current`, `snapshots`, `query_logs`).
- [ ] Create shared registry + contract scaffolding.
  - [ ] `data/sqlite_kb_manifest.yaml`
  - [ ] `config/sqlite_query_contracts/`
  - [ ] `tests/unit/sqlite_kb/test_table1_row_queryability_contract.py` scaffold

## Per-Database Definition of Done (Applies to Every Rank)

- [ ] Implement canonical assets for the target DB.
  - [ ] Builder script exists: `scripts/sqlite_build_<db_name>.py`
  - [ ] Read-only wrapper exists: `scripts/sqlite_query_<db_name>.py`
  - [ ] Smoke runner exists: `scripts/sqlite_smoke_<db_name>.py`
  - [ ] Query contract exists: `config/sqlite_query_contracts/<db_name>.yaml`
  - [ ] Wrapper test exists: `tests/unit/sqlite_kb/test_query_<db_name>.py`
  - [ ] Smoke test exists: `tests/unit/sqlite_kb/test_smoke_<db_name>.py`
- [ ] Pass Table 1 row queryability gate.
  - [ ] Deterministic query results for all rows `1a..1i` keyed by canonical `row_node_id`.
  - [ ] Verdict per row is only `applicable` or `not_applicable` (no `unknown`).
  - [ ] Every `not_applicable` has mandatory source-backed rationale + joinable anchors.
  - [ ] Results are joinable with `rust_iso_evidence_hub` contract fields.
- [ ] Pass operational guardrails and quality checks.
  - [ ] Wrapper blocks write/DDL/ATTACH/extension operations.
  - [ ] Latency/query-size limits are enforced.
  - [ ] Query audit logs emitted to `.cache/sqlite_kb/query_logs/<db_name>/`.
- [ ] Publish snapshot and commit before moving to next rank.
  - [ ] Snapshot promoted to `.cache/sqlite_kb/current/<db_name>.sqlite`.
  - [ ] Manifest updated in `data/sqlite_kb_manifest.yaml`.
  - [ ] Commit created with Conventional Commit message.

## Ranked Execution Order (Sequential)

- [ ] Rank 1: `rust_reference.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 2: `core_docs.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 3: `std_docs.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 4: `rustc_lints.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 5: `clippy_lints.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 6: `rustc_diagnostics.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 7: `unsafe_code_guidelines.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 8: `rustonomicon.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 9: `cargo_book.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 10: `rust_release_notes.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 11: `topsem_rfcs.sqlite`
  - [ ] Complete full Per-Database DoD.
- [ ] Rank 12: `miri_capabilities.sqlite`
  - [ ] Complete full Per-Database DoD.
  - [ ] Keep capability-first scope (runtime findings remain optional later phase).
- [ ] Rank 13: `rust_iso_evidence_hub.sqlite`
  - [ ] Complete full Per-Database DoD.
  - [ ] Verify cross-DB joins for `row_node_id -> violation_pattern -> rust_mechanism -> evidence`.

## Stop Conditions and Rework Policy

- [ ] Stop progression immediately on any gate failure.
  - [ ] Rework schema/index/query style until gate is green.
  - [ ] Do not bypass `not_applicable` rationale requirements.
  - [ ] Do not defer query-wrapper guardrails.

## Completion Handoff

- [ ] Implementation branch ready for controller branch fork.
  - [ ] All 13 ranked DBs complete with passing DoD.
  - [ ] Cross-DB contract smoke passes.
  - [ ] Fork next branch: `feat/table1-sqlite-kb-autoloop`
