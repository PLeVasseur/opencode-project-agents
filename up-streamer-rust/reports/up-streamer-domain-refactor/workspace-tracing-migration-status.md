# Workspace Tracing Migration Status

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Provide per-crate migration status and dependency ledger for tracing/runtime alignment.

## Per-Crate Status Ledger

| Crate | `log` status | `env_logger` status | `tracing` status | `async-std` status | Notes |
|---|---|---|---|---|---|
| `example-streamer-uses` | migrated | migrated | migrated | not-applicable | Binaries now emit `tracing` events and initialize with `tracing_subscriber::fmt::try_init()`. |
| `utils/hello-world-protos` | not-applicable | not-applicable | not-applicable | not-applicable | No runtime/logging surfaces found. |
| `utils/integration-test-utils` | migrated | migrated | migrated | not-applicable | `init_logging` now configures tracing subscriber test writer. |
| `example-streamer-implementations` | migrated | migrated | migrated | not-applicable | `zenoh_someip` migrated to tracing macros and `tracing-subscriber` init. |
| `configurable-streamer` | migrated | migrated | migrated | not-applicable | Main executable migrated to tracing macros and `tracing-subscriber` init. |
| `up-linux-streamer-plugin` | migrated | migrated | migrated | not-applicable | Plugin startup path now uses `tracing-subscriber` instead of `env_logger`. |
| `up-streamer` | migrated | migrated | migrated | not-applicable | Library logging migrated to tracing; removed global init side effect from `Endpoint::new`. |
| `subscription-cache` | migrated | migrated | migrated | migrated | Log usage migrated and stale `async-std`/`env_logger` deps removed. |
| `utils/usubscription-static-file` | migrated | not-applicable | migrated | migrated | Log usage migrated and stale `async-std` dep removed. |

Allowed values for status cells:

- `migrated`
- `retained-with-rationale`
- `not-applicable`

## Subscriber Initialization Boundaries

| Crate | Type (lib/bin/plugin) | Init ownership | Verified |
|---|---|---|---|
| `example-streamer-uses` | bin | each bin owns one-time `tracing_subscriber::fmt::try_init` | yes |
| `utils/hello-world-protos` | lib | no subscriber init needed | yes |
| `utils/integration-test-utils` | lib | test helper owns explicit one-time `tracing_subscriber` init | yes |
| `example-streamer-implementations` | bin | main owns one-time `tracing_subscriber` init | yes |
| `configurable-streamer` | bin | main owns one-time `tracing_subscriber` init | yes |
| `up-linux-streamer-plugin` | plugin | plugin run path owns one-time `tracing_subscriber` init | yes |
| `up-streamer` | lib | no global subscriber init in library surfaces | yes |
| `subscription-cache` | lib | no init call present | yes |
| `utils/usubscription-static-file` | lib | no init call present | yes |

## Deferred/Follow-Up Items

| Item | Reason deferred | Impact | Follow-up owner |
|---|---|---|---|
| None | N/A | N/A | N/A |
