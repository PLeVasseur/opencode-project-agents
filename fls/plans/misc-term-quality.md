# _misc term quality review

## Goal
Evaluate terms still in _misc after the :dc: mapping fix and re-audit, and
flag low-quality ones for follow-up.

## Steps
1. Read `_misc` terms from `reports/glossary-quality/chapter-terms.json`.
2. Use the latest `_misc.md` stub and the glossary-quality rubric.
3. Launch one subagent to produce:
   `reports/glossary-quality/misc-quality.md` with:
   - Term
   - Rating and issue tags
   - Reason for low quality (if any) and suggested next step
4. No repo edits or commits in this plan.
