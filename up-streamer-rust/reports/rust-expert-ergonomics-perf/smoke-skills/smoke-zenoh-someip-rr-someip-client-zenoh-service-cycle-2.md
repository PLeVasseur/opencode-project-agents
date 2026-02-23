# Smoke Report (Cycle 2): smoke-zenoh-someip-rr-someip-client-zenoh-service

Date: 2026-02-11
Scenario: SOME/IP client -> Zenoh service via zenoh_someip streamer
Cycle: 2
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts/`

## Evidence

### 1) Setup artifacts and vsomeip path

- exact command: `source build/envsetup.sh highest && export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts" && mkdir -p "$REPORT_DIR" && rm -f "$REPORT_DIR"/*.log "$REPORT_DIR"/*.pid "$REPORT_DIR"/*.exit "$REPORT_DIR"/*.txt && export VSOMEIP_LIB="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1)" && test -d "$VSOMEIP_LIB" && printf '%s\n' "$VSOMEIP_LIB" > "$REPORT_DIR/vsomeip_lib.path"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `vsomeip_lib.path` created with valid library directory
- concise conclusion: SOME/IP runtime prerequisites are in place.

### 2) Start streamer and service

- exact command: `source ../build/envsetup.sh highest && export LD_LIBRARY_PATH="$(cat "$REPORT_DIR/vsomeip_lib.path"):${LD_LIBRARY_PATH}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/streamer.pid"` and `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/service.log" 2>&1 & printf '%s\n' "$!" > "$REPORT_DIR/service.pid"`
- working directory: `example-streamer-implementations` for streamer command; repo root for service command
- exit status / pass-fail: `0` / PASS
- key output lines:
  - PID files created: `streamer.pid`, `service.pid`
- concise conclusion: Streamer and Zenoh service started successfully.

### 3) Run bounded client

- exact command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="$(cat "$REPORT_DIR/vsomeip_lib.path"):${LD_LIBRARY_PATH}" && export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `client.exit`: `124`
- concise conclusion: SOME/IP client ran bounded request/response loop.

### 4) Request/response functional checks

- exact command: `rg -n -m 2 -o "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE|commstatus: Some\(OK\)" "$REPORT_DIR/client.log" && rg -n -m 2 -o "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `client.log:108: UMESSAGE_TYPE_RESPONSE`
  - `client.log:108: commstatus: Some(OK)`
  - `client.log:109: ServiceResponseListener: Received a message`
  - `service.log:16: ServiceResponseListener: Received a message`
  - `service.log:17: Sending Response message`
- concise conclusion: SOME/IP->Zenoh request/response forwarding is successful and stable.

### 5) Structured logging assertions

- exact command: `rg -n -m 1 "egress_send_attempt" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_send_ok" "$REPORT_DIR/streamer.log" && rg -n -m 1 "egress_worker_create|egress_worker_reuse" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:135: event="egress_send_attempt" ... worker_id="019c4ab7-8899-77b5-9a4b-bf67d4dde226"`
  - `streamer.log:137: event="egress_send_ok" ... worker_id="019c4ab7-8899-77b5-9a4b-bf67d4dde226"`
  - `streamer.log:48: event="egress_worker_create" ... route_label="[in.name: host_endpoint, ... out.name: someip_endpoint, ...]"`
- concise conclusion: Required structured egress log assertions are present.

### 6) Critical-route and lag/closed checks

- exact command: `rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT_DIR/streamer.log" ; critical_status=$?; printf 'critical_route_status=%s\n' "$critical_status" && rg -n "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log" ; lag_status=$?; printf 'lag_closed_status=%s\n' "$lag_status"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `critical_route_status=1`
  - `lag_closed_status=1`
- concise conclusion: No critical route errors; lag/closed not observed in bounded run.

### 7) Teardown

- exact command: `kill -INT "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && sleep 1 && kill -TERM "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true && pkill -TERM -f "zenoh_someip|zenoh_service|someip_client" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - no matching scenario processes remained after teardown
- concise conclusion: Scenario cleanup completed.

## Final Conclusion

Scenario passed in Cycle 2 with stable SOME/IP->Zenoh request/response forwarding and required structured logs.
