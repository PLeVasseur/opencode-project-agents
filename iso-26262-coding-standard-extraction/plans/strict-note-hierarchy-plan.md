# Strict Note/Note_Item Hierarchy Plan

## Intent

- [x] Implement strict hierarchy and reference semantics for informative note content.
- [x] Stop treating NOTE markers as generic `list_item` units.
- [x] Keep marker-first citation behavior while making note lineage explicit and auditable.

## Locked design decisions

- [x] Use strict node types for notes: `note` and `note_item`.
- [x] Use strict note references immediately: `<parent_ref> note <n>` (not `<parent_ref> item <n>`).
- [x] Keep marker-first citation rendering for notes (`NOTE`, `NOTE 1`, ...).
- [x] Remove compatibility aliasing in this workstream (`--node-type list_item` must not return `note_item`).

## Scope

- [x] Parser and ingest lineage updates (`src/commands/ingest.rs`).
- [x] Query contract updates for strict retrieval semantics (`src/commands/query.rs`).
- [x] Validation and structural invariant updates (`src/commands/validate.rs`).
- [x] Gold/smoke artifact updates under `.cache/iso26262/manifests/` and `scripts/`.

## Out of scope

- [ ] Retrieval ranking redesign unrelated to strict note typing.
- [ ] Non-note parser refactors except those required to keep gates passing.

## Phase 0 - Baseline and guardrails

- [ ] Capture baseline manifests before edits:
  - [ ] latest `ingest_run_*.json`
  - [ ] `gold_set_expected_results.json`
  - [ ] `extraction_quality_report.json`
- [ ] Record baseline query examples for current NOTE references and citations.
- [ ] Add a decisions entry documenting strict cutover rationale and expected blast radius.

## Phase 1 - Data model and node taxonomy

- [x] Extend `NodeType` enum with `Note` and `NoteItem`.
- [x] Ensure `as_str()` returns stable values: `note`, `note_item`.
- [x] Add ingest counters for new node types in `IngestCounts`/`ChunkInsertStats`:
  - [x] `note_nodes_inserted`
  - [x] `note_item_nodes_inserted`
- [x] Preserve deterministic ordering using existing `order_index` contract.

## Phase 2 - Parser split for note vs list

- [x] Split marker parsing into two streams:
  - [x] NOTE markers (`NOTE`, `NOTE <n>`) -> note stream.
  - [x] Non-NOTE markers (`a)`, `1a`, `-`, `*`, `•`, ...) -> list stream.
- [x] Add/adjust parser draft structs as needed (for note entries and labels).
- [x] Build strict note lineage under clause/subclause/annex:
  - [x] `clause/subclause/annex -> note -> note_item`.
- [x] Keep existing list lineage for non-note markers:
  - [x] `clause/subclause/annex -> list -> list_item`.
- [x] Keep paragraph segmentation compatible with the strict split so NOTE starts a note block, not a list item.

## Phase 3 - Strict reference and anchor contract

- [x] Change note item reference format to strict form:
  - [x] `<parent_ref> note <n>`.
- [x] Keep `anchor_type = marker` and `anchor_label_norm = NOTE|NOTE <n>` for note items.
- [x] Add explicit parent reference context in query output:
  - [x] `parent_ref` on each result when origin lineage is available.
- [x] Ensure `citation_anchor_id` remains deterministic for note units.

## Phase 4 - Query behavior (strict cutover)

- [x] Add strict query filtering support for `--node-type note` and `--node-type note_item`.
- [x] Ensure `--node-type list_item` returns only true list items.
- [x] Update exact and node match paths so strict note references rank correctly.
- [x] Keep citation rendering marker-first for note markers.
- [x] Confirm descendants/ancestors include note lineage where requested.

## Phase 5 - Validation and structural invariants

- [x] Add structural SQL invariants for note hierarchy:
  - [x] `note_item` parent must be `note`.
  - [x] `note` parent must be `clause`, `subclause`, or `annex`.
  - [x] no dangling note/note_item parent pointers.
- [x] Add/extend hierarchy checks so strict note references validate against `expected_node_type = note_item`.
- [x] Keep existing table/list/paragraph invariants green after strict note split.

## Phase 6 - Gold and smoke migration (same pass)

- [x] Update NOTE-related gold references to strict node and reference semantics:
  - [x] `expected_node_type: note_item`.
  - [x] `ref: <parent_ref> note <n>`.
  - [x] `expected_anchor_type: marker` with NOTE marker labels preserved.
- [x] Add at least one explicit `note`-node gold reference for parent/container checks.
- [x] Update smoke checks:
  - [x] add strict `--node-type note_item` query assertion.
  - [x] ensure NOTE query no longer depends on `--node-type list_item`.

## Phase 7 - Tests and determinism

- [x] Add parser unit tests:
  - [x] NOTE marker classification into note stream.
  - [x] non-NOTE marker classification into list stream.
  - [ ] strict note reference generation (`note <n>`).
- [x] Add validation tests (or focused command assertions) for note invariants.
- [x] Run deterministic gate sequence:
  - [x] `cargo check`
  - [x] `cargo test`
  - [x] `scripts/smoke_part6.sh`
  - [x] `cargo run -- validate --cache-root .cache/iso26262`

## Mainline commit checkpoints (required)

- [ ] Execute directly on `main` unless branch/PR mode is explicitly requested.
- [ ] Use Conventional Commit format `type(scope): short summary` for every checkpoint commit.
- [ ] Keep one concern per commit (do not mix parser/query/validation/gold migration concerns).
- [ ] Commit checkpoint sequence (phase-aligned):
  - [ ] `refactor(ingest): add note and note_item taxonomy`
    - [ ] includes Phase 1 updates only (node types, counters, deterministic ordering wiring).
  - [ ] `feat(ingest): split NOTE markers into strict note hierarchy`
    - [ ] includes Phase 2 updates only (NOTE stream split, `note -> note_item` lineage, strict refs).
  - [ ] `feat(query): enforce strict note retrieval semantics`
    - [ ] includes Phase 3-4 updates only (`parent_ref`, strict node-type behavior, citation consistency).
  - [ ] `feat(validate): add strict note lineage invariants`
    - [ ] includes Phase 5 updates only (note parent checks, dangling checks, hierarchy assertions).
  - [ ] `test(gold): migrate NOTE gold expectations to strict note_item`
    - [ ] includes Phase 6 gold-manifest updates only.
  - [ ] `test(smoke): migrate NOTE smoke assertions to note_item`
    - [ ] includes Phase 6 smoke-script updates only.
  - [ ] `test(parser): add strict note classification regressions`
    - [ ] includes Phase 7 parser/validation tests only.
- [ ] Before each checkpoint commit, run at least `cargo check` and relevant focused tests for that phase.
- [ ] Before final sign-off commit, run full gate bundle:
  - [ ] `cargo check`
  - [ ] `cargo test`
  - [ ] `scripts/smoke_part6.sh`
  - [ ] `cargo run -- validate --cache-root .cache/iso26262`

## Exit criteria

- [x] All NOTE-derived units are stored as `note`/`note_item` (no NOTE rows as `list_item`).
- [x] NOTE references are strict (`<parent_ref> note <n>`) in query and gold artifacts.
- [x] Structural invariant checks pass for note lineage and dangling-parent checks.
- [x] Validation report remains green with updated gold expectations.
- [x] Smoke script passes using strict note queries.

## Risks and mitigations

- [ ] Risk: strict reference cutover breaks existing scripts and gold rows.
  - [ ] Mitigation: migrate gold + smoke in the same change set as parser/query.
- [ ] Risk: ambiguous NOTE block boundaries in noisy OCR/text sections.
  - [ ] Mitigation: add deterministic boundary heuristics and regression tests on known pages.
- [ ] Risk: overlap between note and list markers in annex-heavy content.
  - [ ] Mitigation: enforce exclusive NOTE classification before list classification.
