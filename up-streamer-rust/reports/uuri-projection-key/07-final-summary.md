# Phase 7 Final Summary

## Overall Outcome

- Plan execution status: COMPLETE
- Branch: `refactor/up-streamer-domain-architecture`
- Runtime map/set keying outcome: raw `UUri` removed from touched runtime key semantics in `up-streamer` and `usubscription-static-file`.

## Commit Summary

1. `582481f` - `refactor: restore immutable URI projection keys in up-streamer routing`
   - Scope:
     - `up-streamer/src/routing/uri_identity_key.rs`
     - `up-streamer/src/routing/subscription_cache.rs`
     - `up-streamer/src/routing/publish_resolution.rs`
     - `up-streamer/src/routing/subscription_directory.rs`
     - `up-streamer/src/data_plane/ingress_registry.rs`
     - `up-streamer/src/routing/mod.rs`

2. `8cb0f9a` - `refactor: migrate static subscription dedupe to projection keys`
   - Scope:
     - `utils/usubscription-static-file/src/lib.rs`

## Conversion Strategy Outcome

- `From<UUri>` move-path implemented for both local projection key types:
  - `up-streamer` `UriIdentityKey`
  - `usubscription-static-file` `UriProjectionKey`
- `From<&UUri>` borrowed fallback implemented for both types where values must remain `UUri`.
- No parse/serialize roundtrips (`to_uri`/`from_str`) in projection conversion code paths.

## Lint Policy Outcome

- Production `#[allow(clippy::mutable_key_type)]` removed from touched runtime files.
- Remaining allowance is outside runtime migration path (`utils/integration-test-utils`) and documented as test-support-only rationale.

## Validation Outcome

- Required checks: PASS (`fmt`, `clippy`, `check`, `test --workspace`)
- CI parity matrix: PASS (base, bundled, unbundled)
- Smoke skills: PASS for all required scenarios
  - Details in `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/*.md`

## Commit Discipline Evidence

- Before each commit, executed and recorded:
  - `git rev-parse --abbrev-ref HEAD`
  - `git status --short --branch`
  - `git diff --name-only --cached`
  - `git diff --stat --cached`
- No OPENCODE report artifacts were staged for commits.

## Accepted Deviations and Rationale

1. Suggested Commit C in plan not created as a separate commit.
   - Rationale: lint-policy cleanup naturally coalesced into Commits A/B with no remaining independent in-repo delta.

2. Smoke client/publisher commands commonly exited with `124`.
   - Rationale: each scenario intentionally uses `timeout 45s` for bounded execution; pass/fail is based on log evidence criteria, not process natural completion.
