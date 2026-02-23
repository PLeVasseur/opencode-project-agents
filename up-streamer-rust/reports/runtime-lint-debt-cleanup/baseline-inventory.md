# Phase 0 Baseline Inventory

Date: 2026-02-10

## Evidence

### 1) Branch and working tree baseline

- exact command: `git status --short --branch`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `## refactor/up-streamer-domain-architecture`
- concise conclusion: Work started on the required execution branch.

### 2) Manifest async runtime inventory

- exact command: `rg -n "async-std|async_std" . --glob "Cargo.toml"`
- working directory: repo root
- exit status/pass-fail: `1` (no matches)
- key output lines:
  - `(no matches)`
- concise conclusion: No direct `async-std` references found in workspace manifests.

### 3) Source async runtime inventory

- exact command: `rg -n "async-std|async_std|async_std::" . --glob "*.rs"`
- working directory: repo root
- exit status/pass-fail: `1` (no matches)
- key output lines:
  - `(no matches)`
- concise conclusion: No direct `async-std` source usage found.

### 4) Async-related dependency tree inventory

- exact command: `cargo tree --workspace --all-features | rg "async-std|async_std|async-io|async-global-executor|smol" || true`
- working directory: repo root
- exit status/pass-fail: `0` (pass; no matching dependency lines)
- key output lines:
  - `(no matches)`
- concise conclusion: No target async-runtime crates detected in all-features dependency tree output.

### 5) Logging API baseline inventory

- exact command: `rg -n "\\blog::|tracing::log::|try_init_log_from_env" . --glob "*.rs"`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./up-linux-streamer-plugin/src/lib.rs:67:            zenoh_util::try_init_log_from_env();`
  - `./up-linux-streamer-plugin/src/lib.rs:139:        zenoh_util::try_init_log_from_env();`
  - `./up-linux-streamer-plugin/src/lib.rs:140:        trace!("up-linux-streamer-plugin: after try_init_log_from_env()");`
  - `./up-linux-streamer-plugin/src/lib.rs:196:            tracing::log::trace!("someip_config_file_abs_path: {someip_config_file_abs_path:?}");`
- concise conclusion: Project-owned legacy logging usage is currently isolated to `up-linux-streamer-plugin`.

### 6) Source `allow` inventory (broad)

- exact command: `rg -n "#\\!\\[allow\\(|#\\[allow\\(" . --glob "*.rs" --glob "!target/**"`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./up-linux-streamer-plugin/src/lib.rs:107:        #[allow(dead_code)] // Allowing this to be able to configure streamer at runtime later`
  - `./up-streamer/src/routing/subscription_directory.rs:21:    #[allow(clippy::mutable_key_type)]`
  - `./utils/usubscription-static-file/src/lib.rs:14:#![allow(clippy::mutable_key_type)]`
  - `./utils/integration-test-utils/src/integration_test_utils.rs:253:#[allow(clippy::too_many_arguments)]`
- concise conclusion: Multiple `allow` attributes remain across workspace crates; candidates for burn-down in later phases.

### 7) `allow(dead_code|clippy|unused)` focused inventory

- exact command: `rg -n "allow\\(dead_code\\)|allow\\(clippy::|allow\\(unused" . --glob "*.rs" --glob "!target/**"`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./example-streamer-uses/src/bin/common/cli.rs:79:#[allow(dead_code)]`
  - `./up-streamer/tests/support/mod.rs:22:#[allow(dead_code)]`
  - `./subscription-cache/src/lib.rs:268:    #[allow(clippy::mutable_key_type)]`
  - `./up-streamer/src/data_plane/ingress_registry.rs:292:                #[allow(clippy::mutable_key_type)]`
- concise conclusion: `dead_code` and clippy-targeted allows are present and need feasibility review.

### 8) Dead-code marker inventory

- exact command: `rg -n "todo!\\(|unimplemented!\\(" . --glob "*.rs"`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./utils/integration-test-utils/src/up_client_failing_register.rs:43:        unimplemented!()`
  - `./utils/integration-test-utils/src/up_client_foo.rs:103:                                    unimplemented!("Still need to handle Publish messages");`
  - `./utils/usubscription-static-file/src/lib.rs:46:        todo!()`
  - `./up-streamer/src/lib.rs:45://! #             unimplemented!("not needed for this doctest")`
- concise conclusion: Runtime and utility crates still contain concrete TODO/unimplemented markers that need triage.

### 9) Strict clippy baseline

- exact command: `cargo clippy --workspace --all-targets --all-features -- -W warnings -D warnings`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `Checking up-streamer v0.1.0 (/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/up-streamer)`
  - `Checking up-linux-streamer-plugin v0.1.0 (/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/up-linux-streamer-plugin)`
  - `Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 11.72s`
- concise conclusion: Current baseline is strict-clippy clean across workspace/all features.
