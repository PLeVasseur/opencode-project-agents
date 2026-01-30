# Newsletter Cache Tooling Plan

## Goal
Build a Python tool that pulls monthly activity from the SCRC GitHub repos via `gh`, writes cached JSON under `.cache/`, and supports the newsletter skills. Include unit tests and verification steps.

## Decisions
- Tooling location: `tools/newsletter/` in the repo.
- Data source: `gh` CLI for commits, PRs, issues, and releases.
- Date range default: previous calendar month (UTC).
- Cache layout:
  - `.cache/YYYY-MM/summary.json`
  - `.cache/YYYY-MM/<owner>-<repo>/commits.json`
  - `.cache/YYYY-MM/<owner>-<repo>/prs.json`
  - `.cache/YYYY-MM/<owner>-<repo>/issues.json`
  - `.cache/YYYY-MM/<owner>-<repo>/releases.json`
- Filter merge commits (multiple parents).
- Add unit tests for date-range handling and filtering.

## Files to Add or Update
- `tools/newsletter/fetch_activity.py` (CLI tool)
- `tools/newsletter/tests/test_fetch_activity.py` (unit tests)
- `tools/__init__.py`, `tools/newsletter/__init__.py`
- `pyproject.toml` (uv + ruff config)
- `.gitignore` (ignore `.cache/` and Python artifacts)
- `.cache/` directory
- `~/opencode-project-agents/scrc-newsletter/AGENTS.md` (update commands and cache usage)
- `~/opencode-project-agents/scrc-newsletter/skills/*` (use cache, add refresh skill)

## Implementation Steps
1. Create `.cache/`, `tools/newsletter/`, and `tools/newsletter/tests/` directories.
2. Implement `fetch_activity.py` with:
   - Date range resolution (month or explicit start/end).
   - `gh` commands for commits, merged PRs, closed issues, releases.
   - Merge-commit filtering and JSON normalization.
   - Cache write logic and `summary.json` aggregation.
3. Add unit tests for date-range calculation and filtering behavior.
4. Add uv/ruff config in `pyproject.toml` and ignore `.cache/` in `.gitignore`.
5. Update AGENTS and skills to use the cache and add a cache-refresh skill.

## Verification
- Lint: `uv run ruff check tools/newsletter`
- Unit tests: `uv run python -m unittest discover -s tools/newsletter/tests`
- Manual check: `uv run python tools/newsletter/fetch_activity.py --month YYYY-MM` and verify `.cache/YYYY-MM/summary.json` and per-repo JSON files exist.
