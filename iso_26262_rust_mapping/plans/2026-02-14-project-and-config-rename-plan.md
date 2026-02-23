# Project + OpenCode Config Rename Plan

## Goal
- [ ] Rename the project repository directory from `iso26262_docgen_full` to `iso_26262_rust_mapping`.
  - [ ] Preserve the git repository intact (history, branch pointers, `.git/`, hooks).
  - [ ] Preserve current local working state in the renamed folder.
- [ ] Rename the matching OpenCode config directory to keep auto-discovery aligned.
  - [ ] Move `$HOME/opencode-project-agents/iso26262_docgen_full` to `$HOME/opencode-project-agents/iso_26262_rust_mapping`.
  - [ ] Keep all config assets (`AGENTS.md`, `opencode.jsonc`, `plans/`, local artifacts) intact.
- [ ] Ensure shell/env resolution points to the new config path after rename.
  - [ ] Verify `OPENCODE_CONFIG_DIR` resolves to the new directory.
  - [ ] Verify `OPENCODE_CONFIG` resolves to `.../iso_26262_rust_mapping/opencode.jsonc`.

## Target Names and Paths
- [ ] Lock old/new names before execution.
  - [ ] Old repo dir: `/home/pete.levasseur/personal/iso26262_docgen_full`
  - [ ] New repo dir: `/home/pete.levasseur/personal/iso_26262_rust_mapping`
  - [ ] Old config dir: `/home/pete.levasseur/opencode-project-agents/iso26262_docgen_full`
  - [ ] New config dir: `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping`
- [ ] Confirm the rename is a hard cutover.
  - [ ] Do not leave duplicate active config directories.
  - [ ] Do not rely on temporary symlinks unless a rollback bridge is explicitly needed.

## Phase 0 - Safety and Preconditions
- [ ] Confirm no long-running process is using the old repo path.
  - [ ] Check for active shells/editor terminals rooted in old repo dir.
  - [ ] Close or re-root sessions that can hold stale working directories.
- [ ] Capture a quick state snapshot before moving directories.
  - [ ] In repo: run `git -C /home/pete.levasseur/personal/iso26262_docgen_full status --short --branch`.
  - [ ] In config parent repo (optional awareness): run `git -C /home/pete.levasseur/opencode-project-agents status --short --branch`.
  - [ ] Record current `printenv OPENCODE_CONFIG_DIR` value.
- [ ] Verify parent directories exist and destination paths are free.
  - [ ] Confirm `/home/pete.levasseur/personal/` exists.
  - [ ] Confirm `/home/pete.levasseur/opencode-project-agents/` exists.
  - [ ] Confirm `/home/pete.levasseur/personal/iso_26262_rust_mapping` does **not** exist.
  - [ ] Confirm `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping` does **not** exist.

## Phase 1 - Execute Directory Renames
- [ ] Rename project repo directory first.
  - [ ] Run: `mv /home/pete.levasseur/personal/iso26262_docgen_full /home/pete.levasseur/personal/iso_26262_rust_mapping`.
  - [ ] Verify new repo path exists.
  - [ ] Verify old repo path no longer exists.
- [ ] Rename OpenCode config directory second.
  - [ ] Run: `mv /home/pete.levasseur/opencode-project-agents/iso26262_docgen_full /home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping`.
  - [ ] Verify new config path exists.
  - [ ] Verify old config path no longer exists.
- [ ] Validate contents survived both moves.
  - [ ] Repo still contains expected project files (`README.md`, `make.py`, `src/`, `docgen/`, etc.).
  - [ ] Config dir still contains `AGENTS.md`, `opencode.jsonc`, and `plans/`.

## Phase 2 - Refresh OpenCode Environment Resolution
- [ ] Re-enter the renamed repo and refresh shell hook.
  - [ ] `cd /home/pete.levasseur/personal/iso_26262_rust_mapping`
  - [ ] `source /home/pete.levasseur/opencode-project-agents/shell/opencode-env.sh` (or open a fresh shell).
- [ ] Verify env variables now point to renamed config path.
  - [ ] Run `printenv OPENCODE_CONFIG_DIR` and confirm `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping`.
  - [ ] Run `printenv OPENCODE_CONFIG` and confirm `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping/opencode.jsonc`.
- [ ] Verify auto-bootstrap behavior stays clean.
  - [ ] Ensure no new accidental `.../iso26262_docgen_full` config directory was recreated.
  - [ ] Ensure no duplicate `iso_26262_rust_mapping` config directory variants were created.

## Phase 3 - Functional Validation in New Location
- [ ] Validate git usability in renamed project path.
  - [ ] Run `git status --short --branch` in `/home/pete.levasseur/personal/iso_26262_rust_mapping`.
  - [ ] Confirm branch and worktree are as expected.
- [ ] Validate project command flow still works by path.
  - [ ] Run `uv run python make.py validate`.
  - [ ] Run `uv run python make.py build`.
  - [ ] (Optional strict check) run `uv run python make.py verify` if render deps are present.
  - [ ] (Fallback check) run `uv run python make.py verify --render-pages 0` if `soffice`/`pdftoppm` are unavailable.
- [ ] Validate artifact paths remain correct post-rename.
  - [ ] Confirm generated docx at `build/docx/iso26262_rust_mapping_generated.docx`.
  - [ ] Confirm compare report at `build/reports/compare_report.md`.

## Phase 4 - OpenCode Config Integrity Checks
- [ ] Confirm config files resolve correctly from renamed config directory.
  - [ ] Read `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping/opencode.jsonc`.
  - [ ] Read `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping/AGENTS.md`.
- [ ] Confirm plan continuity.
  - [ ] Verify old plan files are present under new path `.../iso_26262_rust_mapping/plans/`.
  - [ ] Confirm newly created rename plan is present under new path.

## Phase 5 - Update Human/Tooling References (if needed)
- [ ] Update any personal shortcuts that reference the old repo path.
  - [ ] Shell aliases/functions.
  - [ ] IDE workspace entries.
  - [ ] Local scripts or cron jobs.
- [ ] Update any explicit references to old config path (if present outside auto-discovery).
  - [ ] Custom automation using hardcoded `$HOME/opencode-project-agents/iso26262_docgen_full`.
  - [ ] Notes/docs that mention old absolute paths.

## Rollback Plan
- [ ] Define rollback trigger conditions.
  - [ ] `OPENCODE_CONFIG_DIR` does not resolve to new path after refresh.
  - [ ] Project commands fail due to path-level issues.
  - [ ] Missing config assets after move.
- [ ] Execute rollback atomically if required.
  - [ ] Move repo back: `mv /home/pete.levasseur/personal/iso_26262_rust_mapping /home/pete.levasseur/personal/iso26262_docgen_full`.
  - [ ] Move config back: `mv /home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping /home/pete.levasseur/opencode-project-agents/iso26262_docgen_full`.
  - [ ] Re-source `opencode-env.sh` and re-check env values.

## Completion Criteria
- [ ] Repo directory rename is complete and stable.
  - [ ] `/home/pete.levasseur/personal/iso_26262_rust_mapping` exists and functions.
  - [ ] `/home/pete.levasseur/personal/iso26262_docgen_full` no longer exists.
- [ ] OpenCode config directory rename is complete and stable.
  - [ ] `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping` exists with expected files.
  - [ ] `/home/pete.levasseur/opencode-project-agents/iso26262_docgen_full` no longer exists.
- [ ] OpenCode environment resolution matches renamed directories.
  - [ ] `OPENCODE_CONFIG_DIR` points to `.../iso_26262_rust_mapping`.
  - [ ] `OPENCODE_CONFIG` points to `.../iso_26262_rust_mapping/opencode.jsonc`.
- [ ] Basic project validation succeeds from renamed path.
  - [ ] `uv run python make.py validate` succeeds.
  - [ ] Build/verify flow succeeds per available render dependencies.
