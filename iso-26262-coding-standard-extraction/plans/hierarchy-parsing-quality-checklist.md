# Hierarchy Parsing and Citation-Anchor Checklist

## Intent

- [x] Establish a strict quality gate for hierarchy extraction that supports reliable citations.
- [x] Integrate table/list/section/paragraph segmentation into one coherent hierarchy model.
- [x] Make citation anchors deterministic and human-auditable for ISO 26262 content.

## Locked decisions (agreed)

- [x] Citation policy is marker-first: use explicit source markers when present (for example `9.1(b)`, `1a`, `NOTE 2`).
- [x] Paragraph numbering is secondary and used when explicit markers are not present.
- [x] `requirement_atom` remains an analysis layer, not the primary citation anchor.

## Scope and constraints

- [x] Work only inside approved roots: `$OPENCODE_CONFIG_DIR` and `.`.
- [x] Keep licensed artifacts local in `.cache/iso26262/`; do not commit extracted text or DB files.
- [x] Keep checkpoints small and reversible via Conventional Commits on `main`.

## Holistic hierarchy integration target

- [x] Adopt one hierarchy that supports citations and retrieval context:
  - [x] `document -> section_heading -> clause/subclause -> paragraph`
  - [x] `clause/subclause -> list -> list_item`
  - [x] `clause/subclause -> table -> table_row -> table_cell`
  - [x] `clause/subclause -> note -> note_item`
  - [x] optional semantic overlay: `paragraph/list_item -> requirement_atom`
- [x] Keep `origin_node_id`, `leaf_node_type`, and `ancestor_path` on chunks as the join contract.
- [x] Add a stable citation-anchor identifier per retrievable unit (`citation_anchor_id`).

## Citation anchor contract (marker-first)

- [x] Define anchor fields in the data model and query output:
  - [x] `anchor_type` (`marker`, `paragraph`, `table_row`, `table_cell`, `note`, `clause`)
  - [x] `anchor_label_raw` (exact label from source, e.g. `b)`)
  - [x] `anchor_label_norm` (normalized value, e.g. `b`)
  - [x] `anchor_order` (deterministic sequence within parent)
  - [x] `parent_ref` (e.g. `9.1`)
  - [x] `citation_display` (e.g. `ISO 26262-6:2018, 9.1(b), PDF p.27`)
- [x] Citation formatting rules:
  - [x] If marker exists, cite marker first.
  - [x] If marker absent, cite paragraph index (`para N`).
  - [x] Include part/year/ref/page in all citations.

## Definition of done (all required)

- [x] Build integrity: `cargo check` passes.
- [x] Runtime integrity: `ingest`, `query`, and `validate` commands complete successfully.
- [x] Validation checks: `Q-009` (lineage) and `Q-010` (hierarchy expectations) both `pass`.
- [x] Structural invariants: required node/parent lineage SQL checks return zero violations.
- [x] Table/list parser thresholds on Part 6 run:
  - [x] `table_raw_fallback_count / table_chunks_inserted <= 0.10`
  - [x] `list_parse_fallback_count / (list_nodes_inserted + list_parse_fallback_count) <= 0.10`
- [x] Table row/cell fidelity scorecard thresholds on Part 6 run:
  - [x] `table_sparse_row_ratio <= 0.20`
  - [x] `table_overloaded_row_ratio <= 0.10`
  - [x] `table_marker_sequence_coverage >= 0.90`
  - [x] `table_description_coverage >= 0.90`
- [x] Marker and paragraph citation quality thresholds:
  - [x] Marker extraction coverage for marker-bearing gold references `>= 0.95`
  - [x] Marker citation accuracy for marker-bearing gold references `>= 0.90`
  - [x] Paragraph fallback citation accuracy for unmarked references `>= 0.90`
- [x] Retrieval confidence: representative reference queries return expected lineage and descendants.
- [x] Regression protection: parser unit/integration tests cover key success and failure patterns.

## Mainline commit checkpoints (required)

- [x] Execute integration work directly on `main` (no branch/PR mode unless explicitly requested).
- [x] Use Conventional Commit format `type(scope): short summary` for every checkpoint.
- [x] Keep one concern per commit and follow the sequence in `plans/hierarchy-citation-model-design.md`:
  - [x] `C1` schema anchor fields and indexes
  - [x] `C2` section-heading integration
  - [x] `C3` paragraph segmentation
  - [x] `C4` marker/list/note parsing
  - [x] `C5` table reconstruction hardening
  - [x] `C6` query anchor output and marker-first citation rendering
  - [x] `C7` validation and gold-set anchor checks
  - [x] `C8` regression and determinism tests
  - [x] `C9` local quality artifact refresh
- [ ] Run the gate command bundle before each checkpoint commit and at final sign-off.

## Table row/cell fidelity scorecard (required)

- [x] Define and emit table quality counters in ingest manifest:
  - [x] `table_sparse_rows_count` (rows with marker but empty/near-empty payload)
  - [x] `table_overloaded_rows_count` (rows containing concatenated payload from multiple markers)
  - [x] `table_rows_with_markers_count` (rows whose first cell matches marker grammar)
  - [x] `table_rows_with_descriptions_count` (marker rows with non-empty description cell)
  - [x] `table_marker_expected_count` and `table_marker_observed_count` (for marker sequence coverage)
- [x] Compute scorecard metrics from counters:
  - [x] `table_sparse_row_ratio = table_sparse_rows_count / table_row_nodes_inserted`
  - [x] `table_overloaded_row_ratio = table_overloaded_rows_count / table_row_nodes_inserted`
  - [x] `table_marker_sequence_coverage = table_marker_observed_count / table_marker_expected_count`
  - [x] `table_description_coverage = table_rows_with_descriptions_count / table_rows_with_markers_count`
- [x] Report scorecard in `extraction_quality_report.json` under a dedicated table-quality section.
- [x] Fail validation when any scorecard threshold in Definition of Done is violated.

## Phase A - PDF structure reconnaissance and baseline

- [ ] Confirm per-PDF structure characteristics and capture evidence:
  - [ ] `pdfinfo` metadata (tagged status, page count, producer)
  - [ ] `pdftohtml -xml` outline availability and heading quality
  - [ ] `pdftotext` ordering behavior on representative pages
- [ ] Create/update a structure profile artifact in `.cache/iso26262/manifests/` (local only):
  - [ ] `pdf_structure_profile.json` with extraction strategy hints by part.
- [x] Run baseline ingest (Part 6 sample):
  - [x] `cargo run -- ingest --cache-root .cache/iso26262 --target-part 6 --max-pages-per-doc 60`
- [x] Record baseline metrics from latest ingest manifest:
  - [x] `table_chunks_inserted`, `table_raw_fallback_count`
  - [x] `list_nodes_inserted`, `list_parse_fallback_count`
  - [x] `table_row_nodes_inserted`, `table_cell_nodes_inserted`
  - [x] `table_sparse_rows_count`, `table_overloaded_rows_count`
  - [x] `table_marker_expected_count`, `table_marker_observed_count`
  - [x] `table_rows_with_markers_count`, `table_rows_with_descriptions_count`
  - [x] paragraph and marker counters (add if missing)
- [x] Capture baseline validation summary:
  - [x] `cargo run -- validate --cache-root .cache/iso26262`
  - [x] persist `passed/failed/pending` and `Q-009/Q-010` before/after comparison.

## Phase B - Data model and schema extension

- [ ] Extend node model for section/paragraph/marker-aware retrieval:
  - [ ] add/confirm node types for section headings, paragraphs, notes, and note items
  - [x] add anchor fields (`anchor_type`, `anchor_label_raw`, `anchor_label_norm`, `anchor_order`, `citation_anchor_id`)
  - [x] preserve deterministic ordering via `order_index`
- [x] Extend chunk model/output:
  - [x] expose citation anchor fields in query responses
  - [x] keep existing lineage fields backward-compatible

## Phase C - Parser integration (holistic)

- [x] Use richer extraction sources where available (XML/outline/coordinates) to improve structure fidelity.
- [x] Section and clause segmentation:
  - [x] capture top-level headings (e.g. `9 Software unit verification`)
  - [x] maintain clause/subclause boundaries and parent mapping
- [x] Paragraph segmentation:
  - [x] merge wrapped lines into paragraph units
  - [x] split paragraphs by vertical spacing/indent and marker transitions
  - [x] keep stable paragraph ordering within clause
- [x] Marker extraction:
  - [x] detect alphanumeric markers (`a)`, `b)`, `1a`, `1b`)
  - [x] detect note markers (`NOTE`, `NOTE 1`, `NOTE 2`)
  - [x] detect dash bullets (`-`, `*`, `•`, em-dash forms)
  - [x] normalize marker labels without losing raw label fidelity
- [ ] Table parsing hardening:
  - [x] remove page furniture/licensing noise
  - [ ] improve row grouping for wrapped table text using coordinate-aware row bands
  - [ ] improve cell splitting for tabs/multi-space/pipes plus x-cluster boundary inference
  - [x] add orphan-marker row repair (attach continuation text to marker row)
  - [x] add overloaded-row split pass when multiple markers are detected in one row payload
  - [ ] add ASIL-style table templates for marker + description + ratings columns
  - [x] preserve deterministic row/cell ordering

## Phase D - Structural invariants and acceptance SQL

- [x] Verify all non-document nodes have valid parents.
- [x] Verify no dangling parent pointers.
- [x] Verify table lineage (`table_row -> table`, `table_cell -> table_row`).
- [x] Verify list lineage (`list_item -> list`, marker order monotonic).
- [x] Verify paragraph/marker lineage (`paragraph -> clause/subclause`, markers tied to correct parent).
- [x] Verify chunk lineage fields populated when expected.

## Phase E - Gold set and validation enrichment

- [x] Extend gold references with hierarchy and anchor expectations:
  - [x] `expected_node_type`
  - [x] `expected_parent_ref`
  - [x] `expected_anchor_type`
  - [x] `expected_marker_label`
  - [x] `expected_paragraph_index`
  - [x] `expected_min_rows`, `expected_min_cols`, `expected_min_list_items`
- [x] Add at least:
  - [x] 10 marker-bearing references (mixed clause/list/note/table)
  - [x] 10 paragraph-only references (no explicit marker)
- [x] Add/extend validation checks for marker coverage and citation accuracy thresholds.

## Phase F - Retrieval and citation acceptance

- [x] Run representative query set (`Table 3`, selected clauses, list-heavy clauses, note-heavy pages).
- [x] For each target, verify:
  - [x] top result anchor matches expected marker or paragraph index
  - [x] `ancestor_nodes` and descendants reflect correct hierarchy
  - [x] citation display uses marker-first policy when marker exists
- [ ] For table-heavy targets (`Table 3`, `Table 6`, `Table 10`), verify:
  - [x] marker rows are individually represented (no large catch-all row)
  - [x] description column is non-empty for marker-bearing rows
  - [ ] ASIL rating cells are distributed across the correct rows
- [x] Confirm citation always includes part/year/reference/page fields.

## Phase G - Regression, determinism, and final gate

- [x] Add tests for:
  - [x] section/clause heading detection
  - [x] paragraph merge/split edge cases
  - [x] marker normalization and ordering
  - [x] table/list parsing under noisy/wrapped inputs
- [x] Run tests and ensure no regressions.
- [x] Verify idempotence by running ingest twice and comparing key counts/anchor stability.
- [x] Re-run full gate sequence:
  - [x] `cargo check`
  - [x] `cargo run -- ingest --cache-root .cache/iso26262 --target-part 6 --max-pages-per-doc 60`
  - [x] `cargo run -- query --cache-root .cache/iso26262 --query "9.1" --part 6 --with-ancestors --with-descendants --json --limit 3`
  - [x] `cargo run -- query --cache-root .cache/iso26262 --query "Table 3" --part 6 --with-ancestors --with-descendants --json --limit 1`
  - [x] `cargo run -- validate --cache-root .cache/iso26262`
- [x] Verify table scorecard metrics are within thresholds and trend positively from baseline.
- [ ] Verify all definition-of-done criteria pass.
- [x] Update local run artifacts (`ingest_run_*.json`, `extraction_quality_report.json`, `decisions_log.jsonl`, `run_state.json`).
- [x] Create focused Conventional Commit(s) for parser + citation-anchor integration.

## Out of scope

- [ ] Broad retrieval ranking redesign unrelated to citation correctness.
- [ ] Storage engine changes unrelated to hierarchy/anchor quality.
- [ ] Scaling to more ISO parts before Part 6 gate passes.
