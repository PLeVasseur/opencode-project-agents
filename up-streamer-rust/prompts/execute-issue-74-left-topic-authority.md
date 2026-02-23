Execute the plan at:

`plans/issue-74-pubsub-subscription-mapping-debug-plan.md`

Execution requirements:

1. Follow phases and gates in strict order; do not skip gate criteria.
2. Update the plan file continuously as work progresses.
3. Change each checkbox from `[ ]` to `[x]` immediately after completion.
4. Start from `perf/ci-pr-latency-reduction` and branch from it:
   - `git fetch --all --prune`
   - `git checkout perf/ci-pr-latency-reduction`
   - `git pull --ff-only`
   - `git checkout -b bugfix/issue-74-left-topic-authority`
5. Keep all work on one branch and one PR.
6. Use logical commits exactly as defined in the plan's commit slicing section.
7. Before each commit, run:
   - `git diff --name-only --cached`
   - `git diff --stat --cached`

Scope constraints:

- Primary runtime fix is issue #74 left-side/topic authority enforcement in publish forwarding.
- Right-side wildcard semantics are explicitly out of scope for this issue.
- Add CLI parameterization to example binaries with defaults preserved.
- Parameterization must support overriding identifiers such as:
  - `--uauthority authority-c`
  - `--uentity 0x5BA0`
  - `--uversion 0x1`
  - `--resource 0x8001`

Artifact and documentation constraints:

- Write reports and temporary configs under `$OPENCODE_CONFIG_DIR/reports/issue-74/`.
- Do not create repo-local plans/prompts/reports.
- Update docs required by the plan so the issue-74 scenario is runnable without code edits.

Validation requirements:

1. Add fail-before/pass-after automated regression coverage for issue #74.
2. Run the manual issue-74 repro runbook using parameterized binaries and capture objective log evidence.
3. Ensure allowed source (A) forwards and disallowed source (C) is blocked for map `A -> B`.
4. Run CI parity checks listed in the plan.

Risk fallback policy:

- If timeline risk appears, prioritize in this order:
  1) streamer fix + regression tests,
  2) MQTT/Zenoh pub/sub binary parameterization + docs for issue-74 repro,
  3) remaining example binary parameterization.
- Any de-scoping must be documented in `$OPENCODE_CONFIG_DIR/reports/issue-74/` with explicit follow-ups.

Final deliverables:

1. Final commit list (hash + subject + scope).
2. PR URL (base should be `perf/ci-pr-latency-reduction`).
3. Test evidence (fail-before/pass-after) for issue #74.
4. Manual reproduction evidence (commands + key log outcomes) using parameterized binaries.
5. CI/parity command outcomes.
6. Any deferred items with rationale and follow-up actions.
