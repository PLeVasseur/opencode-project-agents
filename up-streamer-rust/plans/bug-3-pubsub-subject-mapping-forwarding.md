# Plan: Bug #3 pubsub messages forwarded despite subject mapping mismatch

## Context
- Repo: `eclipse-uprotocol/up-streamer-rust`
- Upstream issue: `https://github.com/eclipse-uprotocol/up-streamer-rust/issues/74`
- Relevant code paths:
  - Listener registration and filter construction: `up-streamer/src/ustreamer.rs:281` to `up-streamer/src/ustreamer.rs:296`
  - Subscription cache lookup keyed by subscriber authority: `subscription-cache/src/lib.rs:125`, `subscription-cache/src/lib.rs:144`

## Problem statement
- Publish messages can be forwarded even when source/topic mappings should not allow forwarding.
- Current listener setup appears too broad in some cases (authority-level and/or insufficiently constrained publish filters), enabling false-positive forwarding.

## Goal
- Enforce strict pubsub forwarding based on configured source-topic -> subscriber mapping.
- Prevent unauthorized or unintended cross-authority topic flow.

## Investigation plan
1. Reproduce issue #74 exactly
- Use the authority A/B/C scenario from the issue body with the provided subscription JSON.
- Capture observed forwarding matrix (expected vs actual delivery).

2. Trace effective matching model
- Document how `USubscriptionStaticFile` data becomes `SubscriptionCache` entries.
- Trace how `ForwardingListeners::insert` registers:
  - authority-level listener for request/response/notification
  - publish listeners for each `subscriber.topic`
- Verify whether registered `source_uri` filters are sufficiently restrictive for publish matching semantics of each transport.

3. Identify mismatch root cause
- Determine whether incorrect forwarding is due to:
  - overly broad topic filters,
  - authority-keyed cache model losing necessary specificity,
  - transport listener semantics differences,
  - or a combination.

## Fix plan
1. Narrow pubsub match criteria in streamer
- Ensure publish listener registration uses the full intended source topic constraints and does not rely on authority-only routing.
- Keep request/response/notification logic separate from publish logic.

2. Tighten subscription selection model if required
- If authority-only cache keying is insufficient, extend cache indexing to include topic dimensions required for unambiguous publish matching.

3. Add test coverage for negative cases
- Add integration tests with three authorities (A/B/C) where only A->B is allowed.
- Assert C->B publish is not forwarded.
- Add wildcard variant tests from issue #74 to lock in expected behavior.

4. Cross-transport verification
- Verify behavior in at least zenoh<->mqtt and zenoh<->someip scenarios to ensure transport-specific listener semantics do not reintroduce leakage.

## Validation checklist
- Repro from issue #74 fails before fix and passes after fix.
- Negative publish forwarding tests exist and pass.
- Allowed mapping still forwards correctly.
- No regressions for request/response/notification forwarding.

## Risks and mitigations
- Risk: tightening filters may block legitimate wildcard subscriptions.
  - Mitigation: add explicit wildcard tests that represent intended permissive behavior.
- Risk: transport differences in listener semantics.
  - Mitigation: validate across multiple transports with shared test expectations.

## Exit criteria
- Publish forwarding obeys configured subject mappings with no cross-topic leakage.
- Issue #74 reproduction is resolved with automated regression coverage.
