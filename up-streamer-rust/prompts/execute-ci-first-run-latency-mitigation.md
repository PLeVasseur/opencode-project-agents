You are executing CI latency optimization work for `up-streamer-rust`.

Primary objective:
- Reduce first-run PR latency for required checks without reducing validation coverage or changing required check names.

Read and follow this execution plan exactly:
- `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/plans/ci-first-run-latency-mitigation-plan.md`

Hard constraints:
- Keep work on one branch and one PR.
- CI/workflow/docs scope only; no runtime behavior changes.
- Preserve required check names exactly:
  - Bundled: `Lint`, `Test`, `Build documentation`
  - Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- Keep branch-protection signal intact.
- Keep one-writer cache policy (unless plan phase explicitly changes it).
- Do not squash or amend unless explicitly requested.

Execution requirements:
1. Follow plan phases in order.
2. Update the plan checkboxes immediately as items complete.
3. Commit in logical chunks aligned with plan commit sections.
4. After each push, validate CI before proceeding to next phase.
5. If a job fails, diagnose the failing job as soon as it completes (do not wait for entire workflow if unnecessary).

Artifact location policy:
- Read plans from `$OPENCODE_CONFIG_DIR/plans/`.
- Write prompts to `$OPENCODE_CONFIG_DIR/prompts/`.
- Write reports to `$OPENCODE_CONFIG_DIR/reports/`.
- Do not create repo-local `plans/`, `prompts/`, or `reports/` artifacts unless explicitly requested.

Known external blocker:
- `eclipsefdn/eca` may fail on new SHAs due to identity mapping outside CI workflow scope.
- Treat ECA as external unless there is clear evidence of commit metadata mismatch introduced by your changes.

What to execute (high-level):
- Phase A: preflight, baseline freeze, guardrails.
- Phase B: OpenSSL no-vendor mitigation (`OPENSSL_NO_VENDOR=1`, system OpenSSL deps) across required and timing workflows.
- Phase C: bundled lint feature de-duplication (remove redundant two-pass compile while preserving strict clippy signal).
- Phase D: bundled vsomeip stability/cache hygiene (no `-lvsomeip3` regressions, no cache contention).
- Phase E: optional, only if needed and only with measured ROI.

Validation checklist after each phase:
- Required checks triggered and completed.
- Required check names unchanged.
- Cache contention errors absent (`Unable to reserve cache`).
- For timing phases: capture run URLs and before/after durations for bundled/unbundled `Lint` and `Test`.

Final deliverables to provide:
1. Commit list (hash + subject)
2. PR URL
3. Before/after timing comparison table
4. Confirmation required check names remained intact
5. Cache behavior summary (writer vs restore-only jobs; contention status)
6. Cargo timings bottleneck summary and follow-up opportunities not included

Quality bar:
- Prefer smallest high-confidence changes with measurable impact.
- Revert quickly on instability and follow rollback order from the plan.
- Always include concrete evidence: run URLs, job durations, and relevant log lines.
