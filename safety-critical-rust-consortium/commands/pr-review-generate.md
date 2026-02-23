---
description: Generate split PR review feedback files (00 summary plus 01+ issues)
agent: build
---

Use the `skill` tool to load `pr-review-split-format`, then follow it before generating any files.

Task inputs:

- PR number: `$1` (required)
- Optional slug override: `$2`

Generate review files for the target PR in this format:

- Output directory: `$OPENCODE_CONFIG_DIR/pr-reviews/<pr-number>-<slug>/`
- Required files:
  - `00-summary.md`
  - `01-<issue>.md`
  - `02-<issue>.md`
  - and so on (one issue per file)

Rules:

- If `$2` is empty, derive slug from PR title.
- Resolve and use the absolute config path from `OPENCODE_CONFIG_DIR`.
- Include YAML frontmatter for every file.
- Inline issue files must include `comment_type: inline`, `target_file`, `line_start`, `line_end`, and `context`.
- General comments must use `comment_type: general` and null line fields.
- Do not post anything to GitHub during generation.
- Keep comment bodies copy-paste ready for GitHub review comments.

At the end, return:

- Created directory path
- Ordered file list
- Count of inline issue files
