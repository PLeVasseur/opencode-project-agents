---
name: pr-review-split-format
description: Generate split PR feedback files with line-anchored frontmatter for draft review posting
---

## Purpose

Use this skill when producing reusable PR review feedback files that will later be posted as pending inline comments by automation.

## Output contract

Create a directory:

`$OPENCODE_CONFIG_DIR/pr-reviews/<pr-number>-<slug>/`

Inside it, create:

- `00-summary.md` (overall summary, manual final review body)
- `01-<issue>.md`
- `02-<issue>.md`
- etc.

Requirements:

- One issue per `01+` file.
- Numbering must be gapless and sorted.
- Keep file names short and descriptive.

## Frontmatter schema

All files must include YAML frontmatter.

Inline issue files (`01+`) must include:

```yaml
pr: <number>
comment_type: inline
target_file: <path-or-unique-suffix>
line_start: <int>
line_end: <int>
context: "<quoted snippet around target line>"
```

General files (summary or non-inline feedback) must include:

```yaml
pr: <number>
comment_type: general
target_file: null
line_start: null
line_end: null
context: "<short label>"
```

## Content rules

- Bodies must be copy-paste ready for GitHub comments.
- Keep each issue body focused and actionable.
- Avoid duplicate issues across files.
- Put blocking/build/correctness issues first.
- Keep `00-summary.md` concise and prioritized.

## Line-anchor quality rules

- Do not invent line numbers.
- Anchor to lines that are part of the PR diff.
- Include enough context text to confirm the right location.
- If feedback is not line-specific, use `comment_type: general`.

## Suggested generation workflow

1. Read PR metadata and file list.
2. Inspect relevant diff hunks for line-anchored issues.
3. Draft `00-summary.md`.
4. Draft `01+` issue files in priority order.
5. Verify frontmatter for every file.

## Final checklist before returning

- Directory exists under `$OPENCODE_CONFIG_DIR/pr-reviews/`.
- `00-summary.md` exists.
- Every `01+` file has valid inline frontmatter and non-empty body.
- Numbering is gapless.
- Output is ready for `/pr-review-draft ... --dry-run`.
