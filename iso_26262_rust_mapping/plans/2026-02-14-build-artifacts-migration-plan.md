# ISO26262 Docgen Build/Reshuffle Plan

## Objectives
- [ ] Stabilize the build workflow so it works cleanly on a fresh machine.
  - [ ] Confirm required runtime tools (`python3`, `uv`) are documented and validated.
  - [ ] Keep strict `verify` defaults and make render tooling requirements explicit.
  - [ ] Preserve existing document generation behavior and output parity.
- [ ] Convert `build/` into the generated-artifacts root.
  - [ ] Move Python source code out of `build/` to a non-artifact package path.
  - [ ] Ensure all generated files land under `build/` (or subdirectories of it).
  - [ ] Use fixed generated DOCX path: `build/docx/iso26262_rust_mapping_generated.docx`.
  - [ ] Ensure generated artifacts are ignored by default in git.
- [ ] Add a repo-root `.gitignore` that matches the new layout and workflow.
  - [ ] Ignore local environment and cache files.
  - [ ] Ignore generated artifacts.
  - [ ] Avoid ignoring actual source code.

## Phase 1 - Baseline and Design Decisions
- [ ] Capture a baseline of current behavior before reshuffling directories.
  - [ ] Run `uv sync --frozen`.
  - [ ] Run `uv run python make.py validate`.
  - [ ] Run `uv run python make.py build`.
  - [ ] Run `uv run python make.py verify` (default strict render behavior).
  - [ ] If verify fails due to missing render tools, install them and rerun.
  - [ ] Record current generated paths and high-level report outcomes.
- [ ] Decide and lock the new source package name (recommended: `docgen/`).
  - [ ] Confirm no collisions with stdlib/common tooling names.
  - [ ] Ensure name reads clearly in imports.
  - [ ] Ensure it communicates "source code" not "artifacts".
- [ ] Define target artifact layout under `build/`.
  - [ ] `build/docx/` for generated `.docx` outputs.
  - [ ] `build/reports/` for compare reports.
  - [ ] `build/render_compare/` for optional visual QA outputs.
  - [ ] Optionally reserve `build/tmp/` for transient intermediate files.
- [ ] Lock migration defaults to avoid execution drift.
  - [ ] Keep `verify` default strict at `--render-pages 2`.
  - [ ] Do not add auto-skip/graceful fallback when render tools are missing.
  - [ ] Use fixed DOCX output path `build/docx/iso26262_rust_mapping_generated.docx`.
  - [ ] Remove configurable output path behavior (`--output`) from migration scope.
  - [ ] Execute hard cutover from `out/` to `build/` with no compatibility layer.

## Phase 2 - Source Code Reshuffle (`build/` code -> new package)
- [ ] Relocate source modules currently living in `build/`.
  - [ ] Move `build/__init__.py` to `docgen/__init__.py`.
  - [ ] Move `build/compare.py` to `docgen/compare.py`.
  - [ ] Move `build/docx_builder.py` to `docgen/docx_builder.py`.
  - [ ] Move `build/render.py` to `docgen/render.py`.
  - [ ] Move `build/util.py` to `docgen/util.py`.
  - [ ] Move `build/validate.py` to `docgen/validate.py`.
- [ ] Update imports and references after move.
  - [ ] Update `make.py` imports from `build.*` to `docgen.*`.
  - [ ] Verify internal relative imports still resolve cleanly.
  - [ ] Search repo for stale `from build` or `import build` references.
  - [ ] Run a runtime import smoke-check to ensure no third-party `build` package is accidentally resolved.
- [ ] Remove source/caches from legacy `build/` location.
  - [ ] Delete any tracked `build/__pycache__/` content.
  - [ ] Ensure no Python source remains under root `build/`.
  - [ ] Reserve root `build/` for generated artifacts only.

## Phase 3 - Artifact Path Migration (`out/` -> `build/`)
- [ ] Replace hardcoded output paths in CLI orchestration.
  - [ ] Set generated DOCX output to `build/docx/iso26262_rust_mapping_generated.docx`.
  - [ ] Set compare report output to `build/reports/compare_report.md`.
  - [ ] Set render output directory to `build/render_compare/`.
- [ ] Enforce deterministic CLI output behavior.
  - [ ] Remove `--output` argument from `build` and `verify` commands.
  - [ ] Update argparse help text to reflect fixed output paths.
  - [ ] Ensure artifact parent directories are created automatically.
- [ ] Execute hard cutover from legacy `out/`.
  - [ ] Remove all runtime writes to `out/`.
  - [ ] Remove all code paths that read/write `out/`.
  - [ ] Do not implement compatibility shims (no dual-write, symlink, or fallback).
- [ ] Ensure no accidental reliance on old `out/` paths remains.
  - [ ] Search for string literals referencing `out/`.
  - [ ] Update docs, examples, and migration notes.
  - [ ] Confirm only intentional historical mentions of `out/` remain.

## Phase 4 - `.gitignore` and Tracking Policy
- [ ] Add repo-root `.gitignore` with clear, minimal patterns.
  - [ ] Ignore Python bytecode and caches (`__pycache__/`, `*.pyc`, etc.).
  - [ ] Ignore local virtual environments (`.venv/`, `venv/`).
  - [ ] Ignore generated artifact directories under `build/`.
  - [ ] Ignore legacy `out/` folder if it appears locally during/after migration.
- [ ] Protect source code from overbroad ignore rules.
  - [ ] Do not ignore `docgen/` source package.
  - [ ] Do not ignore `src/`, `templates/`, or `ref/`.
  - [ ] Confirm `.gitignore` does not mask required tracked files.
- [ ] Normalize git index after ignore policy lands.
  - [ ] Untrack previously committed cache files (especially `build/__pycache__/*`).
  - [ ] Untrack generated artifacts now that they are treated as generated outputs.
  - [ ] Verify `git status` shows clean tracking boundaries after rebuild.

## Phase 5 - Documentation and Developer Workflow Updates
- [ ] Update `README.md` for the new source and artifact layout.
  - [ ] Refresh project layout section to mention `docgen/` and `build/` artifact roles.
  - [ ] Update output examples to `build/docx/`, `build/reports/`, `build/render_compare/`.
  - [ ] Keep quickstart commands aligned with actual defaults.
- [ ] Clarify strict visual QA dependency behavior.
  - [ ] Document that default `verify` requires `soffice` and `pdftoppm` and fails if missing.
  - [ ] Document how to install `soffice` and `pdftoppm` by platform.
  - [ ] Explain expected outputs for strict/default verify runs.
- [ ] Update all user-facing path and command strings with explicit scope.
  - [ ] Update `make.py` module docstring path/layout/output references.
  - [ ] Update `make.py` argparse help text for fixed output and strict verify behavior.
  - [ ] Update all README output path examples from `out/...` to `build/...`.
  - [ ] Add migration note that cutover is hard (`out/` removed, no compatibility path).
  - [ ] Run final repository search for stale `out/` references in `.py`/`.md`.
- [ ] Add a short migration note for existing contributors.
  - [ ] Mention `build/` semantic change (source -> artifacts).
  - [ ] Mention hard removal of `out/` runtime behavior.
  - [ ] Mention cleanup step (`git rm --cached` for stale tracked artifacts).

## Phase 6 - Validation and Acceptance
- [ ] Validate behavior after reshuffle.
  - [ ] Run `uv sync --frozen` on a clean checkout.
  - [ ] Run `uv run python make.py validate`.
  - [ ] Run `uv run python make.py build` and verify outputs in `build/docx/`.
  - [ ] Run `uv run python make.py verify` and verify report in `build/reports/`.
- [ ] Validate artifact tracking behavior.
  - [ ] Re-run build commands.
  - [ ] Confirm generated files in `build/` do not appear as untracked (if ignored).
  - [ ] Confirm source changes still appear correctly in `git status`.
- [ ] Validate content parity.
  - [ ] Inspect compare report for structural parity counts.
  - [ ] Confirm text similarity remains at expected level.
  - [ ] Spot-check generated DOCX opens correctly.

## Phase 7 - Rollout Strategy
- [ ] Implement in logical commits to simplify review.
  - [ ] Commit 1: source package rename (`build/` code -> `docgen/`) + import updates.
  - [ ] Commit 2: artifact path migration (`out/` -> `build/`) + fixed output contract (remove `--output`).
  - [ ] Commit 3: `.gitignore` + untracking generated/cache files.
  - [ ] Commit 4: README/docs migration notes and final cleanup.
- [ ] Keep rollback path straightforward.
  - [ ] Ensure each commit passes basic validate/build checks.
  - [ ] Avoid mixing mechanical file moves with behavioral changes when possible.
  - [ ] Preserve reference inputs (`ref/`, `templates/`, `src/`) unchanged unless required.

## Completion Criteria
- [ ] `build/` is exclusively for generated artifacts.
  - [ ] No Python source files remain under root `build/`.
  - [ ] All generated outputs land in `build/` subdirectories.
- [ ] Source code composes under a clearly named package (`docgen/` or chosen equivalent).
  - [ ] `make.py` imports resolve without legacy path hacks.
  - [ ] Build and verify commands run successfully.
- [ ] Output behavior is deterministic and fixed.
  - [ ] Generated DOCX path is always `build/docx/iso26262_rust_mapping_generated.docx`.
  - [ ] `--output` is removed from the supported interface.
  - [ ] No runtime artifact writes occur under `out/`.
- [ ] `.gitignore` enforces clean workspace hygiene.
  - [ ] Local env and bytecode are ignored.
  - [ ] Generated artifacts are ignored by default.
  - [ ] `git status` remains clean after a full local build.
