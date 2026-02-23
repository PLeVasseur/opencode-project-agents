# Tracing Migration Plan

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Define workspace-wide migration from `log`/`env_logger` usage to `tracing`/`tracing-subscriber`.

## Policy

- [x] Libraries do not unconditionally perform global subscriber initialization.
- [x] Binaries/plugins own one-time subscriber initialization boundaries.
- [x] Event and span naming conventions documented.

## Migration Inventory

| Crate | `log::*` usage | `env_logger` usage | `tracing` target state | Priority |
|---|---:|---:|---|---|
| `example-streamer-uses` | present (multi-bin logging macros) | present (`env_logger::init` per bin) | migrate macros to `tracing::{info,...}` and centralize init helper per executable | high |
| `utils/hello-world-protos` | none found | none found | no migration needed | low |
| `utils/integration-test-utils` | present (debug-heavy helpers) | present (`env_logger::builder` test helper) | switch helpers to tracing test subscriber utility | medium |
| `example-streamer-implementations` | present | present | migrate bin to tracing + single init at program start | high |
| `configurable-streamer` | present | present | migrate bin to tracing + single init at program start | high |
| `up-linux-streamer-plugin` | mixed (`tracing` and `tracing::log`) | present (`env_logger::init`) | remove log bridge calls; use tracing events only + one plugin-owned subscriber init path | high |
| `up-streamer` | present (core library + tests) | present (`Endpoint::new` try_init) | migrate library instrumentation to tracing and remove global-init side effect from library API | highest |
| `subscription-cache` | present | manifest includes env_logger but runtime init absent | migrate macros to tracing; drop unused env_logger dep if confirmed | medium |
| `utils/usubscription-static-file` | present | none found | migrate macros to tracing (library, no global init) | medium |

## Sequencing

| Step | Scope | Risk | Validation |
|---|---|---|---|
| 1 | establish subscriber init policy in affected executables/plugins | medium (startup regressions) | `cargo check --workspace --all-targets` + smoke run of main binaries/plugin load |
| 2 | migrate library instrumentation points (`up-streamer`, `subscription-cache`, `usubscription-static-file`, test utils) | high (library side effects and log shape changes) | targeted crate tests + behavior-conservation matrix spot checks |
| 3 | migrate binary/plugin instrumentation and init boundaries | medium (double-init or missing output) | startup checks for `configurable-streamer`, `zenoh_someip`, example bins, plugin run |
| 4 | close out remaining `log`/`env_logger` usages | low-medium (stragglers) | workspace grep audit + clippy/test matrix |

## Event/Span Conventions

- Event names use domain verbs and nouns (`route_added`, `listener_registered`, `publish_filter_rejected`).
- Include stable keys: `in_authority`, `out_authority`, `forwarding_id`, and transport role (`ingress`/`egress`).
- Use spans for lifecycle scopes (`add_forwarding_rule`, `delete_forwarding_rule`, plugin startup).
- Reserve `error` events for actionable failures; use `debug` for high-volume transport message details.
- Keep library crates init-free; executables/plugins install subscribers once at process/plugin boundary.

## Validation and Completion

- [ ] Workspace tracing hygiene check completed.
- [x] `workspace-tracing-migration-status.md` fully populated.
- [x] Any deferred migration is explicitly documented and approved.
