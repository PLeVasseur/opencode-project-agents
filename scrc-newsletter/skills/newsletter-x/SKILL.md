---
name: newsletter-x
description: Draft the monthly SCRC post for X.
compatibility: opencode
---

# Monthly X Thread

## Purpose
Create a concise thread for X summarizing monthly SCRC activity.

## Inputs
- Required: `MONTH: YYYY-MM`
- Optional: `START_DATE: YYYY-MM-DD`
- Optional: `END_DATE: YYYY-MM-DD`
- Optional: `CACHE_DIR: default .cache`
- Optional: `HIGHLIGHTS: list of must-include items`
- Optional: `NEWSLETTER_URL: plain-text URL`

## Steps
1. Determine the date range. Use `START_DATE` and `END_DATE` if provided, otherwise use the full calendar month for `MONTH`.
2. Load cached data from `.cache/YYYY-MM/summary.json` and per-repo JSON files. If missing, run the cache refresh skill first.
3. Draft a thread of 3 to 4 posts. Each post is one paragraph, separated by a blank line. Do not number the posts.
4. Use a relaxed, all-lowercase tone.
5. Each post must state which repo it refers to in natural language.
6. Use plain text only. Do not use Markdown links or images.
7. Include at most one plain-text URL per post, and only if it directly relates to the highlight in that post.
8. Limit hashtags to 0 to 2 total across the thread. Avoid @ mentions unless requested.
9. Save to `newsletter/YYYY-MM/x.md`.

## Output
- The Markdown file path.
