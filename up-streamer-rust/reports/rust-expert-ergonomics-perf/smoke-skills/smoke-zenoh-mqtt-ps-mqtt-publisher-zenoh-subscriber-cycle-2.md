# Smoke Report (Cycle 2): smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber

Date: 2026-02-11
Scenario: MQTT publisher -> Zenoh subscriber via configurable-streamer
Cycle: 2
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-artifacts/`

## Evidence

### 1) Setup artifacts and broker

- exact command: `source build/envsetup.sh highest && export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-artifacts" && mkdir -p "$REPORT_DIR" && rm -f "$REPORT_DIR"/*.log "$REPORT_DIR"/*.pid "$REPORT_DIR"/*.exit "$REPORT_DIR"/*.txt && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Running`
- concise conclusion: MQTT broker and scenario artifact directory are ready.

### 2) Start streamer and subscriber

- exact command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"` and `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001 > "$REPORT_DIR/subscriber.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/subscriber.pid"`
- working directory: `configurable-streamer` for streamer command; repo root for subscriber command
- exit status / pass-fail: `0` / PASS
- key output lines:
  - PID files created: `streamer.pid`, `subscriber.pid`
- concise conclusion: Streamer and Zenoh subscriber launched successfully.

### 3) Run bounded publisher

- exact command: `source build/envsetup.sh highest && export RUST_LOG="info,up_transport_mqtt5=debug,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `publisher.exit`: `124`
- concise conclusion: MQTT publisher loop ran for bounded test duration.

### 4) Traffic forwarding checks

- exact command: `rg -n -m 2 -o "Sending Publish message" "$REPORT_DIR/publisher.log" && rg -n -m 2 -o "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `publisher.log:7: Sending Publish message`
  - `publisher.log:10: Sending Publish message`
  - `subscriber.log:20: PublishReceiver: Received a message`
  - `subscriber.log:21: PublishReceiver: Received a message`
- concise conclusion: MQTT publish traffic was forwarded and received by Zenoh subscriber.

### 5) Structured logging assertions

- exact command: `rg -n -m 1 "egress_send_attempt" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_send_ok" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_worker_create|egress_worker_reuse" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: event="egress_send_attempt" ... worker_id="019c4aad-4ace-731d-8b02-15543b96fcec"`
  - `streamer.log:49: event="egress_send_ok" ... worker_id="019c4aad-4ace-731d-8b02-15543b96fcec"`
  - `streamer.log:11: event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, ... out.name: endpoint_mqtt_1, ...]"`
- concise conclusion: Required egress structured logging fields are present.

### 6) Lag/closed bounded-run check

- exact command: `rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log" ; status=$?; printf 'lag_closed_status=%s\n' "$status"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `lag_closed_status=1`
- concise conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded run.

### 7) Teardown

- exact command: `kill -INT "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && sleep 1 && kill -TERM "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && docker compose -f utils/mosquitto/docker-compose.yaml down || true && pkill -TERM -f "configurable-streamer|zenoh_subscriber|mqtt_publisher" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
- concise conclusion: Scenario cleanup completed.

## Final Conclusion

Scenario passed in Cycle 2 with successful MQTT->Zenoh pub/sub forwarding and required structured logging assertions.
