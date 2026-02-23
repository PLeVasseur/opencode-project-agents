# Hierarchy and Citation Model Design

## Purpose

This document is the implementation blueprint for marker-first citation extraction.

It complements `plans/hierarchy-parsing-quality-checklist.md`:

- the checklist defines pass/fail gates,
- this design defines data contracts, parsing behavior, and integration steps to pass those gates.

## Scope

- Build a deterministic hierarchy model for ISO 26262 content extraction.
- Support citation anchors that prioritize explicit source markers.
- Integrate section, clause, paragraph, list, table, and note segmentation.
- Preserve lineage and traceability for retrieval and validation.

## Constraints

- Work only inside `$OPENCODE_CONFIG_DIR` and `.`.
- Keep licensed artifacts local in `.cache/iso26262/`.
- Do not commit extracted licensed text or local DB artifacts.
- Use small Conventional Commits on `main`.

## Mainline Workflow and Commit Rules

- Execute integration work directly on `main` (mainline-first).
- Do not create feature branches or PR flow unless explicitly requested later.
- Use Conventional Commit format exactly: `type(scope): short summary`.
- Keep one concern per commit (schema, parser, query, validate, tests).
- Do not mix planning-doc updates with implementation-code commits.
- Keep config-only planning artifacts in `$OPENCODE_CONFIG_DIR`.

## Terminology (normative for implementation)

- `section_heading`: top-level heading with integer ref and title, for example `9 Software unit verification`.
- `clause`: numbered heading within a section that contains a decimal point, for example `9.1 Objectives`.
- `subclause`: deeper dotted heading, for example `9.4.2 Verification specification`.
- `paragraph`: prose unit under section/clause/subclause/note/list item, formed by wrapped-line merge rules.
- `marker`: explicit source label such as `a)`, `1a`, `NOTE 2`, or dash bullet.
- `list_item`: marker-bearing unit in an ordered or unordered list.
- `table_row` and `table_cell`: structural children of a table.
- `note_item`: item inside NOTE content when NOTE text itself contains list structure.
- `requirement_atom`: semantic statement candidate extracted from paragraph/list content (analysis layer only).

## Design Principles

- Marker-first citation policy: explicit markers are primary anchors.
- Paragraph fallback policy: paragraph index is used only when marker does not exist.
- Determinism first: same input produces stable order and IDs.
- Auditability: every citation must be traceable to a node with page, ref, and source hash.
- Graceful degradation: use richer extraction when available, fallback cleanly when not.

## Extraction Inputs and Priority

Use multiple extraction streams and reconcile them by confidence:

1. `pdftohtml -xml` (preferred)
   - outline (`<item>`) for section/clause discovery,
   - per-text box coordinates (`top`, `left`, `width`, `height`) for paragraph and marker grouping,
   - font information for heading confidence.
2. `pdftotext -tsv` (secondary)
   - word-level boxes when XML grouping is insufficient.
3. `pdftotext -layout` (secondary)
   - line rendering fallback for table and paragraph heuristics.
4. `pdftotext` plain output (last resort)
   - text-only extraction for content salvage.

Per-PDF strategy hints are recorded in local manifest `pdf_structure_profile.json`.

## Canonical Hierarchy Model

### Node Types

Required node types:

- `document`
- `section_heading`
- `clause`
- `subclause`
- `paragraph`
- `list`
- `list_item`
- `table`
- `table_row`
- `table_cell`
- `note`
- `note_item`
- `annex`
- `requirement_atom` (optional overlay)

### Parent Rules

- `document` has no parent.
- `section_heading` parent is `document`.
- `clause` parent is `section_heading` or `document` when section heading is missing.
- `subclause` parent is `clause` or another `subclause`.
- `paragraph` parent is one of `section_heading`, `clause`, `subclause`, `note`, `list_item`, `annex`.
- `list` parent is one of `paragraph`, `clause`, `subclause`, `note`, `annex`.
- `list_item` parent is `list`.
- `table` parent is one of `clause`, `subclause`, `annex`.
- `table_row` parent is `table`.
- `table_cell` parent is `table_row`.
- `note` parent is one of `clause`, `subclause`, `table`, `annex`.
- `note_item` parent is `note`.
- `requirement_atom` parent is one of `paragraph`, `list_item`, `note_item`.

### Node Fields

Minimum node fields:

- `node_id` (stable deterministic key)
- `doc_id`
- `node_type`
- `ref` (source ref when applicable)
- `title` (heading text)
- `text` (content body)
- `parent_node_id`
- `order_index` (stable order among siblings)
- `page_pdf_start`, `page_pdf_end`
- `source_hash`
- `anchor_type`
- `anchor_label_raw`
- `anchor_label_norm`
- `anchor_order`
- `citation_anchor_id`
- `lineage_depth`

## Citation Anchor Model (Marker-First)

### Anchor Types

- `marker`: explicit marker in source, for example `a)`, `1a`, `NOTE 2`.
- `paragraph`: synthetic paragraph index fallback.
- `table_row`: row-level table citation.
- `table_cell`: cell-level table citation when needed.
- `note`: note-level citation.
- `clause`: heading-level citation where no finer anchor exists.

### Anchor Normalization

- Keep exact marker in `anchor_label_raw`.
- Normalize in `anchor_label_norm`:
  - strip trailing punctuation (`)` `.` `:`),
  - collapse whitespace,
  - uppercase prefix keywords (`NOTE`, `EXAMPLE`) while preserving numeric payload,
  - preserve alphanumeric markers (`1a`, `3b`).

### Citation Synthesis

Rule order:

1. If explicit marker exists, cite marker.
2. Else if paragraph index exists, cite paragraph.
3. Else cite clause/subclause.

Display examples:

- `ISO 26262-6:2018, 9.1(b), PDF p.27`
- `ISO 26262-6:2018, 9.1, para 3, PDF p.27`
- `ISO 26262-6:2018, Table 6 row 1b, PDF p.27`
- `ISO 26262-6:2018, NOTE 2, item 4, PDF p.20`

## Deterministic ID and Ordering Strategy

### Ordering

- `order_index` is assigned from visual reading order:
  - primary sort: page number,
  - secondary sort: top coordinate,
  - tertiary sort: left coordinate,
  - tie-break by extraction stream and text hash.
- Marker-bearing siblings must have strictly increasing `anchor_order`.

### IDs

`node_id` format:

`{doc_id}:node:{node_type}:{parent_ref_or_root}:{stable_suffix}`

Where `stable_suffix` is derived from normalized anchor/ref/order tuple.

`citation_anchor_id` format:

`{doc_id}:{ref_or_parent_ref}:{anchor_type}:{anchor_label_norm_or_para_index}`

## Segmentation Algorithms

### A. Heading and Structural Boundary Detection

- Use XML outline `<item>` as high-confidence heading candidates.
- Reconcile with page text by nearest matching normalized heading string.
- Backfill missing headings with regex fallback:
  - section: `^\s*(\d+)\s+(.+)$`
  - clause/subclause: `^\s*(\d+(?:\.\d+)+)\s+(.+)$`
  - annex: `^\s*Annex\s+([A-Z])\b(.*)$`
- Promote heading confidence by font weight/size when available.

### B. Paragraph Segmentation

- Start from line clusters in visual order.
- Merge wrapped lines when all are true:
  - next line indent is continuation-compatible,
  - vertical gap below paragraph split threshold,
  - no marker or heading start on next line.
- Split paragraph when any are true:
  - next line starts a heading,
  - next line starts marker,
  - vertical gap exceeds threshold,
  - font style change indicates structural boundary.
- Assign paragraph index per parent container.

### C. Marker and List Segmentation

Supported marker classes:

- alpha markers: `a)` `b)`
- numeric markers: `1)` `2)`
- alphanumeric markers: `1a` `1b`
- note markers: `NOTE`, `NOTE 1`, `NOTE 2`
- bullet markers: `-`, `*`, dot-bullet forms, em dash forms

Rules:

- Start new list on first marker under current container.
- Attach continuation lines to previous list item if indentation and vertical-gap rules match.
- Preserve marker raw text and normalized marker label.
- Maintain monotonic `anchor_order` in display order.

### D. Table Segmentation

- Detect table headers by `Table <num>` headings.
- Establish table scope from heading to next structural boundary.
- Build row candidates by y-clustering and line-gap heuristics.
- Build columns from x-clusters and recurring alignment points.
- Merge wrapped cell text with same row and column cluster.
- Record fallback reason whenever table parsing reverts to text-block mode.

### D1. Table Sparse-Row and Overloaded-Row Remediation

Apply this repair pipeline after initial table parse and before node/chunk persistence:

1. Row classification pass
   - classify each row as `healthy`, `sparse`, or `overloaded`,
   - `sparse` row heuristic: marker present with empty or near-empty description payload,
   - `overloaded` row heuristic: row payload contains multiple marker tokens (`1a`, `1b`, etc.) or abnormally long multi-topic description.
2. Orphan-marker row repair
   - for `sparse` marker rows, absorb continuation lines from adjacent rows until next marker boundary,
   - retain deterministic ordering and do not merge across page/section boundaries.
3. Overloaded row split
   - split rows containing multiple marker tokens into one logical row per marker,
   - preserve inherited ASIL rating cells when split confidence is high,
   - flag low-confidence splits for metrics and audit log.
4. Column realignment
   - rebuild x-cluster boundaries using header anchors and recurring symbol columns (`+`, `++`),
   - re-map cell payloads so ratings align to the correct marker row.
5. Post-repair validation
   - enforce marker sequence monotonicity,
   - enforce non-empty description coverage for marker-bearing rows,
   - emit per-table repair counters and confidence scores.

### E. Note Segmentation

- Detect NOTE blocks (`NOTE`, `NOTE n`) and attach to nearest structural parent.
- Parse internal bullets/markers into `note_item` children.
- Keep note text and item-level anchors.

### F. Requirement-Atom Overlay

- Derive from paragraph/list_item/note_item text.
- Preserve parent anchor link to avoid citation drift.
- Do not use requirement_atom as default citation anchor.

## Schema Evolution Plan

## Tables

- `nodes`:
  - add `anchor_type`, `anchor_label_raw`, `anchor_label_norm`, `anchor_order`, `citation_anchor_id`
  - add `order_index`, `lineage_depth`
- `chunks`:
  - keep `origin_node_id`, `leaf_node_type`, `ancestor_path`
  - add `anchor_type`, `anchor_label_raw`, `anchor_label_norm`, `anchor_order`, `citation_anchor_id`

## Indexes

- index on `(doc_id, parent_node_id, order_index)`
- index on `(doc_id, citation_anchor_id)`
- index on `(doc_id, ref, anchor_label_norm)`

## Query Contract Updates

Query output must include:

- lineage fields (`origin_node_id`, `leaf_node_type`, `ancestor_path`, optional ancestor list)
- anchor fields (`anchor_type`, `anchor_label_raw`, `anchor_label_norm`, `anchor_order`, `citation_anchor_id`)
- rendered citation string using marker-first policy

Sorting and ranking:

- exact ref + exact anchor match outranks all
- exact ref + paragraph fallback next
- FTS hits after structured matches

## Validation Design

## Structural Invariants

- no orphan nodes except `document`
- no dangling `parent_node_id`
- `table_row` parent is always `table`
- `table_cell` parent is always `table_row`
- `list_item` parent is always `list`
- marker order monotonic inside each list
- paragraph indices contiguous within parent

## Quality Metrics

- table parse fallback ratio
- list parse fallback ratio
- marker extraction coverage and accuracy
- paragraph fallback citation accuracy
- lineage completeness rate
- table sparse-row ratio
- table overloaded-row ratio
- table marker-sequence coverage
- table description coverage for marker-bearing rows

### Table Row/Cell Fidelity Scorecard

Required scorecard counters (emitted per ingest run):

- `table_sparse_rows_count`
- `table_overloaded_rows_count`
- `table_rows_with_markers_count`
- `table_rows_with_descriptions_count`
- `table_marker_expected_count`
- `table_marker_observed_count`

Derived scorecard metrics:

- `table_sparse_row_ratio = table_sparse_rows_count / table_row_nodes_inserted`
- `table_overloaded_row_ratio = table_overloaded_rows_count / table_row_nodes_inserted`
- `table_marker_sequence_coverage = table_marker_observed_count / table_marker_expected_count`
- `table_description_coverage = table_rows_with_descriptions_count / table_rows_with_markers_count`

Scorecard output location:

- include scorecard metrics in `extraction_quality_report.json` under a dedicated table-quality block,
- include raw counters in `ingest_run_*.json` for trend tracking.

## Acceptance Thresholds

Align with checklist thresholds; add:

- marker extraction coverage for marker-bearing gold refs `>= 0.95`
- marker citation accuracy for marker-bearing gold refs `>= 0.90`
- paragraph fallback citation accuracy `>= 0.90`
- table sparse-row ratio `<= 0.20`
- table overloaded-row ratio `<= 0.10`
- table marker-sequence coverage `>= 0.90`
- table description coverage `>= 0.90`

## Gold Set Expansion Plan

- Include mixed anchor types across Part 6 first:
  - marker-bearing clauses (`a)`, `b)`, `NOTE n`)
  - table rows (`1a`, `1b`, etc.)
  - paragraph-only references where markers are absent
- For each gold entry, store expected:
  - `expected_parent_ref`
  - `expected_anchor_type`
  - `expected_marker_label` or `expected_paragraph_index`
  - optional minimum table/list structure expectations

## Implementation Phases (execution checklist)

### Phase 0 - Baseline and Profiling

- [ ] Generate/refresh `pdf_structure_profile.json` for all target PDFs.
- [x] Capture baseline ingest/query/validate metrics for Part 6.

### Phase 1 - Data Model and Migration

- [x] Add anchor fields to model structs and DB schema.
- [x] Add indexes for anchor-oriented query paths.
- [x] Preserve backward compatibility with existing lineage fields.

### Phase 2 - Section and Clause Integration

- [x] Integrate XML outline into heading detection.
- [x] Add `section_heading` nodes and parent mapping.
- [x] Stabilize clause/subclause relationships.

### Phase 3 - Paragraph and Marker Parsing

- [x] Implement line-group paragraph segmentation.
- [x] Implement marker grammar and normalization.
- [ ] Implement list and note item extraction with continuation handling.

### Phase 4 - Table Reconstruction Hardening

- [ ] Improve row and cell grouping using coordinate clusters.
- [x] Reduce one-cell-row noise for wrapped table content.
- [x] Implement sparse-row and overloaded-row repair passes.
- [ ] Add header-anchored column realignment for ASIL-style tables.
- [x] Emit scorecard counters for sparse/overloaded/marker/description metrics.
- [x] Preserve deterministic row and cell ordering.

### Phase 5 - Query and Citation Formatting

- [x] Expose anchor fields in query output.
- [x] Implement marker-first citation rendering.
- [x] Add query ranking preference for exact anchor matches.

### Phase 6 - Validation and Gold Set

- [x] Extend gold set with anchor expectations.
- [x] Add validation checks for marker coverage/accuracy.
- [x] Ensure `Q-009` and `Q-010` pass with new model.

### Phase 7 - Regression and Determinism

- [x] Add unit tests for segmentation and marker normalization.
- [x] Add integration tests for representative Part 6 pages.
- [x] Verify idempotence across repeated ingest runs.

## Commit Checkpoints on `main`

This sequence is the default execution plan. Each checkpoint should be committed only after its gate passes.

### C1 - Schema baseline

- Commit: `feat(schema): add citation-anchor fields to nodes and chunks`
- Scope:
  - model updates for anchor fields,
  - DB schema migration for `nodes` and `chunks`,
  - indexes for anchor retrieval.
- Gate:
  - `cargo check` passes,
  - ingest command runs with schema migration path intact,
  - no loss of existing lineage fields.

### C2 - Section heading integration

- Commit: `feat(ingest): integrate PDF outline for section headings`
- Scope:
  - parse and map outline heading items,
  - emit `section_heading` nodes,
  - attach clauses to section parents when present.
- Gate:
  - representative section headings (for example clause 9 parent heading) are queryable,
  - parent links for section-aware clauses are valid.

### C3 - Paragraph segmentation

- Commit: `feat(ingest): add paragraph segmentation with stable ordering`
- Scope:
  - wrapped-line merge and split heuristics,
  - deterministic paragraph indexing.
- Gate:
  - paragraph nodes created for representative clause pages,
  - paragraph order is contiguous and stable across repeated ingest.

### C4 - Marker, list, and note parsing

- Commit: `feat(ingest): add marker list and note anchor parsing`
- Scope:
  - marker grammar and normalization,
  - list/list_item and note/note_item extraction,
  - `anchor_label_raw`, `anchor_label_norm`, `anchor_order` population.
- Gate:
  - representative list markers (`a`, `b`, `c`, `d`) extracted in correct order,
  - NOTE markers captured and linked to parents.

### C5 - Table reconstruction hardening

- Commit: `fix(ingest): improve table row and cell reconstruction`
- Scope:
  - row clustering and continuation handling,
  - cell boundary improvements,
  - fallback reason classification,
  - sparse-row and overloaded-row repair,
  - table row/cell fidelity scorecard instrumentation.
- Gate:
  - table/list fallback metrics improve versus baseline,
  - row/cell lineage invariants pass,
  - table scorecard thresholds pass.

### C6 - Query anchor output and citation rendering

- Commit: `feat(query): expose anchor metadata and marker-first citations`
- Scope:
  - return anchor fields in query JSON/text,
  - render marker-first citations,
  - ranking preference for exact anchor matches.
- Gate:
  - query output includes anchor contract fields,
  - marker-bearing results render marker-first citation strings.

### C7 - Validation and gold-set anchor checks

- Commit: `feat(validate): add marker coverage and citation accuracy checks`
- Scope:
  - extend gold reference expectations with anchor fields,
  - add marker coverage and citation accuracy checks,
  - retain existing `Q-009` and `Q-010` lineage checks.
- Gate:
  - validate report includes anchor metrics and check results,
  - quality gates can fail with actionable reason codes.

### C8 - Regression and determinism tests

- Commit: `test(ingest): add segmentation and anchor determinism tests`
- Scope:
  - unit tests for heading/paragraph/marker/table segmentation,
  - integration tests for representative Part 6 pages,
  - deterministic ID and ordering checks.
- Gate:
  - `cargo test` passes,
  - ingest idempotence checks pass on repeated runs.

### C9 - Local quality artifacts checkpoint

- Commit: `chore(manifests): refresh local hierarchy quality artifacts`
- Scope:
  - refresh local manifests and run-state evidence,
  - record final quality metrics after gates pass.
- Gate:
  - final gate command bundle passes,
  - artifacts reflect post-change baseline and decisions log updates.

## Commit Gate Command Bundle

Run this bundle at phase boundaries and before the final checkpoint commit:

- `cargo check`
- `cargo run -- ingest --cache-root .cache/iso26262 --target-part 6 --max-pages-per-doc 60`
- `cargo run -- query --cache-root .cache/iso26262 --query "9.1" --part 6 --with-ancestors --with-descendants --json --limit 3`
- `cargo run -- query --cache-root .cache/iso26262 --query "Table 3" --part 6 --with-ancestors --with-descendants --json --limit 1`
- `cargo run -- validate --cache-root .cache/iso26262`

## Test Matrix (minimum)

- Part 6, page with marker list under clause (`9.1` style)
- Part 6, page with table row labels (`Table 6` style)
- Part 6, page with NOTE and dash bullets (`NOTE 2` style)
- One tagged PDF part and one non-tagged part for fallback behavior

## Risks and Mitigations

- Risk: mixed extraction order causes marker shuffle
  - Mitigation: coordinate-based ordering with deterministic tie-breaks
- Risk: heading false positives from table rows
  - Mitigation: heading confidence scoring using outline and font cues
- Risk: table parsing over-fragments rows
  - Mitigation: y-cluster merge thresholds and continuation rules
- Risk: non-tagged PDFs degrade structure quality
  - Mitigation: fallback strategy profile and explicit quality metrics per part

## Deliverables

- Updated hierarchy-aware schema and model contracts
- Marker-first citation output in query responses
- Expanded validation and gold set coverage
- Updated local manifests showing quality and determinism improvements

## Completion Criteria

This design is considered implemented when:

- all checklist DoD criteria pass,
- marker-first citations are stable for representative references,
- table/list/paragraph segmentation quality meets thresholds,
- and repeated ingestion yields stable anchor IDs and lineage.
