# Update missing "See ..." lines

## Goal
Add missing legacy "See ..." lines to definitions in main chapters so the
missing-see-line count becomes zero after re-audit.

## Scope
Main chapters only (see orchestrate-glossary-improvements.md). Appendices and
_misc are excluded.

## Steps
1. Baseline count:
   - Parse main chapter stubs in `reports/glossary-quality/chapters/` for the
     `missing-see-line` tag and record the total.
2. Build a term -> legacy "See ..." line mapping using
   `reports/glossary-quality/glossary-compare.json`.
3. Group missing-see terms by chapter using `term-chapter.json`.
4. Launch one subagent per main chapter with missing-see terms:
   - Edit `src/<chapter>.rst` and add the missing legacy "See ..." line as its
     own paragraph immediately after the definition.
   - Add a new `:dp:` ID for each inserted paragraph
     (use `./generate-random-ids.py`).
   - Preserve the legacy "See ..." text exactly.
5. Run `./make.py --check-generated-glossary`.
6. Defer the full `glossary-quality-audit.md` plan until after
   `revise-glossary-collection.md` (see orchestration).
7. Recount `missing-see-line` tags in main chapters after the full audit; the
   count must be zero.
   - Verify affected terms now show rating 5 with
     `definition-same-role-change-expected`.
8. Commit: `docs(glossary): restore legacy See lines`.
