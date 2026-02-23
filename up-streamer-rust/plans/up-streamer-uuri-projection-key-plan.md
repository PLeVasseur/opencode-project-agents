# up-streamer UUri projection-key rollback+hardening plan

Status: ready  
Execution mode: manual only (no autopilot orchestration)  
Target branch: `refactor/up-streamer-domain-architecture`

## Objective

Restore projection-key keying (as used before `0a27762`) for runtime `HashMap`/`HashSet` usage and harden it with explicit cheap conversions so strict clippy passes without production `#[allow(clippy::mutable_key_type)]`, while preserving:

1. Existing behavior and dedupe semantics.
2. Existing public API/value surfaces that use `UUri`.
3. Cheap conversion boundaries (move-based where ownership is available).

## Non-goals

- No transport-architecture redesign.
- No outward API shape changes.
- No behavior/policy change in route resolution.

## Design constraints (source of truth)

- Runtime map keys must not be `UUri`.
- Runtime map keys must use immutable/hash-safe projected fields.
- Keep `UUri` in values and external/public-facing structures.
- Projection semantics for key fields follow canonical historic behavior:
  - `ue_version_major: u8`
  - `resource_id: u16`
- Conversions must be explicit and cheap:
  - `From<UUri>` for key projection (move path, no extra allocation)
  - `From<&UUri>` for projection from borrowed values (string clone only when unavoidable)
- No parse/serialize roundtrip for projection conversion.
- Production code should not require `#[allow(clippy::mutable_key_type)]` after migration.
- Test-only allowances are acceptable when ergonomics outweigh churn.

## Fixed decisions for this run

- [x] Use historical parity key widths (`u8`/`u16`) for version/resource in projection keys.
- [x] Pull projection-key shape back from the pre-`0a27762` model, then add conversion hardening.
- [x] Keep one local projection-key item per local domain:
  - [x] one canonical projection key type in `up-streamer` routing internals (shared by runtime routing users)
  - [x] one canonical projection key type local to `usubscription-static-file` runtime internals

## Execution discipline (strict)

- [x] Manual execution only; no autopilot orchestration.
- [x] Stay on branch `refactor/up-streamer-domain-architecture`.
- [x] Before each phase and before each commit, run:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
- [x] Follow phases/gates in strict order; if a gate fails, stop and remediate.
- [x] Continuously update this plan; flip each completed checkbox from `[ ]` to `[x]` immediately.

## Artifact policy

- [x] Write reports only under `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/`.
- [x] Do not create repo-local plan/report artifacts.

---

## Phase 0 - Fresh-session preflight (must be first action)

- [x] Verify environment/artifact roots:
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `test -n "$OPENCODE_CONFIG_DIR"`
  - [x] `test -d "$OPENCODE_CONFIG_DIR/plans"`
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/uuri-projection-key"`
- [x] Capture baseline:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] confirm current branch is `refactor/up-streamer-domain-architecture`
  - [x] `git status --short --branch`
  - [x] `git log --oneline -n 12`
- [x] Tooling sanity:
  - [x] `command -v cargo`
  - [x] `command -v rg`
- [x] Write preflight evidence:
  - [x] `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/00-preflight.md`

### Gate P0

- [x] Preflight complete and branch validated.

---

## Phase 1 - Inventory and exact migration surface

- [x] Inventory all current `mutable_key_type` allows and classify runtime vs test:
  - [x] `rg -n "allow\(clippy::mutable_key_type\)" up-streamer utils`
- [x] Capture rollback baselines from prior projection-key state:
  - [x] `git show 7f91836:up-streamer/src/routing/subscription_cache.rs`
  - [x] `git show 7f91836:up-streamer/src/routing/publish_resolution.rs`
  - [x] `git show 3ae173b:utils/usubscription-static-file/src/lib.rs`
- [x] Inventory runtime `UUri` key aliases/types/usages:
  - [x] `up-streamer/src/routing/subscription_cache.rs`
  - [x] `up-streamer/src/routing/publish_resolution.rs`
  - [x] `up-streamer/src/routing/subscription_directory.rs`
  - [x] `up-streamer/src/data_plane/ingress_registry.rs`
  - [x] `utils/usubscription-static-file/src/lib.rs`
- [x] Confirm key-type placement (fixed decision):
  - [x] one shared local key type in `up-streamer` runtime routing internals
  - [x] one local static-adapter key type in `usubscription-static-file`
- [x] Record inventory and decisions:
  - [x] `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/01-inventory-and-decisions.md`

### Gate 1

- [x] Full runtime migration surface is known and decisioned.

---

## Phase 2 - Implement projection key types + cheap conversions

- [x] Introduce projection key type(s) with immutable fields:
  - [x] `authority_name: String`
  - [x] `ue_id: u32`
  - [x] `ue_version_major: u8`
  - [x] `resource_id: u16`
- [x] Derive `Clone, Debug, Eq, PartialEq, Hash`.
- [x] Implement conversions:
  - [x] `impl From<UUri> for <ProjectionKey>` (move path; no authority clone)
  - [x] `impl From<&UUri> for <ProjectionKey>` (borrowed path; clone only where unavoidable)
  - [x] reverse conversion only if required by call sites
- [x] Add focused unit tests for conversion correctness and key equality semantics:
  - [x] owned-vs-borrowed conversion yields identical projected key
  - [x] projected key follows canonical version/resource extraction (`uentity_major_version`/`resource_id` semantics)
  - [x] no `to_uri()/from_str()` roundtrip used by conversion code paths
- [x] Write phase evidence:
  - [x] `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/02-key-type-and-conversions.md`

### Gate 2

- [x] Projection key type(s) compile and conversion tests pass.

---

## Phase 3 - Migrate `up-streamer` runtime maps to projection keys

- [x] Add one canonical projection-key item for runtime routing internals:
  - [x] create `up-streamer/src/routing/uri_identity_key.rs`
  - [x] wire module in `up-streamer/src/routing/mod.rs` (`pub(crate) mod uri_identity_key;`)
  - [x] re-use this single type from `subscription_cache` and `publish_resolution` (no duplicate per-file key structs)
- [x] Update `up-streamer/src/routing/subscription_cache.rs`:
  - [x] `SubscriptionIdentityKey` uses projection keys (not raw `UUri`)
  - [x] preserve wildcard merge/rebuild/dedupe behavior
- [x] Update `up-streamer/src/routing/publish_resolution.rs`:
  - [x] `SourceFilterLookup` keyed by projection key, values remain `UUri`
  - [x] preserve publish filter derivation behavior
- [x] Update call-through sites as needed:
  - [x] `up-streamer/src/routing/subscription_directory.rs`
  - [x] `up-streamer/src/data_plane/ingress_registry.rs`
- [x] Prefer move-path conversion at insertion boundaries where source `UUri` ownership exists.
- [x] Remove runtime `#[allow(clippy::mutable_key_type)]` in above runtime paths.
- [x] Keep or reduce test-only allowances as appropriate.
- [x] Run focused tests:
  - [x] `cargo test -p up-streamer`
- [x] Write phase evidence:
  - [x] `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/03-up-streamer-runtime-migration.md`

### Gate 3

- [x] `up-streamer` runtime no longer uses raw `UUri` map keys.
- [x] `up-streamer` focused tests pass.

---

## Phase 4 - Migrate `usubscription-static-file` runtime maps

- [x] Keep a single local static-adapter projection key item:
  - [x] one local key type reused for both topic/subscriber projection and dedupe maps
  - [x] avoid multiple competing local URI projection wrappers
- [x] Update `utils/usubscription-static-file/src/lib.rs`:
  - [x] runtime dedupe maps use projection keys
  - [x] values/responses remain `UUri`
  - [x] preserve resource-id normalization and subscriber dedupe semantics
- [x] Prefer move-path conversion in loops where `UUri` ownership is available.
- [x] Remove runtime `#[allow(clippy::mutable_key_type)]` in adapter production paths.
- [x] Keep test-only allowance only if still justified.
- [x] Run focused tests:
  - [x] `cargo test -p usubscription-static-file`
- [x] Write phase evidence:
  - [x] `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/04-static-adapter-migration.md`

### Gate 4

- [x] Static adapter runtime no longer uses raw `UUri` map keys.
- [x] Static adapter tests pass.

---

## Phase 5 - Lint policy hardening

- [x] Verify runtime paths have no `mutable_key_type` allows:
  - [x] `rg -n "allow\(clippy::mutable_key_type\)" up-streamer/src utils/usubscription-static-file/src`
- [x] Verify runtime paths have no raw `UUri` map/set keying:
  - [x] `rg -n "HashMap<\s*UUri|HashSet<\s*UUri" up-streamer/src/routing up-streamer/src/data_plane/ingress_registry.rs utils/usubscription-static-file/src/lib.rs`
  - [x] if any match remains in runtime code, refactor or document a narrow justified exception
- [x] Confirm remaining allows, if any, are test-only and justified.
- [x] Add brief rationale note for any retained test-only allow(s).
- [x] Write phase evidence:
  - [x] `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/05-lint-policy-handoff.md`

### Gate 5

- [x] No production `mutable_key_type` allowances remain in touched code.

---

## Phase 6 - Validation matrix

### 6.1 Required checks

- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

### 6.2 CI parity matrix (repo policy)

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo fmt -- --check`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [x] Unbundled matrix when prerequisite available:
  - [x] verify `VSOMEIP_INSTALL_PATH`
  - [x] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [x] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] if unavailable, record constrained skip + remediation

### 6.3 Mandatory smoke validation

- [x] Prepare and record smoke prerequisites:
  - [x] `source build/envsetup.sh highest`
  - [x] start MQTT broker: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
  - [x] ensure SOME/IP runtime libs are available on `LD_LIBRARY_PATH` for SOME/IP scenarios
  - [x] run each scenario from the working directory/config expected by that skill
- [x] Run each smoke skill and write scenario evidence under `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`:
  - [x] Skill: `transport-smoke-validation`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/transport-smoke-validation.md`
  - [x] Skill: `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
  - [x] Skill: `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
  - [x] Skill: `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
  - [x] Skill: `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
  - [x] Skill: `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
  - [x] Skill: `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
  - [x] Skill: `smoke-zenoh-someip-rr-zenoh-client-someip-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
  - [x] Skill: `smoke-zenoh-someip-rr-someip-client-zenoh-service`
    - [x] Report: `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service.md`
- [x] Record command/output evidence and pass/fail conclusion for each scenario report above.
- [x] If any scenario is blocked by missing external prerequisites, record constrained skip + concrete remediation in that scenario report.

### Gate 6

- [x] Validation complete and green (or constrained skip documented with remediation).

---

## Phase 7 - Reporting and commit discipline

### 7.1 Reports

- [x] Write final reports under `$OPENCODE_CONFIG_DIR/reports/uuri-projection-key/`:
  - [x] `00-preflight.md`
  - [x] `01-inventory-and-decisions.md`
  - [x] `02-key-type-and-conversions.md`
  - [x] `03-up-streamer-runtime-migration.md`
  - [x] `04-static-adapter-migration.md`
  - [x] `05-lint-policy-handoff.md`
  - [x] `06-validation-summary.md`
  - [x] `07-final-summary.md`

### 7.2 Commit chunking (suggested)

- [x] Commit A: projection key types + `up-streamer` runtime migration
- [x] Commit B: static adapter runtime migration + focused tests
- [x] Commit C: lint-policy cleanup + in-repo docs/code touchups (no OPENCODE report artifacts in git commits)

Before each commit, run and record:

- [x] `git rev-parse --abbrev-ref HEAD`
- [x] `git status --short --branch`
- [x] `git diff --name-only --cached`
- [x] `git diff --stat --cached`
- [x] ensure no `$OPENCODE_CONFIG_DIR/reports/**` artifacts are staged for commit

### Gate 7

- [x] Reports complete.
- [x] Commits scoped and documented.

---

## Exit criteria

- [x] Runtime keying no longer uses raw `UUri` where map/set key semantics matter.
- [x] Public behavior/API remains unchanged.
- [x] Conversion boundaries are explicit and cheap (`From<UUri>` move path first; borrowed path only when needed).
- [x] Projection key semantics match historic canonical behavior (`u8`/`u16` for version/resource).
- [x] One canonical local projection-key item exists per local domain (`up-streamer` routing, static adapter runtime).
- [x] Production `mutable_key_type` allowances removed from touched runtime paths.
- [x] CI parity checks pass (or constrained skips documented with remediation).
