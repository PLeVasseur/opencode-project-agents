# Issue 371 - Label command parsing and naming alignment

## Context
- /label parsing breaks on hyphens in label names (e.g. sign-off: create pr).
- Reviewer guidance references a non-existent label name.
- Auto-PR workflow should be removed; issue-to-RST helper and snapshot tests should be renamed to reflect purpose.

## Goals
- Allow /label to handle spaces and hyphens inside label names.
- Align documentation and guidance to the existing label name: sign-off: create pr.
- Remove the auto-PR workflow, while keeping the issue-to-RST helper and its tests under accurate names.

## Plan
1. Update /label parsing in scripts/reviewer_bot.py so + or - are operators only at the start or after whitespace.
2. Add reviewer-bot tests for labels with spaces and hyphens (sign-off: create pr).
3. Update reviewer guidance to reference sign-off: create pr.
4. Remove .github/workflows/auto-pr-on-issue.yml.
5. Rename issue-to-RST helper and tests:
   - scripts/auto-pr-helper.py -> scripts/guideline-from-issue.py
   - .github/auto-pr-tests/ -> .github/guideline-from-issue-tests/
   - .github/workflows/snapshot-ci.yml -> .github/workflows/guideline-from-issue-snapshots.yml
6. Update references across docs and scripts to the new names.
7. Run:
   - uv run ruff check --fix
   - uv run pytest .github/reviewer-bot-tests

## Success criteria
- /label correctly adds/removes labels with hyphens and spaces.
- All references use sign-off: create pr.
- Auto-PR workflow file removed; helper/tests renamed and documented.
- Reviewer-bot tests pass.
