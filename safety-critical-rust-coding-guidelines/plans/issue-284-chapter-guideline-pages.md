# Issue 284 - Chapter guideline pages

## Intent
- Render chapter landing pages as a flat list of guideline links rather than inlining guideline content.
- Keep guideline content in per-guideline source files while making each guideline its own page.

## Acceptance Criteria
- Chapter landing pages list guideline links instead of embedding guideline bodies.
- Each guideline renders on its own page and is reachable from its chapter list.
- Guideline content remains unchanged.
- Documentation build continues to work with the new structure.

## Plan
1. Collapse guidelines to single `.rst` pages (remove `.rst.inc` content files) and keep chapter indexes as toctree lists.
2. Update scripts and tooling to emit, scan, and validate `.rst` guidelines only.
3. Audit make.py/build_cli paths and close any flag gaps (e.g., --check-links).
4. Run lint, scripts, tests, and make.py code paths; fix failures.

## Verification Checklist
- Lint: `uv run ruff check --fix`
- Script: `uv run python generate_guideline_templates.py --number-of-templates 1`
- Script (issue JSON): `gh issue view 135 --repo rustfoundation/safety-critical-rust-coding-guidelines --json number,title,body | uv run python scripts/guideline-from-issue.py`
- Script (issue JSON): `gh issue view 135 --repo rustfoundation/safety-critical-rust-coding-guidelines --json number,title,body | uv run python scripts/generate-rst-comment.py`
- Script: `uv run python scripts/split_guidelines.py --dry-run --all --update-index`
- Script: `uv run python scripts/migrate_rust_examples.py --dry-run`
- Script: `uv run python scripts/extract_rust_examples.py --extract`
- Script: `uv run python scripts/extract_rust_examples.py --test`
- Script (network): `uv run python scripts/fls_audit.py --summary-only`
- Manual audit: `scripts/fls_audit_issue.py` (credentialed)
- Manual audit: `scripts/reviewer_bot.py` (credentialed)
- Tests: `uv run pytest`
- make.py default: `uv run python make.py`
- make.py XML: `uv run python make.py --xml`
- make.py debug: `uv run python make.py --debug`
- make.py offline: `uv run python make.py --offline`
- make.py ignore spec lock: `uv run python make.py --ignore-spec-lock-diff`
- make.py linkcheck path: `uv run python make.py --check-links`
- make.py URL validation (network): `uv run python make.py --validate-urls`
- make.py serve (startup check): `uv run python make.py --serve` (terminate after confirming startup)
- Skip `uv run python make.py --update-spec-lock-file` unless explicitly requested.
