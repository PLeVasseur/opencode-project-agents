# Glossary Sphinx-Env Generator Plan

Date: 2026-02-05

## Goals
- Single parser: glossary entries parsed only by Sphinx/docutils.
- Keep a generated glossary in build/ for review.
- Keep a static glossary in repo for qualification.
- Natural sort order (matches glossary lint behavior).
- Mismatch warning + overwrite option in make.py.
- Incremental builds stay in sync with generated glossary.

## Non-goals
- Changing glossary content semantics.
- Removing the static glossary from the repo.

## Decisions
- Two-pass build for --use-generated-glossary is acceptable.
- Add :glossary-dp: to glossary-entry directives and require it for exported terms.
  - Required when an entry has :glossary: or has :chapter: with :propagate: true.
  - Not required for chapter-only entries that do not propagate.
  - Format: `fls_` prefix followed by one or more ASCII letters/digits (case-sensitive), no spaces.
  - Derived from `generate-random-ids.py`: `fls_` + 12 chars from ASCII letters/digits (12 recommended).
- Use Sphinx env storage as the data source for generation.
- Sort with the same numeric-aware compare used by alphabetical_section_titles.py.
- Sorting is casefold + numeric chunks (matches glossary lint behavior).
- Generator must support Sphinx tags and use the same tags as the build.
- Preserve the top-level glossary anchor `.. _fls_bc2qwbfibrcs:` verbatim.
- Section underline length must match the title length.

## Implementation Steps
1) Add glossary-id support
   - Extend `exts/ferrocene_spec/glossary.py` to accept `:glossary-dp:`.
   - Validate `fls_` prefix + `[A-Za-z0-9]+` format and uniqueness for glossary dp ids and terms.
   - Store `glossary_dp` in `GlossaryEntryData`.

2) Env-based generator
   - Rewrite `generate-glossary.py` to build a Sphinx env (dummy builder).
   - Accept `--tag/-t` options and pass them to the Sphinx app tags.
   - Read entries from `ferrocene_spec.glossary.get_storage(app.env)`.
   - Render a full glossary file (prelude + glossary section + entries).
   - Reuse rendering helpers from the extension (avoid re-parsing).
   - Sort entries using the same numeric-aware key as the glossary lint.

3) Prelude and anchors
   - Preserve SPDX headers, `.. default-domain:: spec`, and `.. informational-page::`.
   - Preserve the glossary section anchor `.. _fls_bc2qwbfibrcs:` and title.
   - Generate underlines that match the title length exactly.
   - Use `:glossary-dp:` for term anchors.

4) Migration
    - One-off script (under $OPENCODE_CONFIG_DIR) to:
      - Parse `src/glossary.static.rst.inc` for `term -> fls_id`.
      - Insert `:glossary-dp:` into every `.. glossary-entry::` in `src/**/*.rst` and `src/**/*.rst.inc`.
      - Fail on missing term/anchor mapping or duplicates.
    - Add checks to error when an exported glossary term lacks `:glossary-dp:`.

5) make.py and CI
   - Keep generator step before Sphinx build.
   - Pass `--tag/-t` options to both the generator and Sphinx build.
   - Add `--overwrite-glossary-from-build` to update `src/glossary.static.rst.inc` and continue the build.
   - If mismatch and no overwrite flag, warn with explicit instruction.
   - Keep CI diff check unchanged.

6) Incremental build staleness
   - `glossary-include` should call `env.note_dependency()` for included files.
   - For `--serve`, pass a pre-build hook to `sphinx-autobuild` to run `./generate-glossary.py`.
     - If the installed `sphinx-autobuild` lacks `--pre-build`, use a wrapper script.

## Testing
- Baseline: `./generate-glossary.py` then `diff -u build/generated.glossary.rst src/glossary.static.rst.inc`.
- Real mismatch test (in repo):
  - Edit one glossary-entry body in a chapter file (e.g., `src/expressions.rst`).
  - Run `./generate-glossary.py` and confirm diff.
  - Run `./make.py` and confirm warning.
  - Run `./make.py --overwrite-glossary-from-build` and confirm static updates + build completes.
  - Revert the chapter edit if this was test-only.
- Serve test:
  - `./make.py --serve --use-generated-glossary`.
  - Edit a glossary-entry body and confirm rebuild reflects the change.

## Risks and Mitigations
- Two-pass build time: use dummy builder for env-only build.
- Missing anchors: enforce `:glossary-id:` and error on duplicates/missing ids.
- Tag-conditional content: ensure tags are passed consistently to generator/build.
7) Update generate-glossary-entry.py
   - Emit `:glossary-dp:` in generated directives.
   - Accept `--glossary-dp` explicitly.
   - If not provided, look up the term anchor in `src/glossary.static.rst.inc`.
   - Error when neither `--glossary-dp` nor a static anchor exists.
