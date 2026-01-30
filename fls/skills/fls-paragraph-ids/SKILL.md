---
name: fls-paragraph-ids
description: Paragraph ID placement, generation, and exceptions for FLS.
compatibility: opencode
---

## What I do

- Explain where `:dp:` IDs are required (paragraphs, list items, table first cells)
- Call out exceptions for `index` and `changelog` via `lint_no_paragraph_ids`
- Provide the ID generation command `./generate-random-ids.py`

## When to use me

- Adding or moving paragraphs and you hit paragraph-id lint warnings

## References

- `exts/ferrocene_spec/README.rst`
- `exts/ferrocene_spec_lints/require_paragraph_ids.py`
- `src/conf.py`
