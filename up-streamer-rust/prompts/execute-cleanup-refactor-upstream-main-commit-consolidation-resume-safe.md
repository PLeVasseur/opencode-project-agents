# Execute commit consolidation for `cleanup/refactor-upstream-main` (resume-safe)

Execute the checklist plan at:

`$OPENCODE_CONFIG_DIR/plans/cleanup-refactor-upstream-main-commit-consolidation-plan.md`

This execution must be crash-resilient and resume-safe.

Execution requirements:

1. Manual execution only; no autopilot shortcuts.
2. Follow the plan exactly, including all mandatory crash-resilience mechanics.
3. At startup, use the plan's resume-first logic:
   - If an unfinished run exists via `cleanup-refactor-upstream-main-consolidation.current`, run Phase 0R and resume from the first unchecked checkbox.
   - If no unfinished run exists, start a new run from Phase 0.
4. Tick checkboxes immediately after each completed item (`[ ]` -> `[x]`); never batch-update.
5. Enforce all hard invariants before rewrite:
   - Local `HEAD` must equal `origin/cleanup/refactor-upstream-main` before rewriting.
   - Create and push durable backup refs (branch + tag) before any history edits.
6. Use the headless rebase strategy from the plan:
   - deterministic rebase todo,
   - non-TTY `GIT_SEQUENCE_EDITOR` script,
   - `break` checkpoints,
   - per-commit validation gates.
7. Maintain crash resilience throughout:
   - keep `session-state.env`, `phase-markers.log`, and `command-transcript.log` current,
   - create and push remote checkpoint tags at required safe points,
   - preserve rollback capability at all times.
8. Run all required validation gates, including:
   - per-commit checkpoint gates,
   - final integrated CI-parity checks,
   - final branch-guarded smoke matrix with `--skip-build`.
9. Push rewrite only after all gates pass, using explicit lease:
   - `git push --force-with-lease=cleanup/refactor-upstream-main:<pre-rewrite-remote-sha> origin cleanup/refactor-upstream-main`

Completion requirements:

- Confirm final branch head SHA and commit count (`<= 6`) vs `upstream/main`.
- Confirm no content loss (`tree` equality vs backup) and intended diff scope.
- Confirm smoke matrix passed with zero failed scenarios.
- Provide recovery evidence:
  - backup branch/tag names and SHAs,
  - remote checkpoint tags created,
  - state/report artifact paths.
- Write the full execution report to the path defined by the plan.
- If blocked by a true external prerequisite, ask exactly one targeted question with a recommended default.
