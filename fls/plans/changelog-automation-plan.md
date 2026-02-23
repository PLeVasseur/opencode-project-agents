# Plan: Changelog Automation Script for make.py

## Requirements derived from best practices
- Detect when spec changes in `src/` need changelog updates.
- Associate changes with the current Rust release (from `version.rst`) and upstream item link when possible.
- Use Sphinx/docutils so changes are markup-aware (roles, literals, list structure), not just plaintext.
- Record new, removed, or changed paragraphs, syntax, sections, glossary entries, and role usage.
- Treat role changes (`:dt:`, `:t:`, `:s:`, `:ds:`), term additions/removals, and definition moves as changelog candidates.
- Generate explicit change tags for each detected change and include those tags in changelog entries.
- Err on the side of thoroughness: report and tag all detected change types, leaving humans to prune.
- Ensure a release section exists in `src/changelog.rst` for the current release.
- Allow "No change" entries when a language item has no spec impact.

## Proposed script placement and CLI
- New script: `tools/changelog_assistant.py` (or `generate-changelog.py` at repo root for parity with other scripts).
- CLI flags:
  - `--check` (default): verify changelog coverage for spec diffs; exit non-zero on missing entries.
  - `--update`: insert or update entries when data is sufficient.
  - `--release X.Y.Z` (default from `version.rst`).
  - `--base <git-ref>` (default: `origin/main` if available, else `main`, else `HEAD~1`).
  - `--upstream-pr` and `--title` for supplying release item metadata when not inferable.
  - `--emit-report <path>` (default: `build/changelog-diff.json` and `build/changelog-diff.md`).
  - `--require-tags` (fail check when changelog entries omit tags).

## Implementation steps
1. Diff discovery (committed + staged + unstaged + untracked)
   - Use `git diff --name-only <base>...HEAD -- src` and ignore `src/changelog.rst`.
   - Union with:
     - staged: `git diff --name-only --cached -- src`
     - unstaged: `git diff --name-only -- src`
     - untracked: `git ls-files --others --exclude-standard -- src`
   - If all sets are empty, exit cleanly.
   - Build the head Sphinx env from the working tree so staged/unstaged/untracked edits are included.

2. Build isolation
   - Use dedicated subfolders under `build/` (e.g., `build/changelog-base`, `build/changelog-head`).
   - Avoid worktrees or archives; rely on Sphinx build outputs only.
   - Clean these subfolders on each run (unless `--keep-temp` is added later).

3. Build Sphinx environments for base and head
   - Run a lightweight Sphinx build (`-b dummy -E -a`) for both refs to produce doctrees.
   - Emit `paragraph-ids.json` as today and add a sibling `paragraph-ids-rich.json` on every build that includes:
     - `markup_checksum` (normalized doctree token stream per paragraph).
     - `role_inventory` per paragraph (counts of `:dt:`, `:t:`, `:s:`, `:ds:`, `:std:`).
     - `literal_inventory` per paragraph (inline literal and literal block counts and hashes).
     - `list_structure` per paragraph (list depth, item count, ordered/unordered).
    - Capture per-definition metadata from `exts/ferrocene_spec/definitions` storages:
      - `term`, `syntax`, `code_term`, `paragraph` items (id, document, anchor).
      - Map definition/ref nodes to paragraph ids in a collector before transforms.
   - Add a JSON Schema for the rich artifact at `exts/ferrocene_spec/schemas/paragraph-ids-rich.schema.json` and link it from `exts/ferrocene_spec/README.rst`.

4. Parse spec changes into structured data
   - `paragraph_added`, `paragraph_removed` by ID diff.
   - `paragraph_changed` by `markup_checksum` diff (plus `plaintext_checksum` for readability).
   - `role_change` by comparing `role_inventory` (added/removed `:dt:`, `:t:`, `:s:`, `:ds:`).
   - `term_def_added/removed` and `syntax_def_added/removed` by definition storage diff.
   - `term_ref_added/removed`, `syntax_ref_added/removed` via per-paragraph role inventory.
   - `literal_change` by literal inventory diff.
   - `list_structure_change` by list structure diff.
   - `section_added/removed` via `env.spec_sections` diff.
   - `definition_relocated` when a definition id changes `document` between base/head.
   - `normative_shift` by detecting modal/conditional keyword changes in plaintext (shall/must/may/only/unless/except/not/any/all/none).

3. Infer release item metadata (best case automation)
   - Read `version.rst` for release version.
   - Try to extract the upstream PR link or title from:
     - `git log -1 --format=%s` (look for `rust-lang/rust#` or a PR URL).
     - Optional CLI args (`--upstream-pr`, `--title`).
   - If missing, generate TODO placeholders and continue.

5. Classification and tag generation
   - Assign explicit tags per paragraph and per release item; do not filter out any change types.
   - Suggested tags:
     - `paragraph-added`, `paragraph-removed`, `paragraph-changed`
     - `role-change`, `term-def-added`, `term-def-removed`, `term-ref-added`, `term-ref-removed`
     - `syntax-def-added`, `syntax-def-removed`, `syntax-ref-added`, `syntax-ref-removed`
     - `literal-change`, `list-structure-change`, `section-added`, `section-removed`
     - `definition-relocated`, `normative-shift`

6. Changelog update logic
   - Ensure a `Language changes in Rust X.Y.Z` section exists; create if missing and insert near the top.
   - If `--update` and metadata is complete, insert a bullet with nested lists for the collected changes.
   - Append a `Change tags:` sub-bullet listing tags that triggered detection for the entry.
   - If metadata is incomplete, append a TODO stub entry and print a warning.

7. Verification mode
   - Scan `src/changelog.rst` for the current release section and compare against collected IDs.
   - Fail (non-zero) if IDs are missing or mismatched; print a summary of required edits.
   - If `--require-tags`, fail when entries lack a `Change tags:` line.

## Integration into make.py
- Add optional args:
  - `--check-changelog` (run script in check mode; fail build if missing).
  - `--update-changelog` (run script in update mode before build).
- Call the script early in `build_docs` (after glossary generation, before Sphinx build).
- For `--serve`, default to check-only (no file writes) unless `--update-changelog` is set.

## Validation
- Add small fixture diffs and unit tests for markup checksums and role inventory extraction.
- Run against a known commit and validate the generated snippet matches existing entries.
- Document usage in make.py help text or a short README section.

## Future enhancements
- Optional input file for release-note items to auto-fill "No change" entries.
- Integration with the existing changelog verification heuristics for more accurate paragraph mapping.

## Branch migration follow-up
- Migrate this automation work from the current long-lived branch to a fresh branch created from `main`.
- Preserve only the changelog automation files and related extension/make.py updates, without unrelated branch history.
- Re-run validation on the fresh branch (`uv run python -m py_compile ...`, `uv run python make.py --xml`, and changelog assistant checks) and fix breakages introduced by rebasing onto `main`.
- Verify the new branch no longer reports legacy `src/` drift from unrelated commits when running changelog checks with default base selection.
