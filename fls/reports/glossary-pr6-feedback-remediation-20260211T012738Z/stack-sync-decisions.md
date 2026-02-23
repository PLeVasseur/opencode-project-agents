# Stack synchronization decisions

## Policy applied

- FF-only was attempted first on each stack edge.
- Published branches with open PRs were synchronized with merge commits (no rebase / no force-push history rewrite).
- After each non-FF sync, strict checker + `./make.py --clear` + `./make.py --check-links` were re-run on the affected branch.

## Decisions and outcomes

1. **step2 <- step1**
   - FF attempt: failed (`git merge --ff-only glossary-step-1-main-text-coverage`).
   - Decision: merge-based sync on published branch.
   - Command: `git -C /home/pete.levasseur/project/fls-wt/step2 merge --no-edit glossary-step-1-main-text-coverage`.
   - Result: merge commit `13a8455`.
   - Follow-up fix: phase2 harmonization commit `be0f38f` to align `cast`/`casting` glossary text after step1 alias addition.
   - Validation: phase2 strict/build/link passed.

2. **step3 <- step2**
   - FF attempt: failed (`git merge --ff-only glossary-step-2-align-duplicate-text`).
   - Decision: merge-based sync on published branch.
   - Command: `git -C /home/pete.levasseur/project/fls-wt/step3 merge --no-edit glossary-step-2-align-duplicate-text`.
   - Merge conflicts resolved in:
     - `src/glossary.rst`
     - `tools/glossary-migration-check.py`
   - Result: merge commit `663a8a3`.
   - Validation: phase3 strict/build/link passed.

3. **step4 <- step3**
   - FF attempt: failed (`git merge --ff-only glossary-step-3-dt-main-only`).
   - Decision: merge-based sync on published branch.
   - Command: `git -C /home/pete.levasseur/project/fls-wt/step4 merge --no-edit glossary-step-3-dt-main-only`.
   - Result: merge commit `a3da34a`.
   - Validation: phase4 strict/build/link passed.

4. **step5 <- step4**
   - FF attempt: failed (`git merge --ff-only glossary-step-4-remove-see-paragraphs`).
   - Decision: merge-based sync on published branch.
   - Command: `git -C /home/pete.levasseur/project/fls-wt/step5 merge --no-edit glossary-step-4-remove-see-paragraphs`.
   - Merge conflict resolved in `src/glossary.rst` by preserving step5 include-based source (`.. include:: glossary.rst.inc`).
   - Result: merge commit `8e8b08b`.
   - Additional parity remediation:
     - `./generate-glossary.py`
     - copy `build/generated.glossary.rst` -> `src/glossary.rst.inc`
     - commit `7444888` (`chore(glossary): refresh generated glossary include`)
   - Validation: phase5 strict/build/link passed.

## Ancestry verification

- `step1 -> step2`: pass
- `step2 -> step3`: pass
- `step3 -> step4`: pass
- `step4 -> step5`: pass
