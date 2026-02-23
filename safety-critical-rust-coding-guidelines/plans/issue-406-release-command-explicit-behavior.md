# Issue 406 - Make /release behavior explicit and actionable

## Context
- The current `/release` behavior is functionally correct but unclear to users.
- Plain `/release` means "release myself".
- Releasing another reviewer requires `/release @username` and triage+ permission.
- In PR 331, a collaborator ran plain `/release` while not assigned reviewer and got `not the current reviewer`, which is accurate but not actionable enough.

## Goals
- [x] Make command behavior explicit in help and guidance text.
- [x] Improve failure messaging so users know exactly what to do next.
- [x] Add regression coverage for the confusing path reported in issue 406.

## Plan
- [x] Update command descriptions in `scripts/reviewer_bot.py`.
  - [x] Clarify `/release [reason]` as releasing your own assignment.
  - [x] Clarify `/release @username [reason]` as releasing someone else (triage+).
- [x] Update reviewer guidance text blocks in `scripts/reviewer_bot.py`.
  - [x] Update `get_issue_guidance` command text.
  - [x] Update `get_fls_audit_guidance` command text.
  - [x] Update `get_pr_guidance` command text.
- [x] Improve `handle_release_command` self-release failure messaging.
  - [x] Include current reviewer username when another reviewer is assigned.
  - [x] Include a direct hint for `/release @current_reviewer` (triage+) when likely intended.
- [x] Add regression tests in `.github/reviewer-bot-tests/test_reviewer_bot.py`.
  - [x] Cover non-current reviewer using plain `/release` and getting actionable guidance.
  - [x] Cover assignee-only fallback behavior when tracked state is missing.
- [x] Run checks.
  - [x] `uv run ruff check --fix`
  - [x] `uv run python -m pytest .github/reviewer-bot-tests/test_reviewer_bot.py -k release`
  - [x] `uv run python -m pytest .github/reviewer-bot-tests/test_reviewer_bot.py`

## Success criteria
- [x] Help text and reviewer guidance clearly distinguish self-release vs releasing another reviewer.
- [x] `/release` error response for non-current reviewers is specific and actionable.
- [x] New regression tests pass and prevent reintroduction of ambiguous behavior.
- [x] Reviewer-bot test suite remains green.
