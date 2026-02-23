# Smoke Report: smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber

- Result: PASS
- Artifacts: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber-artifacts`

## Evidence

### Entry 1
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && export SCENARIO="smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && mkdir -p "$ARTIFACT_DIR" && docker compose -f utils/mosquitto/docker-compose.yaml up -d && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport && cargo build -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Started`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)`
- Conclusion: Broker and required binaries were prepared successfully.

### Entry 2
- Exact command:

```bash
set -euo pipefail && source ../build/envsetup.sh highest && export SCENARIO="smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && { RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$ARTIFACT_DIR/streamer.log" 2>&1 & STREAMER_PID=$!; printf '%s\n' "$STREAMER_PID" > "$ARTIFACT_DIR/streamer.pid"; } && sleep 3
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/configurable-streamer`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: Streamer launched for the scenario with debug logging.

### Entry 3
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && rg -n -m 3 "Sending Publish message" "$ARTIFACT_DIR/publisher.log" && rg -n -m 3 "PublishReceiver: Received a message" "$ARTIFACT_DIR/subscriber.log" && rg -n -m 3 "Sending on out_transport succeeded" "$ARTIFACT_DIR/streamer.log"
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `19:Sending Publish message:`
  - `4: ... PublishReceiver: Received a message: UMessage { ... }`
  - `28: ... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: Publisher produced traffic, subscriber consumed it, and streamer forwarded it.

### Entry 4
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && if test -f "$ARTIFACT_DIR/subscriber.pid"; then kill -INT "$(< "$ARTIFACT_DIR/subscriber.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -INT "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && sleep 1 && if test -f "$ARTIFACT_DIR/subscriber.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/subscriber.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && docker compose -f utils/mosquitto/docker-compose.yaml down && pgrep -fa "configurable-streamer|mqtt_subscriber|zenoh_publisher" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Scenario processes and broker were cleanly torn down.
