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
5. Use a professional, factual tone. Avoid hype and speculation.
6. Output plain text in Markdown. Do not use Markdown links or images. Use plain-text URLs only if needed.
7. If attachments are needed, add an `Attachments:` section with plain-text file names or descriptions.
8. Save to `newsletter/YYYY-MM/email.md`.

## Output
- The Markdown file path.
- Any assumptions or missing data.
