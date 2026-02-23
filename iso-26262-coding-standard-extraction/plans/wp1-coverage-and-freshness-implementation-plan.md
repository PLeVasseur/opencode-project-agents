# WP1 Implementation Plan - Coverage and Freshness Closure

## Objective

- Close the highest-risk readiness gap first: target coverage and corpus freshness for Parts 2, 6, 8, and 9.
- Make validation fail whenever target coverage or target freshness is incomplete.
- Prepare a stable base for WP2-WP5 without changing the broader authoring synthesis scope yet.

## Scope

- In scope:
  - target-to-gold coverage completion (35/35 target references),
  - canonical reference mapping for target refs that are not literal corpus refs,
  - validation checks for coverage and freshness,
  - deterministic full-target ingest mode in the refresh runbook.
- Out of scope:
  - OCR backend implementation,
  - query schema validation and latency baselines,
  - authoring synthesis output generation.

## Investigation Findings (Current)

- Target register size: 35 refs across Parts 2, 6, 8, 9.
- Current target-vs-gold exact coverage: 7/35.
- Query probe for current DB:
  - 35/35 target refs return at least one result,
  - 25/35 have exact top-level ref equality,
  - 10/35 require canonical ref normalization.
- Latest per-part ingest coverage from manifests:
  - Part 6 latest run: `run-20260217T035345Z`.
  - Parts 2/8/9 latest run: `run-20260217T025148Z`.
  - This is mixed-run freshness; no single run currently refreshes all target parts together.

## Why WP1 Must Land Before Other Work

- Without coverage closure, a green quality report can still omit target references.
- Without freshness closure, query behavior may differ by part due to mixed-run data age.
- WP2+ improvements (parser/query hardening) are hard to validate if coverage/freshness gates are weak.

## Deliverables

- D1: Expanded gold manifest with explicit target linkage for all 35 targets.
- D2: New validation checks for coverage completeness and freshness completeness.
- D3: Full-target refresh run mode (Parts 2, 6, 8, 9) in runbook script.
- D4: Updated quality report sections summarizing coverage/freshness.
- D5: Updated runbook docs for quick/part6 mode vs full-target mode.

## WP1 Tracking Checklist

## M0 - Baseline lock and mapping confirmation

- [x] Snapshot baseline artifacts (`gold_set_expected_results.json`, latest `ingest_run_*.json`, `extraction_quality_report.json`).
- [x] Record baseline metrics in notes: target coverage `7/35`, query retrievability `35/35`, exact target-ref matches `25/35`.
- [x] Confirm canonical mapping set for the 10 non-exact target refs.

## M1 - Gold contract extension

- [x] Extend target-linked gold contract with `target_id`, `target_ref_raw`, `canonical_ref`, `ref_resolution_mode`.
- [x] Preserve backward compatibility for non-target deep-check gold rows.
- [x] Add/adjust parsing and validation tests for optional-field handling.

## M2 - Gold expansion to full target coverage

- [x] Add one target-linked gold row per target ID (35 total).
- [x] Apply canonical mappings for all non-exact refs (`Clause N -> N`, broad clause -> concrete subclause where needed).
- [x] Keep existing non-target deep hierarchy gold rows intact.
- [x] Verify no missing or duplicate `target_id` entries.

## M3 - Coverage checks in `validate`

- [x] Implement `Q-020` (target register coverage completeness).
- [x] Implement `Q-021` (target-linked reference retrievability and expectation checks).
- [x] Add `target_coverage` block to `extraction_quality_report.json`.
- [x] Ensure validation fails on missing/unmapped target IDs.

## M4 - Freshness checks in manifests and `validate`

- [x] Emit `processed_parts` in ingest run manifests.
- [x] Add per-part latest-run resolution logic in `validate`.
- [x] Implement `Q-022` (target-part freshness completeness for Parts 2/6/8/9).
- [x] Add `freshness` block to `extraction_quality_report.json` with stale-part reporting.

## M5 - Runbook and operator flow updates

- [x] Add full-target mode to `scripts/refresh_quality_artifacts.sh` (`FULL_TARGET_SET`, `TARGET_PARTS`).
- [x] Keep current quick Part 6 mode for parser iteration.
- [x] Wire full-target mode to ingest Parts `2,6,8,9` deterministically.
- [x] Update `scripts/README.md` with quick mode vs full-target mode usage.

## M6 - Verification and sign-off

- [x] Run `cargo check`.
- [x] Run full-target ingest (`--target-part 2 --target-part 6 --target-part 8 --target-part 9`).
- [x] Run `cargo run -- validate --cache-root .cache/iso26262`.
- [x] Confirm `Q-020`, `Q-021`, and `Q-022` are all `pass`.
- [x] Confirm report shows target coverage `35/35` and no stale target parts.
- [x] Update WP1 items in `plans/new-language-query-readiness-closure-plan.md` to completed.
- [x] Append decisions log entry summarizing coverage/freshness closure.

## WP1 Mainline Commit Phasing

Commit policy for this work package:

- Execute on `main` unless branch/PR mode is explicitly requested later.
- Use Conventional Commit format `type(scope): short summary`.
- Keep one concern per commit and run the listed gate before each checkpoint commit.
- Do not commit `.cache/` artifacts (gold/manifests/DB remain local-only evidence).

## C1 - Gold contract support in validation

- [ ] Commit: `refactor(validate): support target-linked gold metadata`
- [ ] Scope:
  - extend gold entry parsing for `target_id`, `target_ref_raw`, `canonical_ref`, `ref_resolution_mode`,
  - preserve backward compatibility for existing deep-check gold rows.
- [ ] Gate:
  - `cargo check`,
  - focused validate tests for optional gold fields.

## C2 - Coverage gates and report block

- [ ] Commit: `feat(validate): add target coverage gates q020 q021`
- [ ] Scope:
  - implement `Q-020` target coverage completeness,
  - implement `Q-021` target-linked retrievability,
  - emit `target_coverage` section in quality report.
- [ ] Gate:
  - `cargo check`,
  - `cargo run -- validate --cache-root .cache/iso26262` shows new checks and expected pass/fail behavior.

## C3 - Gold expansion to 35/35 target-linked rows

- [ ] Commit: `test(gold): expand target-linked references to full register coverage`
- [ ] Scope:
  - add one target-linked gold row per target ID,
  - apply canonical mappings for the 10 non-exact targets,
  - verify one-to-one target ID mapping (no missing/duplicate target IDs).
- [ ] Gate:
  - consistency check script/query confirms 35 covered targets,
  - `cargo run -- validate --cache-root .cache/iso26262` passes `Q-020` and `Q-021`.

## C4 - Freshness metadata and freshness gate

- [ ] Commit: `feat(validate): add target-part freshness gate q022`
- [ ] Scope:
  - emit `processed_parts` in ingest manifests,
  - implement latest-run-by-part freshness resolution,
  - implement `Q-022` and emit `freshness` report section.
- [ ] Gate:
  - `cargo check`,
  - run ingest then validate and confirm `Q-022` evaluates correctly.

## C5 - Full-target refresh mode in runbook script

- [ ] Commit: `feat(scripts): add full-target refresh mode for parts 2 6 8 9`
- [ ] Scope:
  - add `FULL_TARGET_SET` and `TARGET_PARTS` flow in refresh script,
  - keep existing quick Part 6 mode unchanged.
- [ ] Gate:
  - execute script in quick mode and full-target mode,
  - confirm generated ingest command targets expected parts in each mode.

## C6 - Runbook documentation and WP1 sign-off updates

- [ ] Commit: `docs(runbook): document wp1 quick and full-target refresh flows`
- [ ] Scope:
  - update `scripts/README.md`,
  - update WP1 status/checklist markers and closure notes in plans.
- [ ] Gate:
  - docs reflect exact command patterns and env flags,
  - WP1 completion criteria and checklist are internally consistent.

## Recommended checkpoint order

1. C1
2. C2
3. C3
4. C4
5. C5
6. C6

## WP1 gate bundle before final sign-off

- `cargo check`
- `cargo run -- ingest --cache-root .cache/iso26262 --target-part 2 --target-part 6 --target-part 8 --target-part 9`
- `cargo run -- validate --cache-root .cache/iso26262`
- verify quality report shows:
  - `target_coverage.covered_target_total == 35`,
  - `freshness.stale_parts == []`,
  - `Q-020`, `Q-021`, `Q-022` all `pass`.

## Workstream A - Data Contract for Target Coverage

## A1. Extend gold manifest contract

- Add optional fields to each gold entry:
  - `target_id` (required for target-linked entries in WP1),
  - `target_ref_raw` (for traceability to target register text),
  - `canonical_ref` (actual retrievable ref used for evaluation when different from target ref).
- Keep backward compatibility: non-target gold entries (marker/note/paragraph deep checks) can omit `target_id`.

## A2. Add canonical ref strategy enum

- Add `ref_resolution_mode` in target-linked gold entries:
  - `exact_ref` (target ref equals retrievable ref),
  - `section_heading_numeric` (for `Clause N` targets resolved to `N`),
  - `nearest_exact_clause` (for broad clause refs that resolve to concrete subclause ref).

## A3. Code touchpoints

- `src/model.rs` (if shared structs are preferred).
- `src/commands/validate.rs` (`GoldReference` struct extension + evaluation path).

## Workstream B - 35/35 Target Mapping and Gold Expansion

## B1. Populate target-linked gold entries

- Add one target-linked gold entry for each target ID in `target_sections.json`.
- Keep existing deep hierarchy gold entries (list_item/note_item/paragraph) for parser-quality checks.

## B2. Canonical mapping rules

- Rule 1: keep exact target refs when exact ref exists in corpus.
- Rule 2: map `Clause N` targets to section-heading ref `N` and `expected_node_type=section_heading`.
- Rule 3: map broad clause refs to concrete retrievable refs where needed:
  - `6.4.6 -> 6.4.6.1`,
  - `6.4.8 -> 6.4.8.1`.

## B3. Missing target list to close (28)

- Part 6 (13): `5.4.2`, `5.4.3`, `Annex B`, `Annex C`, `9.4.4`, `Table 9`, `10.4.2`, `10.4.5`, `Table 12`, `11.4`, `Table 13`, `Table 14`, `Table 15`.
- Part 8 (9): `Clause 7`, `Clause 8`, `Clause 9`, `Clause 10`, `Clause 11`, `Table 3`, `Table 4`, `Table 5`, `Clause 12`.
- Part 2 (4): `6.4.6`, `6.4.7.2`, `6.4.8`, `6.4.13`.
- Part 9 (2): `Clause 5`, `Clause 7`.

## B4. Canonical mappings for non-exact targets (10)

- Part 8:
  - `Clause 7 -> 7` (`section_heading`)
  - `Clause 8 -> 8` (`section_heading`)
  - `Clause 9 -> 9` (`section_heading`)
  - `Clause 10 -> 10` (`section_heading`)
  - `Clause 11 -> 11` (`section_heading`)
  - `Clause 12 -> 12` (`section_heading`)
- Part 2:
  - `6.4.6 -> 6.4.6.1` (`subclause`)
  - `6.4.8 -> 6.4.8.1` (`subclause`)
- Part 9:
  - `Clause 5 -> 5` (`section_heading`)
  - `Clause 7 -> 7` (`section_heading`)

## Workstream C - Coverage Validation Logic

## C1. Coverage completeness check

- Add a new check (proposed `Q-020`): "Target register coverage completeness".
- Logic:
  - load target register,
  - collect target IDs,
  - collect gold entries with `target_id`,
  - pass only when every target ID is represented exactly once.

## C2. Target-linked retrieval check

- Add a new check (proposed `Q-021`): "Target-linked references retrievable".
- Logic:
  - evaluate all target-linked gold rows,
  - pass only when all are found and satisfy expected node/anchor constraints.

## C3. Quality report additions

- Add `target_coverage` block:
  - `target_total`,
  - `target_linked_gold_total`,
  - `covered_target_total`,
  - `missing_target_ids`.

## Workstream D - Freshness Validation Logic

## D1. Define freshness contract

- A target part is fresh when at least one ingest manifest for that part is produced in the latest full-target refresh cycle.
- WP1 operational definition for pass:
  - one full-target run covers Parts 2, 6, 8, 9,
  - validate executes against DB state produced after that run.

## D2. Manifest-level freshness tracking

- Add ingest manifest field `processed_parts` (derived from `target_parts` or inventory default).
- Add validate report `freshness` block:
  - latest run ID per target part,
  - latest run timestamp per target part,
  - full-target-cycle run ID (if single run covers all target parts),
  - `stale_parts` list.

## D3. Freshness check

- Add new check (proposed `Q-022`): "Target-part freshness completeness".
- Pass when no target part is stale.

## Workstream E - Runbook and Script Updates

## E1. Refresh script mode split

- Keep quick mode for local Part 6 parser iteration.
- Add full-target mode for WP1 closure.

## E2. Proposed script interface changes

- In `scripts/refresh_quality_artifacts.sh`:
  - `FULL_TARGET_SET=1` to ingest `2,6,8,9` in one run,
  - `TARGET_PARTS="2 6 8 9"` override for explicit control,
  - keep current `PART` behavior when full mode is not selected.

## E3. Docs updates

- Update `scripts/README.md` with two recommended flows:
  - quick parser iteration (Part 6 only),
  - full target freshness refresh (Parts 2/6/8/9).

## Workstream F - Operational Sequence (Step-by-Step)

## F1. Preparation

- Step F1.1: Create a backup copy of `gold_set_expected_results.json`.
- Step F1.2: Generate target probe matrix from current DB for canonical mapping confirmation.
- Step F1.3: Decide canonical refs for all non-exact targets (use mappings listed in this plan).

## F2. Data and validation changes

- Step F2.1: Extend validate data structs and parsing.
- Step F2.2: Add `target_id` linkage and expanded gold rows.
- Step F2.3: Implement checks `Q-020`, `Q-021`, `Q-022` and report sections.

## F3. Freshness/runbook changes

- Step F3.1: Update ingest manifest to emit `processed_parts`.
- Step F3.2: Update refresh script for full-target mode.
- Step F3.3: Update script docs.

## F4. Verification commands

- Step F4.1: `cargo check`.
- Step F4.2: full-target ingest run:
  - `cargo run -- ingest --cache-root .cache/iso26262 --target-part 2 --target-part 6 --target-part 8 --target-part 9`.
- Step F4.3: `cargo run -- validate --cache-root .cache/iso26262`.
- Step F4.4: verify quality report:
  - target coverage `35/35`,
  - freshness check pass for all target parts.

## F5. Completion updates

- Step F5.1: Update `new-language-query-readiness-closure-plan.md` WP1 status from open to complete.
- Step F5.2: Append decision-log entry describing coverage/freshness closure and any canonical ref normalization decisions.

## Acceptance Criteria (WP1 Done)

- Coverage:
  - all 35 target IDs are represented by target-linked gold rows,
  - `Q-020` and `Q-021` pass.
- Freshness:
  - Parts 2/6/8/9 are fresh in the validated cycle,
  - `Q-022` passes.
- Reporting:
  - quality report includes target coverage and freshness sections.
- Runbook:
  - full-target refresh flow is documented and executable.

## Risks and Mitigations

- Risk: canonical mapping drifts if parser heading behavior changes.
  - Mitigation: keep mapping explicit in gold entries via `target_id + canonical_ref + ref_resolution_mode`.
- Risk: full-target ingest is slower and discourages frequent runs.
  - Mitigation: preserve quick Part 6 mode for iteration; enforce full-target mode at milestone/gate checkpoints.
- Risk: duplicate gold rows per target create false confidence.
  - Mitigation: `Q-020` enforces one-to-one target ID linkage for target-linked set.

## Implementation Touchpoints Summary

- Primary implementation repo files (planned):
  - `src/commands/validate.rs`
  - `src/commands/ingest.rs`
  - `src/cli.rs` (only if new args are needed)
  - `src/model.rs` (if manifest structs are centralized)
  - `scripts/refresh_quality_artifacts.sh`
  - `scripts/README.md`
- Primary manifest/artifact files:
  - `.cache/iso26262/manifests/gold_set_expected_results.json`
  - `.cache/iso26262/manifests/extraction_quality_report.json`
  - `.cache/iso26262/manifests/ingest_run_<timestamp>.json`
