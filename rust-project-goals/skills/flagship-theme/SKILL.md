---
name: flagship-theme
description: Create Rust project flagship themes aligned with project goals.
compatibility: opencode
metadata:
  audience: rust-project-goals
  scope: documentation
  year: "2026"
---

## What I do
- Draft or revise a flagship theme narrative using the 2026 structure and tone.
- Connect the theme to its goal docs and ensure the theme appears in navigation.
- Provide a validation checklist to prevent broken links or missing goal entries.

## When to use me
- Creating a new flagship theme page under `src/2026/`.
- Updating an existing theme to match the 2026 writing format.
- Wiring a theme into `src/2026/flagships.md` and `src/SUMMARY.md`.

## Required structure
Use this exact section order and headings:

```
# <Theme Name>

## Summary

## Motivation

### The status quo

### What we are shooting for

### Key use cases

### Design axioms

## 2026 goals

(((FLAGSHIP GOALS: <Theme Name>)))

## Frequently asked questions
```

Notes:
- The placeholder must match the theme name exactly, including punctuation.
- Do not add a metadata table or team asks; those belong in goal docs.

## Writing rules
- Summary: 1-2 sentences that state the theme's promise in plain language.
- Status quo: concrete problem framing and why it matters; avoid deep design.
- What we are shooting for: 3-5 crisp outcomes in present tense.
- Key use cases: 3-6 bullets, each starts with **Bold label** and a colon.
- Design axioms: 2-4 bullets; start with a bold, memorable phrase and 1-2 lines.
- FAQ: 2-4 questions with short answers; explain how goals relate or scope.
- Tone: direct, factual, broadly accessible; avoid marketing or hype.

## Linking and file placement
- Theme file: `src/2026/flagship-<slug>.md`.
- Slug rules: lowercase, spaces to hyphens, remove backticks, replace `&` with `ampersand`.
- Add the theme entry to `src/2026/flagships.md` with milestone links.
- Add the theme entry under 2026 in `src/SUMMARY.md`.
- Each goal in the theme must set metadata `Flagship` to the exact theme name.
- The `Flagship` metadata must be plain text, not a markdown link.

## Validation checklist
- Theme title matches the placeholder and goal metadata exactly.
- `(((FLAGSHIP GOALS: <Theme Name>)))` appears once under `## 2026 goals`.
- `src/2026/flagships.md` contains the theme and all milestone links resolve.
- `src/SUMMARY.md` lists the theme under Rust in 2026.
- No metadata table or team asks in the theme file.

## References
- Template: `src/FLAGSHIP_TEMPLATE.md`
- Exemplars: `src/2026/flagship-beyond-the-ampersand.md`,
  `src/2026/flagship-unblocking-dormant-traits.md`,
  `src/2026/flagship-secure-your-supply-chain.md`
