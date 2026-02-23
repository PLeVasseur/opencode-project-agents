Execute the plan at:

`plans/ci-latency-next-wave-optimization-plan.md`

Execution requirements:

1. Follow phases in order and update the plan file as you work.
2. Tick each task checkbox from `[ ]` to `[x]` immediately after completing it.
3. Keep all work in one branch and one PR unless the plan explicitly requires otherwise.
4. Use logical commits aligned to the plan's commit chunks.
5. Do not squash commits locally.

Implementation constraints:

- Preserve required PR check names exactly:
  - Bundled: `Lint`, `Test`, `Build documentation`
  - Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- Keep scope strictly to CI/workflow/docs changes (no runtime behavior changes).
- Prioritize the highest ROI optimization first: Rust cache topology and writer/restore policy.
- Ensure optimization changes do not reduce validation coverage or branch-protection signal.

What to execute from the plan:

- Phase 0: Baseline and graph mapping (capture current critical path and `needs` graph).
- Phase 1: Fix cache key collisions and enforce one-writer-per-workflow cache policy.
- Phase 2: Add and evaluate `sccache` (`RUSTC_WRAPPER=sccache`, `SCCACHE_GHA_ENABLED=true`).
- Phase 3: Trial `cache-workspace-crates: true` and keep only if measured gains hold.
- Phase 4: Collect `cargo --timings` artifacts and identify crate-level bottlenecks.
- Phase 5: If still needed, parallelize bundled lint internals behind final required check `Lint`.
- Phase 6: Validate all workflows and publish before/after timing comparisons.
- Phase 7: Apply rollback order if any optimization regresses stability or latency.

Validation requirements:

- Confirm workflows trigger and complete successfully on the PR.
- Confirm required check names are unchanged in PR status checks.
- Confirm cache contention errors are removed (`Unable to reserve cache` no longer present).
- Capture before/after timing for bundled and unbundled `Lint` and `Test` jobs.
- Include run URLs plus relevant cache and `sccache` stats.

Final deliverables:

1. Final commit list (hash + subject).
2. PR URL.
3. Before/after timing comparison table.
4. Confirmation that required PR checks remained intact.
5. Cache behavior summary (writer jobs, restore-only jobs, and contention status).
6. `cargo --timings` bottleneck summary and follow-up opportunities not included in this PR.
