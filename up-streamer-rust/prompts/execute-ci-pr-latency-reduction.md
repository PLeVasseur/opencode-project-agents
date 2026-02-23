Execute the plan at:

`plans/ci-pr-latency-reduction-plan.md`

Execution requirements:

1. Follow phases in order and update the plan file as you work.
2. Tick each task checkbox from `[ ]` to `[x]` immediately after completing it.
3. Create a stacked feature branch from the current branch head (`chore/up-rust-0.9-transport-upgrade`) and keep all work there.
4. Open a single stacked PR with base set to `chore/up-rust-0.9-transport-upgrade` (not `main`).
5. Use logical commits exactly aligned to the plan's commit chunks.
6. Do not squash commits locally.

Implementation constraints:

- Preserve existing CI check names that are currently required by branch protection.
- Keep scope strictly to CI/workflow/docs updates (no runtime behavior changes).
- Move PR coverage workload to nightly/main/manual workflow as described in the plan.

Validation requirements:

- Ensure modified workflows trigger and complete successfully on the PR.
- Ensure nightly coverage workflow executes successfully via `workflow_dispatch`.
- Capture before/after timing for bundled and unbundled `Lint` and `Test` jobs.

Final deliverables:

1. Final commit list (hash + subject).
2. PR URL.
3. Before/after timing comparison table.
4. Confirmation that required PR checks remained intact.
5. Follow-up opportunities not included in this PR.
