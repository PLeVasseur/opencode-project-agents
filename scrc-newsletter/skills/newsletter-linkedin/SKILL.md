---
name: newsletter-linkedin
description: Draft the monthly SCRC post for LinkedIn.
compatibility: opencode
---

# Monthly LinkedIn Post

## Purpose
Create a LinkedIn post summarizing monthly SCRC activity with a professional tone.

## Inputs
- Required: `MONTH: YYYY-MM`
- Optional: `START_DATE: YYYY-MM-DD`
- Optional: `END_DATE: YYYY-MM-DD`
- Optional: `CACHE_DIR: default .cache`
- Optional: `HIGHLIGHTS: list of must-include items`
- Optional: `CTA: call to action text`
- Optional: `NEWSLETTER_URL: plain-text URL`

## Steps
1. Determine the date range. Use `START_DATE` and `END_DATE` if provided, otherwise use the full calendar month for `MONTH`.
2. Load cached data from `.cache/YYYY-MM/summary.json` and per-repo JSON files. If missing, run the cache refresh skill first.
3. Summarize 3 to 5 highlights across the three repos.
4. Draft 3 to 5 short paragraphs targeting 900 to 1500 characters.
5. Use a professional tone and clearly attribute each highlight to its repo.
6. If a repo had no activity, state that explicitly.
7. Include a short CTA and an optional plain-text URL if provided.
8. Use plain text only. Do not use Markdown links or images.
9. Include 2 to 4 relevant hashtags on the final line.
10. If attachments are needed, add an `Attachments:` section with plain-text file names or descriptions.
11. Save to `newsletter/YYYY-MM/linkedin.md`.

## Output
- The Markdown file path.
