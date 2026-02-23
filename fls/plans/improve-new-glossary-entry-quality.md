# Improve new glossary entry quality (main chapters)

## Goal
Improve definitions for terms with no legacy entry so they are clear, scoped,
and standalone.

## Steps
1. From `reports/glossary-quality/glossary-compare.json`, collect terms where
   `legacy` is null and the term maps to a main chapter.
   - Prioritize terms rated below 5 in the latest audit.
2. Launch one subagent per main chapter:
   - Edit `src/<chapter>.rst` definitions to add scope/discriminators and fix
     list lead-ins, truncation, and tautologies.
   - Add new `:dp:` IDs for any inserted paragraphs
     (use `./generate-random-ids.py`).
3. Run `./make.py --check-generated-glossary`.
4. Commit: `docs(glossary): improve new-term definitions`.
