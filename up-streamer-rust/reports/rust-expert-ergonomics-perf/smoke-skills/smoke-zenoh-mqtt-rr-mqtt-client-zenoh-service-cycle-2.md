# Smoke Report (Cycle 2): smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service

Date: 2026-02-11
Scenario: MQTT client -> Zenoh service via configurable-streamer
Cycle: 2
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service-artifacts/`

## Evidence

### 1) Setup artifacts and broker

- exact command: `source build/envsetup.sh highest && export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service-artifacts" && mkdir -p "$REPORT_DIR" && rm -f "$REPORT_DIR"/*.log "$REPORT_DIR"/*.pid "$REPORT_DIR"/*.exit "$REPORT_DIR"/*.txt && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- concise conclusion: Broker and artifacts prepared.

### 2) Start streamer and service

- exact command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"` and `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/service.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/service.pid"`
- working directory: `configurable-streamer` for streamer command; repo root for service command
- exit status / pass-fail: `0` / PASS
- key output lines:
  - PID files created: `streamer.pid`, `service.pid`
- concise conclusion: Streamer and Zenoh service are running.

### 3) Run bounded client

- exact command: `source build/envsetup.sh highest && export RUST_LOG="info,up_transport_mqtt5=debug,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `client.exit`: `124`
- concise conclusion: Client ran bounded loop and produced request traffic.

### 4) Request/response functional checks

- exact command: `rg -n -m 2 -o "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/client.log" && rg -n -m 2 -o "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `client.log:11: ServiceResponseListener: Received a message`
  - `client.log:11: UMESSAGE_TYPE_RESPONSE`
  - `service.log:20: ServiceResponseListener: Received a message`
  - `service.log:21: Sending Response message`
- concise conclusion: End-to-end MQTT->Zenoh request/response flow is stable.

### 5) Structured logging assertions

- exact command: `rg -n -m 1 "egress_send_attempt" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_send_ok" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_worker_create|egress_worker_reuse" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: event="egress_send_attempt" ... worker_id="019c4ab0-dd99-7483-97db-f3d0666e7762"`
  - `streamer.log:49: event="egress_send_ok" ... worker_id="019c4ab0-dd99-7483-97db-f3d0666e7762"`
  - `streamer.log:11: event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, ... out.name: endpoint_mqtt_1, ...]"`
- concise conclusion: Required structured egress logging assertions are met.

### 6) Failure-signature and lag/closed checks

- exact command: `rg -ni -m 3 "error|failed|disconnect" "$REPORT_DIR/client.log" "$REPORT_DIR/streamer.log" ; status=$?; printf 'failure_signature_status=%s\n' "$status" && rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log" ; lag_status=$?; printf 'lag_closed_status=%s\n' "$lag_status"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `failure_signature_status=1`
  - `lag_closed_status=1`
- concise conclusion: No transport failure signature matched; lag/closed not observed in bounded run.

### 7) Teardown

- exact command: `kill -INT "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && sleep 1 && kill -TERM "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && docker compose -f utils/mosquitto/docker-compose.yaml down || true && pkill -TERM -f "configurable-streamer|zenoh_service|mqtt_client" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
- concise conclusion: Scenario processes and broker were cleaned up.

## Final Conclusion

Scenario passed in Cycle 2 with stable MQTT->Zenoh request/response forwarding and structured logging evidence.
