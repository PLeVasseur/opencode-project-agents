# up-streamer Route Identity and API Cleanup Plan

Status: ready
Execution mode: manual only (no autopilot orchestration)
Target branch: `refactor/up-streamer-domain-architecture`

## Objective

Resolve architecture/API cleanup concerns raised in review:

1. Remove unnecessary URI key wrappers and use `UUri` directly where safe.
2. Make route lifecycle errors idiomatic Rust errors (`Display` + `Error`).
3. Canonicalize transport identity handling (single local transport identity key; no duplicate wrappers).
4. Remove backward-compatible route alias APIs and migrate all call sites to canonical route APIs.

## Clarified assumptions (source of truth)

- Do not pursue external transport-abstraction migration in this plan; keep transport identity work local to `up-streamer` internals.
- `uSubscription` remains canonical subscription source; `uStreamer` remains dispatcher/router.
- Public refresh API stays `refresh_subscriptions() -> Result<SubscriptionSyncHealth, UStatus>`.
- Public refresh visibility remains sync-health only (no canonical subscription introspection API).
- Keep work on one branch and one PR.

## Execution discipline (strict)

- [x] Manual execution only; do not use autopilot orchestration.
- [x] Stay on branch `refactor/up-streamer-domain-architecture` for the full run.
- [x] Before each phase and before each commit, verify branch via `git rev-parse --abbrev-ref HEAD` and `git status --short --branch`.
- [x] Update this plan continuously: flip each completed checkbox from `[ ]` to `[x]` immediately.
- [x] Follow phases and gates in strict order.
- [x] If a gate fails, stop progression, document blocker evidence, and remediate before proceeding.

## Evidence requirements (all phase reports)

Every evidence entry must include:

- [x] exact command
- [x] working directory (if not repo root)
- [x] exit status and pass/fail
- [x] key output lines proving result
- [x] concise conclusion

---

## Fresh-session preflight (must be first action)

- [x] Verify environment and plan/report roots:
  - [x] `printenv OPENCODE_CONFIG_DIR`
  - [x] `test -n "$OPENCODE_CONFIG_DIR"`
  - [x] `test -d "$OPENCODE_CONFIG_DIR/plans"`
  - [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/route-identity-api-cleanup"`
- [x] Verify branch/worktree and capture baseline:
  - [x] `git status --short --branch`
  - [x] confirm current branch is `refactor/up-streamer-domain-architecture`
  - [x] `git log --oneline -n 12`
- [x] Verify required tooling:
  - [x] `command -v cargo`
  - [x] `command -v rg`
- [x] Record preflight evidence in:
  - [x] `$OPENCODE_CONFIG_DIR/reports/route-identity-api-cleanup/00-preflight.md`

### Gate P0

- [x] Preflight completed and branch validated.

---

## Phase 1 - Inventory and decision capture

### 1.1 Locate current implementation points

- [x] Inventory URI identity wrappers and usage sites:
  - [x] `up-streamer/src/routing/subscription_cache.rs`
  - [x] `up-streamer/src/routing/publish_resolution.rs`
  - [x] `utils/usubscription-static-file/src/lib.rs`
- [x] Inventory route lifecycle error enums:
  - [x] `up-streamer/src/control_plane/route_lifecycle.rs`
- [x] Inventory transport identity key type and usage:
  - [x] `up-streamer/src/control_plane/transport_identity.rs`
  - [x] `up-streamer/src/control_plane/route_table.rs`
  - [x] `up-streamer/src/data_plane/egress_pool.rs`
  - [x] `up-streamer/src/data_plane/ingress_registry.rs`
- [x] Inventory all old API call sites:
  - [x] `add_forwarding_rule`
  - [x] `delete_forwarding_rule`

### 1.2 Decision notes (explicit)

- [x] Capture decision: keep transport identity handling local to `up-streamer` (no external transport-abstraction migration in this scope).
- [x] Capture decision target: replace `UUriIdentityKey` usage with `UUri` map keys unless a correctness/lint blocker is proven.
- [x] Capture decision on lint strategy if `UUri` key triggers clippy mutable-key diagnostics (localized allow only where unavoidable; no broad allow).
- [x] Write decisions and command evidence to:
  - [x] `$OPENCODE_CONFIG_DIR/reports/route-identity-api-cleanup/01-inventory-and-decisions.md`

### Gate 1

- [x] All touchpoints and decisions recorded with file-level scope.

---

## Phase 2 - Replace URI identity wrappers with `UUri`

### 2.1 `up-streamer` routing cache/resolver

- [x] Refactor `up-streamer/src/routing/subscription_cache.rs`:
  - [x] remove `UUriIdentityKey`
  - [x] use `UUri` in `SubscriptionIdentityKey` fields
  - [x] preserve dedupe semantics and wildcard merge behavior
- [x] Refactor `up-streamer/src/routing/publish_resolution.rs`:
  - [x] change `SourceFilterLookup` key to `UUri`
  - [x] preserve publish source filter derivation behavior

### 2.2 Static adapter consistency

- [x] Refactor `utils/usubscription-static-file/src/lib.rs`:
  - [x] remove local `UUriIdentityKey`
  - [x] use `UUri` in subscription/subscriber dedupe maps
  - [x] preserve static resource-id normalization and fetch behavior

### 2.3 Tests and behavior protection

- [x] Update/add tests to keep behavior explicit:
  - [x] same-subscriber/different-topic coexistence
  - [x] rebuild removes stale rows
  - [x] wildcard merge behavior unchanged
  - [x] adapter `fetch_subscribers` dedupe unchanged
- [x] Run focused checks for touched crates:
  - [x] `cargo test -p up-streamer`
  - [x] `cargo test -p usubscription-static-file`

### Gate 2

- [x] `UUriIdentityKey` removed from touched crates (or any exception documented with concrete blocker and rationale).
- [x] Targeted tests pass.

---

## Phase 3 - Route lifecycle errors become idiomatic

### 3.1 Error trait implementation

- [x] Update `up-streamer/src/control_plane/route_lifecycle.rs`:
  - [x] implement `Display` for `AddRouteError`
  - [x] implement `std::error::Error` for `AddRouteError`
  - [x] implement `Display` for `RemoveRouteError`
  - [x] implement `std::error::Error` for `RemoveRouteError`

### 3.2 Mapping and contract preservation

- [x] Update `up-streamer/src/ustreamer.rs` mapping code as needed:
  - [x] maintain existing `UCode` mapping (`INVALID_ARGUMENT`, `ALREADY_EXISTS`, `NOT_FOUND`)
  - [x] keep externally observable behavior stable unless explicitly justified

### 3.3 Test updates

- [x] Add/adjust tests for error-to-status mapping and message stability where applicable.
- [x] Run focused tests:
  - [x] `cargo test -p up-streamer --tests`

### Gate 3

- [x] Route lifecycle errors implement `Display` + `Error`.
- [x] API contract behavior remains correct.

---

## Phase 4 - Transport identity handling cleanup (local scope)

### 4.1 Consolidation

- [x] Ensure exactly one local transport identity type is used workspace-wide in `up-streamer` internals.
- [x] Remove redundant wrappers/aliases if any appear during refactor.
- [x] Keep pointer-identity semantics for transport instance keying (`Arc::ptr_eq` / pointer hash) unless stronger invariant is intentionally introduced.
- [x] No-op exit path: if Phase 1 inventory proves the current state already uses a single local type with no duplicates, record explicit no-op evidence in `04-transport-identity-canonicalization.md` and mark this phase complete without churn edits.

### 4.2 Documentation and tests

- [x] Document why a local transport key type exists (trait-object keying requirements and pointer-identity behavior).
- [x] Keep/adjust route identity tests:
  - [x] route key equality with shared transport instances
  - [x] route key inequality for distinct transport instances

### Gate 4

- [x] Single canonical transport key path is in place and justified.
- [x] Route identity tests pass.

---

## Phase 5 - Remove backward-compatible route alias APIs

### 5.1 API removal

- [x] Remove from `up-streamer/src/ustreamer.rs`:
  - [x] `add_forwarding_rule(...)`
  - [x] `delete_forwarding_rule(...)`

### 5.2 Call-site migration to canonical API

- [x] Update production call sites:
  - [x] `configurable-streamer/src/main.rs` (`add_route`)
  - [x] `example-streamer-implementations/src/bin/zenoh_someip.rs` (`add_route`)
  - [x] `up-linux-streamer-plugin/src/lib.rs` (`add_route`)
- [x] Update test call sites in `up-streamer/tests/**` to `add_route` / `delete_route`.

### 5.3 Docs and references

- [x] Update/remove compatibility references:
  - [x] `up-streamer/src/lib.rs` compatibility note
  - [x] `up-streamer/README.md` diagrams/examples
- [x] Verify no old API references remain:
  - [x] `rg -n "add_forwarding_rule|delete_forwarding_rule" .`
- [x] Add explicit breaking-change migration note in `05-api-alias-removal.md` (and PR summary, if a PR is opened): callers must use `add_route` / `delete_route`.

### Gate 5

- [x] Legacy aliases removed.
- [x] All call sites and docs migrated.

---

## Phase 6 - Validation and regression protection

### 6.1 Required checks

- [x] `cargo fmt -- --check`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo check --workspace --all-targets`
- [x] `cargo test --workspace`

### 6.2 Transport-facing build confidence

- [x] `cargo build -p configurable-streamer`
- [x] `cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`

### 6.3 CI parity matrix (full, per repo policy)

- [x] `source build/envsetup.sh highest`
- [x] `cargo build`
- [x] `cargo clippy --all-targets -- -W warnings -D warnings`
- [x] `cargo fmt -- --check`
- [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- [ ] Unbundled matrix when prerequisite available:
  - [x] verify `VSOMEIP_INSTALL_PATH`
  - [ ] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [x] if unavailable, record constrained skip + remediation

### 6.4 Optional smoke escalation rule

- [ ] If route resolution behavior changes materially after Phase 2/4, run smoke skill matrix and record evidence under:
  - [ ] `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/`

### Gate 6

- [x] Validation complete and green (or constrained skip documented with remediation).

---

## Phase 7 - Reporting and commit discipline

### 7.1 Reports (mandatory)

- [x] Write phase reports under:
  - [x] `$OPENCODE_CONFIG_DIR/reports/route-identity-api-cleanup/`
- [x] Required report files:
  - [x] `00-preflight.md`
  - [x] `01-inventory-and-decisions.md`
  - [x] `02-uuri-key-migration.md`
  - [x] `03-route-error-traits.md`
  - [x] `04-transport-identity-canonicalization.md`
  - [x] `05-api-alias-removal.md`
  - [x] `06-validation-summary.md`
  - [x] `07-final-summary.md`
- [x] `07-final-summary.md` must include:
  - [x] phase/gate completion table
  - [x] commit list (hash + subject + scope)
  - [x] accepted deviations and rationale
  - [x] explicit breaking-change note for alias API removal and migration path

### 7.2 Commit chunking (scoped, meaningful messages)

- [x] Commit A: URI key simplification + associated tests
- [x] Commit B: route lifecycle error traits + status mapping polish
- [x] Commit C: alias API removal + call-site/doc migration

Before every commit:

- [x] `git rev-parse --abbrev-ref HEAD` (must equal `refactor/up-streamer-domain-architecture`)
- [x] `git status --short --branch`
- [x] `git diff --name-only --cached`
- [x] `git diff --stat --cached`

Commit message guidance:

- [x] Use intent-first messages (why-focused), for example:
  - [x] `refactor: use UUri keys for subscription identity dedupe`
  - [x] `refactor: make route lifecycle errors idiomatic and explicit`
  - [x] `refactor: remove forwarding-rule aliases and migrate callers`

### Gate 7

- [x] Reports complete.
- [x] Commits are scoped and documented.

---

## Blocking policy

- [x] If any gate fails, stop progression.
- [x] Record blocker in current phase report with:
  - [x] exact command
  - [x] working directory
  - [x] exit status
  - [x] key output lines
  - [x] concrete remediation path
- [x] Resume only after remediation evidence is captured.

---

## Final acceptance checklist

- [x] `UUriIdentityKey` usage removed from targeted components (or exception explicitly justified with evidence).
- [x] `AddRouteError` and `RemoveRouteError` implement `Display + Error`.
- [x] Transport identity handling is canonicalized to one local key type and documented.
- [x] `add_forwarding_rule` / `delete_forwarding_rule` removed.
- [x] All previous users migrated to `add_route` / `delete_route`.
- [x] Breaking-change migration note is documented in final summary (and PR summary when applicable).
- [x] Docs/tests updated; no stale API references remain.
- [x] Validation matrix complete and evidence written to reports.
- [x] Plan is executable by a fresh session with no hidden assumptions.
