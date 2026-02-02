---
name: newsletter-email
description: Draft the monthly Safety-Critical Rust Consortium email newsletter.
compatibility: opencode
---

# Monthly Newsletter Email

## Purpose
Create the monthly email newsletter covering activity across the SCRC repositories.

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
3. Select 5 to 10 highlights that show progress, decisions, and deliverables. Group by repo and name the repo in each section.
4. Draft the email with these sections:
   - `Subject:` line
   - Intro paragraph (2 to 4 sentences)
   - Highlights by repo (bullets)
   - Optional metrics snapshot (counts of PRs, issues, releases)
   - Looking ahead
   - CTA and closing
5. Target 350 to 450 words (about a 3 minute read).
6. Use a professional, factual tone. Avoid hype and speculation.
7. If no CTA is provided, use a neutral closing. Do not imply special labels, featured items, or tracking unless explicitly confirmed.
8. Output plain text in Markdown. Do not use Markdown links or images. Use plain-text URLs only if needed.
9. If a URL is used, put it on its own line immediately after the sentence that introduces it.
10. If attachments are needed, add an `Attachments:` section with plain-text file names or descriptions.
11. Save to `newsletter/YYYY-MM/email.md`.

## Output
- The Markdown file path.
- Any assumptions or missing data.
