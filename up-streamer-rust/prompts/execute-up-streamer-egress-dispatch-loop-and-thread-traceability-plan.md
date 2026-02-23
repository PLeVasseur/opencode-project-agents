Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-egress-dispatch-loop-and-thread-traceability-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration.
2. Set and pin execution branch at session start:
   - `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
   - hard-fail if current branch differs from `EXEC_BRANCH`.
3. First action must be the plan's Phase 0 fresh-session preflight.
4. Follow phases and gates in strict order; if any gate fails, stop progression.
5. Before each phase and before each commit, run and record:
   - `git rev-parse --abbrev-ref HEAD`
   - `git status --short --branch`
6. Before each commit, also run and record:
   - `git diff --name-only --cached`
   - `git diff --stat --cached`
   - ensure no repo-local `plans/`, `prompts/`, or `reports/` artifacts are staged.
7. Continuously update the plan in place; flip each completed checkbox from `[ ]` to `[x]` immediately.

Implementation requirements:

1. Egress loop semantics
   - Replace the `while let Ok(...)` receive loop with explicit `match` handling.
   - Handle `RecvError::Lagged(skipped)` with `warn!` and continue.
   - Handle `RecvError::Closed` with transport-agnostic `info!` and break.

2. Logging quality
   - Remove transport-specific references (e.g., `UPClientVsomeip`) from generic egress worker paths.
   - Keep send success/failure logs behaviorally consistent.

3. Optional thread-name traceability
   - Implement short unique egress runtime thread names if Phase 2 decision is yes.
   - Keep deterministic searchable prefix and Linux-safe length.
   - If deferred, record explicit rationale in phase evidence.

Artifacts and evidence:

- Write phase reports under:
  - `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/`
- Write smoke reports under:
  - `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/`
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Mandatory smoke validation requirements (8 scenarios):

- Execute all scenarios listed in plan Phase 6 and produce one report per scenario at exact plan paths:
  - `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
  - `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
  - `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
  - `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
  - `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
  - `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
  - `smoke-zenoh-someip-rr-zenoh-client-someip-service`
  - `smoke-zenoh-someip-rr-someip-client-zenoh-service`
- If blocked by missing external prerequisites, record constrained skip and concrete remediation in that scenario report.

Blocking policy:

- If any gate fails, stop progression.
- Record blocker details with exact command/output and remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases are complete, provide a concise final report including:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - exact recv-loop behavior changes (`Lagged` vs `Closed`)
  - transport-agnostic logging outcome
  - optional unique thread naming decision/outcome
  - validation outcomes (fmt/clippy/check/tests)
  - all 8 smoke scenario outcomes
  - accepted deviations and rationale
