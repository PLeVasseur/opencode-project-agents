Execute the recovery plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-domain-modernization-recovery-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration for this run.
2. Follow phases and gates in strict order. Do not skip gates.
3. Update the plan continuously; change each completed checkbox from `[ ]` to `[x]` immediately.
4. Keep work on branch `refactor/up-streamer-domain-architecture`.
5. First action must be the Phase 0 checkpoint commit.

Source-of-truth constraints:

- Outward API remains streamer-centric (`Endpoint`, `UStreamer`).
- Internal modules must be domain-scoped and cohesive (control-plane, routing, data-plane, runtime, API facade).
- Modernize naming/mechanics (not just moving code between files).
- Preserve behavior across unit/integration/workspace and canonical transport E2E scenarios.
- Code-line metrics must count only actual code lines (exclude comments/doc comments/blank lines).

Critical behavior and design requirements:

- Start with canonical transport matrix baseline before refactor edits:
  - Zenoh <=> SOME/IP request/response
  - Zenoh <=> MQTT5 request/response
- Make transport orchestration rock-solid using the plan's terminal-by-terminal steps.
- Use pinned dependency reality: `ComparableTransport` is not publicly reusable from pinned `up-rust 0.9.0`; keep/rename local identity keying with explicit rationale.
- Consolidate redundant facade/runtime layering where it adds no value.
- Ensure each behavior family has one logical owner file/module.

Commit discipline (mandatory):

Before every commit:

- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits wave-scoped and rationale-focused. Do not batch unrelated changes.

Artifacts and evidence:

- Use only the minimal artifact set defined in the plan under:
  - `$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization/`
- For every evidence entry include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Validation requirements:

- Preserve and improve test readability (helper extraction, explicit assertions, scenario clarity).
- Keep E2E example binaries working for expected scenarios.
- Run final checks exactly as specified by the plan (build/fmt/clippy/tests/workspace + canonical transport re-run).

Blocking policy:

- If a gate fails, stop progression.
- Record blocker with exact command/output and a concrete remediation path in the appropriate report.
- Ask one targeted question only if truly blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases complete, provide a concise final report with:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - canonical transport baseline and final outcomes
  - test/workspace validation outcomes
  - any accepted deviations and rationale
