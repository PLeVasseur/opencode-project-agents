---
name: newsletter-bluesky-repost
description: Draft a short Bluesky caption for reposting the newsletter.
compatibility: opencode
---

# Bluesky Repost Caption

## Purpose
Write a short caption to accompany a Bluesky repost of the full newsletter.

## Inputs
- Required: `MONTH: YYYY-MM`
- Optional: `START_DATE: YYYY-MM-DD`
- Optional: `END_DATE: YYYY-MM-DD`
- Optional: `CACHE_DIR: default .cache`
- Optional: `HIGHLIGHTS: list of must-include items`

## Steps
1. Determine the date range. Use `START_DATE` and `END_DATE` if provided, otherwise use the full calendar month for `MONTH`.
2. Load cached data from `.cache/YYYY-MM/summary.json` and per-repo JSON files. If missing, run the cache refresh skill first.
3. Select 1 key highlight to tease the newsletter.
4. Draft a single caption that stays under 240 characters.
5. Use a relaxed, all-lowercase tone.
6. Use plain text only. Do not use Markdown links or images.
7. Do not include links in the repost caption.
8. Limit hashtags to 0 to 1. Avoid @ mentions unless requested.
9. Save to `newsletter/YYYY-MM/bluesky-repost.md`.

## Output
- The Markdown file path.
