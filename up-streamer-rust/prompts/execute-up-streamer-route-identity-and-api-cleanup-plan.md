Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-route-identity-and-api-cleanup-plan.md`

Execution mode and scope:

1. Manual execution only. Do not use autopilot orchestration.
2. First action must be the plan's fresh-session preflight section.
3. Follow phases and gates in strict order; if a gate fails, stop progression.
4. Keep all work on branch `refactor/up-streamer-domain-architecture`.
5. Before each phase and before each commit, run:
   - `git rev-parse --abbrev-ref HEAD`
   - `git status --short --branch`
6. Update the plan continuously; flip each completed checkbox from `[ ]` to `[x]` immediately.

Source-of-truth constraints:

- Do not pursue external transport-abstraction migration in this run; transport identity work remains local to `up-streamer` internals.
- `uSubscription` remains canonical subscription source; `uStreamer` remains dispatcher/router.
- Public refresh API remains `refresh_subscriptions() -> Result<SubscriptionSyncHealth, UStatus>`.
- Public refresh visibility remains health-only (`SubscriptionSyncHealth`), not canonical subscription data introspection.

Implementation requirements:

1. URI identity cleanup
   - Replace `UUriIdentityKey` usage with `UUri` keys where safe in:
     - `up-streamer/src/routing/subscription_cache.rs`
     - `up-streamer/src/routing/publish_resolution.rs`
     - `utils/usubscription-static-file/src/lib.rs`
   - Preserve dedupe/wildcard/resource-id semantics.
   - If a correctness/lint blocker prevents full replacement, document exact blocker and narrow rationale.

2. Route lifecycle error idioms
   - Implement `Display` and `std::error::Error` for:
     - `AddRouteError`
     - `RemoveRouteError`
   - Preserve outward `UStatus` code mapping semantics unless explicitly justified.

3. Transport identity local canonicalization
   - Ensure one local transport identity type path across `up-streamer` internals.
   - Preserve pointer-identity semantics for transport keying.
   - If already canonical per inventory, treat Phase 4 as no-op and record no-op evidence (do not churn code).

4. Remove alias API and migrate callers
   - Remove `add_forwarding_rule` and `delete_forwarding_rule` from `up-streamer/src/ustreamer.rs`.
   - Migrate all usages to `add_route` / `delete_route`, including:
     - `configurable-streamer/src/main.rs`
     - `example-streamer-implementations/src/bin/zenoh_someip.rs`
     - `up-linux-streamer-plugin/src/lib.rs`
     - `up-streamer/tests/**`
   - Update docs/references and ensure no stale alias references remain.

Commit discipline (mandatory):

Before every commit, run and record:

- `git rev-parse --abbrev-ref HEAD`
- `git status --short --branch`
- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits scoped to plan chunks; do not batch unrelated changes.

Artifacts and evidence:

- Use only plan-defined artifacts under:
  - `$OPENCODE_CONFIG_DIR/reports/route-identity-api-cleanup/`
- If optional smoke escalation is triggered, use:
  - `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Critical validation requirements:

- Run all validation commands listed in plan Phase 6.
- Run CI parity matrix exactly as listed in plan Phase 6.3.
- For unbundled matrix: if `VSOMEIP_INSTALL_PATH` is unavailable, record constrained skip + concrete remediation.
- Run optional smoke skills only if route resolution behavior changed materially; record trigger rationale.

Blocking policy:

- If a gate fails, stop progression.
- Record blocker with exact command/output and concrete remediation path in the active phase report.
- Ask one targeted question only if blocked by a missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases complete, provide a concise final report that includes:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - URI identity migration outcome (`UUriIdentityKey` removal/exception)
  - route lifecycle error trait outcome (`Display` + `Error`)
  - transport identity canonicalization outcome (or no-op rationale)
  - alias API removal + migration completion status
  - explicit breaking-change migration note for removed aliases
  - build/fmt/clippy/check/test and CI parity outcomes
  - accepted deviations and rationale
