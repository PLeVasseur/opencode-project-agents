---
name: fls-spec-lock-remediation
description: Audit FLS drift for an issue, write an evidence report, and open a spec-lock-only PR when guideline updates are not required.
compatibility: opencode
---

# FLS Spec Lock Remediation

## Purpose

Provide a repeatable workflow to handle a spec lock drift issue end-to-end:

1. audit and assess impact,
2. document evidence,
3. open a spec-lock-only PR when guideline updates are not needed.

## Inputs

- Required: `ISSUE_URL: <url>`
- Optional: `BASE_REF: upstream/main` (default: `upstream/main`)
- Optional: `HEAD_OWNER: PLeVasseur` (default: `PLeVasseur`)

## Checklist

### 1) Preparation

- [ ] Read issue details from `ISSUE_URL` and capture issue number.
- [ ] Create/update plan file at `$OPENCODE_CONFIG_DIR/plans/issue-<id>-spec-lock-remediation-<date>.md`.
- [ ] Record current branch and working-tree state.
- [ ] Ensure `$OPENCODE_CONFIG_DIR/reports/` exists.
- [ ] Fetch `upstream/main`, switch to local `main`, and fast-forward to `upstream/main`.

### 2) Audit and Evidence

- [ ] Run `uv run python scripts/fls_audit.py`.
- [ ] Run `uv run python scripts/fls_audit.py --print-diffs`.
- [ ] Review `build/fls_audit/report.md` and `build/fls_audit/report.json`.
- [ ] Cross-check local audit output with the issue report (including baseline/current commit differences).
- [ ] Decide whether guideline updates are required.

### 3) Report

- [ ] Write a report at `$OPENCODE_CONFIG_DIR/reports/issue-<id>-fls-audit-assessment-<date>.md` containing:
  - summary counts,
  - affected-guideline evidence,
  - rationale for whether guideline edits are needed,
  - recommendation.

### 4) Decision Gate

- [ ] If guideline updates are required: stop after report and return findings (do not open spec-lock-only PR).
- [ ] If guideline updates are not required: continue with spec lock update path below.

### 5) Spec Lock Update Path (No guideline edits needed)

- [ ] Create a fresh branch from `upstream/main`:
  - `chore/spec-lock-update-issue-<id>-<yyyymmdd>`
- [ ] Run `./make.py --update-spec-lock-file`.
- [ ] Verify scope is spec lock only (`git diff --name-only` should contain only `src/spec.lock`).
- [ ] Commit using Conventional Commits:
  - `chore: update FLS spec lock`
- [ ] Push branch to origin.
- [ ] Open PR targeting `rustfoundation/safety-critical-rust-coding-guidelines` `main` with:
  - `--repo rustfoundation/safety-critical-rust-coding-guidelines`
  - `--head PLeVasseur:<branch>`
  - `Closes #<id>` in PR body.

### 6) Stop Condition

- [ ] Stop after PR creation and wait for user merge confirmation before resuming unrelated work.

## Guardrails

- Do not merge to `main`.
- Keep this work isolated from unrelated branches/PRs.
- Use `uv run python ...` for Python scripts.
- Do not edit guideline files unless the decision gate concludes edits are required.

## Output

- Plan file path
- Report file path
- Decision summary (`guideline updates required: yes/no`)
- PR URL (if opened)
