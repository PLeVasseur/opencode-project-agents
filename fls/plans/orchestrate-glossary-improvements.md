# Orchestrate glossary improvements

## Goals
- Fix missing legacy "See ..." lines in main chapters.
- Re-audit glossary quality and drive follow-on investigations.
- Improve new glossary entries where legacy has no overlap.
- Classify legacy/current definition differences.

## Scope
Main chapters only (per src/index.rst):
- general
- lexical-elements
- items
- types-and-traits
- patterns
- expressions
- values
- statements
- functions
- associated-items
- implementations
- generics
- attributes
- entities-and-resolution
- ownership-and-deconstruction
- exceptions-and-errors
- concurrency
- program-structure-and-compilation
- unsafety
- macros
- ffi
- inline-assembly

Appendices and _misc are excluded unless a plan explicitly says otherwise.

## Orchestration
1. Execute fix-dc-chapter-mapping.md (no repo edits).
2. Execute update-missing-see.md (repo edits + commit).
3. Execute revise-glossary-collection.md (repo edits + commit).
4. Execute glossary-only-see-role.md (repo edits + commit).
5. Execute full glossary-quality-audit.md and confirm missing-see-line count is 0 for main chapters.
6. Execute non-5-score.md (main chapters only).
7. Execute legacy-current-overlap-reasons-different.md (main chapters only, non-5 only).
8. Execute misc-term-quality.md (analysis only; can run in parallel with step 7).
9. Execute improve-new-glossary-entry-quality.md (main chapters only, repo edits + commit).
10. Execute resolve-legacy-overlap-actions.md (main chapters only, repo edits + commit).
11. Execute final-non-5-fixup.md (main chapters only, repo edits + commit).
12. Final full glossary-quality-audit.md run to capture improvements.

## Commit boundaries
- Commit after update-missing-see.md.
- Commit after revise-glossary-collection.md.
- Commit after glossary-only-see-role.md.
- Commit after improve-new-glossary-entry-quality.md.
- Commit after resolve-legacy-overlap-actions.md.
- Commit after final-non-5-fixup.md.
