# Plan: Paragraph-First Changelog Rendering (Added/Removed/Changed + Inline Changed Tags)

## Goal
- [ ] Change changelog entry rendering to paragraph-first structure only:
  - [ ] `Added paragraphs`
  - [ ] `Removed paragraphs`
  - [ ] `Changed paragraphs`
- [ ] Ensure only `Changed paragraphs` lines carry inline tags describing what changed.
- [ ] Remove duplicate paragraph-ID fanout across many per-tag sections.
- [ ] Keep anchor/update/title behavior unchanged from current preserve-title implementation.

## Scope
- [ ] Primary file: `tools/changelog_assistant.py`
- [ ] Validation target entry: upstream PR `https://github.com/rust-lang/rust/pull/145954`
- [ ] Validate missing-anchor behavior with `https://github.com/rust-lang/rust/pull/999999`
- [ ] Write plan/report artifacts under `$OPENCODE_CONFIG_DIR/plans/` and `$OPENCODE_CONFIG_DIR/reports/` only.

## Desired Entry Contract
- [ ] Keep top-level entry headline semantics as-is (anchor-hit preserve by default; replace only with `--replace-title`).
- [ ] Keep `Change tags: ...` summary line.
- [ ] Render body with paragraph lifecycle categories only.
- [ ] `Added paragraphs` and `Removed paragraphs` are plain paragraph-ID bullets.
- [ ] `Changed paragraphs` bullets include an inline tag list, ordered by `CHANGE_TAG_ORDER`.
- [ ] No paragraph ID appears more than once within any category.
- [ ] No dedicated body categories such as `Role changes`, `Term definitions added`, `Term references removed`, `Syntax references added`, `Normative shifts`, etc.

## Example Target Shape
- [ ] Example output pattern for one entry:

```rst
- `Stabilize declaration of C-style variadic functions for the system ABI <https://github.com/rust-lang/rust/pull/145954>`_

  - Change tags: paragraph-added, paragraph-changed, role-change, term-def-added, term-ref-removed, syntax-ref-added, section-added, normative-shift
  - Added paragraphs:
    - :p:`fls_MpcAsy5zhCeW`
    - :p:`fls_...`
  - Changed paragraphs:
    - :p:`fls_qwchgvvnp0qe` (paragraph-changed, role-change, syntax-ref-added)
    - :p:`fls_I9JaKZelMiby` (role-change, term-ref-removed)
```

## Non-goals
- [ ] Do not change diff extraction semantics in this phase.
- [ ] Do not alter branch/rebase/cherry-pick topology.
- [ ] Do not change report schema fields already consumed by existing workflows (`update_action`, anchored metadata).

## Implementation Checklist

### 1) Bootstrap and baseline capture
- [ ] Confirm working branch and cleanly capture current behavior artifacts.
- [ ] Capture one baseline generated entry (current multi-category format) for PR `145954`.
- [ ] Record baseline `git diff -- src/changelog.rst` artifact for before/after comparison.

### 2) Introduce paragraph-centric aggregation helpers
- [ ] Add helper to aggregate `changes` into paragraph lifecycle buckets:
  - [ ] `added_ids`: from `type == paragraph_added`
  - [ ] `removed_ids`: from `type == paragraph_removed`
  - [ ] `changed_tags_by_id`: paragraph ID -> set of tags for paragraph-linked non-add/remove changes
- [ ] Ensure `changed_tags_by_id` includes:
  - [ ] `paragraph-changed`
  - [ ] `role-change`
  - [ ] `term-ref-added` / `term-ref-removed`
  - [ ] `syntax-ref-added` / `syntax-ref-removed`
  - [ ] `literal-change`
  - [ ] `list-structure-change`
  - [ ] `normative-shift`
  - [ ] any future paragraph-linked tags
- [ ] Keep deterministic order:
  - [ ] paragraph IDs sorted lexicographically
  - [ ] inline tags sorted using existing `CHANGE_TAG_ORDER`

### 3) Replace body rendering logic in `entry_lines`
- [ ] Stop iterating over static per-tag section labels.
- [ ] Emit only paragraph lifecycle sections that have records.
- [ ] Format changed paragraph bullets as:
  - [ ] `- :p:`<id>` (<tag1>, <tag2>, ...)`
- [ ] Keep trailing blank-line behavior stable to avoid noisy diffs.

### 4) Handling non-paragraph changes in body
- [ ] Keep non-paragraph tags visible in `Change tags:` summary.
- [ ] Do not render non-paragraph-only detail sections in entry body.
- [ ] Keep full raw change detail in generated JSON/Markdown report output.

### 5) Preserve existing anchor/title/update semantics
- [ ] Verify default anchor-hit update still preserves existing title.
- [ ] Verify anchor-hit + `--replace-title` still replaces title.
- [ ] Verify append behavior for missing anchor (without `--require-anchor`) is unchanged.
- [ ] Verify strict missing anchor with `--require-anchor` remains non-zero.

### 6) Coverage and lint compatibility checks
- [ ] Verify `paragraph_ids_requiring_coverage` behavior still works with new rendering.
- [ ] Verify generated entry still contains all paragraph IDs required by coverage checks.
- [ ] Confirm no regressions to `--require-tags` (`Change tags:` remains present).

### 7) Validation matrix
- [ ] `uv run python -m py_compile tools/changelog_assistant.py`
- [ ] `uv run python tools/changelog_assistant.py --help`
- [ ] `uv run python tools/changelog_tag_verifier.py --mode compare --report-dir <...>`
- [ ] `uv run python tools/changelog_tag_verifier.py --mode extract --report-dir <...>`
- [ ] Canonical anchor update without `--replace-title` (title preserved)
- [ ] Canonical anchor update with `--replace-title` (title replaced)
- [ ] Idempotence rerun for `--replace-title`
- [ ] Missing strict anchor check (`--require-anchor`) returns non-zero
- [ ] Missing default anchor check appends and exits zero

### 8) Structured output assertions (must-pass)
- [ ] For generated `145954` entry, assert section headers present are only:
  - [ ] `Added paragraphs`
  - [ ] `Removed paragraphs` (if applicable)
  - [ ] `Changed paragraphs`
- [ ] Assert no legacy body headers appear (`Role changes`, `Term definitions added`, etc.).
- [ ] Assert each changed-paragraph bullet contains inline parenthesized tags.
- [ ] Assert added/removed bullets do not include inline tags.
- [ ] Assert no duplicate paragraph IDs within each category.

### 9) Evidence and reporting
- [ ] Write artifacts under `$OPENCODE_CONFIG_DIR/reports/<timestamped-plan-run>/`:
  - [ ] command ledger with exit codes
  - [ ] baseline and post-change diffs
  - [ ] generated report JSON/MD for each validation run
  - [ ] section-structure assertion output
- [ ] Write final summary with:
  - [ ] pass/fail per checklist section
  - [ ] key behavior outcomes
  - [ ] any remediation notes

## Acceptance Criteria
- [ ] Changelog body rendering uses paragraph lifecycle categories only.
- [ ] Only `Changed paragraphs` lines include inline tags.
- [ ] Paragraph-ID duplication across many per-tag sections is eliminated.
- [ ] Anchor/title behavior remains correct (default preserve + explicit replace override).
- [ ] Missing-anchor strict/default behavior remains unchanged.
- [ ] Coverage checks and verifier runs still pass.

## Suggested Commit Structure
- [ ] Commit 1: renderer refactor (paragraph buckets + inline changed tags)
- [ ] Commit 2: validation/assertion helpers or fixture updates (if needed)
- [ ] Commit 3: docs/changelog assistant usage notes (if help text needs clarification)

## Session Hand-off Checklist
- [ ] Include exact branch name and HEAD SHA.
- [ ] Include exact report root path.
- [ ] Include before/after snippet for PR `145954` entry.
- [ ] Include confirmation that `calling_convention` is represented via paragraph lifecycle output (not a separate body section).
