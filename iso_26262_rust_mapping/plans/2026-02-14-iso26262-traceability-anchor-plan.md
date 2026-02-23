# ISO 26262 Durable Traceability Plan (Source-Embedded Correlation, Detailed v4)

Date: 2026-02-14
Status: Draft execution plan (rewrite)
Priority: Blocker prerequisite for critique remediation

## 0) Executive decisions (locked)
- [ ] Use source-embedded correlation as the canonical model.
  - [ ] Canonical source->ISO links live in source files only (`src/iso26262_rust_mapping.md` and `src/tables/table-*.yaml`).
  - [ ] Do not maintain a separate manually-authored tracked mapping file set.
  - [ ] Allow generated reverse indexes under `.cache/` and run `reports/` for lookup speed and validation.
- [ ] Require statement-level source anchoring with no gaps at closeout.
  - [ ] Every statement in markdown and YAML receives a stable `source_id`.
  - [ ] Every statement has explicit trace status (`mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`).
  - [ ] The closeout gate fails if any required statement lacks a `source_id`.
- [ ] Keep ISO anchor hierarchy in tracked JSONC.
  - [ ] Progressive disclosure hierarchy is tracked in `traceability/iso26262/**`.
  - [ ] One JSONC file per semantic ISO unit (clause subsection, table object, annex unit, figure object).
  - [ ] Do not create one JSONC file per table cell.
- [ ] Enforce durable source identities with a generic ID generator.
  - [ ] Use generic unique stable `source_id` values for all source node kinds.
  - [ ] IDs are stable across reordering and movement because they are embedded in source nodes.
  - [ ] Uniqueness and format are schema-validated and linted.

## 1) Mission and end-state
- [ ] Deliver exhaustive traceability over relevant ISO PDFs and current repository argument surface.
  - [ ] Every in-scope ISO leaf anchor is represented in JSONC.
  - [ ] Every ISO leaf anchor has a status (`mapped`, `unmapped_with_rationale`, `out_of_scope_with_rationale`).
  - [ ] Every statement-level source node has a `source_id` and trace status.
  - [ ] Every mapped statement-level source node has one or more valid ISO anchor references.
- [ ] Provide practical day-to-day usability.
  - [ ] PDF-first lookup: find source nodes from a PDF location hint.
  - [ ] Source-first lookup: find ISO anchors and PDF location chain from a source node.
  - [ ] Rapid scaffolding for new ISO unit files and source IDs.
- [ ] Surface traceability in generated DOCX with footnote-like detail.
  - [ ] Include exact source placement (`Section X, List Y, Bullet Z` or `Table X, Row Y, Column Z`).
  - [ ] Include exact ISO anchor placement (part + unit + leaf kind + ordinal).
  - [ ] Avoid any copyrighted ISO text leakage.

## 2) Constraints (non-negotiable)
- [ ] No ISO copyrighted text in tracked files.
  - [ ] Do not store verbatim clause/table/list/figure/footnote text in repo.
  - [ ] Do not store extracted PDF raw text snippets in tracked files.
  - [ ] Do not store license/watermark lines in tracked files.
- [ ] Keep extraction outputs untracked.
  - [ ] `.cache/iso26262/pdf/` for source PDFs.
  - [ ] `.cache/iso26262/extracted/` for extraction artifacts.
  - [ ] `.cache/iso26262/fingerprints/` for normalization signatures.
  - [ ] `.cache/iso26262/indexes/` for generated reverse lookup indexes.
- [ ] Maintain reviewable, deterministic tracked artifacts.
  - [ ] JSONC with stable ordering and schema validation.
  - [ ] Explicit parent-child links in hierarchy files.
  - [ ] Strict anti-leak checks in CI-style validation.

## 3) Baseline findings from ISO structure investigation (validated)
- [ ] Part 6 (`ISO 26262-6:2018`) structure baseline.
  - [ ] Clauses include 1..11 with software-focused core in 5..11.
  - [ ] Main-body tables include `Table 1`..`Table 15`.
  - [ ] Annexes: `A` (informative), `B` (informative), `C` (normative), `D` (informative), `E` (informative).
  - [ ] Additional table objects discovered: `Table A.1`, `Table C.1`, `Table E.1`, `Table E.2`.
  - [ ] Figure objects discovered: `Figure 1`, `Figure 2`, `Figure C.1`, `Figure C.2`, `Figure C.3`, `Figure E.1`..`Figure E.4`.
- [ ] Part 8 (`ISO 26262-8:2018`) structure baseline.
  - [ ] Clauses include 1..16 (supporting processes).
  - [ ] Main-body tables include `Table 1`..`Table 8`.
  - [ ] Clause 11 includes TCL/TI/TD core (`Table 3`, `Table 4`, `Table 5`).
  - [ ] Annexes: `A` and `B` (informative).
  - [ ] Additional table objects discovered: `Table A.1`, `Table B.1`, `Table B.2`, `Table B.3`.
  - [ ] Figure objects discovered: `Figure 1`..`Figure 6`.
- [ ] Part 9 (`ISO 26262-9:2018`) structure baseline.
  - [ ] Clauses include 1..8 with core use in 5/6/7.
  - [ ] Annexes: `A`, `B`, `C` (informative).
  - [ ] Table objects discovered: `Table A.1`, `Table C.1`.
  - [ ] Figure objects discovered: `Figure 1`, `Figure 2`, `Figure 3`, `Figure B.1`, `Figure C.1`.
- [ ] Repository argument surface baseline.
  - [ ] Narrative source: `src/iso26262_rust_mapping.md`.
  - [ ] Table source: `src/tables/table-01.yaml` .. `src/tables/table-26.yaml`.
  - [ ] Current docgen parser is deterministic but minimal and does not yet parse trace directives or footnotes.

## 4) Correlation model (source-embedded, no manual mapping files)
- [ ] Define canonical correlation ownership.
  - [ ] Source files own `source_id` and ISO anchor references.
  - [ ] ISO JSONC files own anchor definitions and hierarchical structure.
  - [ ] Reverse indexes are generated (not manually authored) from source + ISO files.
- [ ] Disallow manual tracked mapping files as source-of-truth.
  - [ ] No `traceability/iso26262/mappings/*.jsonc` author-maintained files.
  - [ ] If any mapping-like artifact is needed, it is generated in `.cache/iso26262/indexes/` or run `reports/`.
- [ ] Preserve bidirectional capabilities without separate mapping files.
  - [ ] Source-first: source node directly lists anchor IDs.
  - [ ] PDF-first: anchor lookup + generated reverse index resolves source IDs.

## 5) Source identity model (generic, stable, durable)
- [ ] Create generic `source_id` format and generator.
  - [ ] Format prefix: `SRCN-` + UUIDv7/ULID payload.
  - [ ] IDs are globally unique across markdown and YAML sources.
  - [ ] IDs are immutable once assigned.
- [ ] Apply `source_id` to every statement-level source node kind.
  - [ ] Markdown heading statement nodes.
  - [ ] Markdown paragraph sentence nodes.
  - [ ] Markdown list-item statement nodes (including nested items).
  - [ ] YAML row-level statement nodes for `table-01`..`table-26`.
  - [ ] YAML cell-level statement nodes where cells contain one or more statements.
  - [ ] YAML note/footnote-like statement nodes where present.
- [ ] Enforce identity constraints.
  - [ ] Fail on duplicate IDs.
  - [ ] Fail on malformed IDs.
  - [ ] Fail on missing IDs for any statement-level required node classes.
  - [ ] Fail when statement segmentation changes but IDs are not reconciled.

## 6) Source embedding contract (how metadata is baked into source)
- [ ] Markdown embedding strategy.
  - [ ] Add explicit trace directive syntax consumed by parser tooling.
  - [ ] Directive includes `source_id`, `trace_status`, `anchor_ids`, `relation`, optional `note_code`.
  - [ ] Directive can apply to heading, paragraph-sentence node, list item, or table placeholder block.
  - [ ] Parser strips trace directives from rendered body text.
  - [ ] Add deterministic sentence/list segmentation rules so statement IDs remain stable across edits.
- [ ] YAML embedding strategy.
  - [ ] Add `_trace` object at row level with required `source_id`, `trace_status`, and optional row-level `anchor_ids`.
  - [ ] Add `cell_trace` map keyed by column key for cell-level statement IDs and anchor references.
  - [ ] Keep table semantic content unchanged outside `_trace` metadata.
- [ ] Statement-level persistence rules.
  - [ ] Preserve existing `source_id` values during reorder or move operations.
  - [ ] Mint new `source_id` values only for newly introduced statements.
  - [ ] Mark removed statements as retired in generated reverse index metadata.
- [ ] Relation code vocabulary.
  - [ ] `direct` for explicit normative mapping.
  - [ ] `derived` for derived engineering interpretation.
  - [ ] `supporting` for supporting process/quality/assurance context.
  - [ ] `contextual` for explanatory non-primary references.

## 7) Progressive disclosure hierarchy (tracked JSONC, exhaustive by relevant PDFs)
- [ ] Layer 0: PDF-set root index.
  - [ ] `traceability/iso26262/index/source-pdfset.jsonc` with editions, parts, checksums, page counts.
  - [ ] `traceability/iso26262/index/relevant-pdf-policy.jsonc` defining why P06/P08/P09 are in-scope.
- [ ] Layer 1: Part index files.
  - [ ] `traceability/iso26262/parts/2018-ed2/p06/index.jsonc`.
  - [ ] `traceability/iso26262/parts/2018-ed2/p08/index.jsonc`.
  - [ ] `traceability/iso26262/parts/2018-ed2/p09/index.jsonc`.
- [ ] Layer 2: Structural index files per part.
  - [ ] `clauses.index.jsonc` with clause/subclause unit links.
  - [ ] `tables.index.jsonc` with table object unit links.
  - [ ] `figures.index.jsonc` with figure object unit links.
  - [ ] `annexes.index.jsonc` with annex unit links.
- [ ] Layer 3: Unit files.
  - [ ] Clause units (e.g., `clauses/c06.4.jsonc`, `clauses/c11.4.6.jsonc`).
  - [ ] Table units (e.g., `tables/t04.jsonc`, `tables/tA01.jsonc`, `tables/tB03.jsonc`).
  - [ ] Figure units (e.g., `figures/f02.jsonc`, `figures/fB01.jsonc`).
  - [ ] Annex units (e.g., `annexes/a-c.jsonc`).
- [ ] Layer 4: Leaf anchor records inside unit files.
  - [ ] Paragraph leaves.
  - [ ] List-item leaves.
  - [ ] Table row/cell/note/footnote leaves.
  - [ ] Figure-caption and figure-note leaves where applicable.
- [ ] Hierarchy integrity rules.
  - [ ] All child files referenced by parent indexes.
  - [ ] All child files contain parent pointer metadata.
  - [ ] No orphaned unit files.

## 8) ISO-side anchor contract (tracked JSONC)
- [ ] Anchor ID grammar.
  - [ ] Format: `ISO26262:<edition>:<part>:<unit>:<kind>:<ordinal>`.
  - [ ] Clause list-item example: `ISO26262:2018-ed2:P09:C05.4:L:003.002`.
  - [ ] Table cell example: `ISO26262:2018-ed2:P08:T04:TC:R001.CASIL_D`.
- [ ] Anchor `kind` taxonomy.
  - [ ] `SEC` section node.
  - [ ] `P` paragraph.
  - [ ] `L` list item.
  - [ ] `T` table object.
  - [ ] `TR` table row.
  - [ ] `TC` table cell.
  - [ ] `TN` table note.
  - [ ] `F` footnote.
  - [ ] `FG` figure object/caption node.
  - [ ] `XR` cross-reference pointer.
- [ ] Evolution metadata.
  - [ ] `lineage_id` for cross-edition concept continuity.
  - [ ] `status` in `{active, deprecated, migrated, unresolved}`.
  - [ ] `supersedes[]` and `superseded_by[]`.

## 9) Source-side locator grammar (human-readable + machine-stable)
- [ ] Markdown locators.
  - [ ] `SRC:md:sec:<section-id>`.
  - [ ] `SRC:md:sec:<section-id>:para:<n>`.
  - [ ] `SRC:md:sec:<section-id>:list:<list-id>:item:<n>`.
  - [ ] `SRC:md:sec:<section-id>:list:<list-id>:item:<n>.<m>`.
- [ ] YAML locators.
  - [ ] `SRC:yaml:table-XX`.
  - [ ] `SRC:yaml:table-XX:row:<source_id>`.
  - [ ] `SRC:yaml:table-XX:row:<source_id>:col:<col-key>`.
- [ ] Locator display rules for rendered output.
  - [ ] Convert source locator to human display phrase.
  - [ ] Preserve exact table/row/column or section/list/item identity.

## 10) Relevant-part decomposition manifests (thorough and explicit)
- [ ] Part 6 decomposition manifest (`p06`).
  - [ ] Include clauses `1`..`11` as units with status.
  - [ ] Include all discovered table objects: `T01`..`T15`, `TA01`, `TC01`, `TE01`, `TE02`.
  - [ ] Include discovered figure objects: `F01`, `F02`, `FC01`, `FC02`, `FC03`, `FE01`, `FE02`, `FE03`, `FE04`.
  - [ ] Include annex units `A`, `B`, `C`, `D`, `E` with normative flag on `C`.
  - [ ] Mark repository-required focus units under clauses `5`..`11`.
- [ ] Part 8 decomposition manifest (`p08`).
  - [ ] Include clauses `1`..`16` as units with status.
  - [ ] Include table objects: `T01`..`T08`, `TA01`, `TB01`, `TB02`, `TB03`.
  - [ ] Include figure objects: `F01`..`F06`.
  - [ ] Include annex units `A`, `B`.
  - [ ] Mark repository-required focus units: Clause `11` and supporting Clause `10`/`9` where used.
- [ ] Part 9 decomposition manifest (`p09`).
  - [ ] Include clauses `1`..`8` as units with status.
  - [ ] Include table objects: `TA01`, `TC01`.
  - [ ] Include figure objects: `F01`, `F02`, `F03`, `FB01`, `FC01`.
  - [ ] Include annex units `A`, `B`, `C`.
  - [ ] Mark repository-required focus units: Clause `5`, `6`, `7`.
- [ ] Inclusion/exclusion policy.
  - [ ] Every unit is listed even when out-of-scope for current argument.
  - [ ] Out-of-scope units must have machine-readable rationale code.

## 11) JSONC schemas (tracked)
- [ ] Add ISO hierarchy schemas.
  - [ ] `traceability/iso26262/schema/index.schema.json`.
  - [ ] `traceability/iso26262/schema/unit.schema.json`.
  - [ ] `traceability/iso26262/schema/anchor-record.schema.json`.
  - [ ] `traceability/iso26262/schema/coverage-summary.schema.json`.
- [ ] Add source metadata schemas.
  - [ ] `traceability/iso26262/schema/source-trace-md.schema.json`.
  - [ ] `traceability/iso26262/schema/source-trace-yaml-row.schema.json`.
- [ ] Schema anti-leak rules.
  - [ ] Disallow text fields named `raw_text`, `quote`, `excerpt`, `sentence`, `cell_text`, `paragraph_text`.
  - [ ] Bound freeform comment lengths.
  - [ ] Validate against known watermark/email/order/license patterns.

## 12) Repository layout (tracked) and cache layout (untracked)
- [ ] Tracked layout.
  - [ ] `traceability/iso26262/README.md`.
  - [ ] `traceability/iso26262/index/`.
  - [ ] `traceability/iso26262/parts/`.
  - [ ] `traceability/iso26262/schema/`.
  - [ ] `tools/traceability/`.
  - [ ] No tracked `mappings/` folder as manual source-of-truth.
- [ ] Untracked layout.
  - [ ] `.cache/iso26262/pdf/`.
  - [ ] `.cache/iso26262/extracted/`.
  - [ ] `.cache/iso26262/fingerprints/`.
  - [ ] `.cache/iso26262/indexes/`.
  - [ ] `.cache/iso26262/manifests/`.
- [ ] Ignore policy checks.
  - [ ] Confirm `.cache/` remains ignored in repo `.gitignore`.
  - [ ] Add policy comment in `README.md` and traceability docs.

## 13) Tooling plan (implementation set)
- [ ] ISO extraction and anchor generation tools.
  - [ ] `tools/traceability/extract_pdf_structure.py`.
  - [ ] `tools/traceability/build_anchor_fingerprints.py`.
  - [ ] `tools/traceability/generate_iso_hierarchy.py`.
  - [ ] `tools/traceability/generate_anchor_jsonc.py`.
- [ ] Source metadata tools (source-only correlation).
  - [ ] `tools/traceability/generate_source_ids.py` for markdown + YAML.
  - [ ] `tools/traceability/seed_source_trace_refs.py` for inserting missing metadata blocks.
  - [ ] `tools/traceability/reconcile_source_ids.py` for drift repair while preserving existing IDs.
- [ ] Validation tools.
  - [ ] `tools/traceability/validate_iso_schema.py`.
  - [ ] `tools/traceability/validate_source_trace_schema.py`.
  - [ ] `tools/traceability/validate_source_id_uniqueness.py`.
  - [ ] `tools/traceability/validate_anchor_refind.py`.
  - [ ] `tools/traceability/validate_no_copyright_leak.py`.
  - [ ] `tools/traceability/validate_source_anchor_integrity.py`.
  - [ ] `tools/traceability/validate_hierarchy_integrity.py`.
- [ ] Lookup and navigation tools.
  - [ ] `tools/traceability/build_reverse_indexes.py` (source->anchor and anchor->source).
  - [ ] `tools/traceability/lookup_pdf_to_source.py`.
  - [ ] `tools/traceability/lookup_source_to_iso.py`.
  - [ ] `tools/traceability/path_explain.py`.
  - [ ] `tools/traceability/init_iso_unit.py`.

## 14) Make command integration
- [ ] Extend `make.py` with traceability commands.
  - [ ] `traceability-refresh` -> extract, fingerprint, ISO hierarchy generation, source scan, index generation, validations.
  - [ ] `traceability-validate` -> all validators only.
  - [ ] `traceability-lookup` -> wrapper for source/pdf lookup.
  - [ ] `traceability-seed-source` -> generate/seed missing source IDs and trace metadata stubs.
  - [ ] `traceability-report` -> coverage + unresolved summary.
- [ ] Update `README.md` command docs.
  - [ ] Add prerequisite list.
  - [ ] Add normal update workflow.
  - [ ] Add source-first and PDF-first lookup workflows.

## 15) Docgen integration and rendered traceability (footnote capability)
- [ ] Add parser support for source trace directives in markdown.
  - [ ] Recognize trace directives without rendering directive text.
  - [ ] Associate directive with next heading/paragraph/list-item/table placeholder block.
  - [ ] Preserve deterministic output ordering.
- [ ] Add YAML row/cell trace metadata handling in table rendering.
  - [ ] Read `_trace.source_id`, `_trace.anchor_ids`, `_trace.cell_anchor_ids`.
  - [ ] Allow row-level and cell-level note emission.
- [ ] Add footnote-like output mode.
  - [ ] Phase 1 (required): endnote-style "Traceability Notes" sections with marker tags.
  - [ ] Phase 2 (optional): true DOCX footnotes via OOXML extension when stable.
  - [ ] Ensure notes include source locator + ISO anchor locator and no ISO quoted text.
- [ ] Validate rendered trace integrity.
  - [ ] Every rendered trace marker resolves to source metadata and valid anchor IDs.
  - [ ] No dangling markers.
  - [ ] No duplicate marker IDs in final document.

## 16) Source instrumentation coverage policy
- [ ] Markdown coverage policy.
  - [ ] Every heading statement in `src/iso26262_rust_mapping.md` receives `source_id`.
  - [ ] Every paragraph sentence receives `source_id` and trace status.
  - [ ] Every numbered and bulleted list statement receives `source_id` and trace status.
  - [ ] Every mapped statement includes at least one ISO anchor reference.
- [ ] YAML table coverage policy.
  - [ ] Every row statement in `table-01`..`table-26` receives `source_id` and trace status.
  - [ ] Every cell statement receives `source_id` and trace status when cell contains normative assertions.
  - [ ] Cell-level anchor refs are required when row-level references are insufficiently precise.
- [ ] Coverage exceptions policy.
  - [ ] No silent exceptions are allowed.
  - [ ] Any temporary unmapped statement requires explicit rationale, owner, and remediation target stage.
  - [ ] Final gate requires zero unresolved required statements.

## 17) Bidirectional completeness and KPIs
- [ ] ISO-side completeness metrics.
  - [ ] `iso_unit_total`, `iso_unit_required`, `iso_unit_seeded`.
  - [ ] `iso_leaf_total`, `iso_leaf_required`, `iso_leaf_mapped`, `iso_leaf_unmapped`.
- [ ] Source-side completeness metrics.
  - [ ] `source_statement_total`, `source_statement_required`, `source_statement_with_id`, `source_statement_with_anchor_refs`.
  - [ ] `source_statement_missing_ids`, `source_statement_missing_anchor_refs`.
  - [ ] `source_statement_unmapped_with_rationale`.
- [ ] Integrity metrics.
  - [ ] `dangling_source_anchor_refs`.
  - [ ] `unknown_anchor_ids_in_source`.
  - [ ] `duplicate_source_ids`.
  - [ ] `orphan_iso_units`.
- [ ] Reporting metrics (must be emitted in JSON and Markdown).
  - [ ] `traced_statement_count`.
  - [ ] `untraced_statement_count`.
  - [ ] `trace_coverage_percent`.
  - [ ] `remediation_item_count`.
- [ ] Final gate threshold.
  - [ ] Required unresolved counts must be zero.
  - [ ] Remaining non-required unresolved counts must carry rationale, owner, and remediation plan.

## 18) Durable execution contract (resumable)
- [ ] Execute with `skills/resumable-execution/SKILL.md` process.
  - [ ] Run root: `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-<run-id>/`.
  - [ ] Files: `state.env`, `checklist.state.env`, `run.log`, `artifacts/`.
  - [ ] Single-writer lock file in run root.
  - [ ] Atomic state updates via `reports/tooling/state_tool.py`.
- [ ] Immutable contract fields.
  - [ ] `RUN_ID`, `TASK_NAME`, `RUN_ROOT`, `REPO_ROOT`, `PLAN_PATH`.
  - [ ] `TARGET_BRANCH`, `BASE_PIN_SHA`, `EXPECTED_OLD_REMOTE_SHA`.
  - [ ] `SOURCE_PDFSET_ID`, `P06_SHA256`, `P08_SHA256`, `P09_SHA256`.
- [ ] Resume rules.
  - [ ] Resume from earliest incomplete stage.
  - [ ] If stage marked done with incomplete checklist, resume at that stage.
  - [ ] If push status unknown, reconcile remote SHA before continuing.
  - [ ] If finalization partial, resume only finalization stage.

## 19) Stage plan (detailed and sequential)
- [ ] `S0` Bootstrap run.
  - [ ] Create run root and initialize state/checklist/log files.
  - [ ] Populate immutable contract values and PDF checksums.
  - [ ] Create artifact subdirectories.
- [ ] `S1` ISO decomposition and baseline inventory.
  - [ ] Generate part manifests for P06/P08/P09 units.
  - [ ] Generate repository source surface inventory (md + yaml nodes).
  - [ ] Record baseline metrics.
- [ ] `S2` Schema and contract finalization.
  - [ ] Finalize source trace directive format.
  - [ ] Finalize YAML `_trace` schema updates.
  - [ ] Finalize ISO JSONC schemas.
- [ ] `S3` Tooling foundation.
  - [ ] Implement source ID generation/seeding/reconciliation.
  - [ ] Implement ISO hierarchy/anchor generator.
  - [ ] Implement schema and integrity validators.
- [ ] `S4` Seed ISO hierarchy.
  - [ ] Scaffold all required unit files for P06/P08/P09.
  - [ ] Populate anchor leaves for each unit with fingerprints and locators.
  - [ ] Mark each leaf status (`mapped` vs unresolved categories).
- [ ] `S5` Embed source metadata.
  - [ ] Insert source IDs and trace refs in markdown nodes.
  - [ ] Insert source IDs and trace refs in YAML rows/cells for `table-01..table-26`.
  - [ ] Validate no duplicate IDs and no unknown anchor refs.
- [ ] `S6` Build reverse indexes and lookup workflows.
  - [ ] Generate `.cache/iso26262/indexes/source_to_anchor.json`.
  - [ ] Generate `.cache/iso26262/indexes/anchor_to_source.json`.
  - [ ] Validate PDF-first and source-first lookup paths.
- [ ] `S7` Docgen trace surfacing.
  - [ ] Implement trace directive parsing in docgen.
  - [ ] Add endnote-style trace output and marker linking.
  - [ ] Validate rendered markers and note resolution.
- [ ] `S8` Full source instrumentation freeze.
  - [ ] Instrument all existing markdown statements with `source_id` and trace status.
  - [ ] Instrument all existing YAML row/cell statements with `source_id` and trace status.
  - [ ] Enforce zero missing `source_id` before advancing.
  - [ ] Reconcile moved/reordered statements without regenerating existing IDs.
- [ ] `S9` Validation, reporting, and closeout.
  - [ ] Run all validators and coverage reports.
  - [ ] Generate final JSON and Markdown traceability reports in `$OPENCODE_CONFIG_DIR/reports/`.
  - [ ] Resolve all required unresolved items or record explicit remediation.
  - [ ] Write disposition ledger and operating guide.
  - [ ] Update finalization flags and release lock.

## 20) Stage artifact checklist (required)
- [ ] `S0` artifacts.
  - [ ] `artifacts/bootstrap/contract.json`.
  - [ ] `artifacts/bootstrap/run-initialization.log`.
- [ ] `S1` artifacts.
  - [ ] `artifacts/baseline/pdf-metadata.json`.
  - [ ] `artifacts/baseline/pdf-checksums.json`.
  - [ ] `artifacts/baseline/repo-source-surface.json`.
  - [ ] `artifacts/baseline/iso-unit-manifest.json`.
- [ ] `S2` artifacts.
  - [ ] `artifacts/design/source-embedded-trace-contract.md`.
  - [ ] `artifacts/design/iso-anchor-contract.md`.
  - [ ] `artifacts/design/schema-decisions.md`.
- [ ] `S3` artifacts.
  - [ ] `artifacts/tooling/tooling-smoke-results.json`.
  - [ ] `artifacts/tooling/validator-smoke-results.json`.
- [ ] `S4` artifacts.
  - [ ] `artifacts/iso/seeded-units-summary.md`.
  - [ ] `artifacts/iso/unresolved-iso-leaves.md`.
- [ ] `S5` artifacts.
  - [ ] `artifacts/source/source-id-coverage.md`.
  - [ ] `artifacts/source/missing-source-anchors.md`.
  - [ ] `artifacts/source/unknown-anchor-refs.md`.
- [ ] `S6` artifacts.
  - [ ] `artifacts/indexes/source_to_anchor.stats.json`.
  - [ ] `artifacts/indexes/anchor_to_source.stats.json`.
  - [ ] `artifacts/indexes/lookup-smoke.md`.
- [ ] `S7` artifacts.
  - [ ] `artifacts/render/trace-marker-spec.md`.
  - [ ] `artifacts/render/trace-render-validation.json`.
- [ ] `S8` artifacts.
  - [ ] `artifacts/source/statement-source-id-freeze.md`.
  - [ ] `artifacts/source/missing-source-id-report.json`.
  - [ ] `artifacts/source/statement-segmentation-reconciliation.md`.
- [ ] `S9` artifacts.
  - [ ] `artifacts/validation/schema-validation.json`.
  - [ ] `artifacts/validation/no-leak-validation.json`.
  - [ ] `artifacts/validation/refind-validation.json`.
  - [ ] `artifacts/validation/source-anchor-integrity.json`.
  - [ ] `artifacts/validation/coverage-report.md`.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-<run-id>/traceability-statement-coverage.json`.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/iso26262-traceability-<run-id>/traceability-statement-coverage.md`.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.json`.
  - [ ] `$OPENCODE_CONFIG_DIR/reports/traceability-statement-coverage-latest.md`.
  - [ ] `artifacts/disposition/traceability-disposition-ledger.md`.
  - [ ] `artifacts/summary.md` with next-session resume hints.

## 21) Validation gates (must pass)
- [ ] ISO hierarchy schema gate.
  - [ ] All `traceability/iso26262/**/*.jsonc` schema-valid.
  - [ ] Parent-child hierarchy links are consistent.
- [ ] Source trace schema gate.
  - [ ] Markdown trace directives parse and validate.
  - [ ] YAML `_trace` objects validate in every required row.
- [ ] Statement-level source anchor gate.
  - [ ] Every statement-level source node has a `source_id`.
  - [ ] Every statement-level source node has explicit trace status.
  - [ ] Every mapped statement resolves to at least one valid ISO anchor ID.
- [ ] Integrity gate.
  - [ ] No duplicate source IDs.
  - [ ] No unknown ISO anchor IDs in source.
  - [ ] No orphan anchors required by source references.
- [ ] No-leak gate.
  - [ ] No banned text fields in tracked JSONC.
  - [ ] No watermark/email/order/license strings in tracked files.
- [ ] Re-find gate.
  - [ ] Anchor refind succeeds from cache extraction for required anchors.
  - [ ] Fuzzy fallback is bounded and reported.
- [ ] Coverage gate.
  - [ ] Required ISO leaves unresolved count = 0.
  - [ ] Required source statements unresolved count = 0.
- [ ] Rendered trace gate.
  - [ ] All rendered markers resolve to source IDs and anchor IDs.
  - [ ] No dangling marker references.
- [ ] Final reporting gate.
  - [ ] JSON report generated with traced/untraced breakdown.
  - [ ] Markdown report generated with remediation thoughts and next-step plan.
  - [ ] Reports are written under `$OPENCODE_CONFIG_DIR/reports/` for session handoff.

## 22) Risk register and mitigations
- [ ] Risk: source metadata noise reduces readability.
  - [ ] Mitigation: compact directive format + linted placement rules.
  - [ ] Mitigation: optional formatting helpers to keep markdown readable.
- [ ] Risk: duplicate IDs from copy/paste.
  - [ ] Mitigation: uniqueness validator + auto-repair tool for duplicates.
- [ ] Risk: parser changes break doc generation.
  - [ ] Mitigation: feature-flag trace parsing and regression tests for current output.
- [ ] Risk: inability to implement true DOCX footnotes quickly.
  - [ ] Mitigation: required endnote-style fallback with same locator detail.
- [ ] Risk: extraction variability across PDF layout.
  - [ ] Mitigation: dual extraction + deterministic normalization profile.
- [ ] Risk: accidental copyright leakage.
  - [ ] Mitigation: strict no-leak validator + human spot-check checklist.
- [ ] Risk: long execution interrupted.
  - [ ] Mitigation: stage-gated resumable run state and mandatory artifact checkpoints.

## 23) Commit phasing (logical and reviewable)
- [ ] `docs(plan): rewrite traceability plan for source-embedded correlation`
- [ ] `feat(traceability): add ISO hierarchy schemas and scaffold`
- [ ] `feat(traceability): add source-id generation and source trace validators`
- [ ] `feat(traceability): add ISO extraction, anchor generation, and refind validation`
- [ ] `feat(traceability): seed p06/p08/p09 units and anchors`
- [ ] `feat(traceability): embed source ids and anchor refs in markdown and table YAML`
- [ ] `feat(traceability): add statement-level instrumentation freeze and reconciliation`
- [ ] `feat(docgen): add trace marker parsing and footnote-like note rendering`
- [ ] `feat(traceability): add final coverage reports (json+markdown)`
- [ ] `docs(traceability): add commands, workflow guide, and resume prompt`

## 24) Prompt and new-session operations
- [ ] Add dedicated prompt for this plan.
  - [ ] `prompts/execute-iso26262-traceability-resumable.md`.
  - [ ] Inputs: `RUN_ID` (optional), `MAX_STAGES` (default 1).
  - [ ] Outputs: stage before/after, artifacts changed, blockers, exact next step.
- [ ] Add startup checklist for new sessions.
  - [ ] Verify `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
  - [ ] Load run root by `RUN_ID` or newest incomplete run.
  - [ ] Validate immutable contract and lock state.
  - [ ] Resume at earliest incomplete safe stage.

## 25) Definition of done
- [ ] Source-embedded correlation fully operational.
  - [ ] Source IDs and trace status are embedded for each and every statement in markdown and YAML.
  - [ ] Mapped statements include valid ISO anchor refs.
  - [ ] No manual tracked mapping file set is needed for canonical correlation.
- [ ] ISO progressive hierarchy complete for relevant PDFs.
  - [ ] P06/P08/P09 unit manifests fully seeded with explicit statuses.
  - [ ] Leaf anchor records exist for required units and pass validators.
- [ ] Lookup workflows operational.
  - [ ] PDF-first lookup resolves to source nodes.
  - [ ] Source-first lookup resolves to ISO anchors and unit files.
- [ ] Rendered traceability visible and precise.
  - [ ] Footnote-like or endnote output includes exact source placement and anchor IDs.
  - [ ] No leakage of ISO text in output annotations.
- [ ] Final traceability reporting complete.
  - [ ] JSON report in `$OPENCODE_CONFIG_DIR/reports/` enumerates what traced and what did not.
  - [ ] Markdown report in `$OPENCODE_CONFIG_DIR/reports/` includes remediation thoughts and plan.
- [ ] Durability and handoff complete.
  - [ ] Resumable run state finalized with summary and disposition ledger.
  - [ ] Next session can resume deterministically with no ambiguity.
