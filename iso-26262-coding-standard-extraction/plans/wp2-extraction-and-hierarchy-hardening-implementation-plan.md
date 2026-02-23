# WP2 Implementation Plan - Extraction and Hierarchy Hardening

## Objective

- Harden extraction and hierarchy fidelity so query results are citation-reliable under mixed PDF conditions, not only retrieval-complete.
- Close the remaining WP2 scope from the master closure plan: OCR fallback/provenance, normalization hardening, printed-page mapping, long-clause split semantics, nested list semantics, and richer table-cell contracts.
- Preserve WP1 gains (`35/35` target coverage + full-target freshness) while increasing structural trust for guideline authoring.

## Scope

- In scope:
  - extraction backend control and per-page provenance,
  - normalization quality loop (header/footer suppression + conservative dehyphenation),
  - printed-page mapping population and reporting,
  - deterministic long-clause splitting with overlap,
  - nested list semantics and table-cell semantic metadata,
  - stronger ASIL table alignment acceptance and WP2 quality checks.
- Out of scope:
  - query JSON schema/versioning and latency benchmarking (WP3),
  - language-profile synthesis outputs (WP4),
  - traceability evidence materialization and requirement map finalization (WP5).

## Investigation Baseline (Current State)

Source snapshot used for this plan:

- Latest full-target ingest run: `run-20260217T135538Z`.
- Latest quality report: `manifest_version=2`, `status=passed`, `22/22` checks passing.
- WP1 checks are green (`Q-020`, `Q-021`, `Q-022`).

Current extraction/hierarchy baseline metrics:

- Printed-page mapping coverage in `chunks`: `0/613` populated (`page_printed_start/end` currently unused).
- OCR usage: `ocr_page_count=0` with no OCR control flags exposed in CLI.
- Table/list fallback counters in latest ingest manifest:
  - `table_raw_fallback_count=12`
  - `list_parse_fallback_count=46`
- Clause chunk sizing:
  - `547` clause chunks total,
  - `16` clause chunks over `300` words,
  - `1` clause chunk over `900` words,
  - max clause chunk length `1863` words (`ISO26262-2-2018`, ref `5.2`).
- Table row/cell shape quality:
  - `390` table rows total,
  - `280` rows have exactly one cell (`71.79%` one-cell ratio), indicating remaining row/cell grouping weakness.

Current structural constraints observed in code:

- `parse_list_items` creates `depth: 1` only, and depth is not persisted (`depth` currently ignored on insert).
- Nodes/chunks schema does not yet include explicit list/table semantic fields requested by plan:
  - missing list semantics: `list_depth`, `list_marker_style`, `item_index`.
  - missing table-cell semantics: `table_node_id`, `row_idx`, `col_idx`, `is_header`, `row_span`, `col_span`.
- Long-clause split contract (300-900 with overlap, stable `chunk_seq` per ref) is not implemented.

## Gap Register for WP2

## G1 - Extraction backend control and provenance

What remains:

- Ingest uses text-layer extraction only (`pdftotext`) with no optional OCR path.
- Per-page backend provenance is not emitted.

Resolution target:

- Add explicit extraction backend policy and page-level provenance artifacts.

## G2 - Normalization hardening

What remains:

- Normalization is minimal (`trim` + noise-line filter), without repeated header/footer suppression or dehyphenation heuristics.

Resolution target:

- Add deterministic normalization passes and manifest counters for removals/rewrites.

## G3 - Printed-page mapping

What remains:

- `page_printed_start/end` exists in schema but remains unpopulated.

Resolution target:

- Populate printed-page labels when detectable and report coverage/reason codes.

## G4 - Long-clause split semantics

What remains:

- No 300-900 word split with overlap and no per-reference split contract.

Resolution target:

- Enforce deterministic split+overlap contract with contiguous `chunk_seq` by `doc_id+ref`.

## G5 - Nested list semantics

What remains:

- List depth is not parsed/persisted; parent contract is flat (`list_item -> list` only).

Resolution target:

- Parse and persist list depth/marker style/index and support nested lineage.

## G6 - Table-cell semantics and ASIL alignment hardening

What remains:

- Table-cell semantic fields are absent.
- ASIL alignment check is useful but still coarse for column semantics.

Resolution target:

- Add explicit table-cell metadata fields and stricter ASIL row-column validation.

## Workstream Design

## WS-A - OCR and extraction backend policy

Implementation:

- Add ingest flags:
  - `--ocr-mode off|auto|force` (default `off`),
  - `--ocr-lang <lang>` (default `eng`),
  - `--ocr-min-text-chars <n>` (auto mode threshold).
- Add extraction backend abstraction:
  - text-layer backend (current `pdftotext` path),
  - OCR backend (page-level fallback only in `auto` mode).
- Add page-level provenance artifact:
  - `ingest_page_provenance_<run_id>.json` with `doc_id`, `page_pdf`, `backend`, `reason`.
- Extend ingest manifest counts with backend summaries:
  - `text_layer_page_count`, `ocr_page_count`, `empty_page_count`, `ocr_fallback_page_count`.

Code touchpoints:

- `src/cli.rs`
- `src/commands/ingest.rs`
- `src/model.rs`

Exit criteria:

- OCR mode options are available and deterministic.
- Every processed page has backend provenance (`text_layer` or `ocr` or explicit skip reason).

## WS-B - Normalization quality loop

Implementation:

- Add repeating header/footer suppression using frequency heuristics at document level.
- Add conservative line-wrap dehyphenation.
- Add normalization counters in ingest manifest:
  - `header_lines_removed`,
  - `footer_lines_removed`,
  - `dehyphenation_merges`.
- Add safety guards so numbering/table labels are preserved.

Code touchpoints:

- `src/commands/ingest.rs` (normalization pipeline before structure parsing)

Exit criteria:

- Normalization counters are emitted and non-zero where expected.
- Parser quality does not regress on existing WP1/WP2 sample queries.

## WS-C - Printed-page mapping population

Implementation:

- Add printed-page label extraction pass per PDF page.
- Populate `page_printed_start/end` for chunks when mapping is available.
- Add explicit mapping status fields (manifest-level or chunk-level) for non-detectable cases.

Code touchpoints:

- `src/commands/ingest.rs`
- optional manifest struct extension in `src/model.rs`

Exit criteria:

- Printed-page mapping appears in chunk rows where detectable.
- Mapping coverage and non-detectable reasons are reported in artifacts.

## WS-D - Long-clause split + overlap contract

Implementation:

- Split long clause/annex text into semantic sub-chunks:
  - target chunk size: 300-900 words,
  - overlap: 50-100 words,
  - preserve same `doc_id`, `ref`, `origin_node_id`.
- Redefine `chunk_seq` semantics as contiguous sequence per `(doc_id, ref)` within each run.
- Ensure deterministic chunk boundaries across repeated ingest runs.
- Add an explicit Q-025 exemption register for unavoidable oversize chunks:
  - path: `plans/wp2-q025-exemption-register.md`,
  - required fields per exemption: `doc_id`, `ref`, `reason`, `owner`, `expires_after`, `decision_id`,
  - `Q-025` fails if a >900-word chunk is not listed in the register or has an expired exemption.

Code touchpoints:

- `src/commands/ingest.rs` (chunk assembly path)

Exit criteria:

- No clause chunk exceeds 900 words unless explicitly exempted and reported.
- Split references show contiguous `chunk_seq` without gaps.
- Exemption register exists and every active exemption is auditable and time-bounded.

## WS-E - Nested list semantics

Implementation:

- Extend list parser to infer nesting depth using marker transitions + indentation cues.
- Persist list semantics:
  - `list_depth`,
  - `list_marker_style` (`alpha`, `numeric`, `bullet`, `note`, etc.),
  - `item_index` (position within its parent depth).
- Update parent contract to support nested list lineage:
  - allow `list_item` parent to be `list` (depth 1) or `list_item` (depth > 1).
- Update structural invariant checks accordingly.

Code touchpoints:

- `src/commands/ingest.rs`
- `src/commands/validate.rs`

Exit criteria:

- Nested list items are represented with stable depth metadata.
- Structural invariants stay green with nested list parent rules.

## WS-F - Table-cell semantic contract + ASIL template hardening

Implementation:

- Extend node schema for table semantics:
  - `table_node_id`, `row_idx`, `col_idx`,
  - `is_header`, `row_span`, `col_span`.
- Populate these fields for `table_cell` nodes (and optionally `table_row` where useful).
- Improve row/cell grouping for wrapped text using row-band and marker-assisted alignment.
- Add ASIL table template alignment rules for key tables (`Table 3`, `Table 6`, `Table 10`).

Code touchpoints:

- `src/commands/ingest.rs`
- `src/commands/validate.rs`

Exit criteria:

- Table-cell semantic fields are populated for all table-cell nodes.
- Global one-cell row ratio trends down materially from baseline (71.79%) and is used as a directional/regression signal.
- Targeted ASIL table semantics (`Table 3`, `Table 6`, `Table 10`) pass stricter alignment criteria.

## WS-G - Validation expansion for WP2

Implementation:

- Add WP2 checks (`Q-023` to `Q-030`):
  - `Q-023` extraction backend provenance completeness,
  - `Q-024` printed-page mapping coverage/status completeness,
  - `Q-025` long-clause split contract compliance,
  - `Q-026` nested list depth/marker semantics completeness,
  - `Q-027` table-cell semantic field completeness,
  - `Q-028` strict ASIL row-column alignment,
  - `Q-029` normalization effectiveness/non-regression gate,
  - `Q-030` citation parity non-regression for target-linked references.
- Add report blocks:
  - `extraction_fidelity`,
  - `hierarchy_semantics`,
  - `table_semantics`,
  - `citation_parity`.

Code touchpoints:

- `src/commands/validate.rs`

Exit criteria:

- New checks fail appropriately when fidelity contracts are violated.
- Full-target run passes WP1 + WP2 checks.

## WP2 Metric Targets and Citation Parity Strategy

Threshold policy:

- Use a two-stage threshold rollout:
  - Stage A (instrumentation): emit metrics and warnings while parser behavior is stabilized.
  - Stage B (hard gate): convert thresholds below to `failed` outcomes in `validate`.
- Preserve WP1 gates as hard requirements during both stages.

Gate rollout matrix (warn vs fail):

| Check | Stage A mode | Stage B mode | Promotion trigger to Stage B |
|---|---|---|---|
| `Q-023` Extraction provenance | **Fail** on unknown backend pages; warn on backend-specific replay instability | **Fail** on unknown backend pages and backend-specific replay thresholds below target | 2 consecutive full-target runs with `100%` page provenance coverage and replay metrics populated |
| `Q-024` Printed-page mapping | **Fail** on invalid printed ranges/labels; warn on low mapping coverage or detectability anomalies | **Fail** on status coverage, detectable-page mapping, or unexplained detectability collapse below policy | 2 consecutive runs with valid labels, stable detectability behavior, and threshold-compliant mapping |
| `Q-025` Long-clause split | warn on oversize chunks/overlap/sequence issues during splitter tuning | **Fail** on non-exempt oversize chunks, low overlap compliance, or non-contiguous `chunk_seq` | 2 consecutive runs with deterministic split boundaries and zero contract violations |
| `Q-026` Nested list semantics | warn on field completeness and depth-parent violations | **Fail** on missing list semantic fields, depth-parent violations, or high fallback ratio (fixed denominator) | list-depth parser merged, fixtures added, denominator definition locked, and 2 consecutive runs pass |
| `Q-027` Table-cell semantics | **Fail** on invalid span values; warn on completeness and global one-cell ratio | **Fail** on semantic field completeness and targeted table semantic misses; global one-cell ratio remains directional/regression guard | schema fields populated and 2 consecutive runs meet completeness + targeted semantic checks |
| `Q-028` Strict ASIL alignment | current ASIL gate remains **Fail**-capable; stricter thresholds warn | stricter ASIL thresholds become **Fail** conditions (targeted blocker for Table 3/6/10) | stricter thresholds met in 2 consecutive full-target runs for Table 3/6/10 |
| `Q-029` Normalization non-regression | **Fail** on hard regressions; warn on residual leakage/false positives while tuning | **Fail** on normalization thresholds (near-zero global leakage + zero target-linked leakage) | normalization fixtures stable and 2 consecutive runs meet thresholds |
| `Q-030` Citation parity | generate baseline/report; warn on parity deltas while tuning | **Fail** when top-1/top-3/page-range parity is below target (tie-aware equivalence rules) | baseline frozen and 2 consecutive runs satisfy citation parity thresholds |

Stage control location:

- `validate` computes all WP2 metrics in both stages.
- Runbook/scripts decide enforcement mode (`warn` vs `fail`) based on stage flag.
- Recommended flagging approach:
  - `WP2_GATE_STAGE=A` for instrumentation/tuning,
  - `WP2_GATE_STAGE=B` for hard-gate milestone and sign-off.
- Stage setting and effective policy should be written into the quality report for auditability.

Metric interpretation guardrails (avoid gaming and overfitting):

- Primary release blockers: `Q-030` citation parity and targeted ASIL semantics in `Q-028`.
- Secondary structural blockers: provenance integrity, mapping validity, split contract, nested-list and table-cell semantic completeness.
- Directional metric only: global one-cell row ratio; it must never be the sole reason to fail sign-off.
- For `Q-026`, fallback ratio denominator is fixed and reported (`fallback_candidates_failed / fallback_candidates_total`) to prevent metric drift.
- For `Q-030`, top-k parity uses tie-aware equivalence classes (canonical ref + anchor/page identity) to avoid false regressions from harmless rank ties.

Proposed metrics and targets:

| Check | Metric | Baseline | WP2 target (hard gate) |
|---|---|---:|---:|
| `Q-023` | page provenance coverage (`tagged_pages / processed_pages`) | N/A | `100%` |
| `Q-023` | unknown backend pages | N/A | `0` |
| `Q-023` | text-layer replay stability on rerun | N/A | `>=99.9%` |
| `Q-023` | OCR replay stability on rerun | N/A | `>=98.0%` |
| `Q-023` | OCR page ratio | `0` | informational only (not pass/fail by itself) |
| `Q-024` | printed-page mapping status coverage (`mapped + explicit_not_detectable`) | `0/613 mapped` | `100% status coverage` |
| `Q-024` | printed-page detectability rate stability | establish in Stage A | no unexplained drop `>5` percentage points from baseline |
| `Q-024` | printed-page mapping on detectable pages | `0%` | `>=98%` |
| `Q-024` | invalid printed page ranges/labels | N/A | `0` |
| `Q-025` | clause chunks over 900 words | `1` | `0` |
| `Q-025` | max clause chunk words | `1863` | `<=900` (or exemption list) |
| `Q-025` | overlap compliance for split pairs (50-100 words) | N/A | `>=95%` |
| `Q-025` | per-ref `chunk_seq` contiguity | mixed | `100%` |
| `Q-026` | list semantic field completeness (`depth/style/index`) | N/A | `100%` |
| `Q-026` | nested list parent-depth violations | N/A | `0` |
| `Q-026` | list parse fallback ratio (`fallback_candidates_failed / fallback_candidates_total`) | `46/265 = 17.36%` | `<=5%` |
| `Q-027` | table-cell semantic field completeness | N/A | `100%` |
| `Q-027` | invalid span values (`row_span < 1` or `col_span < 1`) | N/A | `0` |
| `Q-027` | header flag completeness on table headers | N/A | `>=98%` |
| `Q-027` | global one-cell table-row ratio | `280/390 = 71.79%` | `<=50%` (directional/regression guard, non-blocking alone) |
| `Q-028` | ASIL rating coverage | current min gate `>=0.60` | `>=0.85` |
| `Q-028` | malformed marker-description ratio | current max gate `<=0.10` | `<=0.05` |
| `Q-028` | outlier cell-count ratio | current max gate `<=0.15` | `<=0.08` |
| `Q-028` | ASIL table one-cell row ratio (`Table 3/6/10`) | N/A | `<=25%` |
| `Q-029` | residual furniture/licensing noise leakage (global) | N/A | `<=0.1%` of chunks |
| `Q-029` | residual furniture/licensing noise leakage (target-linked refs) | N/A | `0` |
| `Q-029` | dehyphenation false-positive rate (fixture-based) | N/A | `<=2%` |
| `Q-029` | WP1/WP2 regression coupling check | N/A | all prior required checks stay `pass` |
| `Q-030` | citation parity top-1 (target-linked set) | establish in Stage A | `>=99%` |
| `Q-030` | citation parity top-3 containment (tie-aware equivalence) | establish in Stage A | `100%` |
| `Q-030` | citation page-range parity | establish in Stage A | `>=99%` |

Citation parity execution approach:

- Build baseline artifact from the last known-good pre-WP2 run:
  - `.cache/iso26262/manifests/citation_parity_baseline.json`
- Produce run-scoped parity report during validate:
  - `.cache/iso26262/manifests/citation_parity_report.json`
- Evaluate parity over target-linked gold references only (`target_id` rows), comparing:
  - canonical reference match,
  - anchor identity (`citation_anchor_id` where present),
  - page range consistency,
  - top-k result ordering tolerance (top-1 strict, top-3 containment) using tie-aware equivalence classes.
- Treat parity regressions as blocker for WP2 sign-off even when structural metrics improve.

Baseline freeze protocol (new sessions):

- Freeze baseline once, immediately before WP2 parser changes begin, from a known-good Stage A run.
- Baseline metadata must include: `run_id`, `generated_at`, `db_schema_version`, `target_linked_count`, and query options used for parity extraction.
- Baseline may only be replaced when all of the following are true:
  - a deliberate quality-policy change was made (not an accidental parser drift),
  - the change is recorded in `decisions_log.jsonl` with rationale,
  - replacement is called out in run notes for the session.
- Keep a baseline checksum in the parity report so accidental edits are detectable.

## WS-H - Runbook, smoke flows, and docs

Implementation:

- Extend refresh runbook usage for WP2 fidelity mode (full-target only).
- Add/update smoke script(s) for WP2 checks, acceptance SQL assertions, and citation parity assertions.
- Add a dependency preflight step (`pdftotext`, `pdftohtml`, `sqlite3`, and `tesseract` when OCR mode is enabled).
- Document operational modes and dependency expectations (OCR backend optional but explicit).

Code touchpoints:

- `scripts/refresh_quality_artifacts.sh`
- `scripts/README.md`
- optional new `scripts/smoke_wp2_fidelity.sh`

Exit criteria:

- Operators can run WP2 gate end-to-end with deterministic commands.

## New Session Bootstrap (WP2)

Use this sequence at the start of a fresh session before touching parser logic:

1. Confirm config context:
   - `printenv OPENCODE_CONFIG_DIR`
2. Run toolchain/dependency preflight:
   - `cargo check`
   - `pdftotext -v`
   - `pdftohtml -v`
   - `sqlite3 --version`
   - `tesseract --version` (only required when testing OCR-enabled modes)
3. Set gate stage explicitly for the session:
   - `WP2_GATE_STAGE=A` for instrumentation/tuning work,
   - `WP2_GATE_STAGE=B` only for sign-off runs.
4. Verify/initialize citation parity baseline:
   - if missing, create `citation_parity_baseline.json` from the current known-good run and log the freeze decision,
   - if present, verify checksum and metadata continuity.
5. Execute one full-target refresh cycle and capture artifacts:
   - `FULL_TARGET_SET=1 TARGET_PARTS="2 6 8 9" scripts/refresh_quality_artifacts.sh`
   - `cargo run -- validate --cache-root .cache/iso26262`
6. Confirm expected startup state before implementation:
   - WP1 checks remain `pass`,
   - WP2 metrics are present in report output,
   - active stage and policy are recorded in the quality report.

## WP2 Tracking Checklist

## M0 - Baseline lock for WP2

- [x] Record baseline metrics from latest full-target run.
- [x] Confirm current schema gaps for list/table semantics and printed-page mapping.
- [x] Confirm current parser gaps (OCR absence, depth not persisted, long-clause split missing).

## M1 - Backend and normalization scaffolding

- [x] Add CLI options and ingestion backend policy scaffolding.
- [x] Add normalization pipeline hooks and counters.
- [x] Add/adjust unit tests for normalization and backend option parsing.

## M2 - Provenance and printed-page mapping

- [x] Emit page-level extraction provenance artifact.
- [x] Populate printed-page mapping fields where detectable.
- [x] Add printed-page mapping status/reason reporting.

## M3 - Long-clause split contract

- [x] Implement split+overlap logic (300-900, overlap 50-100).
- [x] Enforce contiguous per-ref `chunk_seq` semantics.
- [x] Add deterministic split regression tests.

## M4 - Nested list semantics

- [x] Parse nested list depth and marker style.
- [x] Persist list semantics (`list_depth`, `list_marker_style`, `item_index`).
- [x] Update structural invariants for nested list parent contracts.

## M5 - Table-cell semantic fields and alignment hardening

- [x] Add schema fields for table-cell semantics.
- [x] Populate row/column/header/span fields during ingest.
- [x] Improve row/cell grouping and ASIL template alignment quality.

## M6 - Validation and quality report expansion

- [x] Implement `Q-023` to `Q-030` checks.
- [x] Add WP2 report sections (`extraction_fidelity`, `hierarchy_semantics`, `table_semantics`).
- [x] Add `citation_parity` section with baseline-vs-current deltas.
- [x] Add stage-aware enforcement policy (`WP2_GATE_STAGE=A/B`) and include effective stage in report output.
- [x] Encode anti-gaming definitions (fixed denominators, detectability policy, tie-aware parity equivalence) directly in check logic.
- [x] Ensure failed conditions are explicit and actionable.

## M7 - Runbook and smoke gating

- [x] Add WP2 fidelity run mode and smoke checks.
- [x] Update scripts/docs with operator guidance.
- [x] Add dependency preflight checks and failure messaging.
- [x] Add explicit new-session bootstrap procedure to runbook docs.
- [x] Verify quick mode behavior remains suitable for local parser iteration.

## M8 - WP2 sign-off

- [x] Run full-target ingest + validate with WP2 gates.
- [x] Confirm WP1 checks remain green.
- [x] Confirm WP2 checks pass (including citation parity gate).
- [x] Confirm Stage B is active and promotion evidence criteria were met.
- [x] Confirm citation baseline freeze policy was respected (or replacement was formally logged).
- [x] Confirm Q-025 exemption register entries are current, justified, and unexpired.
- [x] Update master closure plan WP2 checklist to completed.
- [x] Append decision-log entry for WP2 closure rationale and impact.

## WP2 Mainline Commit Phasing

Commit policy:

- Commit to `main` (unless explicit branch/PR mode requested).
- Use Conventional Commits (`type(scope): short summary`).
- Keep one concern per commit and run the listed gate before each checkpoint commit.
- Do not commit `.cache/` extracted artifacts.

## C1 - Backend policy and CLI

- [x] Commit: `feat(cli): add ingest extraction backend controls`
- [x] Scope: add OCR/backend flags and plumbing.
- [x] Gate: `cargo check`, CLI help and arg parsing tests.

## C2 - Provenance and normalization counters

- [x] Commit: `feat(ingest): emit page provenance and normalization counters`
- [x] Scope: per-page backend provenance + normalization metrics in manifests.
- [x] Gate: `cargo check`, ingest manifest includes new fields/artifact.

## C3 - Printed-page mapping

- [x] Commit: `feat(ingest): populate printed page mappings for chunks`
- [x] Scope: printed-page mapping extraction + persistence.
- [x] Gate: ingest run shows non-zero/qualified mapping status and no parser regressions.

## C4 - Long-clause split contract

- [x] Commit: `feat(ingest): split long clauses with deterministic overlap`
- [x] Scope: 300-900 split, overlap, per-ref contiguous `chunk_seq`.
- [x] Gate: split determinism tests pass; oversized clause violations reduced to policy target; exemption register enforcement works as specified.

## C5 - Nested list semantics

- [x] Commit: `feat(ingest): add nested list depth and marker semantics`
- [x] Scope: parse/persist depth, marker style, parent linkage updates.
- [x] Gate: list-structure tests pass; invariants updated and green.

## C6 - Table-cell semantic metadata

- [x] Commit: `feat(schema): add table-cell semantic fields and population`
- [x] Scope: row/col/header/span fields + population logic.
- [x] Gate: schema migration safe; field completeness checks pass on sample runs.

## C7 - ASIL alignment hardening

- [x] Commit: `fix(ingest): improve asil table row-column alignment`
- [x] Scope: row grouping and rating-column distribution improvements.
- [x] Gate: ASIL-focused acceptance checks pass with stricter criteria.

## C8 - WP2 validate checks

- [x] Commit: `feat(validate): add wp2 metrics and reporting blocks`
- [x] Scope: implement metric computation for `Q-023`..`Q-030` and add report sections (including citation parity artifacts).
- [x] Gate: validate output includes complete WP2 metric/report payload under Stage A.

## C9 - Stage-aware enforcement policy

- [x] Commit: `feat(validate): add stage-aware wp2 gate enforcement`
- [x] Scope: apply `WP2_GATE_STAGE=A/B` policy to warn/fail behavior, and emit effective policy in report output.
- [x] Gate: validate shows expected Stage A warning behavior and Stage B pass/fail behavior for each new check.

## C10 - Runbook/docs closure

- [x] Commit: `docs(runbook): document wp2 fidelity gate workflow`
- [x] Scope: script/docs updates + operator flow.
- [x] Gate: documented commands execute successfully end-to-end.

## Suggested checkpoint order

1. C1
2. C2
3. C3
4. C4
5. C5
6. C6
7. C7
8. C8
9. C9
10. C10

## Acceptance Gate Bundle (WP2)

Core commands:

- `pdftotext -v && pdftohtml -v && sqlite3 --version`
- `cargo check`
- `cargo test`
- `WP2_GATE_STAGE=A FULL_TARGET_SET=1 TARGET_PARTS="2 6 8 9" scripts/refresh_quality_artifacts.sh`
- `WP2_GATE_STAGE=A cargo run -- validate --cache-root .cache/iso26262`
- `WP2_GATE_STAGE=B cargo run -- validate --cache-root .cache/iso26262` (sign-off only)

Acceptance SQL probes (sqlite3):

- Printed-page mapping coverage:
  - `SELECT COUNT(*) total, SUM(CASE WHEN page_printed_start IS NOT NULL OR page_printed_end IS NOT NULL THEN 1 ELSE 0 END) mapped FROM chunks;`
- Clause size compliance:
  - `WITH words AS (...) SELECT SUM(CASE WHEN wc > 900 THEN 1 ELSE 0 END) FROM words;`
- Per-ref split sequence coherence:
  - contiguous `chunk_seq` checks per `(doc_id, ref)` for split references.
- Table row/cell shape quality:
  - one-cell row ratio query from `nodes` (`table_row` + `table_cell` join).
- Citation parity:
  - compare `citation_parity_report.json` against `citation_parity_baseline.json` and enforce top-1/top-3/page-range thresholds.

Target pass condition for WP2 sign-off:

- WP1 checks (`Q-020`..`Q-022`) remain pass.
- WP2 checks (`Q-023`..`Q-030`) all pass.
- `Q-030` citation parity and targeted ASIL semantics (`Q-028`) are treated as primary blockers.
- Global one-cell ratio is used as directional/regression guard and cannot independently fail sign-off.
- No regressions on existing Part 6 smoke expectations.

## Risks and Mitigations

- OCR nondeterminism and runtime cost:
  - mitigate with explicit `--ocr-mode` defaults and reproducible provenance logs.
- Over-aggressive normalization harming references:
  - mitigate with conservative heuristics + regression fixtures for clause/table labels.
- Schema expansion risk on existing DB:
  - mitigate with additive migrations + backward-compatible validation parsing.
- Parser complexity regressions:
  - mitigate with incremental commits and per-checkpoint gate runs.

## Definition of Done for WP2

- Extraction backend provenance is explicit per processed page.
- Printed-page mappings are populated where detectable and coverage is reported.
- Long-clause split contract (size + overlap + deterministic `chunk_seq`) is enforced.
- Nested list semantics are persisted and validated.
- Table-cell semantic fields are populated and ASIL alignment checks are stricter and green.
- Citation parity for target-linked references meets Stage B thresholds.
- Full-target run (`2/6/8/9`) passes WP1 + WP2 check suite.
- Runbook and smoke workflow document and execute WP2 gate deterministically.
