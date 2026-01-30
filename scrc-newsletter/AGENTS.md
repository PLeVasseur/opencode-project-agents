# Project Instructions

## Quick Commands
Use UTC date ranges. Default to previous calendar month unless the user specifies a range.

Refresh cache:
```
uv run python tools/newsletter/fetch_activity.py --month YYYY-MM
```

Lint and tests:
```
uv run ruff check tools/newsletter
uv run python -m unittest discover -s tools/newsletter/tests
```

Set a range:
```
START=2026-01-01
END=2026-01-31
```

Repos:
```
rustfoundation/safety-critical-rust-consortium
rustfoundation/safety-critical-rust-coding-guidelines
rustfoundation/safety-critical-rust-consortium-rfcs
```

Merged PRs:
```
gh pr list --repo rustfoundation/safety-critical-rust-consortium --state merged --search "merged:$START..$END" --limit 100
gh pr list --repo rustfoundation/safety-critical-rust-coding-guidelines --state merged --search "merged:$START..$END" --limit 100
gh pr list --repo rustfoundation/safety-critical-rust-consortium-rfcs --state merged --search "merged:$START..$END" --limit 100
```

Closed issues:
```
gh issue list --repo rustfoundation/safety-critical-rust-consortium --state closed --search "closed:$START..$END" --limit 100
gh issue list --repo rustfoundation/safety-critical-rust-coding-guidelines --state closed --search "closed:$START..$END" --limit 100
gh issue list --repo rustfoundation/safety-critical-rust-consortium-rfcs --state closed --search "closed:$START..$END" --limit 100
```

Releases:
```
gh release list --repo rustfoundation/safety-critical-rust-consortium --limit 20
gh release list --repo rustfoundation/safety-critical-rust-coding-guidelines --limit 20
gh release list --repo rustfoundation/safety-critical-rust-consortium-rfcs --limit 20
```

## Skills
- Cache refresh: `skills/newsletter-cache-refresh/SKILL.md`
- Email newsletter: `skills/newsletter-email/SKILL.md`
- Bluesky post: `skills/newsletter-bluesky/SKILL.md`
- Bluesky repost caption: `skills/newsletter-bluesky-repost/SKILL.md`
- X post: `skills/newsletter-x/SKILL.md`
- LinkedIn post: `skills/newsletter-linkedin/SKILL.md`

## Overview
This workspace defines skills and instructions for drafting a monthly Safety-Critical Rust Consortium newsletter across multiple channels. Content is derived from activity in the three SCRC repositories and adapted per medium.

## Workflow
- Refresh the cache using `tools/newsletter/fetch_activity.py` before drafting posts.
- Use `.cache/YYYY-MM/summary.json` and per-repo JSON files as the source of truth.
- Draft a master list of highlights before adapting to each medium so the outputs stay consistent.
- Save each output to `newsletter/YYYY-MM/<medium>.md`.
- OpenCode setup: ensure `opencode-env.sh` is sourced so `OPENCODE_CONFIG_DIR` is set and skills are discoverable.

## Content and Formatting Rules
- Output is Markdown files, but use plain text only.
- Do not use Markdown links or images. Use plain-text URLs only if required.
- If a platform needs an attachment, add a plain-text `Attachments:` section listing the files or descriptions to attach.
- Keep tone professional, factual, and concise. Avoid hype and speculation.

## Sources
- `rustfoundation/safety-critical-rust-consortium`
- `rustfoundation/safety-critical-rust-coding-guidelines`
- `rustfoundation/safety-critical-rust-consortium-rfcs`

## Files to Know
- `.cache/` cached repo activity, grouped by month and repo.
- `tools/newsletter/fetch_activity.py` cache refresh CLI.
- `pyproject.toml` uv and ruff configuration.
- `newsletter/` outputs live here, organized by `YYYY-MM/`.
