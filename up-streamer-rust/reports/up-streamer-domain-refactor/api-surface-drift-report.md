# API Surface Drift Report

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)
Baseline anchor commit SHA: `42d5a26136fd4f71ea873b7e414f8f6fdd9f17a8`

## Purpose

Prove public API stability (or explicitly document approved exceptions) for `up-streamer`.

## Hardening note

- [x] This report is gate-authoritative and all placeholder tokens are resolved.

## Capture Method

- [x] Baseline public API snapshot captured
- [x] Post-refactor public API snapshot captured
- [x] Same capture method used for both snapshots

### Capture command notes

```text
# Baseline capture method (Phase 2):
# 1) Read `up-streamer/src/lib.rs` for crate-root re-exports.
# 2) Read defining files for re-exported public types/methods:
#    - `up-streamer/src/endpoint.rs`
#    - `up-streamer/src/ustreamer.rs`
# 3) Record only crate-reachable public items for common users.
#
# Post-refactor capture method (locked): repeat exact same three-step method
# against the refactored tree to produce comparable baseline vs post snapshots.
```

## Public Item Diff

| Public item | Baseline | Post-refactor | Change type | Compatibility | Notes |
|---|---|---|---|---|---|
| `up_streamer::Endpoint` (re-export) | present (`pub use endpoint::Endpoint`) | present (`pub use endpoint::Endpoint`) | none | non-breaking | Primary outward type name is unchanged. |
| `Endpoint::new(name, authority, transport) -> Endpoint` | present | present | none | non-breaking | Constructor signature is unchanged. |
| `up_streamer::UStreamer` (re-export) | present (`pub use ustreamer::UStreamer`) | present (`pub use ustreamer::UStreamer`) | none | non-breaking | Primary outward type name is unchanged. |
| `UStreamer::new(name, message_queue_size, usubscription) -> Result<UStreamer, UStatus>` | present | present | none | non-breaking | Signature is unchanged for consumer crates. |
| `UStreamer::add_forwarding_rule(in, out) -> Result<(), UStatus>` | present | present | none | non-breaking | Signature is unchanged; behavior validated by API contract tests. |
| `UStreamer::delete_forwarding_rule(in, out) -> Result<(), UStatus>` | present | present | none | non-breaking | Signature is unchanged; behavior validated by API contract tests. |

## Approved Exceptions (if any)

| Exception | Reason | Migration guidance | Approval |
|---|---|---|---|
| None approved at Phase 2 design gate | DG-G requires API stability for common users | Any future exception must add before/after signature + call-site migration example | Pending only if exception is proposed |

## Conclusion

- [x] Public API remained stable for intended users.
- [x] Any differences are approved and documented with migration guidance.

Phase 7 note: post-refactor snapshot/diff finalization is complete and confirms no crate-root public API drift for common users.

## DG-G Acceptance Notes (Phase 2)

- Crate-root API stability is the default requirement.
- Internal module path churn is allowed if crate-root exports and common signatures remain stable.
- If unavoidable public drift appears in later waves, this report must include:
  - compatibility class (`non-breaking`, `source-breaking`, `behavioral`)
  - explicit migration snippet for each affected call site
  - approval record tied to DG-G follow-up review
