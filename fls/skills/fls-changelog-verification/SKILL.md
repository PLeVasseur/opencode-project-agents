---
name: fls-changelog-verification
description: Verify changelog entries against spec changes.
compatibility: opencode
---

## What I do

- Identify the diff range and spec files that changed in `src/`.
- Extract paragraph IDs added or removed in a diff and locate the `:dp:` IDs that own modified text.
- Check whether syntax categories, sections, or glossary entries changed and should be recorded.
- Provide a checklist to ensure `src/changelog.rst` has the right release entry and references (`:p:`, `:s:`, `:t:`, `:ref:`).

## When to use me

- After editing spec text for a Rust release note item.
- When reviewing a PR that adds or fixes changelog entries.

## Diff source variants

- Feature PR branch checked out: `git diff main...HEAD -- src`
- Changelog-only follow-up PR: diff the spec-change range `git diff <spec-base>..<spec-head> -- src` or inspect with `gh pr diff <spec-pr> --repo rust-lang/fls`
- Local WIP: `git diff -- src` (unstaged) and `git diff --cached -- src` (staged)

## Workflow

1. Pick a base for the diff (default `main...HEAD`, or `origin/main...HEAD` if you have the remote).
2. List changed spec files:
   `git diff --name-only main...HEAD -- src`
3. Collect new and removed paragraph IDs:
   `git diff --unified=0 main...HEAD -- src | rg '^[+]\s*:dp:'`
   `git diff --unified=0 main...HEAD -- src | rg '^[-]\s*:dp:'`
4. Identify changed paragraphs with existing IDs:
   - For each diff hunk, find the nearest `:dp:` above the change in the file and record that ID.
   - Use `git diff --unified=3 main...HEAD -- src/path.rst` and search in the file with `rg -n ':dp:' src/path.rst`.
5. Check for other changelog-worthy items:
   - `.. syntax::` blocks or grammar category names -> "New/Changed syntax" using `:s:`.
   - New section anchors (`.. _fls_...:`) -> "New section" using `:ref:`.
   - New glossary entries in `src/glossary.rst` -> "New glossary entry" using `:t:`.
6. Cross-check `src/changelog.rst`:
   - Entry is under the correct "Language changes in Rust X.Y.Z".
   - Upstream PR link is present.
   - Lists of changed/new/removed paragraphs match the IDs you collected (`:p:`).
   - "No change: ..." reason is present when appropriate.

## References

- `src/changelog.rst`
- `src/glossary.rst`
- `exts/ferrocene_spec/README.rst`
