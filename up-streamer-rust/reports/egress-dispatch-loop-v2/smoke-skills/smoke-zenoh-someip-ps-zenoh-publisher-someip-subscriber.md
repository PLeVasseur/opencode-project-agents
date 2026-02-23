# Smoke Report: smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber

- Result: PASS
- Artifacts: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts`

## Evidence

### Entry 1
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport && cargo build -p example-streamer-uses --bin someip_subscriber --features "vsomeip-transport,bundled-vsomeip"
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Compiling up-linux-streamer v0.1.0`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)`
- Conclusion: Required SOME/IP streamer, publisher, and subscriber binaries were built.

### Entry 2
- Exact command:

```bash
set -euo pipefail && source ../build/envsetup.sh highest && export SCENARIO="smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && shopt -s nullglob && vsomeip_libs=("$PWD"/../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test ${#vsomeip_libs[@]} -gt 0 && export LD_LIBRARY_PATH="${vsomeip_libs[0]}:${LD_LIBRARY_PATH:-}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && { cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$ARTIFACT_DIR/streamer.log" 2>&1 & STREAMER_PID=$!; printf '%s\n' "$STREAMER_PID" > "$ARTIFACT_DIR/streamer.pid"; } && sleep 4
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: `zenoh_someip` streamer started with bundled SOME/IP runtime libraries.

### Entry 3
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && rg -n -m 3 "Sending Publish message" "$ARTIFACT_DIR/publisher.log" && rg -n -m 3 "PublishReceiver: Received a message" "$ARTIFACT_DIR/subscriber.log" && rg -n -m 3 "Sending on out_transport succeeded" "$ARTIFACT_DIR/streamer.log"
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `19:Sending Publish message:`
  - `25: ... someip_subscriber::common ... PublishReceiver: Received a message ...`
  - `130: ... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: Pub/sub forwarding from Zenoh publisher to SOME/IP subscriber succeeded.

### Entry 4
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && if test -f "$ARTIFACT_DIR/subscriber.pid"; then kill -INT "$(< "$ARTIFACT_DIR/subscriber.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -INT "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && sleep 1 && if test -f "$ARTIFACT_DIR/subscriber.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/subscriber.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && pgrep -fa "zenoh_someip|zenoh_publisher|someip_subscriber" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `/bin/bash: line 1: kill: (...) - No such process` (already exited)
- Conclusion: Scenario processes were no longer active at teardown; cleanup complete.
