Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-ergonomics-perf-guardrails-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration.
2. Set and pin execution branch at the start of the session:
   - `export EXEC_BRANCH="refactor/up-streamer-domain-architecture"`
   - Hard-fail immediately if current branch differs from `EXEC_BRANCH`.
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

Benchmarking and guardrail requirements:

- Use Criterion as the benchmark framework exactly as specified in the plan.
- Use the Rust CLI `criterion-guardrail` for threshold gating (no Python guardrail).
- Keep benchmark commands pinned to the plan's canonical command set and arguments.
- Respect rerun-on-breach policy exactly as specified.

Artifact and evidence constraints:

- Write all execution reports only under:
  - `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/`
- Write benchmark raw exports only under:
  - `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/`
- Write smoke skill reports only under this plan-unique location:
  - `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills/`
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Mandatory smoke validation requirements:

- Execute all smoke skills listed in plan section `10.3 Mandatory smoke validation`.
- Produce one report per required scenario at the exact paths listed in the plan.
- If blocked by missing external prerequisites, record constrained skip and concrete remediation in that scenario report.

Blocking policy:

- If any gate fails, stop progression.
- Record blocker details with exact command/output and remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

When all phases are complete, provide a concise final report with:

- phase/gate completion summary
- commit list (hash + subject + scope)
- ergonomics outcomes (composition/lifetimes/API ergonomics)
- benchmark outcomes vs baseline and threshold status
- guardrail CLI outcomes and CI/advisory status
- build/fmt/clippy/check/test and CI parity outcomes
- smoke skill execution outcomes (all scenarios)
- accepted deviations and rationale
