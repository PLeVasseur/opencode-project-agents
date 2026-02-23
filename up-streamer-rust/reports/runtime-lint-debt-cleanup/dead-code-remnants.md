# Phase 3 Dead Code Removal and Remnants

Date: 2026-02-10

## Removal pass completed

- Removed unused `RunningPluginInner` fields (`name`, `runtime`) from `up-linux-streamer-plugin/src/lib.rs`.
- Replaced production `todo!`/`unimplemented!` implementations in `utils/usubscription-static-file/src/lib.rs` with concrete read-only behavior and explicit `UNIMPLEMENTED` status errors for unsupported mutating APIs.
- Restored O(1)-capable routing/cache lookup interfaces without introducing new dead-code markers.

## Verification evidence

### 1) Dead/unused strict clippy

- exact command: `cargo clippy --workspace --all-targets --all-features -- -W dead_code -W unused -D warnings`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `Checking usubscription-static-file v0.1.0 (...)`
  - `Checking up-streamer v0.1.0 (...)`
  - `Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 4.94s`
- concise conclusion: Workspace remains clean under strict dead/unused lint settings.

### 2) Dead-code allow scan

- exact command: `rg -n "allow\\(dead_code\\)" . --glob "*.rs" --glob "!target/**"`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./example-streamer-uses/src/bin/common/cli.rs:79:#[allow(dead_code)]`
  - `./example-streamer-uses/src/bin/common/mod.rs:13:#[allow(dead_code)]`
  - `./up-streamer/tests/support/mod.rs:22:#[allow(dead_code)]`
- concise conclusion: Remaining `dead_code` allowances are confined to test/example helper modules.

### 3) `todo!/unimplemented!` marker scan

- exact command: `rg -n "todo!\\(|unimplemented!\\(" . --glob "*.rs"`
- working directory: repo root
- exit status/pass-fail: `0` (pass)
- key output lines:
  - `./utils/integration-test-utils/src/up_client_foo.rs:103: unimplemented!("Still need to handle Publish messages")`
  - `./utils/integration-test-utils/src/up_client_failing_register.rs:43: unimplemented!()`
  - `./up-streamer/src/lib.rs:45://! #             unimplemented!("not needed for this doctest")`
- concise conclusion: Remaining markers are in test utility shims and doctest snippets only; none remain in production runtime code.

## Required remnant inventory (line-level)

| file:line | why removal is currently unsafe/unwanted | alternatives attempted | follow-up removal trigger |
|---|---|---|---|
| `utils/integration-test-utils/src/up_client_foo.rs:103` | Publish branch is intentionally unimplemented in this test mock transport; current tests do not require publish dispatch in this helper. | Considered implementing publish dispatch via existing listener flow; deferred to avoid introducing unvalidated test harness semantics. | Remove when integration tests require publish behavior from this mock and expected semantics are codified. |
| `utils/integration-test-utils/src/up_client_foo.rs:236` | `receive()` is intentionally unsupported in this test mock and unused by current listener-based tests. | Considered returning deterministic `UStatus`; deferred to avoid changing established failure-mode behavior in existing tests. | Remove when mock contract is expanded to support pull-based receive behavior. |
| `utils/integration-test-utils/src/up_client_failing_register.rs:43` | Mock is purpose-built to fail `register_listener`; `receive()` is intentionally out-of-scope for this test utility. | Considered replacing with explicit error return; deferred until helper behavior contract is revised. | Remove when failing-register helper is expanded beyond register-path testing. |
| `up-streamer/src/endpoint.rs:38` | `todo!()` is inside a doc-only snippet, not production runtime logic. | Considered replacing with a fully concrete doctest implementation; deferred to dedicated docs refresh pass. | Remove during doctest/docs modernization pass. |
| `up-streamer/src/endpoint.rs:46` | `todo!()` is inside a doc-only snippet, not production runtime logic. | Considered replacing with concrete mock transport in docs; deferred to docs-focused cleanup. | Remove during doctest/docs modernization pass. |
| `up-streamer/src/lib.rs:45` | `unimplemented!()` is in a crate-level doctest snippet used for illustrative setup. | Considered replacing with full runnable fixture; deferred to keep docs concise in this scope. | Remove when doctest examples are rewritten to fully executable fixtures. |
| `up-streamer/src/lib.rs:115` | `unimplemented!()` is in a crate-level doctest snippet used for illustrative setup. | Considered replacing with full runnable fixture; deferred to docs-focused follow-up. | Remove during docs executable-example sweep. |
