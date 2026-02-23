# Smoke Report (Cycle 2): smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber

Date: 2026-02-11
Scenario: Zenoh publisher -> MQTT subscriber via configurable-streamer
Cycle: 2
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber-artifacts/`

## Evidence

### 1) Setup artifacts and broker

- exact command: `source build/envsetup.sh highest && export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber-artifacts" && mkdir -p "$REPORT_DIR" && rm -f "$REPORT_DIR"/*.log "$REPORT_DIR"/*.pid "$REPORT_DIR"/*.exit "$REPORT_DIR"/*.txt && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- concise conclusion: MQTT broker and clean artifact directory are ready.

### 2) Start streamer and subscriber

- exact command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"` and `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport -- --uauthority authority-a --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-b --source-uentity 0x3039 --source-uversion 0x1 --source-resource 0x8001 --broker-uri localhost:1883 > "$REPORT_DIR/subscriber.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/subscriber.pid"`
- working directory: `configurable-streamer` for streamer command; repo root for subscriber command
- exit status / pass-fail: `0` / PASS
- key output lines:
  - PID files created: `streamer.pid`, `subscriber.pid`
- concise conclusion: Streamer and subscriber were launched in background successfully.

### 3) Run bounded publisher

- exact command: `source build/envsetup.sh highest && export RUST_LOG="info,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `publisher.exit`: `124`
- concise conclusion: Publisher loop ran for bounded window as expected.

### 4) Traffic forwarding checks

- exact command: `rg -n -m 2 -o "Sending Publish message" "$REPORT_DIR/publisher.log" && rg -n -m 2 -o "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `publisher.log:19: Sending Publish message`
  - `publisher.log:21: Sending Publish message`
  - `subscriber.log:4: PublishReceiver: Received a message`
  - `subscriber.log:5: PublishReceiver: Received a message`
- concise conclusion: Publisher emitted messages and subscriber received forwarded publish traffic.

### 5) Structured logging assertions

- exact command: `rg -n -m 1 "egress_send_attempt" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_send_ok" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_worker_create|egress_worker_reuse" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: event="egress_send_attempt" ... worker_id="019c4ab9-3485-7230-aaa6-fd73a904197e"`
  - `streamer.log:50: event="egress_send_ok" ... worker_id="019c4ab9-3485-7230-aaa6-fd73a904197e"`
  - `streamer.log:11: event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, ... out.name: endpoint_mqtt_1, ...]"`
- concise conclusion: Required structured egress lifecycle/send logging is present.

### 6) Lag/closed bounded-run check

- exact command: `rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log" ; status=$?; printf 'lag_closed_status=%s\n' "$status"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `lag_closed_status=1`
- concise conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded run.

### 7) Teardown

- exact command: `kill -INT "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && sleep 1 && kill -TERM "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && docker compose -f utils/mosquitto/docker-compose.yaml down || true && pkill -TERM -f "configurable-streamer|mqtt_subscriber|zenoh_publisher" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
- concise conclusion: Scenario processes and broker were cleaned up.

## Final Conclusion

Scenario passed in Cycle 2 with successful publish forwarding and required structured logging assertions.
