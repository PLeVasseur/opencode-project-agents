---
name: issue-fix
description: Fix one GitHub issue end to end for this repo.
compatibility: opencode
---

# Issue Fix

## Purpose

Provide a consistent workflow to fix a single GitHub issue URL for this repo.

## Inputs

- Required: `ISSUE_URL: <url>`

## Steps

1. Fetch the issue and read it fully.
2. Summarize intent, acceptance criteria, and constraints.
3. Scan the repo for impacted files, tests, and workflows. Use the explore subagent if helpful.
4. Create a plan file at `$OPENCODE_CONFIG_DIR/plans/issue-<id>-<slug>.md`.
5. Implement the fix in the repo.
6. Run relevant checks or tests (follow project instructions for tooling).
7. Summarize changes, files touched, and test results.
8. If the user asked for a commit or PR, follow git conventions and include `Closes #<id>` in the PR body. If not requested, ask for the next step.

## Output

- Summary of the fix and rationale
- File list
- Tests or checks run
- Next steps
