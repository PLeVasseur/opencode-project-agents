# Plan: Add standalone FLS maintenance corrections changelog entry for dedupe IDs

## Goal
- [ ] Add a standalone maintenance section to `src/changelog.rst` documenting the glossary paragraph-ID dedup fix.
- [ ] Keep this separate from Rust release language-change entries (including Rust 1.93 ABI items).
- [ ] Land this first as a focused, reviewable change on the dedupe line of work.

## Scope
- [ ] Repository: `/home/pete.levasseur/project/fls`
- [ ] Base branch: `dedupe-paragraph-ids-mainline`
- [ ] New feature branch: `dedupe-maintenance-corrections-changelog`
- [ ] Files in scope:
  - [ ] `src/changelog.rst`
  - [ ] (validation only) build artifacts/logs under `$OPENCODE_CONFIG_DIR/reports/`

## Non-goals
- [ ] Do not include tooling refactors in this PR.
- [ ] Do not include ABI content reshaping in this PR.
- [ ] Do not rewrite the 1.93 ABI entry for this task, except if absolutely required for consistency checks (document if done).

## Proposed changelog content
- [ ] Insert this standalone section before `Language changes in Rust 1.93.0`:

```rst
FLS maintenance corrections
---------------------------

- Deduplicate historically reused paragraph IDs in the glossary (ID-integrity fix).

  - Corrected glossary `discriminant type` paragraph ID:
    - old reused ID: ``fls_t4yeovFm83Wo``
    - new unique ID: ``fls_kqdvWGi9cglm``
  - Corrected glossary `local trait` paragraph ID:
    - old reused ID: ``fls_I9JaKZelMiby``
    - new unique ID: ``fls_H5vkbMFvzrFs``
  - This is a historical FLS maintenance correction (no Rust language semantics change).
```

## Why this is separate from 1.93
- [ ] The dedupe commit (`0165ee6...`) corrects historical ID collisions, not a Rust language release-note item.
- [ ] Old reused IDs already exist as active IDs in other chapters:
  - [ ] `src/types-and-traits.rst:652` (`fls_t4yeovFm83Wo`)
  - [ ] `src/types-and-traits.rst:2742` (`fls_I9JaKZelMiby`)
- [ ] Corrected glossary IDs now live at:
  - [ ] `src/glossary.rst:1815` (`fls_kqdvWGi9cglm`)
  - [ ] `src/glossary.rst:3938` (`fls_H5vkbMFvzrFs`)

## Execution checklist

### 1) Branch/worktree prep
- [ ] Ensure clean workspace for this task (or use a fresh worktree).
- [ ] Create/switch to feature branch from dedupe base:
  - [ ] `git worktree add -b dedupe-maintenance-corrections-changelog <new-worktree> dedupe-paragraph-ids-mainline`
  - [ ] Verify branch and status are clean.

### 2) Edit changelog
- [ ] Insert `FLS maintenance corrections` section near top of `src/changelog.rst`.
- [ ] Keep release sections untouched unless formatting normalization is strictly necessary.
- [ ] Preserve existing reStructuredText conventions and spacing.

### 3) Validate
- [ ] Build docs:
  - [ ] `./make.py`
- [ ] Capture warnings/errors under `$OPENCODE_CONFIG_DIR/reports/<timestamp>/`.
- [ ] Verify section placement and text with a targeted diff/readback.
- [ ] Optional informational check:
  - [ ] `uv run python tools/changelog_assistant.py --check --base <appropriate-base>`
  - [ ] If this check reports release-section coverage expectations, document rationale that this is a maintenance correction section (not a release language change).

### 4) Commit
- [ ] Stage only intended files (`src/changelog.rst` unless explicitly needed otherwise).
- [ ] Commit with Conventional Commit, e.g.:
  - [ ] `docs(changelog): add maintenance note for deduplicated glossary IDs`
- [ ] Record commit SHA in report.

### 5) PR preparation
- [ ] PR title focused on maintenance correction (not ABI/tooling).
- [ ] PR summary should explicitly state:
  - [ ] what IDs were corrected,
  - [ ] why this is historical maintenance,
  - [ ] why it is intentionally not part of the 1.93 ABI entry.

## Risks and handling
- [ ] Risk: reviewer prefers release-only changelog headings.
  - [ ] Mitigation: keep the section concise and explicitly marked as maintenance correction.
- [ ] Risk: automation expects release-section-only coverage.
  - [ ] Mitigation: document expected behavior and keep this PR isolated; handle automation policy in tooling follow-up PR if needed.

## Acceptance criteria
- [ ] `src/changelog.rst` contains the standalone `FLS maintenance corrections` section with both old->new ID mappings.
- [ ] The change is isolated to maintenance documentation intent (no bundled tooling/ABI refactor).
- [ ] Build succeeds (or warnings are documented with rationale).
- [ ] Commit is ready as a standalone first PR in landing order.
