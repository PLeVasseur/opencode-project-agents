Resume execution of the recovery plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-domain-modernization-recovery-plan.md`

Mission:

Close the remaining work with strict evidence integrity, starting at the earliest incomplete gate (Gate 6), then Gate 7. Preserve behavior/API compatibility and do not over-check items without command-level proof.

Execution constraints:

1. Manual execution only (no autopilot orchestration).
2. Stay on branch `refactor/up-streamer-domain-architecture`.
3. Follow phases/gates in order; do not skip Gate 6.
4. Treat every existing checkmark as provisional unless this session has sufficient evidence.

Required startup sequence:

1. Run the exact **Fresh-session bootstrap** commands from the plan.
2. Re-verify each command in this session context.
3. For upstream handling, follow the conditional branch in the plan (no-upstream vs upstream-present) and keep parent/child statuses consistent.

Mandatory first work item:

Perform a strict checklist/evidence audit before new coding:

- If a checked parent has any unchecked child, uncheck the parent.
- If evidence is ambiguous/conflicting, default to unchecked.
- If a claim is broad, split it into explicit child checkboxes and set each from evidence.

Current focus (must execute in this order):

## 1) Gate 6 reconciliation (Phase 6)

- Reconcile `phase6-doctest-hardening.md` with raw doctest logs.
- Re-run required Phase 6 validation commands and capture command-level evidence:
  - `cargo doc -p up-streamer --no-deps`
  - `cargo test -p up-streamer --doc`
- Prove whether control-plane/routing/data-plane/runtime doctests are actually executed vs ignored.
- Update Phase 6 and Gate 6 checkboxes strictly from current-session evidence.
- If non-ignored layer doctests still cannot be proven, keep related checkboxes unchecked and record blocker/remediation.

## 2) Gate 7 closure (Phase 7)

Run and evidence all required checks:

- `cargo build`
- `cargo fmt -- --check`
- `cargo clippy --all-targets -- -W warnings -D warnings`
- `cargo check --workspace --all-targets`
- `cargo test --workspace`

Then complete final transport re-validation:

- Re-run canonical Zenoh<=>SOME/IP scenario and capture pass/fail proof.
- Re-run canonical Zenoh<=>MQTT5 scenario and capture pass/fail proof.
- Ensure expected example binaries are used and outcomes are explicit.

Use the canonical setup/teardown/validation instructions from the plan section:

- `Canonical smoke test runbook (applies to Phase 1 baseline and Phase 7 rerun)`

Do not duplicate or diverge from those commands in this prompt; treat the plan as the single source of truth.

Produce/update required artifacts:

- `$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization/transport-matrix-final.md`
- `$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization/final-validation-summary.md`

Evidence policy (strict):

- Write/update artifacts only under:
  - `$OPENCODE_CONFIG_DIR/reports/up-streamer-domain-modernization/`
- For each evidence entry include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving the result
  - concise conclusion

Checkbox policy (always on):

- Parent `[x]` only when all nested children are `[x]`.
- Partial completion = unchecked parent + explicit child statuses.
- For conditional branches, check only the branch that actually occurred.

Commit discipline (strict):

Before every commit, capture and record:

- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits phase/wave scoped and rationale-focused.

Blocking behavior:

- If a gate fails, stop progression.
- Record blocker with exact command/output and concrete remediation path in the relevant report.
- Ask exactly one targeted question only if blocked by missing external prerequisite/credential or true ambiguity that materially changes outcome.

Completion output format:

When done, provide a concise final report containing:

- phase/gate status (including intentionally unchecked items)
- commit list (hash + subject + scope)
- canonical baseline vs final transport outcomes
- doctest/docs/core/workspace/test outcomes
- remaining blockers/follow-ups (if any)
