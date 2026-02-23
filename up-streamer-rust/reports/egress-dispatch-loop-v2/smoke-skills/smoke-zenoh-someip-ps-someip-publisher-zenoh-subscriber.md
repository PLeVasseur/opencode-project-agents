# Smoke Report: smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber

- Result: PASS
- Artifacts: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber-artifacts`

## Evidence

### Entry 1
- Exact command:

```bash
set -euo pipefail && source ../build/envsetup.sh highest && export SCENARIO="smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && shopt -s nullglob && vsomeip_libs=("$PWD"/../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test ${#vsomeip_libs[@]} -gt 0 && export LD_LIBRARY_PATH="${vsomeip_libs[0]}:${LD_LIBRARY_PATH:-}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && { cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$ARTIFACT_DIR/streamer.log" 2>&1 & STREAMER_PID=$!; printf '%s\n' "$STREAMER_PID" > "$ARTIFACT_DIR/streamer.pid"; } && sleep 4
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: `zenoh_someip` streamer launched successfully.

### Entry 2
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && export SCENARIO="smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && shopt -s nullglob && vsomeip_libs=("$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test ${#vsomeip_libs[@]} -gt 0 && export LD_LIBRARY_PATH="${vsomeip_libs[0]}:${LD_LIBRARY_PATH:-}" && export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug" && set +e && timeout 45s cargo run -p example-streamer-uses --bin someip_publisher --features "vsomeip-transport,bundled-vsomeip" > "$ARTIFACT_DIR/publisher.log" 2>&1 && PUBLISHER_EXIT=0 || PUBLISHER_EXIT=$? && set -e && printf '%s\n' "$PUBLISHER_EXIT" > "$ARTIFACT_DIR/publisher.exit"
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
  - `client/publisher exit recorded as 124` (timeout window elapsed)
- Conclusion: SOME/IP publisher executed for the full smoke window.

### Entry 3
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && rg -n -m 3 "Sending Publish message" "$ARTIFACT_DIR/publisher.log" && rg -n -m 3 "PublishReceiver: Received a message" "$ARTIFACT_DIR/subscriber.log" && rg -n -m 3 "Sending on out_transport succeeded" "$ARTIFACT_DIR/streamer.log"
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `40: ... someip_publisher ... Sending Publish message:`
  - `19: ... zenoh_subscriber::common ... PublishReceiver: Received a message ...`
  - `123: ... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: Pub/sub forwarding from SOME/IP publisher to Zenoh subscriber is confirmed.

### Entry 4
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && if test -f "$ARTIFACT_DIR/subscriber.pid"; then kill -INT "$(< "$ARTIFACT_DIR/subscriber.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -INT "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && sleep 1 && if test -f "$ARTIFACT_DIR/subscriber.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/subscriber.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && pgrep -fa "zenoh_someip|zenoh_subscriber|someip_publisher" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `/bin/bash: line 1: kill: (...) - No such process` (process already exited)
- Conclusion: Scenario resources were cleaned up successfully.
