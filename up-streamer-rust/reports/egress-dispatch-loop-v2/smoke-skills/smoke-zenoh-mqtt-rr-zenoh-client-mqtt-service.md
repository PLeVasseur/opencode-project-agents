# Smoke Report: smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service

- Result: PASS
- Artifacts: `$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts`

## Evidence

### Entry 1
- Exact command:

```bash
set -euo pipefail && source build/envsetup.sh highest && export SCENARIO="smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && mkdir -p "$ARTIFACT_DIR" && docker compose -f utils/mosquitto/docker-compose.yaml up -d && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin zenoh_client --features zenoh-transport && cargo build -p example-streamer-uses --bin mqtt_service --features mqtt-transport
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Running`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)`
- Conclusion: Scenario binaries and broker were prepared.

### Entry 2
- Exact command:

```bash
set -euo pipefail && source ../build/envsetup.sh highest && export SCENARIO="smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && { RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$ARTIFACT_DIR/streamer.log" 2>&1 & STREAMER_PID=$!; printf '%s\n' "$STREAMER_PID" > "$ARTIFACT_DIR/streamer.pid"; } && sleep 3
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/configurable-streamer`
- Exit status: `0` (pass)
- Key output lines:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: Streamer process started with expected MQTT debug instrumentation.

### Entry 3
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && rg -n -m 3 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$ARTIFACT_DIR/client.log" && rg -n -m 3 "ServiceResponseListener: Received a message|Sending Response message" "$ARTIFACT_DIR/service.log" && rg -n -m 3 "Sending on out_transport succeeded" "$ARTIFACT_DIR/streamer.log" && if rg -ni "error|failed|disconnect" "$ARTIFACT_DIR/client.log" "$ARTIFACT_DIR/streamer.log"; then exit 1; fi
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - `21: ... zenoh_client::common ... ServiceResponseListener: Received a message ... UMESSAGE_TYPE_RESPONSE ...`
  - `4: ... mqtt_service::common ... ServiceResponseListener: Received a message ...`
  - `28: ... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
  - (no matches for `error|failed|disconnect` in client/streamer logs)
- Conclusion: Request/response forwarding was stable and free of transport failure signatures.

### Entry 4
- Exact command:

```bash
set -euo pipefail && export SCENARIO="smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service" && export ARTIFACT_DIR="$OPENCODE_CONFIG_DIR/reports/egress-dispatch-loop-v2/smoke-skills/${SCENARIO}-artifacts" && if test -f "$ARTIFACT_DIR/service.pid"; then kill -INT "$(< "$ARTIFACT_DIR/service.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -INT "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && sleep 1 && if test -f "$ARTIFACT_DIR/service.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/service.pid")" || true; fi && if test -f "$ARTIFACT_DIR/streamer.pid"; then kill -TERM "$(< "$ARTIFACT_DIR/streamer.pid")" || true; fi && pgrep -fa "configurable-streamer|mqtt_service|zenoh_client" || true
```

- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: `0` (pass)
- Key output lines:
  - (no remaining scenario processes)
- Conclusion: Scenario service and streamer were cleaned up successfully.
