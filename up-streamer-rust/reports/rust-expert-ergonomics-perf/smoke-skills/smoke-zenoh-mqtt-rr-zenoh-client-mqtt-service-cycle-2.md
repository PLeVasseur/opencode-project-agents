# Smoke Report (Cycle 2): smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service

Date: 2026-02-11
Scenario: Zenoh client -> MQTT service via configurable-streamer
Cycle: 2
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts/`

## Evidence

### 1) Setup artifacts and broker

- exact command: `source build/envsetup.sh highest && export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts" && mkdir -p "$REPORT_DIR" && rm -f "$REPORT_DIR"/*.log "$REPORT_DIR"/*.pid "$REPORT_DIR"/*.exit "$REPORT_DIR"/*.txt && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- concise conclusion: Broker and artifact location prepared.

### 2) Start streamer and service

- exact command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"` and `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin mqtt_service --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/service.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/service.pid"`
- working directory: `configurable-streamer` for streamer command; repo root for service command
- exit status / pass-fail: `0` / PASS
- key output lines:
  - PID files created: `streamer.pid`, `service.pid`
- concise conclusion: Streamer and MQTT service launched correctly.

### 3) Run bounded client

- exact command: `source build/envsetup.sh highest && export RUST_LOG="info,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin zenoh_client --features zenoh-transport > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `client.exit`: `124`
- concise conclusion: Client executed bounded request loop as expected.

### 4) Request/response functional checks

- exact command: `rg -n -m 2 -o "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/client.log" && rg -n -m 2 -o "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `client.log:22: ServiceResponseListener: Received a message`
  - `client.log:22: UMESSAGE_TYPE_RESPONSE`
  - `service.log:5: ServiceResponseListener: Received a message`
  - `service.log:6: Sending Response message`
- concise conclusion: Requests traversed streamer and responses returned successfully.

### 5) Structured logging assertions

- exact command: `rg -n -m 1 "egress_send_attempt" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_send_ok" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_worker_create|egress_worker_reuse" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: event="egress_send_attempt" ... worker_id="019c4aaf-1e20-758f-a413-362a084d1bb2"`
  - `streamer.log:50: event="egress_send_ok" ... worker_id="019c4aaf-1e20-758f-a413-362a084d1bb2"`
  - `streamer.log:11: event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, ... out.name: endpoint_mqtt_1, ...]"`
- concise conclusion: Structured egress assertions are satisfied.

### 6) Failure-signature and lag/closed checks

- exact command: `rg -ni -m 3 "error|failed|disconnect" "$REPORT_DIR/client.log" "$REPORT_DIR/streamer.log" ; status=$?; printf 'failure_signature_status=%s\n' "$status" && rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log" ; lag_status=$?; printf 'lag_closed_status=%s\n' "$lag_status"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `failure_signature_status=1`
  - `lag_closed_status=1`
- concise conclusion: No transport failure signatures; lag/closed not observed in bounded run.

### 7) Teardown

- exact command: `kill -INT "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && sleep 1 && kill -TERM "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && docker compose -f utils/mosquitto/docker-compose.yaml down || true && pkill -TERM -f "configurable-streamer|mqtt_service|zenoh_client" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
- concise conclusion: Scenario resources were cleaned up.

## Final Conclusion

Scenario passed in Cycle 2 with stable Zenoh->MQTT request/response and required structured logging checks.
