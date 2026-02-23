Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-structured-tracing-commonization-commit-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration.
2. Set and pin execution branch at session start:
   - `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
   - hard-fail if current branch differs from `EXEC_BRANCH`.
3. First action must follow the plan's execution guardrails and artifact-path setup.
4. Follow commit sequence and gates in strict order (Commit 1 -> Commit 2 -> Commit 3 -> Commit 4 -> Commit 4b; Commit 5 optional).
5. Before each phase and before each commit, run and record:
   - `git rev-parse --abbrev-ref HEAD`
   - `git status --short --branch`
6. Before each commit, also run and record:
   - `git diff --name-only --cached`
   - `git diff --stat --cached`
   - ensure no repo-local `plans/`, `prompts/`, or `reports/` artifacts are staged.
7. Continuously update the plan in place; flip each completed checkbox from `[ ]` to `[x]` immediately.

Implementation requirements:

1. Structured tracing contract
   - Implement event names and field keys defined by the plan.
   - Maintain stable `worker_id` semantics per egress worker lifecycle.
   - Keep `route_label` to worker correlation grepable.

2. Commonization
   - Add shared observability helpers (`events` + `fields`) first.
   - Reuse helpers consistently across core module migrations.

3. Behavior preservation
   - Do not change control/data-plane semantics while modernizing logging.
   - Keep egress `Lagged`/`Closed` behavior unchanged.

Artifacts and evidence:

- Write phase/commit reports under:
  - `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/phase-reports/`
- Write smoke reports under:
  - `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/`
- Write smoke artifacts under:
  - `$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/<scenario>-artifacts/`
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Mandatory smoke validation requirements (all 8 scenarios):

- Execute the full smoke matrix and produce one report per scenario at exact plan paths:
  - `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - `smoke-zenoh-someip-rr-someip-client-zenoh-service`
- In each scenario report, include structured logging verification from streamer logs:
  - `event=egress_send_attempt` with `worker_id`
  - `event=egress_send_ok` with `worker_id`
  - `event=egress_worker_create` or `event=egress_worker_reuse` with `route_label`
- If lag/closed events are not naturally observed in bounded runs, record explicit note and rationale.
- If blocked by missing external prerequisites, record constrained-skip plus concrete remediation in that scenario report.

Blocking policy:

- If any gate fails, stop progression.
- Record blocker details with exact command/output and remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases are complete, provide a concise final report including:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - structured tracing contract implementation summary
  - stable worker-id and route-label correlation outcome
  - validation outcomes (fmt/clippy/check/tests)
  - all 8 smoke scenario outcomes
  - structured logging smoke assertions outcome
  - accepted deviations and rationale
