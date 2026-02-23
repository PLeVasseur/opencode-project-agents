# Phase 2 Logging Modernization (`log` usage -> `tracing`)

Date: 2026-02-10

## Migration actions

- Updated `up-linux-streamer-plugin/src/lib.rs` to replace `zenoh_util::try_init_log_from_env()` calls with `tracing_subscriber::fmt::try_init()` via `try_init_tracing_from_env()` helper.
- Replaced `tracing::log::trace!(...)` with native `trace!(...)` macro usage.
- Removed residual `try_init_log_from_env` callsites from project-owned source.

## Evidence

### 1) Direct `log` API usage scan

- exact command: `rg -n "\\blog::|tracing::log::" . --glob "*.rs"`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status/pass-fail: `1` (no matches)
- key output lines:
  - `(no matches)`
- concise conclusion: No project-authored source currently calls direct `log::` or `tracing::log::*` APIs.

### 2) Legacy `try_init_log_from_env` scan

- exact command: `rg -n "try_init_log_from_env" . --glob "*.rs"`
- working directory: repo root
- exit status/pass-fail: `1` (no matches)
- key output lines:
  - `(no matches)`
- concise conclusion: Legacy zenoh log-init bridge callsites were removed from project-owned source.

### 3) `log` crate reverse dependency inspection

- exact command: `cargo tree -i log`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `log v0.4.29`
  - `├── tracing v0.1.44`
  - `│   ├── up-linux-streamer-plugin v0.1.0 (...)`
  - `├── paho-mqtt v0.13.3`
- concise conclusion: `log` remains as a transitive dependency in third-party stacks (including tracing ecosystem and transport dependencies), not via direct project logging API calls.

## Safety/behavior note

The plugin initialization now uses `tracing_subscriber::fmt::try_init()` (non-panicking on prior global subscriber setup), preserving safe startup behavior when host/runtime logging is already initialized.
