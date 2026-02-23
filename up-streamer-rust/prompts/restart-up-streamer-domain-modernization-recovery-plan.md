Restart execution of the recovery plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-domain-modernization-recovery-plan.md`

Mission:

Complete the remaining plan work in a fresh session with strict checkbox/evidence integrity, without regressing behavior or API compatibility.

Execution mode and constraints:

1. Manual execution only (no autopilot orchestration).
2. Stay on branch `refactor/up-streamer-domain-architecture`.
3. Follow phases and gates in order; do not skip gates.
4. Treat prior checkmarks as historical claims that must be re-validated in this session context.

Required startup sequence:

1. Run the exact "Fresh-session bootstrap" commands from the plan.
2. Re-verify each step in this session even if previously checked.
3. For upstream handling, follow the conditional checklist branch in the plan (no-upstream vs upstream-present) and keep parent/child statuses consistent.

Mandatory first work item (before new coding):

Perform a restart audit of checked items, focusing on strict parent/child integrity and evidence sufficiency:

- If a checked parent has unchecked/incomplete children, uncheck the parent.
- If a checked item is broad/conditional, split it into explicit child checkboxes and set statuses per actual evidence.
- If evidence is missing/ambiguous, default to unchecked and state what proof is needed.

After audit, continue execution from the earliest still-incomplete gate.

Always-on checkbox policy (must be enforced continuously):

- A parent checkbox may be `[x]` only when every nested child is `[x]`.
- Partial completion must be represented by an unchecked parent plus explicit checked/unchecked children.
- Conditional branches must be represented explicitly; only check the branch that actually occurred.

Evidence and artifact policy:

- Write/update artifacts only under:
  - `$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization/`
- Do not create repo-local plans/prompts/reports.
- For each evidence entry include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Commit discipline (strict):

Before every commit, capture and record:

- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits phase/wave scoped and rationale-focused.

Known pending strictness gaps to resolve during restart:

- Add dedicated command-level Phase 3 hardening evidence linkage/artifact.
- Complete non-ignored layer doctest execution for control-plane/routing/data-plane/runtime (or keep related items unchecked with explicit blocker rationale).
- Finish Phase 7 full validation + final transport matrix rerun + final summary artifacts.

Blocking behavior:

- If any gate fails, stop progression.
- Record blocker with exact command/output and concrete remediation path in the appropriate report.
- Ask one targeted question only if blocked by missing external prerequisite/credential or true ambiguity that changes outcomes.

Completion output:

When done, provide a concise completion report with:

- phase/gate status (including any intentionally unchecked items)
- commit list (hash + subject + scope)
- canonical transport baseline/final outcomes
- test/workspace/doc/doctest outcomes
- remaining follow-ups (if any)
