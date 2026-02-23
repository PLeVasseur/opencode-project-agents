# PR-83 up-rust idiomatic usage sweep exemptions

Date: 2026-02-17

## Policy

- Every exemption must include exact file and line.
- Every exemption must cite missing API or compatibility blocker.
- Every exemption must include follow-up action.

## Exemptions

- Exemption ID: `EX-RB-001` (Category R-B ownership/perf)
  - File: `up-streamer/src/routing/uri_identity_key.rs:32`
  - File: `utils/usubscription-static-file/src/lib.rs:52`
  - Pattern: direct owned move of `uri.authority_name`.
  - Rationale: `UUri::authority_name()` returns an owned `String`; in these `From<UUri>` conversions, direct field move avoids unnecessary clone/allocation.
  - Follow-up action: replace with accessor only if `up-rust` introduces by-value extraction semantics or if conversion path changes make clone cost irrelevant.

- Exemption ID: `EX-RC-001` (Category R-C API-gap mutation)
  - File: `utils/integration-test-utils/src/integration_test_utils.rs:365`
  - File: `utils/integration-test-utils/src/integration_test_utils.rs:367`
  - Pattern: direct mutable message attribute internals (`msg.attributes.as_mut()`, `attributes.id.0 = ...`).
  - Rationale: `up-rust 0.9.0` provides read accessors for message IDs but no equivalent mutable setter/accessor path for in-place ID regeneration in this helper flow.
  - Follow-up action: migrate to setter-based idiom when available, or refactor helper to rebuild messages through builder APIs if project decides mutation should be eliminated.

- Exemption ID: `EX-RD-001` (Category R-D full `ue_id` helper gap)
  - File: `up-streamer/src/routing/publish_resolution.rs:55`
  - File: `up-streamer/src/routing/publish_resolution.rs:87`
  - File: `up-streamer/src/routing/publish_resolution.rs:194`
  - File: `up-streamer/src/routing/uri_identity_key.rs:33`
  - File: `up-streamer/src/routing/uri_identity_key.rs:44`
  - File: `utils/usubscription-static-file/src/lib.rs:53`
  - File: `utils/usubscription-static-file/src/lib.rs:64`
  - File: `up-linux-streamer-plugin/src/lib.rs:180`
  - File: `example-streamer-implementations/src/bin/zenoh_someip.rs:113`
  - File: `example-streamer-uses/src/bin/common/cli.rs:127`
  - Pattern: direct reads of full `ue_id` field.
  - Rationale: `up-rust` provides component helpers (`uentity_type_id`, `uentity_instance_id`) but no accessor returning the full canonical raw `ue_id` value used in these projection/build/assertion paths.
  - Follow-up action: replace direct field reads if/when `up-rust` exposes a full-identity accessor.

- Exemption ID: `EX-RD-002` (Category R-D resource canonicalization write gap)
  - File: `utils/usubscription-static-file/src/lib.rs:172`
  - File: `utils/usubscription-static-file/src/lib.rs:308`
  - Pattern: direct `resource_id` writes for canonicalization.
  - Rationale: no higher-level setter/helper exists for this canonicalization mutation path.
  - Follow-up action: migrate when setter-style helper support is available, or if canonicalization is redesigned around immutable reconstruction.
