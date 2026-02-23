# Phase 4 - Validation Summary

Status: completed (with constrained unbundled skip)

## CI parity matrix

1) Base setup

- command: `source build/envsetup.sh highest`
- working directory: repo root
- exit status: `0` (pass)
- key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- conclusion: environment bootstrap succeeded

2) Base build/lint/fmt

- command: `cargo build`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: `Finished dev profile ...`
- conclusion: base build succeeded

- command: `cargo clippy --all-targets -- -W warnings -D warnings`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: `Checking configurable-streamer`, `Checking up-streamer`, `Finished dev profile ...`
- conclusion: base clippy warnings gate succeeded

- command: `cargo fmt -- --check`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: no output (clean formatting state)
- conclusion: formatting check succeeded

3) Bundled transport feature matrix

- command: `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: `Compiling up-linux-streamer-plugin ...`, `Finished dev profile ...`
- conclusion: bundled transport build succeeded

- command: `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: `Checking example-streamer-uses`, `Checking up-linux-streamer`, `Finished dev profile ...`
- conclusion: bundled transport clippy succeeded

4) Unbundled transport checks (constrained skip path)

- command: `if [ -n "$VSOMEIP_INSTALL_PATH" ] && [ -d "$VSOMEIP_INSTALL_PATH" ]; then printf 'VSOMEIP_INSTALL_PATH=%s\nSTATUS=valid\n' "$VSOMEIP_INSTALL_PATH"; else printf 'VSOMEIP_INSTALL_PATH=%s\nSTATUS=invalid\n' "$VSOMEIP_INSTALL_PATH"; fi`
- working directory: repo root
- exit status: `0` (command succeeded, prerequisite check reported unavailable)
- key output lines:
  - `VSOMEIP_INSTALL_PATH=`
  - `STATUS=invalid`
- conclusion: external unbundled prerequisite unavailable in this environment

- command: `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
- working directory: repo root
- exit status: not executed (constrained skip)
- key output lines: prerequisite unavailable (`VSOMEIP_INSTALL_PATH` invalid)
- conclusion: skipped per plan policy

- command: `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
- working directory: repo root
- exit status: not executed (constrained skip)
- key output lines: prerequisite unavailable (`VSOMEIP_INSTALL_PATH` invalid)
- conclusion: skipped per plan policy

- remediation path: provide a valid external vsomeip install tree and export `VSOMEIP_INSTALL_PATH`, then rerun both unbundled commands above.

5) Workspace checks

- command: `cargo check --workspace --all-targets`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: `Checking up-streamer`, `Finished dev profile ...`
- conclusion: workspace check succeeded

- command: `cargo test --workspace`
- working directory: repo root
- exit status: `0` (pass)
- key output lines:
  - `test result: ok. 18 passed; 0 failed` (`up-streamer` unit tests)
  - `test result: ok. 8 passed; 0 failed` (`up-streamer` doc-tests)
- conclusion: workspace tests succeeded

## Transport smoke skills (all 8)

Evidence was recovered from existing per-skill artifacts (post-crash resume path), then re-validated from artifact logs/validation outputs without re-running full triads.

1) Process hygiene + artifact presence

- command: `pgrep -fa "zenoh_someip|configurable-streamer|zenoh_service|someip_client|someip_service|mqtt_client|mqtt_service|zenoh_client|zenoh_subscriber|someip_subscriber|mqtt_subscriber|zenoh_publisher|someip_publisher|mqtt_publisher" || true`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: only the `pgrep` wrapper process line appears
- conclusion: no stale transport processes detected pre/post verification

- command: `ls -d "$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills"/smoke-*`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: all 8 `smoke-*` directories listed
- conclusion: per-skill evidence directories exist

- command: `test -f "$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md" && printf 'skills-execution-summary.md present\n'`
- working directory: repo root
- exit status: `0` (pass)
- key output lines: `skills-execution-summary.md present`
- conclusion: summary artifact exists

- command: `rg -n "Passed skills:\s*8/8|Failed skills after fixes:\s*0/8" "$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md"`
- working directory: repo root
- exit status: `0` (pass)
- key output lines:
  - `Passed skills: 8/8`
  - `Failed skills after fixes: 0/8`
- conclusion: all 8 skills are green

2) Per-skill command/exit/key-line evidence

- detailed per-skill entries (exact command, working directory, exit status, key output lines, conclusion) are captured in:
  - `$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/skills-execution-summary.md`
  - section: `Recovered evidence verification (post-crash resume)`

## Mode-specific acceptance checks

1) Static mode default remains active in required binaries

- command: `rg -n 'mode:\s*"static_file"' "configurable-streamer/CONFIG.json5" "example-streamer-implementations/DEFAULT_CONFIG.json5"`
- working directory: repo root
- exit status: `0` (pass)
- key output lines:
  - `configurable-streamer/CONFIG.json5:20:      mode: "static_file",`
  - `example-streamer-implementations/DEFAULT_CONFIG.json5:24:      mode: "static_file",`
- conclusion: static mode remains default in required streamer binaries

2) Reserved `live_usubscription` fail-fast behavior

- command: `cargo run -- --config "$OPENCODE_CONFIG_DIR/reports/usubscription-decoupled-pubsub-migration/live_usubscription-configurable.CONFIG.json5"`
- working directory: `configurable-streamer`
- exit status: `1` (expected fail-fast)
- key output lines:
  - `Error: UStatus { code: UNIMPLEMENTED, message: Some("live_usubscription mode is reserved in this phase; live runtime integration is deferred ...") }`
- conclusion: required fail-fast semantics preserved

- command: `cargo run -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "$OPENCODE_CONFIG_DIR/reports/usubscription-decoupled-pubsub-migration/live_usubscription-zenoh_someip.DEFAULT_CONFIG.json5"`
- working directory: repo root
- exit status: `1` (expected fail-fast)
- key output lines:
  - `Error: UStatus { code: UNIMPLEMENTED, message: Some("live_usubscription mode is reserved in this phase; live runtime integration is deferred ...") }`
- conclusion: required fail-fast semantics preserved

## Gate 4 conclusion

- CI parity matrix: pass for base + bundled; unbundled commands constrained-skipped per explicit plan policy due missing external prerequisite, with remediation documented.
- Smoke validation: all 8 skills verified green from recovered artifacts, with per-skill command-level evidence recorded.
- Mode checks: static mode default confirmed; reserved live mode fail-fast confirmed in both required binaries.
- Follow-up readiness: deferred live integration rationale/prerequisites/entry criteria captured in `05-live-integration-deferred.md`.
