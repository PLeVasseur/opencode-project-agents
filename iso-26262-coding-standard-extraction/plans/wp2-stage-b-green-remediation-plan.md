# WP2 Stage B Green Remediation Plan (Q-024/Q-026/Q-028/Q-029 + Q-030 lockfile hardening)

## Objective

- Drive Stage B (`WP2_GATE_STAGE=B`) to green by improving extraction quality, not by relaxing thresholds.
- Close the four currently failing checks:
  - `Q-024` Printed-page mapping coverage/status completeness
  - `Q-026` Nested list depth/marker semantics completeness
  - `Q-028` Strict ASIL row-column alignment
  - `Q-029` Normalization effectiveness/non-regression gate
- Hard-enable durable `Q-030` parity governance by replacing cache-local implicit baselining with a repo-tracked lockfile workflow.

## Baseline Snapshot (Current Stage B)

Source: `.cache/iso26262/manifests/extraction_quality_report.json` (`run-20260217T165919Z`)

- `Q-024` failed: `printed_mapping_on_detectable = 0.9772727273` (target `>= 0.98`)
- `Q-026` failed: `list_parse_fallback_ratio = 0.1528239203` (target `<= 0.05`)
- `Q-028` failed:
  - `asil_rating_coverage = 0.6296296296` (target `>= 0.85`)
  - `asil_malformed_ratio = 0.0740740741` (target `<= 0.05`)
  - `asil_outlier_ratio = 0.0740740741` (target `<= 0.10`, currently pass)
- `Q-029` failed:
  - `normalization_noise_ratio = 0.2631578947` (target `<= 0.01`)
  - `normalization_target_noise_count = 10` (target `= 0`)
  - `dehyphenation_false_positive_rate = 0.0` (pass)

## Remediation Strategy

- Fix metric truthfulness by aligning ingest behavior with validator semantics.
- Keep thresholds unchanged.
- Add regression tests for each fix before final Stage B verification.
- Land changes in small commits so each metric delta is auditable.
- Remove implicit baseline creation from normal validation paths; baseline creation/rotation must be explicit and auditable.

## Work Package A - Q-024 Printed-page range mapping

Problem:

- Ingest currently maps printed labels only from chunk boundary pages (`page_start`/`page_end`).
- Validate marks a chunk detectable if any page in the chunk range has a detected printed label.
- Result: multi-page chunks with interior-only detection are detectable but unmapped.

Example signatures observed:

- `ISO26262-8-2018`, clause `11.2`, pages `34..36`: page 35 detected, boundaries missing, chunk mapped `null/null`.
- `ISO26262-6-2018`, `Annex C`, pages `48..54`: interior detections exist, chunk mapped `null/null`.

Implementation:

- Add helper in `src/commands/ingest.rs` to compute printed labels over full page range.
  - Input: `labels`, `start_page`, `end_page`
  - Output: `(first_detected_in_range, last_detected_in_range)`
  - Handle invalid ranges and out-of-bounds robustly.
- Replace boundary-only mapping call sites for structured chunks with range-aware mapping.
- Preserve existing behavior for single-page chunks.

Tests:

- Add unit test: interior-only detectable pages in a range still produce non-null start/end mapping.
- Add unit test: no detectable pages in range returns `None/None`.

Exit criteria:

- `printed_mapping_on_detectable >= 0.98` in Stage B.

## Work Package B - Q-026 list candidate/fallback denominator correction

Problem:

- `parse_list_items` currently treats note markers as list-like candidates.
- Note-only chunks can be counted as list parse candidates/fallbacks, inflating fallback ratio.

Example signature observed:

- Clause with `NOTE` content produces `note_item` descendants only, but contributes to list fallback denominator/numerator.

Implementation:

- In `src/commands/ingest.rs`, split candidate accounting:
  - `list_marker_candidates`: increment only when a list marker regex match occurs.
  - Do not count note markers for list fallback metrics.
- Set `had_list_candidates = list_marker_candidates > 0`.
- Set `used_fallback = had_list_candidates && items.is_empty()`.
- Keep note parsing behavior unchanged.

Tests:

- Add unit test for note-only text:
  - expected `items=[]`, `had_candidates=false`, `fallback=false`.
- Add unit test for mixed list+note text:
  - expected list candidates counted from list markers only.

Exit criteria:

- `list_parse_fallback_ratio <= 0.05` in Stage B.

## Work Package C - Q-029 normalization leakage suppression

Problem:

- Watermark/license payload (`Order/license/Downloaded/single user/networking prohibited`) is still present in chunk text.
- This dominates noise counters globally and in target-linked references.

Implementation:

- Harden normalization in `src/commands/ingest.rs`:
  - Detect and strip repeated watermark/license lines deterministically during page normalization.
  - Ensure removal is signature-based and does not remove legitimate safety text.
- Keep `line_is_noise` contract consistent with watermark signature.
- Tighten `contains_normalization_noise` in `src/commands/validate.rs` to match explicit watermark detection tokens and avoid overbroad triggers.

Tests:

- Add unit test: watermark block removed from sample page text.
- Add unit test: normal clause text with unrelated words remains intact.

Exit criteria:

- `normalization_noise_ratio <= 0.01`
- `normalization_target_noise_count = 0`
- `dehyphenation_false_positive_rate <= 0.01`

## Work Package D - Q-028 ASIL strict row/column alignment

Problem:

- Target ASIL tables (`Table 3`, `Table 6`, `Table 10` in Part 6) still contain merged marker rows and detached rating streams.
- This depresses rating coverage and increases malformed marker row ratio.

Implementation:

- Strengthen table-row reconstruction in `src/commands/ingest.rs`:
  - Expand marker-list reconstruction (`1b 1c ...`) into explicit marker rows.
  - Reassign trailing rating token streams to the intended marker rows where alignment cues are available.
  - Prevent narrative footnote blocks from being interpreted as rating columns.
- Keep `table_node_id/row_idx/col_idx/is_header/span` completeness unchanged.

Tests:

- Add parser fixtures for representative extracted patterns from `Table 3`, `Table 6`, and `Table 10`.
- Assert expected row count, marker coverage, and rating presence per marker row.

Exit criteria:

- `asil_rating_coverage >= 0.85`
- `asil_malformed_ratio <= 0.05`
- `asil_outlier_ratio <= 0.10`
- `asil_one_cell_row_ratio <= 0.20`

## Work Package E - Q-030 citation parity lockfile hardening

Problem:

- Citation parity baseline is currently created under `.cache/.../citation_parity_baseline.json` when missing.
- New sessions can silently self-baseline, weakening non-regression guarantees.
- Cache-local baselines are not durable or reviewable as repository artifacts.

Implementation:

- Introduce a canonical repo-tracked lockfile path:
  - `manifests/citation_parity_baseline.lock.json`
- Keep lockfile payload metadata-only (no copyrighted extracted text):
  - allowed fields: run ids/timestamps/schema/checksum/target ids/doc ids/reference strings/anchor identities/page ranges/top-k ordering metadata.
  - explicitly reject payload fields like `text`, `snippet`, `heading`, `chunk_text`, `table_md`, `table_csv`.
- Update `validate` baseline policy:
  - Stage A (`WP2_GATE_STAGE=A`): missing lockfile emits warning/recommendation unless explicit bootstrap mode is requested.
  - Stage B (`WP2_GATE_STAGE=B`): missing lockfile is a hard fail with actionable remediation command.
  - Normal validate paths do not auto-create baselines.
- Add explicit baseline bootstrap/rotation mode:
  - e.g. `WP2_CITATION_BASELINE_MODE=bootstrap` to write or rotate lockfile intentionally.
  - rotation requires decision-log rationale (decision id + reason).

Tests:

- Missing lockfile + Stage B returns deterministic hard-fail issue.
- Bootstrap mode writes lockfile at canonical path with expected schema.
- Lockfile schema guard rejects forbidden text-bearing fields.

Exit criteria:

- `manifests/citation_parity_baseline.lock.json` exists and is tracked in git.
- Stage B fails when lockfile is missing.
- Stage A bootstrap command can intentionally (re)create lockfile.
- No implicit baseline creation occurs during standard validate runs.

## Execution Order and Commit Plan

1. `fix(ingest): map printed labels across chunk page ranges` (Q-024)
2. `fix(ingest): correct list fallback denominator for note-only chunks` (Q-026)
3. `fix(ingest): strip repeated watermark/license noise during normalization` (Q-029 ingest side)
4. `fix(validate): align normalization noise detection with watermark signature` (Q-029 validate side)
5. `feat(validate): enforce repo-tracked citation parity lockfile policy` (Q-030 governance hardening)
6. `fix(ingest): improve asil marker row and rating column reconstruction` (Q-028)

## Verification Loop

After each work package:

- `cargo check`
- `cargo test`
- `WP2_GATE_STAGE=A PART=6 MAX_PAGES=60 scripts/refresh_quality_artifacts.sh` (fast signal)

Before closure:

- `WP2_GATE_STAGE=A FULL_TARGET_SET=1 FULL_MAX_PAGES=0 PART=6 MAX_PAGES=60 scripts/refresh_quality_artifacts.sh`
- `WP2_CITATION_BASELINE_MODE=bootstrap WP2_GATE_STAGE=A cargo run -- validate --cache-root .cache/iso26262` (first-time lockfile bootstrap only)
- `WP2_GATE_STAGE=B cargo run -- validate --cache-root .cache/iso26262`

Definition of done:

- Stage B report shows `status=passed`.
- `Q-024`, `Q-026`, `Q-028`, and `Q-029` all report `pass`.
- Citation parity lockfile exists at `manifests/citation_parity_baseline.lock.json` and is used by Stage B.
- No regression in `Q-020`, `Q-021`, `Q-022`, `Q-023`, `Q-025`, `Q-027`, `Q-030`.

## Risks and Mitigations

- Risk: Over-aggressive noise filtering removes legitimate content.
  - Mitigation: signature-based removals + explicit tests for false removals.
- Risk: ASIL reconstruction heuristics overfit one table pattern.
  - Mitigation: fixture coverage across Tables 3/6/10 + keep fallback path deterministic.
- Risk: Fixing one metric shifts denominators unexpectedly.
  - Mitigation: log before/after counters from ingest manifest and report for each commit.
- Risk: Baseline lockfile churn obscures meaningful regressions.
  - Mitigation: require explicit bootstrap/rotation mode + decision-log rationale and review in code/config repo.

## Tracking Checklist

- [x] A1 Implement range-aware printed-page mapping
- [x] A2 Add Q-024 regression tests
- [x] B1 Implement list candidate denominator correction
- [x] B2 Add Q-026 regression tests
- [x] C1 Implement watermark/license stripping in normalization
- [x] C2 Align validator normalization-noise detection
- [x] C3 Add Q-029 regression tests
- [x] D1 Implement ASIL marker/rating reconstruction improvements
- [x] D2 Add Q-028 fixture tests
- [x] E1 Implement repo-tracked citation parity lockfile path and schema guard
- [x] E2 Enforce Stage B hard-fail on missing lockfile
- [x] E3 Add explicit bootstrap/rotation flow and docs
- [x] F1 Run full Stage A + Stage B validation loop
- [x] F2 Confirm Stage B green and document deltas
