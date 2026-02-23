# Non-5 score investigations (main chapters)

## Goal
Collect all terms rated below 5 in main chapters and create per-chapter
investigation files.

## Steps
1. After the latest re-audit, scan main chapter stubs for ratings 0-4.
2. For each main chapter, launch a subagent to create:
   `reports/glossary-quality/investigations/investigation-<chapter>.md` with:
   - Term
   - Rating and issue tags
   - Source file and :dt: location (or closest anchor)
   - Diagnosis of why the definition is non-5
   - Suggested fix
3. No repo edits or commits in this plan.
