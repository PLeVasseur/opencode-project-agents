# Glossary chapter stubs

All sub-agent work happens in this directory: `$OPENCODE_CONFIG_DIR/reports/glossary-quality/chapters/`.
Edit only the file for your assigned chapter or appendix. Each stub contains a checklist and a per-term template.

Main chapters
- `general.md` -> `src/general.rst`
- `lexical-elements.md` -> `src/lexical-elements.rst`
- `items.md` -> `src/items.rst`
- `types-and-traits.md` -> `src/types-and-traits.rst`
- `patterns.md` -> `src/patterns.rst`
- `expressions.md` -> `src/expressions.rst`
- `values.md` -> `src/values.rst`
- `statements.md` -> `src/statements.rst`
- `functions.md` -> `src/functions.rst`
- `associated-items.md` -> `src/associated-items.rst`
- `implementations.md` -> `src/implementations.rst`
- `generics.md` -> `src/generics.rst`
- `attributes.md` -> `src/attributes.rst`
- `entities-and-resolution.md` -> `src/entities-and-resolution.rst`
- `ownership-and-deconstruction.md` -> `src/ownership-and-deconstruction.rst`
- `exceptions-and-errors.md` -> `src/exceptions-and-errors.rst`
- `concurrency.md` -> `src/concurrency.rst`
- `program-structure-and-compilation.md` -> `src/program-structure-and-compilation.rst`
- `unsafety.md` -> `src/unsafety.rst`
- `macros.md` -> `src/macros.rst`
- `ffi.md` -> `src/ffi.rst`
- `inline-assembly.md` -> `src/inline-assembly.rst`

Appendices
- `licenses.md` -> `src/licenses.rst`
- `glossary.md` -> `src/glossary.rst`
- `undefined-behavior.md` -> `src/undefined-behavior.rst`
- `changelog.md` -> `src/changelog.rst`
- `background.md` -> `src/background.rst`

Misc bucket
- `_misc.md` -> terms not mapped to a chapter or appendix

Conventions
- Only edit your assigned stub file.
- Headings: alphabetical by term.
- Coverage: fill `expected <count> / found <count>` in your stub after mapping; counts must match before consolidation.
Rating rubric (0-5): 5=Clear, scoped, standalone definition; no ambiguity; adds discriminators and context. 4=Mostly clear; minor missing detail or slight reliance on other terms but still useful. 3=Adequate but vague; relies on multiple other terms or lacks scope/edge cases. 2=Low signal; largely tautological, circular, or too abstract; hard to apply. 1=Bare alias, link-only "See ...", or fragment; not independently useful. 0=Missing definition or nonsensical/incoherent text.
Issue tags: missing, link-only, alias-only, tautological, circular, truncated, fragment, list-leadin-without-list, missing-scope, missing-discriminator, low-signal, regression-vs-legacy, inconsistent-term, editorial-noise, wrong-domain, missing-see-line, definition-same-role-change-expected
Legacy policy: legacy link-only/alias-only definitions are intentional; if generated expands them, mark as regression-vs-legacy and set `Legacy: better`.
Overrides: if legacy vs generated differs only by :dt: vs :t:, rate 5 and tag definition-same-role-change-expected (override all other criteria). If legacy had a "See ..." line and generated lacks it, rate 3 and tag missing-see-line; include the missing "See ..." line in Notes.

