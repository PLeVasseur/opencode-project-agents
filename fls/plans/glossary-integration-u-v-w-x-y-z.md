# Glossary U/V/W/X/Y/Z Integration Plan

## Purpose

- [ ] Integrate the U, V, W, X, Y, Z glossary migrations into `glossary-auto-generation`.
- [ ] Verify glossary migration checks remain satisfied after integration.

## Context

- [ ] Repo root: `/home/pete.levasseur/project/fls`
- [ ] Plan source: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-migration.md`
- [ ] Worktrees:
  - [ ] `/home/pete.levasseur/project/fls` (glossary-auto-generation)
  - [ ] `/home/pete.levasseur/project/fls-glossary-U`
  - [ ] `/home/pete.levasseur/project/fls-glossary-V`
  - [ ] `/home/pete.levasseur/project/fls-glossary-W`
  - [ ] `/home/pete.levasseur/project/fls-glossary-X`
  - [ ] `/home/pete.levasseur/project/fls-glossary-Y`
  - [ ] `/home/pete.levasseur/project/fls-glossary-Z`

## Checks from glossary-migration plan

- [ ] Reconcile each letter against the legacy glossary snapshot.
- [ ] Ensure each definition is placed in the owning chapter (no catch-all sections).
- [ ] Verify every `:dt:` sentence is glossary-ready and stands alone.
- [ ] Update the placement report, per-letter audit file, and migration checklist.
- [ ] Run `./make.py --check-generated-glossary`.
- [ ] Regenerate the coverage report; commit the checkpoint; mark the letter complete.

## Integration steps (U/V/W/X/Y/Z)

- [ ] Record U/V/W/X/Y/Z commit SHAs and confirm each worktree is clean.
- [ ] Review U/V/W/X/Y/Z diffs for plan compliance:
  - [ ] `src/glossary.rst` remains a stub.
  - [ ] No `src/glossary-definitions.rst` is introduced.
  - [ ] `:dp:`/`:dt:` usage is correct and each definition covers exactly one term.
- [ ] Cherry-pick U, V, W, X, Y, Z commits onto `glossary-auto-generation` (order: U, V, W, X, Y, Z).
- [ ] Resolve any conflicts using glossary-migration placement and definition rules.
- [ ] Run `./make.py --check-generated-glossary` after integration.
- [ ] Regenerate the coverage report.
- [ ] Confirm migration checklist and per-letter audit files reflect U/V/W/X/Y/Z completion.
- [ ] Verify `git status` is clean; optionally clean up worktrees later.

## Requested follow-up

- [ ] Rewrite U/V/W/X/Y/Z audit files to the short format and mark checklists complete.
- [ ] Update `glossary-only-placement.md` with U/V/W/X/Y/Z entries.
- [ ] Update `migration-checklist.md` to check all U/V/W/X/Y/Z terms.
- [ ] Carry forward any outstanding spacing/formatting fixes discovered during U/V/W/X/Y/Z integration.

## Outputs to verify

- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/migration-checklist.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/U.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/V.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/W.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/X.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/Y.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/Z.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/glossary-only-placement.md`
- [ ] `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-auto-generation/glossary-coverage-compare.md`
