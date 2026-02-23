---
name: artifact-hygiene-guard
description: Enforce plan/report artifact placement in OPENCODE config directories and keep repo clean.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: artifact-hygiene
---

## When to use

Use this skill whenever creating execution plans, validation notes, migration reports, or ad hoc investigation artifacts.

## Rules

- Plans must live in `$OPENCODE_CONFIG_DIR/plans/`.
- Reports must live in `$OPENCODE_CONFIG_DIR/reports/`.
- Do not create repo-local plan/report files by default.

## Workflow

1. Resolve config directory:
   - `printenv OPENCODE_CONFIG_DIR`
2. Write artifacts only under config dirs.
3. Before commit, run scope check:
   - `git diff --name-only --cached`
4. If repo-local artifacts were accidentally added, remove them before merge.

## Typical accidental files to reject

- `plans/*.md` in repo root
- root-level `*VALIDATION*.md`, `*REPORT*.md`, `*MIGRATION*.md`
- temporary smoke logs under tracked directories

## Report template

Always report:

1. Artifact file paths created under `$OPENCODE_CONFIG_DIR`
2. Confirmation that repo-local artifacts were not added (or were removed)
