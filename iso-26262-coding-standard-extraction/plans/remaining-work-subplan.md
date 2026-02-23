# Remaining Work Sub-Plan

Small handoff plan to restart quickly and finish the remaining scope.

## Baseline Snapshot

- Part 6 quality gate is green (`validate` passing with full check set).
- Key Part 6 gold references are passing, including `Table 1`, `Table 6`, `Table 7`, `Table 10`, `8.4.5`, `9.4.2`, and `Annex D`.
- Remaining gold gaps are the non-Part-6 targets still marked `skip`.
- Traceability is scaffolded but not yet mapped end-to-end.

## Work Package 1 - Close Remaining Part 6 Hierarchy Gaps

Status: in progress

Scope:

- [x] Add missing `note` and `note_item` hierarchy coverage (parser + node lineage).
- [x] Complete anchor contract gap for parent reference context (`parent_ref`-equivalent output).
- [x] Add explicit structural invariant checks (parent validity, dangling pointers, table/list lineage).
- [x] Close remaining Part 6 parser quality items:
  - [x] paragraph merge/split edge-case coverage,
  - [x] table row/cell alignment checks for ASIL-style rows (`Table 3`, `Table 6`, `Table 10`).

Exit criteria:

- [x] Remaining open items in `plans/hierarchy-parsing-quality-checklist.md` that are Part 6-specific are checked.
- [x] `cargo test`, `scripts/smoke_part6.sh`, and `cargo run -- validate --cache-root .cache/iso26262` all pass.

## Work Package 2 - Complete P2/P3 Gold Targets (Current `skip` Items)

Status: done

Scope:

- [x] Ingest and validate the required non-Part-6 targets (Parts 8, 2, and 9 references already listed in gold set).
- [x] Replace `TBD-after-first-ingest` page patterns with concrete expectations.
- [x] Confirm expected anchor/hierarchy metadata for those entries and move them from `skip` to `pass`.

Exit criteria:

- [x] Gold set has no remaining `skip` entries for planned P2/P3 references.
- [x] `validate` stays green after expanding corpus scope.

## Work Package 3 - Finish Traceability Mapping

Status: done

Scope:

- [x] Populate `traceability_matrix.csv` with real mappings (`rule_id`, `verification_method`, `evidence_artifact`, `owner`, `status`).
- [x] Map P0/P1 first, then P2/P3 governance/safety-case links.
- [x] Update `target_sections.json` statuses from `planned` to `indexed`/`validated`/`mapped` as evidence is completed.

Exit criteria:

- [x] Milestone D can be checked in `plans/iso-26262-coding-standard-targeting-plan.md`.
- [x] Traceability rows are no longer placeholders for completed references.

## Work Package 4 - Runbook and Versioning Closure

Status: done

Scope:

- [x] Close remaining deterministic runbook items (notably `R00`, `R01`, `R04`, `R07`).
- [x] Add parser/query engine version pinning and compatibility checks to resume logic.
- [x] Finalize controlled rebuild/restart behavior documentation and manifest handling.

Exit criteria:

- [x] Phase 8 and Phase 9 checklist items are either completed or explicitly deferred with rationale.

## Suggested Restart Sequence (Next Session)

1. `printenv OPENCODE_CONFIG_DIR`
2. `cargo check`
3. `scripts/refresh_quality_artifacts.sh`
4. Execute Work Package 4 follow-ups for commit governance and final release notes.
