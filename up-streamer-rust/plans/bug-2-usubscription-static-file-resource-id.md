# Plan: Bug #2 hardcoded resource ID in usubscription-static-file

## Context
- Repo: `eclipse-uprotocol/up-streamer-rust`
- Affected code: `utils/usubscription-static-file/src/lib.rs:119` to `utils/usubscription-static-file/src/lib.rs:124`
- Current behavior force-sets `uri.resource_id = 0x8001` during subscription file parsing.

## Problem statement
- Subscription keys from JSON are parsed, then their `resource_id` is overwritten.
- Any Route/subscription mapping that uses non-`0x8001` resource IDs is silently changed.
- This can break topic-level routing correctness in multi-topic deployments.

## Goal
- Preserve `resource_id` from the subscription JSON as authoritative input.
- Keep backward compatibility for existing configs that already use `0x8001`.

## Implementation plan
1. Define expected parsing semantics
- Parsed topic UUri fields from JSON must remain unchanged unless validation explicitly fails.
- Remove implicit mutation of `resource_id`.

2. Implement minimal code fix
- In `USubscriptionStaticFile::fetch_subscriptions`, stop mutating `uri.resource_id`.
- Replace warning text with either:
  - no warning, or
  - explicit deprecation/compat warning only if an opt-in compatibility mode is ever introduced.

3. Add regression tests
- Add tests for `usubscription-static-file` parsing with at least two distinct resource IDs.
- Assert cache/subscription entries preserve per-topic resource IDs exactly as configured.

4. Verify integration behavior
- Exercise streamer setup with subscription file containing mixed resource IDs.
- Confirm forwarding listener registrations are created per expected topic (no forced collapse to `0x8001`).

5. Optional compatibility strategy (if needed)
- If downstream users rely on old behavior, gate legacy override behind explicit config flag (default off).
- Document migration note: old implicit behavior removed.

## Validation checklist
- No code path overwrites parsed `resource_id` by default.
- New tests fail on old behavior and pass with fix.
- Existing `0x8001` examples still pass unchanged.
- Mixed-resource subscription files route as configured.

## Risks and mitigations
- Risk: some setups unknowingly depend on the bug.
  - Mitigation: communicate behavior change clearly; offer temporary opt-in compatibility flag only if required.
- Risk: inadequate test coverage for topic matching.
  - Mitigation: add explicit mixed-resource integration case.

## Exit criteria
- Subscription parsing preserves user-configured resource IDs.
- Topic routing behavior matches JSON mapping without hidden mutation.
- Regression tests enforce this permanently.
