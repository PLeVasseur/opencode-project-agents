# Smoke Report (Cycle 2): smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber

Date: 2026-02-11
Scenario: SOME/IP publisher -> Zenoh subscriber via zenoh_someip streamer
Cycle: 2
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber-artifacts/`

## Evidence

### 1) Setup artifacts and vsomeip path

- exact command: `source build/envsetup.sh highest && export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber-artifacts" && mkdir -p "$REPORT_DIR" && rm -f "$REPORT_DIR"/*.log "$REPORT_DIR"/*.pid "$REPORT_DIR"/*.exit "$REPORT_DIR"/*.txt && export VSOMEIP_LIB="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1)" && test -d "$VSOMEIP_LIB" && printf '%s\n' "$VSOMEIP_LIB" > "$REPORT_DIR/vsomeip_lib.path"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `vsomeip_lib.path` created with valid library directory
- concise conclusion: SOME/IP runtime prerequisites are configured.

### 2) Start streamer and subscriber

- exact command: `source ../build/envsetup.sh highest && export LD_LIBRARY_PATH="$(cat "$REPORT_DIR/vsomeip_lib.path"):${LD_LIBRARY_PATH}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"` and `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001 > "$REPORT_DIR/subscriber.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/subscriber.pid"`
- working directory: `example-streamer-implementations` for streamer command; repo root for subscriber command
- exit status / pass-fail: `0` / PASS
- key output lines:
  - PID files created: `streamer.pid`, `subscriber.pid`
- concise conclusion: Streamer and Zenoh subscriber launched successfully.

### 3) Run bounded publisher

- exact command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="$(cat "$REPORT_DIR/vsomeip_lib.path"):${LD_LIBRARY_PATH}" && export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin someip_publisher --features "vsomeip-transport,bundled-vsomeip" > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `publisher.exit`: `124`
- concise conclusion: SOME/IP publisher ran in bounded window and generated traffic.

### 4) Traffic forwarding checks

- exact command: `rg -n -m 2 -o "Sending Publish message" "$REPORT_DIR/publisher.log" && rg -n -m 2 -o "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `publisher.log:41: Sending Publish message`
  - `publisher.log:59: Sending Publish message`
  - `subscriber.log:16: PublishReceiver: Received a message`
  - `subscriber.log:17: PublishReceiver: Received a message`
- concise conclusion: SOME/IP publish traffic reached Zenoh subscriber through streamer.

### 5) Structured logging assertions

- exact command: `rg -n -m 1 "egress_send_attempt" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_send_ok" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_worker_create|egress_worker_reuse" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:134: event="egress_send_attempt" ... worker_id="019c4ab4-54f0-77a3-89e0-56e72aa8e14e"`
  - `streamer.log:135: event="egress_send_ok" ... worker_id="019c4ab4-54f0-77a3-89e0-56e72aa8e14e"`
  - `streamer.log:48: event="egress_worker_create" ... route_label="[in.name: host_endpoint, ... out.name: someip_endpoint, ...]"`
- concise conclusion: Structured egress event assertions are satisfied.

### 6) Lag/closed bounded-run check

- exact command: `rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log" ; status=$?; printf 'lag_closed_status=%s\n' "$status"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `lag_closed_status=1`
- concise conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded run.

### 7) Teardown

- exact command: `kill -INT "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && sleep 1 && kill -TERM "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && pkill -TERM -f "zenoh_someip|zenoh_subscriber|someip_publisher" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - no matching scenario processes remained after teardown
- concise conclusion: Scenario cleanup completed.

## Final Conclusion

Scenario passed in Cycle 2 with successful SOME/IP->Zenoh pub/sub forwarding and required structured logs.
