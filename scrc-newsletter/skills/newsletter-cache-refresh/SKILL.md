---
name: newsletter-cache-refresh
description: Refresh cached SCRC activity data using the gh-based tool.
compatibility: opencode
---

# Newsletter Cache Refresh

## Purpose
Populate `.cache/YYYY-MM/` with activity data from the three SCRC repositories.

## Inputs
- Required: `MONTH: YYYY-MM`
- Optional: `START_DATE: YYYY-MM-DD`
- Optional: `END_DATE: YYYY-MM-DD`
- Optional: `OUTPUT_DIR: default .cache`

## Steps
1. Resolve the date range. Use `START_DATE` and `END_DATE` if provided, otherwise use the full calendar month for `MONTH`.
2. Run the cache tool:
   - `uv run python tools/newsletter/fetch_activity.py --month YYYY-MM`
   - If a custom range is needed: `--start-date` and `--end-date`.
3. Confirm the outputs exist:
   - `.cache/YYYY-MM/summary.json`
   - `.cache/YYYY-MM/<owner>-<repo>/commits.json`
   - `.cache/YYYY-MM/<owner>-<repo>/prs.json`
   - `.cache/YYYY-MM/<owner>-<repo>/issues.json`
   - `.cache/YYYY-MM/<owner>-<repo>/releases.json`
4. Note any missing data or gh authentication errors.

## Output
- Cache folder path and list of generated files.
- Any errors or missing data.
