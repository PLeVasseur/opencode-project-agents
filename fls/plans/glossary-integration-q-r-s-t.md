# Glossary Q/R/S/T Integration Plan

## Purpose

- Integrate the Q, R, S, T glossary migrations into `glossary-auto-generation`.
- Verify glossary migration checks remain satisfied after integration.

## Context

- Repo root: `/home/pete.levasseur/project/fls`
- Plan source: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-migration.md`
- Worktrees:
  - `/home/pete.levasseur/project/fls` (glossary-auto-generation)
  - `/home/pete.levasseur/project/fls-glossary-Q`
  - `/home/pete.levasseur/project/fls-glossary-R`
  - `/home/pete.levasseur/project/fls-glossary-S`
  - `/home/pete.levasseur/project/fls-glossary-T`

## Checks from glossary-migration plan

- [ ] Reconcile each letter against the legacy glossary snapshot.
- [ ] Ensure each definition is placed in the owning chapter (no catch-all sections).
- [ ] Verify every `:dt:` sentence is glossary-ready and stands alone.
- [ ] Update the placement report, per-letter audit file, and migration checklist.
- [ ] Run `./make.py --check-generated-glossary`.
- [ ] Regenerate the coverage report; commit the checkpoint; mark the letter complete.

## Integration steps (Q/R/S/T)

- [ ] Record Q/R/S/T commit SHAs and confirm each worktree is clean.
- [ ] Review Q/R/S/T diffs for plan compliance:
  - `src/glossary.rst` remains a stub.
  - No `src/glossary-definitions.rst` is introduced.
  - `:dp:`/`:dt:` usage is correct and each definition covers exactly one term.
- [ ] Cherry-pick Q, R, S, T commits onto `glossary-auto-generation` (order: Q, R, S, T).
- [ ] Resolve any conflicts using glossary-migration placement and definition rules.
- [ ] Run `./make.py --check-generated-glossary` after integration.
- [ ] Regenerate the coverage report.
- [ ] Confirm migration checklist and per-letter audit files reflect Q/R/S/T completion.
- [ ] Verify `git status` is clean; optionally clean up worktrees later.

## Requested follow-up

- [ ] Rewrite Q/R/S/T audit files to the short format and mark checklists complete.
- [ ] Update `glossary-only-placement.md` with Q/R/S/T entries.
- [ ] Update `migration-checklist.md` to check all Q/R/S/T terms.
- [ ] Commit paragraph-spacing fixes in `src/expressions.rst` and `src/types-and-traits.rst`.

## Outputs to verify

- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/migration-checklist.md`
- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/Q.md`
- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/R.md`
- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/S.md`
- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/T.md`
- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/glossary-only-placement.md`
- `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/glossary-coverage-compare.md`
