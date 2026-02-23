# Smoke Report: smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber

Date: 2026-02-11
Scenario: MQTT publisher -> Zenoh subscriber via configurable-streamer
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-artifacts/`

## Evidence

### 1) Build binaries

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber-artifacts" && mkdir -p "$REPORT_DIR" && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport && cargo build -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.64s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.62s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.57s`
- concise conclusion: Required binaries built successfully.

### 2) Start broker

- exact command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- concise conclusion: MQTT broker is available.

### 3) Start streamer

- exact command: `(source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1) & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"`
- working directory: `configurable-streamer`
- exit status / pass-fail: `0` / PASS
- key output lines:
  - streamer started in background; PID captured in `streamer.pid`
- concise conclusion: Streamer process started with log capture.

### 4) Start subscriber

- exact command: `(source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001 > "$REPORT_DIR/subscriber.log" 2>&1) & printf '%s\n' "$!" > "$REPORT_DIR/subscriber.pid"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - subscriber started in background; PID captured in `subscriber.pid`
- concise conclusion: Zenoh subscriber process started with expected source filters.

### 5) Run publisher

- exact command: `source build/envsetup.sh highest && export RUST_LOG="info,up_transport_mqtt5=debug,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `publisher.exit`: `124`
  - bounded timeout is expected for continuous publisher loop
- concise conclusion: Publisher ran for bounded window and produced traffic.

### 6) Publisher emitted traffic check

- exact command: `rg -n "Sending Publish message" "$REPORT_DIR/publisher.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `publisher.log:5: ... Sending Publish message:`
  - `publisher.log:119: ... Sending Publish message:`
- concise conclusion: Publisher emitted repeated publish messages.

### 7) Subscriber received traffic check

- exact command: `rg -n "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `subscriber.log:19: ... PublishReceiver: Received a message ...`
  - `subscriber.log:57: ... PublishReceiver: Received a message ...`
- concise conclusion: Zenoh subscriber received forwarded publish messages.

### 8) Structured logging assertion: egress_send_attempt with worker_id

- exact command: `rg -n "event=\"?egress_send_attempt\"?.*worker_id=|worker_id=.*event=\"?egress_send_attempt\"?" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: ... event="egress_send_attempt" ... worker_id="019c4987-1553-73c6-9eab-e9c95ab217d8" ...`
- concise conclusion: Streamer logs include `egress_send_attempt` with `worker_id`.

### 9) Structured logging assertion: egress_send_ok with worker_id

- exact command: `rg -n "event=\"?egress_send_ok\"?.*worker_id=|worker_id=.*event=\"?egress_send_ok\"?" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:49: ... event="egress_send_ok" ... worker_id="019c4987-1553-73c6-9eab-e9c95ab217d8" ...`
- concise conclusion: Streamer logs include `egress_send_ok` with `worker_id`.

### 10) Structured logging assertion: worker create/reuse with route_label

- exact command: `rg -n "event=\"?egress_worker_create\"?.*route_label=|event=\"?egress_worker_reuse\"?.*route_label=" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:11: ... event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, ... out.name: endpoint_mqtt_1, ...]" ...`
  - `streamer.log:29: ... event="egress_worker_reuse" ... route_label="[in.name: endpoint_zenoh_2, ... out.name: endpoint_zenoh_1, ...]" ...`
- concise conclusion: Streamer logs include worker lifecycle event with `route_label`.

### 11) Lag/closed bounded-run check

- exact command: `rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `1` / PASS
- key output lines:
  - `No files found`
- concise conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded run.

### 12) Teardown

- exact command: `pkill -INT -f "configurable-streamer|zenoh_subscriber|mqtt_publisher" || true; sleep 1; pkill -TERM -f "configurable-streamer|zenoh_subscriber|mqtt_publisher" || true; docker compose -f utils/mosquitto/docker-compose.yaml down || true; pgrep -fa "[c]onfigurable-streamer|[z]enoh_subscriber|[m]qtt_publisher" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - no matching processes remained after teardown
- concise conclusion: Scenario processes and broker were cleaned up.

## Final Conclusion

Scenario passed: bounded MQTT publish traffic was forwarded by configurable-streamer to Zenoh subscriber, with required structured egress lifecycle/send logging assertions satisfied.
