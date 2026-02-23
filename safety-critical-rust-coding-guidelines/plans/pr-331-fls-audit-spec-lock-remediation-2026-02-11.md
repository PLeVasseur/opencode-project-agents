# Plan: PR #331 FLS Audit + Spec Lock Remediation (2026-02-11)

## Goal

- [x] Confirm the exact FLS drift affecting PR `#331` and determine whether guideline updates are required.
- [x] If no guideline updates are required, open a spec-lock-only PR against `upstream/main`.
- [x] Pause for user merge of that PR, then resume and verify PR `#331` CI status.

## Execution Checklist

### 1) Preparation and Isolation

- [x] Record current branch and working-tree state (`git status --short --branch`).
- [x] Fetch latest refs from `origin` and `upstream`.
- [x] Check out local `main` and fast-forward it to `upstream/main`.

### 2) Audit and Evidence Collection

- [x] Run `uv run python scripts/fls_audit.py --summary-only` on `main`.
- [x] Run `uv run python scripts/fls_audit.py` on `main`.
- [x] Run `uv run python scripts/fls_audit.py --print-diffs` on `main`.
- [x] Review `build/fls_audit/report.md` and `build/fls_audit/report.json`.
- [x] Cross-check audit findings against the Netlify failure evidence from PR `#331`.
- [x] Decide whether guideline updates are required (`yes`/`no`) (decision: no).

### 3) Write Assessment Report

- [x] Write a report to `$OPENCODE_CONFIG_DIR/reports/pr-331-fls-audit-assessment-2026-02-11.md` containing:
- [x] Summary counts (added/removed/content changed/renumbered/header/affected guidelines).
- [x] Evidence for whether any guideline updates are needed.
- [x] Recommendation and next action.

### 4) Decision Gate

- [x] If guideline updates are required: stop and report findings (do not open spec-lock-only PR) (not applicable).
- [x] If guideline updates are **not** required: continue with spec-lock update path.

### 5) Spec Lock Update PR Path (Only if no guideline edits needed)

- [x] Create branch from `upstream/main`: `chore/spec-lock-update-pr331-20260211`.
- [x] Run `./make.py --update-spec-lock-file`.
- [x] Verify only `src/spec.lock` changed (`git diff --name-only`).
- [x] Commit with Conventional Commit message: `chore: update FLS spec lock`.
- [x] Push branch to `origin`.
- [x] Open PR targeting `rustfoundation/safety-critical-rust-coding-guidelines:main` with `Closes #393` if appropriate.
- [x] Share PR URL with user.

### 6) User Merge Gate (Required Pause)

- [x] **Stop and tell user to merge the spec update PR.**
- [x] Wait for explicit user confirmation that merge to `upstream/main` is complete.

### 7) Resume After Merge and Re-check PR #331

- [x] Fetch `upstream/main` and confirm the spec-lock PR commit is present.
- [x] Check out `docs/update-contributing-md-with-bot-details`.
- [x] Rebase or merge latest `upstream/main` into `docs/update-contributing-md-with-bot-details` to pick up updated `src/spec.lock`.
- [x] Push only `docs/update-contributing-md-with-bot-details` to `origin`.
- [x] Re-check PR `#331` checks (`gh pr checks 331 --repo rustfoundation/safety-critical-rust-coding-guidelines`).
- [x] Confirm whether Netlify/FLS checks pass; if not, capture failing output and recommend next fix.

## Guardrails

- [x] Do not merge directly to `main` from local git.
- [x] Keep spec-lock remediation isolated from unrelated changes.
- [x] Use `uv run python ...` for Python commands.
- [x] Stop immediately and report exact command output if blocked.
