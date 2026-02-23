Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-runtime-lint-debt-cleanup-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration for this run.
2. Follow phases and gates in strict order, including the preflight gate and blocking policy.
3. Update the plan continuously; change each completed checkbox from `[ ]` to `[x]` immediately.
4. Keep work on branch `refactor/up-streamer-domain-architecture`.
5. First action must be the fresh-session preflight section in the plan.

Source-of-truth constraints:

- Runtime standardization target is Tokio (no project `async-std` usage in source/manifests).
- Logging standardization target is `tracing` for project-owned code.
- Transitive `log` crate presence is acceptable only when no direct project `log::` / `tracing::log::*` API usage remains.
- Remove dead code where feasible without changing intended behavior.
- Remove `#[allow(...)]` where feasible by rewriting code, not by broad suppression.
- Preserve existing behavior across workspace tests and transport smoke scenarios.

Commit discipline (mandatory):

Before every commit:

- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits wave-scoped and rationale-focused. Do not batch unrelated changes.

Artifacts and evidence:

- Use only plan-defined artifacts under:
  - `$OPENCODE_CONFIG_DIR/reports/runtime-lint-debt-cleanup/`
- For smoke skill execution evidence, use:
  - `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`
- For every evidence entry include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Critical validation requirements:

- Run strict clippy checks exactly as defined in the plan.
- For dead code and `allow` remnants, produce explicit line-level reports when anything remains.
- If transport/plugin integration is touched, run the unbundled checks when `VSOMEIP_INSTALL_PATH` is available; otherwise record constrained skip with remediation.
- Execute all 8 smoke skills listed in the plan and verify:
  - per-skill evidence directories under `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-*/`
  - summary at `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md`

Blocking policy:

- If a gate fails, stop progression.
- Record blocker with exact command/output and a concrete remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases complete, provide a concise final report with:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - async runtime result (`async-std` removal/proof)
  - logging migration result (`log` -> `tracing`) and any accepted transitive-only exceptions
  - dead-code status (removed vs remnant report links)
  - clippy-allow status (removed vs remnant report links)
  - build/fmt/clippy/check/test outcomes
  - 8-skill smoke execution outcomes
  - accepted deviations and rationale
