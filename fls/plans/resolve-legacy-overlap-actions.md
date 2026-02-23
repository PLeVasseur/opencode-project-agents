# Resolve legacy overlap actions (main chapters)

## Goal
For each term where legacy/current definitions differ, choose the best action
(merge/split/reword/move) and update the chapter definitions without disrupting
chapter flow. Bias toward retaining the legacy glossary definition when it
provides a clearer baseline, then append any chapter-specific constraints or
list lead-ins as needed.

## Scope
Main chapters only.

## Action guidelines
- merge: combine best parts of legacy/current into a single scoped definition.
- split: separate overloaded definition into two terms or add clarifying
  sub-definition (rare; prefer legacy + addendum).
- reword: keep structure but add discriminators, scope, or fix tautology.
- move: relocate definition within the same section to align with flow
  (flexible if needed).

## Steps
1. Read `reports/glossary-quality/diffs/differ-<chapter>.md` for each main chapter.
2. Launch one subagent per main chapter to:
   - Choose an action per term.
   - Apply changes in `src/<chapter>.rst`.
   - Preserve section flow; avoid broad refactors.
   - Add new `:dp:` IDs for any new paragraphs (`./generate-random-ids.py`).
3. Run `./make.py --check-generated-glossary`.
4. Commit: `docs(glossary): reconcile legacy overlap definitions`.
5. Run the full glossary-quality-audit plan to refresh ratings.
