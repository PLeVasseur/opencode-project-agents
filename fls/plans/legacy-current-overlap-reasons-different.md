# Legacy/current overlap differences (main chapters)

## Goal
Classify why legacy and generated definitions differ for overlapping terms.

## Steps
1. From `reports/glossary-quality/glossary-compare.json`, select terms where:
   - legacy exists, and
   - the generated definition differs beyond role-only changes.
2. Filter to main chapters using `term-chapter.json`.
3. Launch one subagent per main chapter to create:
   `reports/glossary-quality/diffs/differ-<chapter>.md` with:
   - Term
   - Legacy snippet
   - Generated snippet
   - Classification (e.g., scope loss, missing discriminator, alias-only
     expansion, list-leadin, truncation, regression vs legacy)
4. No repo edits or commits in this plan.
