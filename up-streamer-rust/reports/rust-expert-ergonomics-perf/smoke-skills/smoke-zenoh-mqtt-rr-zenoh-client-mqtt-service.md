# Smoke Report: smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service

Date: 2026-02-11
Scenario: Zenoh client -> MQTT service request/response via configurable-streamer
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts/`

## Evidence

### 1) Pre-scenario stale-process cleanup

- exact command: `pkill -INT -f "configurable-streamer|mqtt_service|zenoh_client|mqtt_client|zenoh_service|mqtt_publisher|mqtt_subscriber|zenoh_publisher|zenoh_subscriber|zenoh_someip|someip_" || true; sleep 1; pkill -TERM -f "configurable-streamer|mqtt_service|zenoh_client|mqtt_client|zenoh_service|mqtt_publisher|mqtt_subscriber|zenoh_publisher|zenoh_subscriber|zenoh_someip|someip_" || true; docker compose -f utils/mosquitto/docker-compose.yaml down || true; pgrep -fa "[c]onfigurable-streamer|[m]qtt_service|[z]enoh_client|[m]qtt_client|[z]enoh_service|[m]qtt_publisher|[m]qtt_subscriber|[z]enoh_publisher|[z]enoh_subscriber|[z]enoh_someip|[s]omeip_" || true`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status / pass-fail: `0` / PASS
- key output lines:
  - no remaining matching processes were listed
- concise conclusion: Scenario started from a clean process state.

### 2) Build binaries

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts" && mkdir -p "$REPORT_DIR" && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin zenoh_client --features zenoh-transport && cargo build -p example-streamer-uses --bin mqtt_service --features mqtt-transport`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.82s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.51s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.58s`
- concise conclusion: All scenario binaries built successfully.

### 3) Start broker

- exact command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Running`
- concise conclusion: MQTT broker is available for request/response routing.

### 4) Start streamer

- exact command: `set -e; source ../build/envsetup.sh highest; REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts"; RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & pid=$!; printf '%s\n' "$pid" > "$REPORT_DIR/streamer.pid"; printf 'streamer_pid=%s\n' "$pid"`
- working directory: `configurable-streamer`
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer_pid=1566993`
- concise conclusion: Streamer started in background with captured logs and pid.

### 5) Start service

- exact command: `set -e; source build/envsetup.sh highest; REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts"; RUST_LOG=info cargo run -p example-streamer-uses --bin mqtt_service --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/service.log" 2>&1 & pid=$!; printf '%s\n' "$pid" > "$REPORT_DIR/service.pid"; printf 'service_pid=%s\n' "$pid"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `service_pid=1567087`
- concise conclusion: MQTT service started and is ready to handle incoming requests.

### 6) Run bounded client

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts" && export RUST_LOG="info,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin zenoh_client --features zenoh-transport > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `client.exit`: `124`
  - bounded timeout is expected for continuous request loop
- concise conclusion: Client executed for the bounded window and exercised sustained request flow.

### 7) Client received responses

- exact command: `rg -n -m 3 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/client.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `client.log:21: ... ServiceResponseListener: Received a message ... type_: UMESSAGE_TYPE_RESPONSE ...`
  - `client.log:24: ... ServiceResponseListener: Received a message ... type_: UMESSAGE_TYPE_RESPONSE ...`
  - `client.log:27: ... ServiceResponseListener: Received a message ... type_: UMESSAGE_TYPE_RESPONSE ...`
- concise conclusion: Zenoh client received valid response traffic through the bridge.

### 8) Service handled requests

- exact command: `rg -n -m 3 "ServiceRequestListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `service.log:5: ... Sending Response message:`
  - `service.log:8: ... Sending Response message:`
  - `service.log:11: ... Sending Response message:`
- concise conclusion: MQTT service processed requests and emitted responses.

### 9) Failure-signature scan

- exact command: `rg -ni -m 5 "error|failed|disconnect" "$REPORT_DIR/client.log" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `1` / PASS
- key output lines:
  - no matches
- concise conclusion: No transport-level failure signatures were observed in bounded run logs.

### 10) Structured logging assertion: `egress_send_attempt` with `worker_id`

- exact command: `rg -n -m 3 "egress_send_attempt.*worker_id" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: ... event="egress_send_attempt" ... worker_id="019c49a6-82ff-7804-a4ed-a498a9bad019" ...`
  - `streamer.log:52: ... event="egress_send_attempt" ... worker_id="019c49a6-831a-7c18-8a34-9f9403702eb4" ...`
- concise conclusion: Required `egress_send_attempt` structured event includes `worker_id`.

### 11) Structured logging assertion: `egress_send_ok` with `worker_id`

- exact command: `rg -n -m 3 "egress_send_ok.*worker_id" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:50: ... event="egress_send_ok" ... worker_id="019c49a6-82ff-7804-a4ed-a498a9bad019" ...`
  - `streamer.log:53: ... event="egress_send_ok" ... worker_id="019c49a6-831a-7c18-8a34-9f9403702eb4" ...`
- concise conclusion: Required `egress_send_ok` structured event includes `worker_id`.

### 12) Structured logging assertion: worker create/reuse with `route_label`

- exact command: `rg -n -m 3 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:11: ... event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, ... out.name: endpoint_mqtt_1, ...]" ...`
  - `streamer.log:29: ... event="egress_worker_reuse" ... route_label="[in.name: endpoint_zenoh_2, ... out.name: endpoint_zenoh_1, ...]" ...`
- concise conclusion: Required worker lifecycle structured event includes `route_label`.

### 13) Lag/closed bounded-run check

- exact command: `rg -n -m 3 "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `1` / PASS
- key output lines:
  - no matches
- concise conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded run.

### 14) Teardown

- exact command: `REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service-artifacts" && read -r service_pid < "$REPORT_DIR/service.pid" && read -r streamer_pid < "$REPORT_DIR/streamer.pid" && kill -INT "$service_pid" "$streamer_pid" || true; sleep 1; kill -TERM "$service_pid" "$streamer_pid" || true; docker compose -f utils/mosquitto/docker-compose.yaml down || true; pgrep -fa "[c]onfigurable-streamer|[m]qtt_service|[z]enoh_client" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
  - no matching processes remained
- concise conclusion: Scenario services and broker were fully cleaned up.

## Final Conclusion

Scenario passed: bounded Zenoh client request traffic was forwarded to MQTT service and responses returned to the client through configurable-streamer, with required structured egress lifecycle/send logging assertions satisfied.
