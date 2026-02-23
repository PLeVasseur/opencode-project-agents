# PR-78 Copyright Header Remediation Plan

## Objective

Add missing copyright headers and correct non-2026 year values for files introduced by this branch, while preserving behavior and keeping fixture/data artifacts unchanged.

## Session Bootstrap (fresh session)

- [x] Fetch refs and verify the working branch context.
  - [x] `git fetch --all --prune`
  - [x] `git rev-parse --verify bugfix/issue-74-left-topic-authority`
  - [x] `git rev-parse --verify cleanup/refactor-upstream-main`
  - [x] `git checkout cleanup/refactor-upstream-main`
- [x] Generate the authoritative in-scope file list from git range (do not rely only on static inventory).
  - [x] `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$'`
  - [x] Reconcile any drift between command output and the Target Inventory section before editing.
- [x] Capture baseline audit snapshot before edits.
  - [x] Missing-header baseline: `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$' | xargs -r rg -L "Copyright"`
  - [x] Non-2026 baseline: `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$' | xargs -r rg -n "Copyright \\(c\\) (2024|2025|2027|2028|2029)"`
  - [x] Wrong-year seed check: `rg -n "Copyright \\(c\\)" up-streamer/tests/api_contract_forwarding_rules.rs`

## Scope Lock

- Branch scope for remediation: `bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main`
- In scope:
  - Newly added code/config/script files in the above range (`.rs`, `.toml`, `.sh`)
  - One wrong-year header correction
- Out of scope (no header insertion):
  - Fixture/data artifacts (`.log`, `.csv`, `.json`) such as:
    - `utils/transport-smoke-suite/tests/fixtures/**/*.log`
    - `utils/criterion-guardrail/tests/fixtures/**/*.csv`
    - `utils/transport-smoke-suite/claims/*.json`
- [x] Confirm out-of-scope fixture/data policy is preserved.
  - [x] Keep claims `.json` files header-free (JSON does not support comments).
  - [x] Keep fixture `.log` and `.csv` files header-free as deterministic data inputs.

## Header Style Contract

- Rust (`.rs`): match existing block style used in `up-streamer/src/lib.rs` with year `2026`.
- TOML (`.toml`): match `#` comment style used in existing workspace manifests with year `2026`.
- Shell (`.sh`): keep shebang on line 1, then add `#`-style copyright block with year `2026`.

- [x] Use exact header templates (copy/paste-safe) with year `2026`.
  - [x] Rust header template:

```rust
/********************************************************************************
 * Copyright (c) 2026 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Apache License Version 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************/
```

  - [x] TOML header template:

```toml
# Copyright (c) 2026 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
```

  - [x] Shell header template (insert after shebang):

```bash
#
# Copyright (c) 2026 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
```

## Target Inventory

### A) Correct non-2026 header (1 file)

- [x] `up-streamer/tests/api_contract_forwarding_rules.rs` (`2024` -> `2026`)

### B) Add missing headers to new code/config/script files (48 files)

#### Script

- [x] `scripts/bench_streamer_criterion.sh`

#### up-streamer Rust files

- [x] `up-streamer/benches/streamer_criterion.rs`
- [x] `up-streamer/src/benchmark_support.rs`
- [x] `up-streamer/src/control_plane/mod.rs`
- [x] `up-streamer/src/control_plane/route_lifecycle.rs`
- [x] `up-streamer/src/control_plane/route_table.rs`
- [x] `up-streamer/src/control_plane/transport_identity.rs`
- [x] `up-streamer/src/data_plane/egress_pool.rs`
- [x] `up-streamer/src/data_plane/egress_worker.rs`
- [x] `up-streamer/src/data_plane/ingress_listener.rs`
- [x] `up-streamer/src/data_plane/ingress_registry.rs`
- [x] `up-streamer/src/data_plane/mod.rs`
- [x] `up-streamer/src/observability/events.rs`
- [x] `up-streamer/src/observability/fields.rs`
- [x] `up-streamer/src/observability/mod.rs`
- [x] `up-streamer/src/routing/authority_filter.rs`
- [x] `up-streamer/src/routing/mod.rs`
- [x] `up-streamer/src/routing/publish_resolution.rs`
- [x] `up-streamer/src/routing/subscription_cache.rs`
- [x] `up-streamer/src/routing/subscription_directory.rs`
- [x] `up-streamer/src/routing/uri_identity_key.rs`
- [x] `up-streamer/src/runtime/mod.rs`
- [x] `up-streamer/src/runtime/worker_runtime.rs`
- [x] `up-streamer/src/subscription_sync_health.rs`
- [x] `up-streamer/tests/support/mod.rs`

#### criterion-guardrail files

- [x] `utils/criterion-guardrail/Cargo.toml`
- [x] `utils/criterion-guardrail/src/lib.rs`
- [x] `utils/criterion-guardrail/src/main.rs`
- [x] `utils/criterion-guardrail/tests/fixture_tree.rs`

#### transport-smoke-suite files

- [x] `utils/transport-smoke-suite/Cargo.toml`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-rr-someip-client-zenoh-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/smoke-zenoh-someip-rr-zenoh-client-someip-service.rs`
- [x] `utils/transport-smoke-suite/src/bin/transport-smoke-matrix.rs`
- [x] `utils/transport-smoke-suite/src/claims.rs`
- [x] `utils/transport-smoke-suite/src/env.rs`
- [x] `utils/transport-smoke-suite/src/lib.rs`
- [x] `utils/transport-smoke-suite/src/logs.rs`
- [x] `utils/transport-smoke-suite/src/process.rs`
- [x] `utils/transport-smoke-suite/src/report.rs`
- [x] `utils/transport-smoke-suite/src/scenario.rs`
- [x] `utils/transport-smoke-suite/tests/fixture_audit.rs`
- [x] `utils/transport-smoke-suite/tests/scenario_contracts.rs`

## Execution Phases

### Phase 1: Apply headers in-place

- [x] Add `2026` Rust header block to all `.rs` files listed above.
- [x] Add `2026` TOML `#` header block to both new `Cargo.toml` files.
- [x] Add `2026` shell `#` header block to `scripts/bench_streamer_criterion.sh` after shebang.
- [x] Correct year to `2026` in `up-streamer/tests/api_contract_forwarding_rules.rs`.

### Phase 2: Verification

- [x] Rebuild authoritative in-scope file list and confirm it matches Target Inventory.
  - [x] `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$'`
  - [x] If drift exists, update Target Inventory first, then apply/remediate headers.
- [x] Verify no missing headers in in-scope extensions.
  - [x] `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$' | xargs -r rg -L "Copyright"`
- [x] Verify no non-2026 years remain in in-scope extensions.
  - [x] `git diff --name-only --diff-filter=A bugfix/issue-74-left-topic-authority..cleanup/refactor-upstream-main | rg '\\.(rs|toml|sh)$' | xargs -r rg -n "Copyright \\(c\\) (2024|2025|2027|2028|2029)"`
- [x] Verify wrong-year fix file.
  - [x] `rg -n "Copyright \\(c\\) 2026" up-streamer/tests/api_contract_forwarding_rules.rs`
- [x] Verify scope and intent are preserved.
  - [x] `git diff --stat`
  - [x] Spot-check `git diff` to confirm header-only edits in in-scope files.
  - [x] Confirm out-of-scope fixture/data files remain unchanged in meaning.

### Phase 3: Commit and PR update

- [x] Stage only copyright/header edits.
- [x] Commit message: `chore: align new-file copyright headers to 2026`
- [x] Push branch and add PR #78 note: header remediation complete; no functional behavior changes.

## Acceptance Criteria

- [x] All in-scope added `.rs`, `.toml`, and `.sh` files have a copyright header.
- [x] All in-scope new/updated header years are `2026`.
- [x] `up-streamer/tests/api_contract_forwarding_rules.rs` year is `2026`.
- [x] Fixture/data files (`.log`, `.csv`, `.json`) remain intentionally unchanged.
- [x] Command-generated in-scope target list and Target Inventory are reconciled (no drift).
- [x] Header format matches existing repository style for each file type.
- [x] Final diff for this remediation is header-only (no functional behavior changes).
