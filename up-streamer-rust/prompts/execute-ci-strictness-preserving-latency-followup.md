Execute the plan at:

`plans/ci-strictness-preserving-latency-followup-plan.md`

Primary objective:

- Continue CI latency optimization on top of the existing PR branch while preserving strictness and required-check semantics.

Execution context:

- Branch: `perf/ci-pr-latency-reduction`
- PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/76

Hard constraints:

- Keep one branch and one PR.
- CI/workflow/docs scope only; no runtime behavior changes.
- Preserve required check names exactly:
  - Bundled: `Lint`, `Test`, `Build documentation`
  - Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- Preserve branch-protection signal.
- Preserve the spirit of bundled lint validation:
  - bundled feature lint must continue validating with
    `vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
  - do not dilute strict clippy gating (`-W warnings -D warnings`)
  - keep `vsomeip` compile/build signal in bundled lint path
- Keep one-writer cache policy unless a phase explicitly trials a change.
- Do not squash or amend unless explicitly requested.

What to execute:

- Phase A: preflight, baseline freeze, and variance control.
- Phase B: investigate and mitigate unbundled `Lint` regression (if persistent).
- Phase C: branch-protection-safe simplification investigation for bundled `Lint` aggregator.
- Phase D: optional narrow optimization only if needed and measured.

Execution requirements:

1. Follow phases in order.
2. Update plan checkboxes immediately as items complete.
3. Commit in logical chunks aligned to the plan commit section.
4. After each push, validate CI before proceeding.
5. If a job fails, diagnose as soon as it completes (do not wait for all jobs).

Validation checklist after each phase:

- Required checks triggered and completed.
- Required check names unchanged.
- No cache contention (`Unable to reserve cache`).
- No bundled lint link regressions (`unable to find library -lvsomeip3`).
- Capture run URLs and durations for bundled/unbundled `Lint` and `Test`.

Known external blocker:

- `eclipsefdn/eca` may fail on new SHAs due to external identity mapping behavior.
- Treat ECA as external unless commit metadata evidence clearly implicates current changes.

Final deliverables:

1. Commit list (hash + subject)
2. PR URL
3. Before/after timing table
4. Confirmation required check names remained intact
5. Cache behavior summary (writers vs restore-only; contention status)
6. Bottleneck summary and follow-up opportunities not included
