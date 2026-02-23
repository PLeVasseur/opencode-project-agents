# Plan: Replicate typo checking CI from coding-guidelines

## Objective
Implement typo checks in this repository using the same pattern as `rustfoundation/safety-critical-rust-coding-guidelines`:
- GitHub Actions job using `crate-ci/typos@v1.40.0`
- Root `_typos.toml` for targeted, project-specific false positives
- Initial enforcement scope limited to the website directory: `arewesafetycriticalyet.org/`
- Use Conventional Commits for all commits in this rollout

## Execution checklist

- [x] 1) Capture baseline context
  - [x] Confirm existing workflows in `.github/workflows/` and note that typo checking does not already exist.
  - [x] Confirm `_typos.toml` does not already exist at repo root.
  - [x] Confirm website directory path to scope checks:
    - [x] `arewesafetycriticalyet.org/` (deployed in `.github/workflows/arewesafetycriticalyet-org.yml`)
    - [x] Contains site config (`arewesafetycriticalyet.org/docusaurus.config.ts`)
  - [x] Review the source pattern in `rustfoundation/safety-critical-rust-coding-guidelines`:
    - [x] `.github/workflows/build-guidelines.yml` (`check_typos` job)
    - [x] `_typos.toml`

- [x] 2) Sync base branches (as needed)
  - [x] Inspect remotes:
    - [x] `git remote -v`
  - [x] If `upstream` is missing, add it:
    - [x] `git remote add upstream https://github.com/rustfoundation/safety-critical-rust-consortium.git`
  - [x] Fetch latest refs:
    - [x] `git fetch --prune upstream`
    - [x] `git fetch --prune origin`
  - [x] Update local `main` from `upstream/main`:
    - [x] `git checkout main`
    - [x] `git merge --ff-only upstream/main`
  - [x] If needed, sync `origin/main` with `upstream/main`:
    - [x] Compare divergence: `git rev-list --left-right --count origin/main...upstream/main`
    - [x] If `origin/main` is behind and project policy allows:
      - [x] `git push origin upstream/main:main`
    - [x] If `origin/main` is ahead or diverged, stop and coordinate (do not force push)

- [x] 3) Create working branch
  - [x] Create feature branch (recommended):
    - [x] `git checkout -b chore/add-typos-ci`
  - [x] Confirm branch is active:
    - [x] `git status -sb`

- [x] 4) Add dedicated typo-check workflow
  - [x] Create `.github/workflows/check-typos.yml`.
  - [x] Add triggers:
    - [x] `pull_request`
    - [x] `push` to `main`
    - [x] `merge_group` (to support merge queue)
  - [x] Add one job on `ubuntu-latest` with stable check name and steps:
    - [x] Job id: `check_typos`
    - [x] Job name: `check_typos` (for predictable branch-protection context)
    - [x] `actions/checkout@v4`
    - [x] `crate-ci/typos@v1.40.0` with website-only scope:
      - [x] `with.files: ./arewesafetycriticalyet.org`
  - [x] Add `permissions: contents: read` at workflow level.
  - [x] Keep scope narrow: this workflow should only check typos in website content.

- [x] 5) Add root typo configuration
  - [x] Create `_typos.toml` at repository root.
  - [x] Start with minimal configuration and no broad ignores.
  - [x] Add only targeted entries for this repo:
    - [x] `default.extend-words` for valid domain/project terms
    - [x] `default.extend-ignore-identifiers-re` for known identifier patterns
    - [x] file exclusions only if absolutely necessary (for generated/noisy files)
  - [x] Keep configuration compatible with future expansion to whole-repo checks.

- [ ] 6) Calibrate and clean up findings
  - [x] Run local preflight before pushing (recommended):
    - [x] If needed, install CLI: `cargo install typos-cli --locked`
    - [x] Run scoped check: `typos arewesafetycriticalyet.org`
  - [x] Run the workflow in CI (PR and/or merge queue).
  - [x] For each failure:
    - [x] Fix true spelling mistakes in source/docs.
    - [x] Add precise false-positive allowances to `_typos.toml`.
  - [x] Re-run until typo check passes cleanly.

- [x] 7) Optional contributor documentation
  - [x] Decide whether to document local typo checks in `CONTRIBUTING.md`.
  - [x] If yes, add a short section with one recommended local command (for faster feedback before pushing).

- [x] 8) Prepare commits (Conventional Commits)
  - [x] Review staged/unstaged changes before committing:
    - [x] `git status -sb`
    - [x] `git diff`
  - [x] Use one of these commit strategies:
    - [x] **Recommended (split commits)**
      - [x] `ci: add website-scoped typos check workflow`
      - [x] `chore: add baseline typos config`
      - [x] `fix(docs): correct typo in mission heading` (real typo fixed)
      - [x] `docs: add local typo check command` (`CONTRIBUTING.md` updated)
    - [ ] **Alternative (single commit)**
      - [ ] `ci: add website-scoped typos checks`
  - [x] Ensure each commit message is Conventional Commit formatted.

- [ ] 9) Final validation and rollout
  - [x] Ensure the new workflow passes on a PR branch.
  - [ ] Ensure no existing deploy/automation workflows were impacted.
  - [x] Push branch to origin:
    - [x] `git push -u origin chore/add-typos-ci`
  - [x] Open PR with clear summary and rationale.
  - [x] Record exact required status check context from the PR checks tab:
    - [x] Verify it appears as `check_typos`
  - [ ] Configure branch protection to require typo check immediately:
    - [ ] Require `check_typos` on `main` before merge
  - [ ] Future scope note (as needed): expand from `arewesafetycriticalyet.org/` to full repo once baseline noise is proven low.

## Suggested workflow file (reference)

Use this as the starting point for `.github/workflows/check-typos.yml`:

```yaml
name: Check typos

permissions:
  contents: read

on:
  pull_request:
  push:
    branches:
      - main
  merge_group:

jobs:
  check_typos:
    name: check_typos
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check for typos
        uses: crate-ci/typos@v1.40.0
        with:
          files: ./arewesafetycriticalyet.org
```

## Acceptance criteria

- [ ] CI runs typo checks on `pull_request` and pushes to `main` (and `merge_group`).
- [ ] `_typos.toml` exists and contains focused, minimal exceptions.
- [ ] Typos CI is scoped to `arewesafetycriticalyet.org/` for initial rollout.
- [ ] Repository baseline passes typo checks, or remaining exceptions are explicitly justified.
- [ ] Commits follow Conventional Commits format and clearly separate CI/config/content changes.
- [ ] Branch protection requires `check_typos` immediately after rollout.
- [ ] Plan is executable by a new session without additional context.

## Handoff notes for a new session

- [ ] Start from this plan file and execute items in order.
- [ ] Keep initial enforcement focused on `arewesafetycriticalyet.org/`; expand scope later if needed.
- [ ] Prefer fixing typos over adding allowlist entries.
- [ ] Avoid broad excludes; keep signal high for future contributors.
- [ ] Keep action versions pinned as in the source pattern unless intentionally upgrading.
- [ ] Remember: making `check_typos` required is a branch-protection setting (GitHub config), not a git commit.
