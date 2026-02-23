# PR-83 up-rust idiomatic usage sweep inventory

Date: 2026-02-17
Repository: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`

## Finding table

| Status | File | Line | Pattern | Proposed replacement | Risk | Owner phase |
| --- | --- | --- | --- | --- | --- | --- |
| done | up-streamer/src/observability/fields.rs | 73 | deep attribute chains for id/type/source/sink | use `id()`, `type_()`, `source()`, `sink()` accessors | low | L1 |
| done | up-streamer/src/routing/publish_resolution.rs | 63 | wildcard authority string compare | use `has_wildcard_authority()` and `authority_name().as_str()` | low | L1 |
| done | utils/integration-test-utils/src/integration_test_utils.rs | 145 | nested attribute/source/id extraction | accessor helpers where available | medium | L2 |
| done | utils/integration-test-utils/src/up_client_foo.rs | 314 | wildcard authority string compare | semantic URI helper usage | low | L2 |
| done | example-streamer-uses/src/bin/common/mod.rs | 68 | direct `attributes.as_ref().unwrap()` | use `message.attributes()` with explicit missing-attributes handling | low | L2 |
| done | up-streamer/src/control_plane/mod.rs | 20 | doctest custom `MockTransport` | adopt hidden helper around `up_rust::MockTransport` (`test-util`) | medium | L3 |
| done | up-streamer/src/data_plane/mod.rs | 20 | doctest custom `MockTransport` | adopt hidden helper around `up_rust::MockTransport` (`test-util`) | medium | L3 |
| done | up-streamer/src/routing/mod.rs | 19 | doctest custom `MockTransport` | adopt hidden helper around `up_rust::MockTransport` (`test-util`) | medium | L3 |
| done | up-streamer/src/lib.rs | 24 | doctest custom `MockTransport` | adopt hidden helper around `up_rust::MockTransport` (`test-util`) | medium | L3 |
| done | up-streamer/src/data_plane/ingress_listener.rs | 78 | direct payload format field path | use `msg.payload_format().unwrap_or_default()` | low | L4 |
| done | up-streamer/src/routing/subscription_cache.rs | 144 | direct borrowed authority clone | use `uri.authority_name()` accessor | low | L4 |
| done | up-streamer/src/routing/uri_identity_key.rs | 43 | direct borrowed authority clone | use `uri.authority_name()` accessor | low | L4 |
| done | utils/usubscription-static-file/src/lib.rs | 63 | direct borrowed authority clone | use `uri.authority_name()` accessor | low | L4 |
| done | example-streamer-uses/src/bin/common/cli.rs | 126 | direct authority field assertion | use `uuri.authority_name()` accessor in tests | low | L4 |
| exempt | up-streamer/src/routing/uri_identity_key.rs | 32 | direct owned authority move | keep owned move to avoid accessor-induced clone | low | L4 |
| exempt | utils/usubscription-static-file/src/lib.rs | 52 | direct owned authority move | keep owned move to avoid accessor-induced clone | low | L4 |
| exempt | utils/integration-test-utils/src/integration_test_utils.rs | 365 | mutable access to message attributes internals | no equivalent `up-rust` mutable accessor for this mutation flow | medium | L4 |
| exempt | utils/integration-test-utils/src/integration_test_utils.rs | 367 | direct protobuf wrapper mutation (`attributes.id.0`) | no equivalent `up-rust` setter for message ID mutation | medium | L4 |
| exempt | up-streamer/src/routing/publish_resolution.rs | 55 | direct `ue_id` projection read | no helper for full raw `ue_id`; direct field required | low | L4 |
| exempt | up-streamer/src/routing/publish_resolution.rs | 87 | direct `ue_id` source filter construction | no helper for full raw `ue_id`; direct field required | low | L4 |
| exempt | up-streamer/src/routing/publish_resolution.rs | 194 | direct `ue_id` equivalence assertion | no helper for full raw `ue_id`; direct field required | low | L4 |
| exempt | up-linux-streamer-plugin/src/lib.rs | 180 | direct `ue_id` read from UUri-like config path | no helper for full raw `ue_id`; direct field required | low | L4 |
| exempt | example-streamer-implementations/src/bin/zenoh_someip.rs | 113 | direct `ue_id` read from UUri-like config path | no helper for full raw `ue_id`; direct field required | low | L4 |
| exempt | utils/usubscription-static-file/src/lib.rs | 172 | direct `resource_id` mutation for canonicalization | no setter helper for canonicalization writes | low | L4 |
| exempt | utils/usubscription-static-file/src/lib.rs | 308 | direct `resource_id` mutation for canonicalization | no setter helper for canonicalization writes | low | L4 |

## Notes

- Inventory expanded with repository-wide grep sweep for targeted anti-patterns.
- Status values: `open`, `done`, `exempt`.
- Doctest mock modernization is now fully adopted (no exemption for PR-83 scope).
- Residual whole-codebase idiom closure pass (L4) is dispositioned as `done` or `exempt` per policy.
