# Plan: Issue #393 Spec Lock Audit and Update (2026-02-10)

## Scope

- [x] Keep work isolated from current `/rectify` remediation branch and PR.
- [x] Execute audit from `main` synced to `upstream/main`.
- [x] Provide an evidence-based report under `$OPENCODE_CONFIG_DIR/reports/`.
- [x] Only proceed with spec lock update PR if audit evidence shows no guideline updates are needed.

## Execution Checklist

### 1) Preparation

- [x] Record current branch and verify clean working tree.
- [x] Ensure `$OPENCODE_CONFIG_DIR/reports/` exists.
- [x] Fetch `upstream/main` and switch to local `main`.
- [x] Fast-forward local `main` to `upstream/main`.

### 2) Audit and Assessment

- [x] Run `uv run python scripts/fls_audit.py` on `main`.
- [x] Run `uv run python scripts/fls_audit.py --print-diffs` on `main`.
- [x] Review `build/fls_audit/report.md`.
- [x] Review `build/fls_audit/report.json`.
- [x] Cross-check findings against issue #393 and determine whether guideline updates are required.

### 3) Reporting

- [x] Write audit assessment report to `$OPENCODE_CONFIG_DIR/reports/issue-393-fls-audit-assessment-2026-02-10.md`.

### 4) Spec Lock Update Path (Only if no guideline updates are required)

- [x] Create a new branch from current `upstream/main`.
- [x] Run `./make.py --update-spec-lock-file`.
- [x] Verify changed files and confirm scope is spec update only.
- [x] Commit with a Conventional Commit message.
- [x] Push branch and open PR targeting `rustfoundation/safety-critical-rust-coding-guidelines` `main`, referencing #393.

### 5) Stop Condition

- [x] Stop after reporting and PR creation, and wait for user merge before resuming `/rectify` plan.
