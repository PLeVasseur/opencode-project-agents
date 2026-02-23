Resume the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-usubscription-decoupled-pubsub-migration-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration for this run.
2. Follow phases and gates in strict order, including preflight and blocking policy.
3. Update the plan continuously; change each completed checkbox from `[ ]` to `[x]` immediately.
4. Keep work on branch `refactor/up-streamer-domain-architecture`.
5. First action must be the fresh-session preflight section in the plan.

Source-of-truth constraints:

- `uSubscription` remains the canonical subscription source; `uStreamer` remains dispatcher/router.
- `up-streamer` must accept a trait-object subscription snapshot provider at construction.
- Keep static mode default for required streamer binaries.
- Keep `live_usubscription` as reserved/fail-fast in this phase (no silent fallback).
- Public refresh API target: `refresh_subscriptions() -> Result<SubscriptionSyncHealth, UStatus>`.
- Public refresh visibility is health-only (`SubscriptionSyncHealth`), not canonical subscription data introspection.
- Remove `subscription-cache` as a standalone crate by inlining into `up-streamer` internals.
- Keep `usubscription-static-file` as an adapter crate.
- Do not introduce direct `up-subscription-rust` dependency in `up-streamer`.
- Live integration with real `up-subscription-rust` runtime is deferred in this phase; capture follow-up readiness.

Commit discipline (mandatory):

Before every commit:

- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits scoped to the plan chunks. Do not batch unrelated changes.

Artifacts and evidence:

- Use only plan-defined artifacts under:
  - `$OPENCODE_CONFIG_DIR/reports/usubscription-decoupled-pubsub-migration/`
- For smoke skill execution evidence, use:
  - `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`
- For every evidence entry include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Critical validation requirements:

- Run full CI parity matrix exactly as defined in the plan.
- Run all 8 smoke skills and verify:
  - per-skill evidence directories under `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-*/`
  - summary at `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md`
- Validate static mode behavior and reserved-live fail-fast behavior in required streamer binaries.
- Capture deferred live integration rationale/prerequisites in `05-live-integration-deferred.md`.

Blocking policy:

- If a gate fails, stop progression.
- Record blocker with exact command/output and concrete remediation path in the active phase report.
- Ask one targeted question only if blocked by missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases complete, provide a concise final report with:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - provider API and refresh/sync-health outcomes
  - workspace topology result (`subscription-cache` removal, `usubscription-static-file` retained)
  - static mode + reserved-live fail-fast validation outcomes
  - build/fmt/clippy/check/test outcomes
  - 8-skill smoke execution outcomes
  - deferred live-integration follow-up readiness summary
  - accepted deviations and rationale
