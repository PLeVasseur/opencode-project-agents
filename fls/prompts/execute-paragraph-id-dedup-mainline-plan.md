Execute the plan at:
`$OPENCODE_CONFIG_DIR/plans/paragraph-id-dedup-mainline-plan.md`

Context:
- Repo: `/home/pete.levasseur/project/fls`
- Base: `origin/main` (separate PR branch)
- Known duplicate IDs:
  - `fls_t4yeovFm83Wo`
  - `fls_I9JaKZelMiby`
- Keep `types-and-traits` IDs; re-ID glossary duplicates using `./generate-random-ids.py`.
- Artifacts must be written to `$OPENCODE_CONFIG_DIR/reports/`.
- Do not push unless explicitly requested.

Execution requirements:
1. Run bootstrap + create timestamped `REPORT_ROOT`.
2. Capture duplicate-ID inventory before edits.
3. Apply only the two glossary ID replacements.
4. Capture duplicate-ID inventory after edits and confirm no duplicates remain.
5. Run `./make.py` and changelog assistant `--check` with explicit `BASE_REF`.
6. Create a single dedup commit and report its SHA for later cherry-pick.
7. Write `$REPORT_ROOT/summary.md` with pass/fail acceptance criteria.

Finish by returning:
- Checklist status.
- Before/after duplicate evidence.
- Command summary with exit codes.
- Exact artifact paths under `$REPORT_ROOT`.
- Commit SHA and cherry-pick command for `system-abi-variadic` worktree.
