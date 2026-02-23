Execute the plan at:

`$OPENCODE_CONFIG_DIR/plans/up-streamer-uuri-projection-key-plan.md`

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

- Runtime keying must not use raw `UUri` where map/set key semantics matter.
- Projection key semantics must follow historical canonical behavior:
  - `ue_version_major: u8`
  - `resource_id: u16`
- Keep `UUri` in values/public-facing surfaces.
- Conversion boundaries must be explicit and cheap:
  - `From<UUri>` move path first (no authority clone)
  - `From<&UUri>` borrowed path only when ownership is unavailable
  - no parse/serialize (`to_uri`/`from_str`) roundtrip conversions
- Keep one canonical local projection-key item per local domain:
  - one shared local type for `up-streamer` runtime routing internals
  - one local type for `usubscription-static-file` runtime internals
- Production code should not require `#[allow(clippy::mutable_key_type)]` in touched runtime paths.
- Test-only allowances are permitted only with explicit rationale.

Implementation requirements:

1. Rollback baseline and migration surface
   - Capture prior projection-key baselines from:
     - `7f91836:up-streamer/src/routing/subscription_cache.rs`
     - `7f91836:up-streamer/src/routing/publish_resolution.rs`
     - `3ae173b:utils/usubscription-static-file/src/lib.rs`
   - Inventory current runtime `UUri` keying and `mutable_key_type` allows.

2. Projection key type(s) + conversions
   - Reintroduce immutable projection keying with canonical `u8/u16` semantics.
   - Ensure owned-vs-borrowed conversions yield identical projected keys.
   - Prefer move-path conversion at insertion boundaries when `UUri` ownership exists.

3. Runtime migration
   - Migrate `up-streamer` runtime routing maps to projection keys.
   - Migrate `usubscription-static-file` runtime dedupe maps to projection keys.
   - Preserve dedupe/wildcard/resource-id normalization behavior.

4. Lint and policy hardening
   - Remove production `#[allow(clippy::mutable_key_type)]` from touched runtime files.
   - Keep only justified test-only allowances (if any).

Commit discipline (mandatory):

Before every commit, run and record:

- `git rev-parse --abbrev-ref HEAD`
- `git status --short --branch`
- `git diff --name-only --cached`
- `git diff --stat --cached`

Keep commits scoped to plan chunks; do not batch unrelated changes.

Artifacts and evidence:

- Use only plan-defined artifacts under:
  - `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/`
- Mandatory smoke artifacts go under:
  - `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`
- Every evidence entry must include:
  - exact command
  - working directory (if not repo root)
  - exit status/pass-fail
  - key output lines proving result
  - concise conclusion

Critical validation requirements:

- Run all validation commands listed in plan Phase 6.
- Run CI parity matrix exactly as listed in plan Phase 6.2.
- For unbundled matrix: if `VSOMEIP_INSTALL_PATH` is unavailable, record constrained skip + concrete remediation.

Mandatory smoke validation requirements:

- Execute all smoke skills listed in plan Phase 6.3 and write one report per skill at the exact paths specified.
- This includes `transport-smoke-validation` and all explicit `smoke-zenoh-*` scenario skills listed in the plan.
- Each smoke report must include command/output evidence and a pass/fail conclusion.

Blocking policy:

- If a gate fails, stop progression.
- Record blocker with exact command/output and concrete remediation path in the active phase report.
- Ask one targeted question only if blocked by a missing external prerequisite or ambiguity that materially changes behavior.

Completion deliverable:

- When all phases complete, provide a concise final report that includes:
  - phase/gate completion summary
  - commit list (hash + subject + scope)
  - projection-key migration outcome (runtime `UUri` key removal status)
  - conversion strategy outcome (`From<UUri>` move path + borrowed fallback)
  - production lint-policy outcome (`mutable_key_type` allow removal status)
  - build/fmt/clippy/check/test and CI parity outcomes
  - smoke skill execution outcomes (all scenarios)
  - accepted deviations and rationale
