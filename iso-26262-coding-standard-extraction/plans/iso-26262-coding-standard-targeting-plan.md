# ISO 26262 Coding Standard Targeting Plan

## Planning intent

- [ ] Build a local, citation-ready ISO 26262 corpus that supports drafting and auditing a language-specific coding standard.
- [x] Keep all licensed content and derived artifacts local only.
- [x] Prioritize sections that directly drive coding rules, verification evidence, and safety-case traceability.

## Idea-source integration

- [ ] Treat idea documents in `$OPENCODE_CONFIG_DIR/ideas/` as normative planning inputs.
  - [x] Integrate `iso-26262-query-engine-concept.md` into extraction, chunking, indexing, and citation output requirements.
  - [x] Integrate `iso-26262-parts-that-are-important.md` into target section prioritization and traceability mapping.
  - [ ] Keep a clear link from each major phase to at least one idea-derived requirement.

- [ ] Keep an idea-derived requirements map in planning artifacts.
  - [ ] For each requirement, record `idea_source`, `plan_phase`, `implementation_status`, `validation_status`.
  - [ ] Update the map when parser/query behavior changes materially.

## Implementation stack (Rust-first)

- [x] Use Rust as the primary implementation language for extraction, indexing, and query.
  - [x] Pin a stable toolchain in `rust-toolchain.toml`.
  - [x] Use `cargo` workspaces only if multi-crate layout is needed.
  - [x] Keep lockfile policy explicit (`Cargo.lock` tracked for deterministic builds).

- [x] Build a single local CLI binary (working name: `iso26262`) with deterministic subcommands.
  - [x] `inventory` - enumerate PDFs, compute hashes, emit `pdf_inventory.json`.
  - [x] `ingest` - parse PDFs and populate SQLite chunks/FTS.
  - [x] `query` - retrieve citation-ready results.
  - [x] `validate` - run gold-set checks and emit quality report.
  - [x] `status` - print run-state and resume readiness.

- [x] Use Rust-native foundations for reliability and local execution.
  - [x] `rusqlite` for SQLite access and migrations.
  - [x] SQLite FTS5 as the baseline retrieval engine.
  - [x] `serde` / `serde_json` for manifest IO.
  - [x] `sha2` for source hashing.
  - [x] `regex` for heading/reference parsing.

- [x] Apply logging and CLI output policy consistently.
  - [x] Use `tracing` for operational diagnostics and progress logs.
  - [x] Initialize `tracing-subscriber` at process start.
  - [x] Do not use `println!` / `eprintln!` for diagnostics in CLI command paths.
  - [x] Keep stdout reserved for intentional command results (especially machine-readable output modes).
  - [x] Keep diagnostic logs on stderr via tracing subscriber configuration.

- [ ] Apply Rust state-management design constraints to avoid static-state drift.
  - [x] Do not use global mutable state (`static mut`) for parser, query, or ingest flow.
  - [x] Avoid singleton-style global state by default for runtime components.
  - [x] Prefer explicit state ownership in structs and pass context through module boundaries.
  - [x] Keep compiled regex/parser resources as struct fields initialized in constructors.
  - [x] Allow immutable lazy static caches only after profiling proves a measurable benefit.
  - [ ] Record any approved static optimization in `decisions_log.jsonl` with benchmark evidence.

- [ ] Define extraction backend policy compatible with Rust workflows.
  - [x] Use text-layer extraction first (per page).
  - [ ] Run OCR only when text-layer extraction is unavailable for a page.
  - [ ] Keep OCR optional and gated by explicit ingest flag.
  - [x] Keep table extraction tiered with mandatory raw-table fallback.
  - [ ] Record extraction backend choice and fallback reason in ingest manifest.

## Non-negotiable constraints

- [ ] Restrict all exploration and edits to approved roots only.
  - [ ] Allowed root 1: `$OPENCODE_CONFIG_DIR` (planning/config artifacts only).
  - [ ] Allowed root 2: `.` (the active implementation workspace).
  - [ ] Do not list/read/search/edit paths outside these two roots.
  - [ ] Do not inspect sibling repositories, parent directories, or home-level paths.
  - [ ] If a required file appears outside these roots, stop and request explicit user direction.

- [x] Keep licensed PDFs only under `.cache/iso26262/`.
- [x] Keep the extraction database only under `.cache/iso26262/`.
- [x] Treat ingest logs and manifests as mandatory artifacts under `.cache/iso26262/manifests/`.
  - [x] Required path: `.cache/iso26262/manifests/`.
  - [x] Required manifest: `pdf_inventory.json`.
  - [x] Required manifest: `target_sections.json`.
  - [x] Required manifest: `target_sections.csv`.
  - [x] Required manifest: `ingest_run_<timestamp>.json`.
  - [x] Required manifest: `run_state.json`.
  - [x] Required manifest: `decisions_log.jsonl`.
  - [x] Required manifest: `gold_set_expected_results.json`.
  - [x] Required manifest: `extraction_quality_report.json`.
  - [x] Required manifest: `traceability_matrix.csv`.
- [x] Never publish or commit extracted text, table content, or generated DB files.

## Canonical data locations

- [x] Config workspace root (plans/ideas only): `/home/pete.levasseur/opencode-project-agents/iso-26262-coding-standard-extraction/`.
- [x] Execution workspace root (licensed PDFs, DB, manifests): `/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/`.
- [x] Source PDFs: `/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/.cache/iso26262/*.pdf`.
- [x] Working DB: `/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/.cache/iso26262/iso26262_index.sqlite`.
- [x] Manifests and ingest logs (mandatory): `/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/.cache/iso26262/manifests/`.
- [x] Plan document: `/home/pete.levasseur/opencode-project-agents/iso-26262-coding-standard-extraction/plans/iso-26262-coding-standard-targeting-plan.md`.

## Mainline operating model (initial execution)

- [x] Use `main` as the active branch for bootstrap and initial solo execution.
- [x] Make small, phase-aligned Conventional Commits directly on `main`.
- [x] Keep one concern per commit; avoid batching unrelated phase work.
- [ ] If branch/PR mode is explicitly requested later, use `type/phase-<n>-short-topic`.
- [x] Record git context in `run_state.json` (`base_branch`, `active_branch`, `commit_mode`, `last_commit`).

- [ ] Phase-to-commit checkpoint baseline on `main`.
  - [x] Phase 0 checkpoint commit for session resilience and startup governance.
  - [x] Phase 1 checkpoint commit for target section register.
  - [x] Phase 2 checkpoint commit for chunk model and schema contract.
  - [x] Phase 3 checkpoint commit for ingest pipeline implementation.
  - [x] Phase 4 checkpoint commit for query engine and citations.
  - [ ] Phase 5 checkpoint commit for traceability outputs.
  - [x] Phase 6 checkpoint commit for validation and quality loop.
  - [x] Phase 7 checkpoint commit for milestone alignment updates.
  - [ ] Phase 8 checkpoint commit for runbook/recovery finalization.
  - [ ] Phase 9 checkpoint commit for commit governance updates.

## Phase 0 - Session resilience, path contract, and deterministic startup

- [x] Git checkpoint for Phase 0.
  - [x] Active branch: `main`.
  - [x] Use Conventional Commit(s) for startup governance updates.
  - [x] Record `phase_id`, `active_branch`, and `last_commit` in run-state artifacts.

- [x] Enforce workspace and path contract at the start of every session.
  - [x] Confirm `OPENCODE_CONFIG_DIR` equals `/home/pete.levasseur/opencode-project-agents/iso-26262-coding-standard-extraction`.
  - [x] Confirm execution workspace exists at `/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/`.
  - [x] Confirm `.cache/iso26262/` exists before ingest work begins.
  - [x] Confirm manifests path exists at `.cache/iso26262/manifests/`; create if missing.
  - [x] Confirm no licensed artifacts are written under the config workspace.

- [x] Create and maintain mandatory run state manifest.
  - [x] File path: `.cache/iso26262/manifests/run_state.json`.
  - [x] Required fields: `active_run_id`, `current_phase`, `current_step`, `status`.
  - [x] Required fields: `base_branch`, `active_branch`, `phase_id`, `commit_mode`, `last_commit`.
  - [x] Required fields: `last_successful_command`, `next_planned_command`.
  - [x] Required fields: `started_at`, `updated_at`, `last_successful_artifact`.
  - [x] Allowed status values: `not_started`, `running`, `blocked`, `failed`, `completed`.
  - [x] Update `run_state.json` after every completed step, not only at phase boundaries.

- [x] Create and maintain mandatory decision log.
  - [x] File path: `.cache/iso26262/manifests/decisions_log.jsonl`.
  - [x] One JSON object per decision (append-only).
  - [x] Required keys: `timestamp`, `decision_id`, `context`, `options_considered`, `selected_option`, `rationale`, `impact`.
  - [x] Record parser heuristics, table extraction fallbacks, scope changes, and quality exceptions.

- [ ] Verify Rust and extraction runtime prerequisites at startup.
  - [x] Confirm `rustc --version` and `cargo --version` succeed.
  - [ ] Confirm OCR runtime (`tesseract`) availability if OCR is enabled.
  - [x] Capture tool versions in ingest manifest under `tool_versions`.

- [ ] Create deterministic startup checklist so session restarts do not drift.
  - [ ] Step 00: Validate the allowed-root boundary (`$OPENCODE_CONFIG_DIR` and `.` only).
  - [ ] Step 01: Validate path contract and required directories.
  - [ ] Step 02: Load `run_state.json` and determine resume point.
  - [ ] Step 03: Load latest `ingest_run_<timestamp>.json` and compare with `run_state.json`.
  - [ ] Step 04: Load `decisions_log.jsonl` to preserve prior rationale.
  - [ ] Step 05: Load idea-source inputs from `$OPENCODE_CONFIG_DIR/ideas/` and verify requirement links remain current.
  - [ ] Step 06: Resume from the next incomplete checklist step only.
  - [ ] Step 07: Verify git context (`base_branch`, `active_branch`, `commit_mode`, `last_commit`) before making new changes.

- [ ] Define versioning contract for reproducibility and restart safety.
  - [x] Pin `manifest_version` in each manifest file.
  - [x] Pin `db_schema_version` in SQLite metadata.
  - [ ] Pin parser/query tool version identifiers per ingest run.
  - [ ] Pin Rust engine version (CLI semver or git commit) per run.
  - [ ] Require compatibility checks before resuming with existing DB.
  - [ ] Block resume when `db_schema_version` or engine version is incompatible.

## Phase 1 - Build target section register

- [ ] Git checkpoint for Phase 1.
  - [ ] Active branch: `main`.
  - [ ] Keep scope to target register schema, population, and manifest outputs.
  - [ ] Create a Conventional Commit checkpoint when P0-P3 target register content is complete and reviewable.

- [x] Create a machine-readable register for ISO references needed by the coding standard.
  - [x] Define schema fields:
    - [x] `priority` (P0, P1, P2, P3).
    - [x] `part` (2, 6, 8, 9).
    - [x] `year` (2018).
    - [x] `ref` (clause, table, annex id).
    - [x] `ref_type` (`clause`, `table`, `annex`).
    - [x] `why_it_matters` (rule source, evidence source, governance source).
    - [x] `coding_standard_area` (complexity, typing, naming, concurrency, etc).
    - [x] `evidence_type` (review, static analysis, test, coverage, tool confidence).
    - [x] `status` (`planned`, `indexed`, `validated`, `mapped`).
  - [x] Export register as JSON and CSV in mandatory manifests path.

- [x] Populate P0 targets (core coding-rule sources, Part 6).
  - [x] ISO 26262-6:2018 5.4.2.
  - [x] ISO 26262-6:2018 5.4.3.
  - [x] ISO 26262-6:2018 Table 1.
  - [x] ISO 26262-6:2018 8.4.5.
  - [x] ISO 26262-6:2018 Table 6.
  - [x] ISO 26262-6:2018 Annex B.
  - [x] ISO 26262-6:2018 Annex C.
  - [x] ISO 26262-6:2018 Annex D.

- [x] Populate P1 targets (verification and coverage in Part 6).
  - [x] ISO 26262-6:2018 9.4.2.
  - [x] ISO 26262-6:2018 Table 7.
  - [x] ISO 26262-6:2018 9.4.4.
  - [x] ISO 26262-6:2018 Table 9.
  - [x] ISO 26262-6:2018 10.4.2.
  - [x] ISO 26262-6:2018 Table 10.
  - [x] ISO 26262-6:2018 10.4.5.
  - [x] ISO 26262-6:2018 Table 12.
  - [x] ISO 26262-6:2018 11.4.
  - [x] ISO 26262-6:2018 Tables 13, 14, 15.

- [x] Populate P2 targets (governance and tool confidence in Part 8).
  - [x] ISO 26262-8:2018 Clause 7.
  - [x] ISO 26262-8:2018 Clause 8.
  - [x] ISO 26262-8:2018 Clause 9.
  - [x] ISO 26262-8:2018 Clause 10.
  - [x] ISO 26262-8:2018 Clause 11.
  - [x] ISO 26262-8:2018 Table 3.
  - [x] ISO 26262-8:2018 Table 4.
  - [x] ISO 26262-8:2018 Table 5.
  - [x] ISO 26262-8:2018 Clause 12.

- [x] Populate P3 targets (safety plan/case and ASIL tailoring).
  - [x] ISO 26262-2:2018 6.4.6.
  - [x] ISO 26262-2:2018 6.4.7.2.
  - [x] ISO 26262-2:2018 6.4.8.
  - [x] ISO 26262-2:2018 6.4.13.
  - [x] ISO 26262-9:2018 Clause 5.
  - [x] ISO 26262-9:2018 Clause 7.

## Phase 2 - Build citation-capable chunk model

- [ ] Git checkpoint for Phase 2.
  - [x] Active branch: `main`.
  - [ ] Keep scope to chunk schema, metadata contract, and chunking rules.
  - [ ] Create a Conventional Commit checkpoint when chunk model is stable and referenced by ingest implementation.

- [x] Finalize chunk types.
  - [x] `clause`.
  - [x] `subclause`.
  - [x] `table`.
  - [x] `list_item` / `requirement_atom`.
  - [x] `annex`.

- [ ] Finalize hierarchical node model (required for table/list fidelity).
  - [x] Parent-child lineage must support: `document -> clause/subclause -> table -> row -> cell`.
  - [ ] Parent-child lineage must support: `clause/subclause -> list -> list_item -> sub_item`.
  - [x] Define canonical node types: `document`, `clause`, `subclause`, `annex`, `table`, `table_row`, `table_cell`, `list`, `list_item`, `requirement_atom`.
  - [x] Define required node fields: `node_id`, `parent_node_id`, `doc_id`, `node_type`, `ref`, `ref_path`, `heading`, `order_index`, `page_pdf_start`, `page_pdf_end`, `text`, `source_hash`.
  - [ ] Define required table-cell fields: `table_node_id`, `row_idx`, `col_idx`, `is_header`, `row_span`, `col_span`, `cell_text`.
  - [ ] Define required list-item fields: `list_depth`, `list_marker`, `item_index`, `item_text`.
  - [x] Link each table node to the nearest preceding clause/subclause node for contextual retrieval.
  - [x] Preserve stable ordering for rows, cells, and list items (`order_index` must be deterministic).

- [ ] Define chunk-to-node linkage contract.
  - [x] Every chunk must include `origin_node_id`.
  - [x] Every chunk must include `leaf_node_type`.
  - [x] Every chunk must include `ancestor_path` (ordered node path for context reconstruction).
  - [ ] Splitting large text into multiple chunks must preserve the same `origin_node_id` and increment `chunk_seq`.

- [ ] Define required metadata for every chunk.
  - [x] `chunk_id`.
  - [x] `doc_id`.
  - [ ] `part`, `year`, `edition`.
  - [x] `ref`.
  - [x] `ref_path`.
  - [x] `heading`.
  - [x] `type`.
  - [x] `chunk_seq`.
  - [x] `page_pdf_start`, `page_pdf_end`.
  - [ ] `page_printed_start`, `page_printed_end` (when available).
  - [x] `text`.
  - [x] `table_md`, `table_csv` (for table chunks).
  - [x] `origin_node_id`.
  - [x] `leaf_node_type`.
  - [x] `ancestor_path`.
  - [x] `source_hash` (sha256 of source PDF).

- [ ] Define chunking rules.
  - [x] Split on semantic boundaries first (clause/table/list item/annex section).
  - [ ] For long clauses, split into approximately 300-900 words.
  - [ ] Apply overlap of approximately 50-100 words for split chunks.
  - [ ] Preserve original reference and add `chunk_seq` for split chunks.

## Phase 3 - Implement ingestion pipeline

- [ ] Git checkpoint for Phase 3.
  - [x] Active branch: `main`.
  - [ ] Keep scope to extraction, normalization, parsing, persistence, and ingest manifests.
  - [ ] Create a Conventional Commit checkpoint when ingest can run locally and emit reproducible run artifacts.

- [ ] Implement Rust ingestion module boundaries.
  - [ ] `inventory` module for source discovery, hashing, and metadata.
  - [ ] `extract` module for per-page text extraction and OCR fallback.
  - [ ] `normalize` module for header/footer stripping and de-hyphenation.
  - [ ] `parse` module for clauses, subclauses, annexes, tables, list atoms.
  - [ ] `hierarchy` module for parent-child node construction and ordering.
  - [ ] `persist` module for SQLite inserts and FTS synchronization.
  - [ ] `manifest` module for run-state, ingest-run logs, and warnings.

- [x] Implement source discovery and inventory.
  - [x] Enumerate `.cache/iso26262/*.pdf`.
  - [x] Compute SHA-256 hash per PDF.
  - [x] Record inventory manifest in `.cache/iso26262/manifests/pdf_inventory.json`.

- [ ] Implement per-page extraction strategy.
  - [ ] Detect extractable text per page.
  - [ ] Use layout-aware text extraction for text pages.
  - [ ] Use OCR only for pages that are image-only.
  - [ ] Record OCR usage statistics in ingest manifest.

- [ ] Implement text normalization.
  - [ ] Remove repeated headers and footers using frequency heuristics.
  - [ ] Normalize line breaks and spacing.
  - [ ] De-hyphenate conservative line-wrap artifacts.
  - [ ] Preserve numbering and table labels.

- [ ] Implement structure parsing.
  - [x] Parse clause and subclause headings (regex + layout cues).
  - [x] Parse annex headings.
  - [x] Parse table titles and table identifiers.
  - [x] Parse table rows and cells, preserving row/column order.
  - [x] Detect and isolate list items and requirement atoms.
  - [ ] Parse list nesting depth and marker style (`-`, numbered, alpha, etc.).
  - [x] Emit hierarchical nodes with deterministic parent references.

- [ ] Implement table extraction in tiers.
  - [x] Tier A: structured table extraction with row/cell nodes.
  - [x] Tier B: fallback to table text blocks (`table_raw=true` equivalent marker) while still creating a table node.
  - [ ] Tier C: OCR-based table extraction for critical missed tables.
  - [x] Save each accepted table as markdown and CSV.
  - [ ] Record fallback reason and extraction confidence in ingest manifest.

- [ ] Write chunks to SQLite and FTS index.
  - [x] Create `docs` table.
  - [x] Create `nodes` table for hierarchical content objects.
  - [x] Create `chunks` table.
  - [x] Create FTS index table (`chunks_fts`).
  - [x] Create indexes on `nodes(parent_node_id)`, `nodes(doc_id, node_type)`, and `chunks(origin_node_id)`.
  - [x] Fail fast with actionable error if FTS5 is unavailable.
  - [x] Rebuild or sync FTS after ingest.
  - [x] Use transaction batches and prepared statements for chunk inserts.
  - [ ] Validate node parent references and ordering constraints before commit.
  - [ ] Validate referential integrity.

- [ ] Emit mandatory ingest run manifest.
  - [x] File path: `.cache/iso26262/manifests/ingest_run_<timestamp>.json`.
  - [x] Include `manifest_version`, `run_id`, and `db_schema_version`.
  - [ ] Include `tool_versions` (`rustc`, `cargo`, OCR backend, extractor backend).
  - [x] Include ingest command and effective flags for reproducibility.
  - [x] Include `status` (`running`, `failed`, `completed`) and `completed_steps` list.
  - [x] Include `failed_step` and `failure_reason` when status is `failed`.
  - [ ] Include counts by part, chunk type, and table extraction tier.
  - [x] Include hierarchy counts by node type (`table_row`, `table_cell`, `list_item`, `requirement_atom`).
  - [x] Include `table_raw_fallback_count` and list parsing fallback counts.
  - [x] Include warnings for parse ambiguities and OCR fallbacks.
  - [x] Include hash of each source PDF used in that run.

- [ ] Implement idempotent restart semantics.
  - [ ] Treat each ingest stage as an idempotent step with explicit checkpointing.
  - [ ] On restart, skip completed steps and continue from `next_planned_command`.
  - [ ] If source PDF hash set changed, start a new `run_id` and preserve old manifests.
  - [ ] If DB schema/tool version changed incompatibly, block resume and perform controlled rebuild.
  - [ ] Controlled rebuild must archive old DB name with timestamp before replacing it.

## Phase 4 - Build query engine for citation outputs

- [ ] Git checkpoint for Phase 4.
  - [x] Active branch: `main`.
  - [ ] Keep scope to retrieval, ranking, citation formatting, and JSON output.
  - [ ] Create a Conventional Commit checkpoint when clause/table queries return citation-complete results.

- [x] Implement Rust query CLI contract.
  - [x] Support text queries, phrase queries, and reference-style queries.
  - [x] Provide `--json` output mode with stable schema.
  - [x] Provide deterministic tie-breaking for equal-ranked results.
  - [x] Support filters for part/ref/type without changing citation completeness.
  - [x] Support node-type filters (`clause`, `table`, `table_row`, `table_cell`, `list_item`, `requirement_atom`).
  - [x] Support optional context expansion (`--with-ancestors`, `--with-descendants`) for hierarchy-aware responses.

- [ ] Implement query modes.
  - [x] Exact reference lookup (`5.4.3`, `Table 6`, `Annex D`).
  - [x] Keyword and phrase search over headings and body text.
  - [x] Table detail mode that returns row/cell descendants for a matched table node.
  - [x] Requirement-atom mode for `shall`/`should`/`shall not` statements.
  - [ ] Optional semantic mode (deferred until FTS baseline is stable).

- [ ] Implement ranking and retrieval controls.
  - [x] Default top-k retrieval.
  - [x] Apply explicit exact-reference boost before generic FTS ranking.
  - [x] Prioritize exact reference matches over generic term hits.
  - [ ] Support filtering by part, clause, annex, chunk type.

- [ ] Make citation output mandatory for all results.
  - [x] `doc_id`.
  - [x] `part` and `year`.
  - [x] `ref`.
  - [x] `page_pdf_start/page_pdf_end`.
  - [x] `source_hash`.
  - [x] Short snippet with highlighted terms.
  - [x] `origin_node_id`, `leaf_node_type`, and `ancestor_path`.
  - [ ] For cell/list-item hits, include immediate parent context (`table`/`clause` heading).

- [x] Add citation format templates.
  - [x] Human format: `ISO 26262-<part>:2018, <ref>, PDF pages <start>-<end>`.
  - [x] Machine format (JSON object for tool chains).
  - [x] Ensure machine format includes `query`, `rank`, `chunk_id`, `origin_node_id`, and lineage fields for traceability.

- [ ] Add optional open-at-page helper behavior.
  - [ ] Emit deterministic open pointer command text for local viewer integration.
  - [ ] Keep helper output local and non-networked.

## Phase 5 - Build coding-standard traceability outputs

- [ ] Git checkpoint for Phase 5.
  - [ ] Active branch: `main`.
  - [ ] Keep scope to ISO-to-rule mapping, enforcement mapping, and traceability export.
  - [ ] Create a Conventional Commit checkpoint when baseline traceability matrix is generated and reviewable.

- [ ] Create ISO-to-rule traceability matrix.
  - [ ] Map each P0/P1 reference to a coding-standard rule family.
  - [ ] Link each mapping to enforcement method(s).
  - [ ] Link each mapping to evidence artifact expectations.
  - [ ] Link each mapping to responsible lifecycle phase.

- [ ] Complete core mapping coverage from Part 6.
  - [ ] Table 1 topics to coding-standard chapters:
    - [ ] Low complexity.
    - [ ] Language subsets.
    - [ ] Strong typing.
    - [ ] Defensive implementation techniques.
    - [ ] Well-trusted design principles.
    - [ ] Unambiguous graphical representation (if model-based).
    - [ ] Style guides.
    - [ ] Naming conventions.
    - [ ] Concurrency aspects.
  - [ ] Table 6 principles to specific language-level "shall/shall not" rules.

- [ ] Complete enforcement mapping from Part 6 and Part 8.
  - [ ] Unit/integration verification methods to rule compliance checks.
  - [ ] Coverage requirements to coding pattern constraints and tests.
  - [ ] Tool confidence expectations to static analysis/tooling policy.

- [ ] Complete safety-case linkage from Part 2 and Part 9.
  - [ ] Safety plan hooks for coding-standard adoption and control.
  - [ ] Safety case hooks for coding-standard compliance evidence.
  - [ ] ASIL decomposition and dependent-failure concerns to interference/concurrency rules.

- [x] Export mandatory traceability manifest.
  - [x] File path: `.cache/iso26262/manifests/traceability_matrix.csv`.
  - [x] Include columns: `iso_ref`, `rule_id`, `verification_method`, `evidence_artifact`, `owner`, `status`.

## Phase 6 - Validation and quality loop

- [ ] Git checkpoint for Phase 6.
  - [x] Active branch: `main`.
  - [ ] Keep scope to gold-set checks, query quality checks, and quality reporting.
  - [ ] Create a Conventional Commit checkpoint when quality report reflects current pass/fail status and blockers.

- [ ] Define and maintain a gold reference set.
  - [x] Include known-sensitive references (for example: Table 1, Table 6, 8.4.5, 9.4.2, Annex D).
  - [x] Include at least one target from each priority band (P0-P3).
  - [x] Persist expected results snapshot in `.cache/iso26262/manifests/gold_set_expected_results.json`.
  - [x] Include expected keys per gold item: `doc_id`, `ref`, `expected_page_pattern`, `must_match_terms`.
  - [x] Add hierarchy expectation keys where applicable: `expected_node_type`, `expected_parent_ref`, `expected_min_rows`, `expected_min_cols`, `expected_min_list_items`.
  - [ ] Treat gold-set snapshot updates as controlled changes recorded in `decisions_log.jsonl`.

- [x] Run extraction quality checks each ingest run.
  - [x] Confirm each gold reference is retrievable.
  - [x] Confirm citation page ranges are visually correct.
  - [x] Confirm table chunks are present and readable.
  - [x] Confirm key tables are represented as table->row->cell hierarchy (or explicitly marked fallback).
  - [x] Confirm key clauses with bullets are represented as list->list_item hierarchy.
  - [x] Confirm every chunk has a valid `origin_node_id` and lineage path.
  - [x] Confirm no duplicate or conflicting reference IDs.

- [ ] Run query quality checks.
  - [x] Verify exact reference queries return exact top results.
  - [x] Verify keyword queries return relevant clauses/tables.
  - [x] Verify table-detail queries return row/cell descendants in deterministic order.
  - [x] Verify requirement-atom/list-item queries preserve parent clause context.
  - [x] Verify citation fields are never null for returned hits.
  - [x] Verify repeated identical queries return stable ordering.
  - [ ] Verify `query --json` output validates against expected schema.
  - [ ] Track local query latency for top-k retrieval and record baseline metrics.

- [ ] Emit mandatory quality report.
  - [x] File path: `.cache/iso26262/manifests/extraction_quality_report.json`.
  - [x] Include pass/fail by check.
  - [x] Include hierarchy coverage metrics by node type.
  - [ ] Include table/list fallback counts and impacted references.
  - [x] Include unresolved parser/table/OCR issues.
  - [x] Include recommended parser adjustments for next run.

## Phase 7 - Execution order and milestones

- [ ] Git checkpoint for Phase 7.
  - [x] Active branch: `main`.
  - [ ] Keep scope to milestone definitions, sequencing, and execution readiness notes.
  - [ ] Create a Conventional Commit checkpoint when milestone criteria align with implemented capabilities.

- [x] Milestone A: target register complete.
  - [x] `target_sections.json` and `target_sections.csv` generated.
  - [x] P0-P3 references reviewed for completeness.
  - [x] Phase 1 commit checkpoint recorded on `main`.

- [x] Milestone B: ingestion baseline complete.
  - [x] DB created and populated from local PDFs.
  - [x] Hierarchical nodes (`table_row`, `table_cell`, `list_item`) persisted for covered parts.
  - [x] Mandatory ingest manifest generated.
  - [x] Phase 2 and Phase 3 commit checkpoints recorded on `main`.

- [x] Milestone C: citation query baseline complete.
  - [x] Clause/table reference queries returning citation-ready results.
  - [x] Table-detail queries can return row/cell context for key tables.
  - [x] Keyword queries returning snippets with citations.
  - [x] Phase 4 commit checkpoint recorded on `main`.

- [ ] Milestone D: traceability baseline complete.
  - [x] P0/P1 fully mapped to coding rules and evidence.
  - [x] P2/P3 mapped to governance and safety-case hooks.
  - [ ] Phase 5 commit checkpoint recorded on `main`.

- [x] Milestone E: quality gate complete.
  - [x] Gold-set checks pass.
  - [x] Hierarchy checks pass for required table/list references or are explicitly flagged as fallback.
  - [x] Quality report generated with no critical blockers.
  - [x] Phase 6 and Phase 7 commit checkpoints recorded on `main`.

## Phase 8 - Deterministic runbook and crash recovery protocol

- [ ] Git checkpoint for Phase 8.
  - [ ] Active branch: `main`.
  - [ ] Keep scope to runbook determinism, restart controls, and rebuild protocol.
  - [ ] Create a Conventional Commit checkpoint when restart behavior is explicit and operationally testable.

- [x] Maintain deterministic runbook steps with fixed step IDs.
  - [x] `R00`: Sync with base branch (`main`) and ensure `main` is checked out for mainline mode.
  - [x] `R01`: Validate config path (`printenv OPENCODE_CONFIG_DIR`) and execution paths.
  - [x] `R02`: Ensure mandatory directories exist (`.cache/iso26262/`, `.cache/iso26262/manifests/`).
  - [x] `R03`: Initialize or load `run_state.json` and assign `active_run_id`.
  - [x] `R04`: Build or refresh `target_sections.json` and `target_sections.csv` (`iso26262 inventory`).
  - [x] `R05`: Execute ingest pipeline and emit `ingest_run_<timestamp>.json` (`iso26262 ingest`).
  - [x] `R06`: Execute citation and hierarchy validation against gold set (`iso26262 validate`).
  - [x] `R07`: Build `traceability_matrix.csv`.
  - [x] `R08`: Emit `extraction_quality_report.json` and set run status to `completed`.
  - [x] `R09`: Create or verify phase commit checkpoint and record commit hash in `run_state.json`.
  - [x] Persist command-line invocation used for each runbook step in manifests.

- [x] Define exact restart behavior after crash, compaction, or session reset.
  - [x] If `run_state.status` is `running`, treat previous session as interrupted and resume from `current_step`.
  - [x] If `run_state.status` is `failed`, resume from `failed_step` after logging mitigation in `decisions_log.jsonl`.
  - [x] If `run_state.status` is `blocked`, resolve compatibility issue before any further writes.
  - [x] If current branch differs from `run_state.active_branch`, switch to expected branch before resuming.
  - [x] For mainline mode, ensure `run_state.active_branch` is `main` before continuing.
  - [x] If DB schema or source hash set changed, create new `active_run_id` and preserve prior artifacts.
  - [x] Never delete previous manifests; append new run artifacts for auditability.

- [x] Define controlled rebuild protocol (only when resume is unsafe).
  - [x] Archive current DB as `iso26262_index.<timestamp>.sqlite` before rebuild.
  - [x] Create new ingest run manifest documenting rebuild reason.
  - [x] Re-run gold-set validation before replacing run status with `completed`.

## Phase 9 - Commit strategy and incremental delivery

- [ ] Git checkpoint for Phase 9.
  - [ ] Active branch: `main`.
  - [ ] Keep scope to commit policy, mainline execution policy, and commit hygiene requirements.
  - [ ] Create a Conventional Commit checkpoint when commit governance is documented and actionable.

- [x] Enforce Conventional Commits for all repository changes.
  - [x] Use required format: `type(scope): short summary`.
  - [x] Restrict commit types to `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `perf`, `build`, `ci`.
  - [x] Keep commit messages concise and purpose-driven.

- [ ] Keep commits phase-oriented, small, and reversible.
  - [x] One concern per commit (no mixed parser, query, and docs updates in one commit).
  - [ ] Ensure each commit can be reverted independently.
  - [x] Keep milestone progress visible through commit boundaries.

- [ ] Use a standard phase-aligned commit sequence for this plan.
  - [ ] `docs(agents): enforce conventional commit and phased commit policy`.
  - [ ] `chore(rust): bootstrap cli project and pin toolchain`.
  - [ ] `feat(manifests): scaffold run-state, inventory, and quality manifests`.
  - [ ] `feat(db): add sqlite schema and docs catalog initialization`.
  - [ ] `feat(model): add hierarchical node model for tables and list items`.
  - [ ] `feat(ingest): implement extraction, normalization, and chunk persistence`.
  - [ ] `feat(query): implement citation query engine and json output`.
  - [ ] `feat(validate): implement gold-set checks and quality reporting`.
  - [ ] `docs(traceability): finalize mapping workflow and execution runbook`.

- [ ] Add commit checkpoint metadata template for phase consistency.
  - [ ] Commit subject template: `type(scope): phase <n> - <short concern>`.
  - [ ] Commit message body should include: `phase_id`, `run_id`, key manifest paths, validation status.
  - [ ] Record each phase checkpoint commit hash in `run_state.json` and `decisions_log.jsonl`.

- [ ] Apply commit hygiene checks before each commit.
  - [x] Confirm no licensed artifacts from `.cache/` are staged.
  - [ ] Confirm staged changes match exactly one phase concern.
  - [ ] Confirm relevant local checks pass for changed scope.
  - [ ] Update `run_state.json` and `decisions_log.jsonl` before milestone commits.
  - [x] Confirm active branch is `main` for initial execution mode.
  - [ ] Confirm phase checkpoint commit hash is recorded after each milestone commit.
  - [x] Confirm no `println!` / `eprintln!` diagnostics exist in production CLI code paths.

- [x] Deferred items with rationale (Phase 9).
  - [x] Historical bootstrap commit sequence checklist is deferred because bootstrap phases are already complete on `main`.
  - [x] Commit-message body template/checkpoint-hash automation is deferred to the final documentation/governance cleanup pass.

## Scope guardrails and non-goals

- [x] Keep this effort narrowly focused on coding-standard extraction readiness.
  - [x] No cloud upload, remote indexing, or external sharing of extracted corpus.
  - [x] No expansion beyond P0-P3 targets without explicit decision-log entry.
  - [x] No semantic embedding pipeline until FTS baseline and citation quality pass consistently.
  - [x] No safety-case claims without linked traceability and evidence artifacts.
  - [x] Do not treat flattened table/list text as final quality for P0/P1 references unless explicitly waived in decision log.
  - [x] Do not mirror config-only AGENTS/plan documents into the implementation repository unless explicitly requested.

## Definition of done

- [x] All mandatory manifests are present under `.cache/iso26262/manifests/`.
- [x] `run_state.json` and `decisions_log.jsonl` are complete and reflect the final run history.
- [x] `gold_set_expected_results.json` exists and matches the validated gold reference set.
- [x] P0 and P1 references are fully indexed, queryable, and citation-validated.
- [x] P2 and P3 references are indexed and connected in the traceability matrix.
- [x] Query engine returns citations for every result without exceptions.
- [x] Rust CLI subcommands (`inventory`, `ingest`, `query`, `validate`, `status`) execute end-to-end on local corpus.
- [ ] `query --json` output is stable, citation-complete, and schema-valid.
- [x] Key tables (at minimum Table 1, Table 6, Table 7, Table 10) are represented as table->row->cell hierarchy or explicitly flagged fallback.
- [x] Key bullet/shall statements are represented as list_item/requirement_atom nodes with parent clause linkage.
- [ ] Every returned chunk has valid lineage fields (`origin_node_id`, `leaf_node_type`, `ancestor_path`).
- [x] Traceability matrix links ISO references to coding rules and verification evidence.
- [x] Deterministic runbook steps (R00-R09) have been executed or explicitly marked with rationale.
- [x] Commit history on `main` follows Conventional Commit format and phase-aligned granularity.
- [x] `run_state.json` contains current `base_branch`, `active_branch`, `commit_mode`, and `last_commit` metadata.
- [ ] Each completed phase has at least one recorded checkpoint commit hash.
- [x] No licensed `.cache/` artifacts are present in tracked git changes.
- [x] Local-only licensing boundary has been respected throughout execution.
