# Final non-5 fixup (main chapters)

## Goal
Eliminate remaining non-5 glossary definitions in main chapters after the
previous improvement passes. When a term overlaps with legacy, bias toward
the legacy definition and incorporate it as the baseline.

## Steps
1. After the latest full glossary-quality-audit, collect all main-chapter terms
   rated below 5.
2. For each term, check legacy overlap using
   `reports/glossary-quality/glossary-compare.json`.
   - If legacy exists, favor the legacy definition wording and add any missing
     scope/discriminators from the current definition.
3. Launch one subagent per main chapter to:
   - Edit `src/<chapter>.rst` definitions to reach rating 5.
   - Preserve section flow; avoid broad refactors.
   - Add new `:dp:` IDs for new paragraphs (`./generate-random-ids.py`).
4. Run `./make.py --check-generated-glossary`.
5. Commit: `docs(glossary): finalize non-5 definition fixes`.
6. Run the full glossary-quality-audit plan to verify remaining non-5 count is zero.
