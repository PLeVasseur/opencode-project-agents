# Fix :dc: chapter mapping

## Goal
Treat :dc:`term` occurrences as authoritative for chapter mapping so terms like
cfg, derive, and f64 map to their chapters instead of _misc.

## Steps
1. Update `reports/glossary-quality/glossary_quality_build.py`:
   - Add a :dc: regex (e.g., `DC_RE = re.compile(r":dc:`([^`]+)`")`).
   - In the chapter mapping pass, collect terms from both :dt: and :dc:.
   - If a term appears in multiple chapters, record it in mapping-issues as ambiguous.
2. Regenerate mapping and stubs:
   - `python3 /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-quality/glossary_quality_build.py map`
   - `python3 /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-quality/glossary_quality_build.py stubs`
   - `python3 /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-quality/glossary_quality_build.py coverage`
3. Verify `_misc` shrinks in `reports/glossary-quality/chapter-terms.json` and coverage matches.

## Notes
- No repo edits or commits in this plan.
