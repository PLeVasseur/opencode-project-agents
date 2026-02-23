Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/glossary-tshepang-phased-worktree-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Plan objective: execute the 5-phase glossary migration as stacked worktrees/branches, then open stacked PRs on `PLeVasseur/fls`.
- This execution is expected to push branches and create PRs on the fork.
- PR source material: `https://github.com/rust-lang/fls/pull/656`
- Report scaffold root: `$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-phase-scaffold`
- Hard constraints:
  - No `.. glossary-entry::` and no `.. glossary-include::` in landed branches.
  - Use project entrypoints (`./make.py`, `./generate-glossary.py`) for build/parity workflows.
  - Do not run `sphinx-build`/`sphinx-autobuild` directly in manual phase steps.
  - Keep all reports under `$OPENCODE_CONFIG_DIR/reports/`.

Execution requirements:
1. Run the full preflight/bootstrap checklist from the plan and report pass/fail per item.
2. Export `REPORT_SCAFFOLD_ROOT="$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-phase-scaffold"`.
3. Create and print timestamped `REPORT_ROOT` under `$OPENCODE_CONFIG_DIR/reports/`.
4. Copy scaffold templates into `REPORT_ROOT` exactly as specified in the plan.
5. Record term-wave grouping evidence:
   - `git log --reverse --oneline origin/main..origin/glossary-auto-generation > "$REPORT_ROOT/term-wave-history.log"`
6. Execute worktree/branch setup from the plan (idempotently if already present).
7. Before each phase, perform stacked branch synchronization checks exactly as specified in the plan:
   - FF-only sync path when possible,
   - merge/rebase policy when not,
   - ancestry verification commands.
8. Implement all phase work (1 through 5) in order, including guardrails.
9. Implement `tools/glossary-migration-check.py` and wire phase strict checks exactly as defined in the plan.
10. For each phase before PR creation/update:
   - run strict phase check command,
   - run `./make.py --clear`,
   - run `./make.py --check-links`.
11. For each phase, update scaffold tracking files under `REPORT_ROOT/phaseN-.../`:
   - complete `term-wave-checklist.md` for all five waves (`A-H`, `I-P`, `Q-T`, `U-W`, `X-Z + aliases`),
   - update `artifacts-checklist.md`,
   - append `commands.log`,
   - record command exit codes in `exit-codes.md`,
   - capture rationale and blockers in `notes.md`.
12. In phase 5, also run CI-equivalent glossary parity:
   - `./generate-glossary.py && diff -u build/generated.glossary.rst src/glossary.rst.inc`
13. Commit logically with Conventional Commit messages.
14. Push all phase branches to fork with upstream tracking.
15. Create 5 stacked PRs on `PLeVasseur/fls` using the exact base/head ordering and PR command templates from the plan.
16. Capture all evidence in `REPORT_ROOT` (command logs, exit codes, generated reports, ancestry checks, term-wave checklists, and PR metadata).

Completion requirements:
- Do not skip a failed check; either fix and rerun, or stop and document blocker with remediation.
- Preserve unrelated existing worktree changes; do not reset/revert unrelated user edits.

Finish by returning:
- Checklist completion status by major section.
- Term-wave completion status by phase (all five wave buckets per phase).
- Worktree and branch summary (paths, branch names, tip SHAs).
- Stacked ancestry verification results.
- Per-phase command summary with exit codes.
- Commit list by phase (SHA + message).
- Push results for all five branches.
- All five PR URLs with base/head confirmation.
- Exact artifact paths under `REPORT_ROOT` (including phase scaffold files).
- Any blockers, deviations, and proposed follow-ups.
