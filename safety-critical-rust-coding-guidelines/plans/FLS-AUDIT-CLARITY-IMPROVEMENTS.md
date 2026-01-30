# FLS Audit Clarity Improvements Plan

## Purpose

Make FLS audits easy to interpret by adding before/after text diffs, grouping changes by type, and highlighting new-paragraph applicability to existing guidelines. Eliminate path hacks by reorganizing the Python packaging with uv workspaces, while keeping the Sphinx extension in `exts/`.

## Goals

- Provide before/after text diffs for changed paragraphs.
- Separate change categories (added, removed, modified, renumbered-only, header changes).
- Surface potential guideline impact for newly added paragraphs.
- Remove all `sys.path` hacks while keeping `exts/` intact.
- Keep `make.py` and root scripts working under `uv run`.
- Capture deployment metadata in `src/spec.lock` to make baselines deterministic.
- Support baseline/current commit selection from GitHub Pages deployment history.

## Non-Goals

- Do not change the published guideline content.
- Do not change the FLS paragraph checksum algorithm.

## Design Overview

### Workspace Packaging (uv-native)

Use a uv workspace with multiple packages to avoid path hacks while keeping `exts/` intact:

- Workspace root (`pyproject.toml`): package providing module `scripts` (no virtual root).
- Member package 1: `exts/` → distribution `coding-guidelines-ext`, module `coding_guidelines`.
- Member package 2: `builder/` (existing).

This allows `uv run` to install both `scripts` and `coding_guidelines` without `sys.path` manipulation.

### Script Refactor Strategy

- Move shared logic from `generate_guideline_templates.py` into `scripts/common/guideline_templates.py`.
- Keep `generate_guideline_templates.py` as a thin wrapper that imports and calls the new module (no `sys.path` changes).
- Update all `scripts/*.py` imports to use `from scripts...` instead of adding `sys.path`.

### Audit Clarity Enhancements

- Parse FLS RST to extract paragraph text by `:dp:` role (no regex).
- Cache the FLS repo and worktrees in `./.cache/fls-audit/`.
- Add snapshots for before/after diffs:
  - `--write-text-snapshot <path>`
  - `--baseline-text-snapshot <path>`
- For content changes, include before/after text and unified diffs (`difflib`).
- Group report sections by change type:
  - Added
  - Removed
  - Modified (content changed)
  - Renumbered-only
  - Section/document title changes
- Highlight newly added paragraphs that fall in sections/chapters with existing guidelines (potentially impacted).
- Detect section reordering based on section path indices.

### Baseline Strategy

- Add deployment metadata to `src/spec.lock`:
  - `metadata.fls_deployed_commit`
  - `metadata.fls_deployed_at`
  - `metadata.fls_pages_deployment_id`
  - `metadata.fls_source_url`
  - `metadata.previous` (prior metadata snapshot)
- GitHub Pages build endpoints may require auth for public repos (404 without token);
  use the public Deployments API for `environment=github-pages` to populate metadata
  without credentials. Prefer the most recent deployment with a `success` status and
  use its status `created_at` for `fls_deployed_at` (fallback to deployment `created_at`).
  Store the deployment `id` under `fls_pages_deployment_id` for accuracy.
- Audit tool uses `metadata.fls_deployed_commit` as baseline when present.
- If metadata is missing, fall back to GitHub Pages deployment history.
- Support `--baseline-deployment-offset N` for cases where we are multiple deployments behind.
- Allow overrides with `--baseline-fls-commit` / `--current-fls-commit`.
- Listing deployment offsets requires GitHub API access (`GITHUB_TOKEN` recommended in CI).

## Implementation Steps

### 1) Workspace layout (uv)

- Root `pyproject.toml`:
  - Add `[tool.uv.workspace] members = ["builder", "exts"]`.
  - Set `[tool.uv.build-backend] module-root = ""` and `module-name = "scripts"`.
  - Add dependency on `coding-guidelines-ext` with `tool.uv.sources` set to `{ workspace = true }`.
- Create `exts/pyproject.toml`:
  - `name = "coding-guidelines-ext"`
  - `module-root = "."`, `module-name = "coding_guidelines"`
- Add `scripts/__init__.py` and `scripts/common/__init__.py`.

### 2) Remove path hacks

- Remove `sys.path.append("../exts")` from `src/conf.py`.
- Remove `sys.path.insert`/`sys.path.append` in:
  - `scripts/guideline_utils.py`
  - `scripts/generate-rst-comment.py`
  - `scripts/extract_rust_examples.py`
  - `scripts/migrate_rust_examples.py`
  - `scripts/auto-pr-helper.py`

### 3) Move shared guideline template logic

- New module: `scripts/common/guideline_templates.py` with all logic currently in `generate_guideline_templates.py`.
- Update imports in:
  - `scripts/guideline_utils.py`
  - `scripts/generate-rst-comment.py`
- Convert `generate_guideline_templates.py` into a thin wrapper:
  - `from scripts.common.guideline_templates import main`
  - `if __name__ == "__main__": main()`

### 4) FLS RST parsing helpers

- New module: `scripts/common/fls_rst.py`.
- Parse RST files under `src/` using docutils:
  - Detect `:dp:` roles at paragraph start for FLS IDs.
  - Extract paragraph text, section IDs, and section titles.
  - Compute section order paths for reorder detection.
- Normalize text:
  - Collapse whitespace
  - Fix spacing around punctuation
  - Remove leading `fls_` IDs from paragraph text
- Cache the cloned FLS repo + worktrees under `./.cache/fls-audit/`.

### 5) Audit tool enhancements

- Add snapshot support in `scripts/fls_audit.py`.
- Add RST-based baseline/current text extraction using FLS repo commits.
- Add CLI options:
  - `--baseline-fls-commit <sha>`
  - `--current-fls-commit <sha>`
  - `--baseline-deployment-offset N`
  - `--current-deployment-offset N`
  - `--fls-repo-cache-dir <path>` (default: `./.cache/fls-audit`)
- Add grouped report sections and explicit change categorization.
- Add applicability heuristic for newly added paragraphs:
  - Same section → high priority
  - Same chapter → medium priority
  - No nearby guidelines → low priority
- Add section/document title change detection.
- Add section reordering section in the report.
- Hide legacy diff output behind `--include-legacy-report` (Markdown + JSON).
- Add heuristic relevance scoring for new + content-changed paragraphs:
  - Score 0–100
  - Show top 3 guideline matches with reasons
- Hide heuristic match details behind `--include-heuristic-details`.

### 6) Documentation updates

- Update repo `README.md` with:
  - Snapshot usage
  - Baseline commit / deployment offset usage
  - `--include-legacy-report` usage
  - How to interpret grouped report sections
  - New paragraph applicability guidance
- Update runbook and skill outside repo (project-agents):
  - `runbooks/fls-spec-lock-audit.md`
  - `skills/fls-audit/SKILL.md`

### 7) Spec lock metadata

- Update `builder/build_cli.update_spec_lockfile` to embed deployment metadata from GitHub Pages.
- Preserve prior metadata under `metadata.previous` on update.
- Use the Deployments API for public metadata retrieval; do not call Pages build
  endpoints for metadata.

### 8) Build failure guidance

- Update `exts/coding_guidelines/fls_checks.py` error message to suggest running the audit tool.
- Mention commit/token guidance only if the audit tool indicates missing metadata.

### 9) Dependencies

- No new dependencies beyond existing `sphinx`/`docutils`.

## Verification

### Script verification (no path hacks)

- `uv run python scripts/auto-pr-helper.py --help`
- `uv run python scripts/generate-rst-comment.py --help`
- `uv run python scripts/extract_rust_examples.py --help`
- `uv run python scripts/migrate_rust_examples.py --help`
- `uv run python scripts/split_guidelines.py --help`
- `uv run python scripts/reviewer_bot.py --help`
- `uv run python scripts/fls_audit.py --summary-only`
- `uv run python scripts/fls_audit.py --baseline-deployment-offset 1 --summary-only`

### Root script verification

- `uv run python generate_guideline_templates.py --help`

### Build verification

- `./make.py` (ensure Sphinx extension loads without `sys.path` hacks).

## Progress Tracking

- [x] Add uv workspace members for `exts` and set root to package `scripts`.
- [x] Create `exts/pyproject.toml`.
- [x] Add `scripts/__init__.py` and `scripts/common/__init__.py`.
- [x] Remove `sys.path` hacks from scripts and `src/conf.py`.
- [x] Move `generate_guideline_templates.py` logic into `scripts/common/guideline_templates.py`.
- [x] Convert `generate_guideline_templates.py` to wrapper.
- [x] Replace HTML extraction with RST parsing (remove `fls_text.py`).
- [x] Add snapshot support and grouped reporting in `scripts/fls_audit.py`.
- [x] Add new-paragraph applicability section.
- [x] Add header/section title change detection.
- [x] Add `scripts/common/fls_rst.py` (RST parser + section order tracking).
- [x] Add FLS repo cache/worktree helper under `scripts/common/`.
- [x] Add baseline/current commit selection via Pages API + offsets.
- [x] Store deployment metadata in `src/spec.lock` on update.
- [x] Use GitHub Deployments API to populate metadata without auth.
- [x] Rename metadata key to `fls_pages_deployment_id`.
- [x] Update audit tool to use RST baseline/current text.
- [x] Add section reorder reporting.
- [x] Update `.gitignore` to exclude `./.cache/`.
- [x] Update repo `README.md` for the new audit features.
- [x] Update project-agents runbook and skill.
- [x] Remove HTML extraction dependency and update `uv.lock` if needed.
- [x] Add `--include-legacy-report` gating for legacy output.
- [x] Update build failure guidance to recommend audit tool.
- [x] Add heuristic relevance scoring (top 3 matches).
- [x] Run the full verification checklist (pandoc missing for auto-pr/generate-rst-comment).

## Check-in Points

- Check-in 1: Workspace layout + packaging changes validated (imports work, no path hacks).
- Check-in 2: Guideline template logic moved and root wrapper script validated.
- Check-in 3: RST parsing + repo cache wired into audit tool.
- Check-in 4: Report grouping, applicability, and section reorder validated.
- Check-in 5: Documentation and runbooks updated; verification checklist passes.
