# Plan: Bug #1 vsomeip streamer use-case detection (critical)

## Context
- Upstream repo: `eclipse-uprotocol/up-transport-vsomeip-rust`
- Upstream PR: `https://github.com/eclipse-uprotocol/up-transport-vsomeip-rust/pull/42` (open)
- Downstream tracking issue: `https://github.com/eclipse-uprotocol/up-streamer-rust/issues/69`
- Local integration point confirms source filter authority is specific (not wildcard): `up-streamer/src/ustreamer.rs:52`, `up-streamer/src/ustreamer.rs:231`

## Problem statement
- Listener registration for the UStreamer path is misclassified in `determine_message_type.rs` because it expects source authority to be wildcard.
- UStreamer actually registers with a concrete source authority and wildcarded non-authority fields.
- Result: the Zenoh -> Router -> SOME/IP forwarding path may not be recognized as the streamer use case.

## Goal
- Ensure `up-transport-vsomeip` correctly recognizes streamer listener registrations so point-to-point forwarding works for the Zenoh/SOME-IP bridge.

## Scope and non-goals
- [ ] In scope: verify PR #42 correctness for streamer listener registration type detection.
- [ ] In scope: verify no regression in publish/request/response registration classification.
- [ ] In scope: verify downstream behavior in `up-streamer-rust` issue #69 scenario.
- [ ] Out of scope: unrelated refactors or feature work in `up-transport-vsomeip-rust`.
- [ ] Out of scope: general SOME/IP performance tuning or non-deterministic infra fixes beyond minimal reproducibility setup.

## Run order
- [ ] 1) Make local SOME/IP environment reproducible.
- [ ] 2) Capture baseline behavior/evidence with current dependency resolution.
- [ ] 3) Validate PR #42 logic and upstream regression tests.
- [ ] 4) Apply temporary pin/workaround in this repo and re-run downstream scenario.
- [ ] 5) Produce merge-confidence recommendation based on pass criteria.

## Implementation plan
- [ ] 1. Make local environment suitable for reproducible SOME/IP runs
  - Document and apply required env vars for this repo before baseline/e2e validation:
    - `VSOMEIP_INSTALL_PATH` (or bundled setup equivalent)
    - `GENERIC_CPP_STDLIB_PATH`
    - `ARCH_SPECIFIC_CPP_STDLIB_PATH`
    - `LD_LIBRARY_PATH`/`VSOMEIP_LIB_DIR` as needed for runtime loading
  - Use one reproducible path and record it in execution notes (prefer repo-documented setup via `.cargo/config.toml` or `build/envsetup.sh`).

- [ ] 2. Lock a reproducible baseline
  - Record current dependency resolution in this repo (`Cargo.toml`, `Cargo.lock`) including current `up-transport-vsomeip` commit.
  - Confirm baseline behavior in the source-of-truth issue #69 scenario:
    - streamer: `example-streamer-implementations` `zenoh_someip` with `DEFAULT_CONFIG.json5`
    - entities: `someip_client` <-> `zenoh_service`
  - Capture logs/evidence showing incorrect listener registration classification or forwarding failure.

- [ ] 3. Validate upstream candidate fix
  - Inspect PR #42 (`eclipse-uprotocol/up-transport-vsomeip-rust`) and verify streamer detection expects non-wildcard source authority with wildcarded non-authority fields.
  - Validate no behavioral regressions in request/response/publish registration classification.
  - Note whether extra trace logging is acceptable for temporary use or needs follow-up cleanup.

- [ ] 4. Create/maintain a temporary dependency workaround in this repo
  - Until upstream merge/release, pin `up-transport-vsomeip` to the Valtech fork commit containing the fix (`3e277e835916b9428d8492ea1ae1383c5131bca6`, or updated equivalent).
  - Keep all other dependency versions aligned with `up-streamer` compatibility set (`up-rust 0.5.0`, `up-transport-zenoh 0.6.0`) to avoid cross-version breakage.
  - Regenerate lockfile as needed and record exact resolved revision.

- [ ] 5. Add regression tests upstream (target repo)
  - Add focused unit tests for registration type detection:
    - source authority specific + sink authority specific + other fields wildcard => streamer case
    - wildcard source authority => not streamer case
    - publish/request/response classification remains unchanged
  - Ensure tests fail on pre-fix behavior and pass with fix.

- [ ] 6. Verify end-to-end in this repo (issue #69 pass/fail gate)
  - Re-run the agreed scenario (`zenoh_someip` + `someip_client` <-> `zenoh_service`, `DEFAULT_CONFIG.json5`) with fixed dependency.
  - Confirm forwarding works once listener registration is active and capture reproducible evidence (commands, logs, observed request/response flow).
  - Compare against baseline evidence and record final pass/fail outcome for issue #69.

- [ ] 7. Upstream handoff and cleanup
  - Once PR #42 (or equivalent) is merged and released, switch back from fork pin to upstream dependency.
  - Re-run verification and remove temporary workaround notes/pins.

## Evidence to collect
- [ ] Exact commands used for baseline and fixed runs.
- [ ] Key logs that show listener registration classification before and after fix.
- [ ] E2E message-flow evidence for `zenoh_someip` + `someip_client` <-> `zenoh_service` with `DEFAULT_CONFIG.json5`.
- [ ] Dependency evidence (`Cargo.toml`/`Cargo.lock`) proving which `up-transport-vsomeip` revision was tested.
- [ ] Final issue #69-ready result statement: baseline result, fixed result, and reproducibility notes.

## Merge confidence pass criteria
- [ ] Upstream registration-type unit tests cover streamer case and non-streamer boundary cases.
- [ ] Tests demonstrate pre-fix failure (or mismatch) and post-fix success for streamer detection.
- [ ] Publish/request/response classification behavior remains unchanged by the fix.
- [ ] Downstream issue #69 scenario succeeds with fixed dependency under documented environment.
- [ ] Results are repeatable across multiple runs in the same environment.

## Fallback decision path
- [ ] If E2E is flaky or environment-sensitive, run the downstream scenario at least 3 times and report pass rate.
- [ ] If E2E remains inconclusive, require upstream unit-test evidence plus deterministic classification logs before merge recommendation.
- [ ] If regression appears in non-streamer classification, block merge recommendation and isolate minimal reproducer.

## Validation checklist
- [ ] Local environment prerequisites for SOME/IP build/runtime are documented and reproducible.
- [ ] Unit tests in `up-transport-vsomeip-rust` cover streamer-use-case detection.
- [ ] End-to-end zenoh<->someip forwarding works in `example-streamer-implementations/src/bin/zenoh_someip.rs`.
- [ ] No regression in request/response/publish routing paths.
- [ ] `up-streamer-rust` issue #69 can be closed with reproducible evidence.

## Risks and mitigations
- Risk: PR #42 includes extra logging/noise beyond minimal fix.
  - Mitigation: accept functional fix first; optionally follow up with logging cleanup.
- Risk: hidden dependency incompatibilities during fork pin.
  - Mitigation: keep versions aligned to current workspace constraints and lockfile.

## Exit criteria
- [ ] Streamer registration is correctly detected in vsomeip transport.
- [ ] Zenoh -> SOME/IP path is confirmed working in manual/integration testing.
- [ ] Temporary fork pin is either documented as required workaround or removed after upstream release.
