# Cycle 2 Resume Prompt

Continue executing this plan from the first unchecked actionable item:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-rust-expert-ergonomics-performance-phased-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration.
2. First action must be the plan's **Session bootstrap** section (run it in order).
3. Set and pin execution branch at session start:
   - `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
   - hard-fail immediately if current branch differs from `EXEC_BRANCH`.
4. Respect locked decisions in the plan (ArcSwap snapshot strategy, plugin runtime owned in plugin state, staged validation, per-phase commits, no-regression performance gate).
5. Continue in strict sequence for Cycle 2 only:
   - Phase 3 -> Phase 4 -> Phase 5 -> cycle-end gates -> Cycle 2 summary
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
- If Cycle 2 changes runtime/transport/plugin behavior, re-run the full smoke matrix per plan and keep all outputs in the plan-specific directories above.
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Validation and blocking rules:

- Run phase verification commands exactly as listed in the plan.
- Run CI parity preflight gates at Cycle 2 end exactly as listed in the plan.
- Treat any failed gate as blocking.
- If any gate fails, stop progression, record blocker details with exact command/output and remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable (Cycle 2):

- Publish concise final report including:
  - cycle and phase completion summary
  - full commit list (hash + subject + scope)
  - correctness, ergonomics, runtime, and test-determinism outcomes
  - benchmark deltas and no-regression status
  - CI parity and smoke outcomes
  - accepted deviations and rationale
