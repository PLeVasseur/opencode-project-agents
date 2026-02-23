Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-rust-expert-ergonomics-performance-phased-plan.md`

You keep blowing the context window and need to be restarted. Be careful!

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration.
2. First action must be the plan's **Session bootstrap** section (run it in order).
3. Set and pin execution branch at session start:
   - `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
   - hard-fail immediately if current branch differs from `EXEC_BRANCH`.
4. Respect locked decisions in the plan (ArcSwap snapshot strategy, plugin runtime owned in plugin state, staged validation, per-phase commits, no-regression performance gate).
5. Execute in strict sequence:
   - Cycle 1: Phase 0 -> Phase 1 -> Phase 2 -> full smoke-8 gate -> Cycle 1 summary
   - Stop after Cycle 1 and present results; proceed to Cycle 2 only after explicit acceptance.
   - Cycle 2: Phase 3 -> Phase 4 -> Phase 5 -> cycle-end gates -> Cycle 2 summary
6. Before each phase and before each commit, run and record:
   - `git rev-parse --abbrev-ref HEAD`
   - `git status --short --branch`
7. Before each commit, also run and record:
   - `git diff --name-only --cached`
   - `git diff --stat --cached`
   - ensure no repo-local `plans/`, `prompts/`, or `reports/` artifacts are staged.
8. Continuously update the plan in place; flip each completed checkbox from `[ ]` to `[x]` immediately.

Artifact and evidence constraints:

- Write phase and cycle reports only under:
  - `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/`
  - `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/phase-reports/`
- Write smoke reports only under:
  - `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/`
- Write smoke artifacts only under:
  - `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/<scenario>-artifacts/`
- Important: when running smoke skills, override/report paths so outputs land in the plan-specific directories above (not default `transport-smoke-skills`).
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Mandatory smoke gate requirements (Cycle 1 end):

- Execute all 8 scenarios listed in the plan's Cycle 1 smoke section.
- Produce one report per scenario at exact plan paths.
- In each scenario report, include structured logging verification from streamer logs:
  - `event=egress_send_attempt` with `worker_id`
  - `event=egress_send_ok` with `worker_id`
  - `event=egress_worker_create` or `event=egress_worker_reuse` with `route_label`
- If lag/closed events are not naturally observed in bounded runs, record explicit `not observed in bounded run` note and rationale.
- If blocked by missing prerequisites, record `constrained-skip` plus concrete remediation in that scenario report.

Validation requirements:

- Run phase verification commands exactly as listed in the plan.
- Run CI parity preflight gates at cycle ends exactly as listed in the plan.
- Treat any failed gate as blocking.

Blocking policy:

- If any gate fails, stop progression.
- Record blocker details with exact command/output and remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverables:

- At Cycle 1 completion, provide concise report including:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - correctness/perf outcomes vs baseline
  - full smoke-8 outcomes and structured logging assertion status
  - accepted deviations and rationale
- At final completion (Cycle 2), provide concise report including:
  - cycle and phase completion summary
  - full commit list (hash + subject + scope)
  - correctness, ergonomics, runtime, and test-determinism outcomes
  - benchmark deltas and no-regression status
  - CI parity and smoke outcomes
  - accepted deviations and rationale
