# Smoke Report: smoke-zenoh-someip-rr-someip-client-zenoh-service

Date: 2026-02-11
Scenario: SOME/IP client -> Zenoh service request/response via zenoh_someip streamer
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts/`

## Evidence

### 1) Pre-scenario stale-process cleanup

- exact command: `pkill -INT -f "configurable-streamer|mqtt_service|zenoh_client|mqtt_client|zenoh_service|mqtt_publisher|mqtt_subscriber|zenoh_publisher|zenoh_subscriber|zenoh_someip|someip_" || true; sleep 1; pkill -TERM -f "configurable-streamer|mqtt_service|zenoh_client|mqtt_client|zenoh_service|mqtt_publisher|mqtt_subscriber|zenoh_publisher|zenoh_subscriber|zenoh_someip|someip_" || true; pgrep -fa "[c]onfigurable-streamer|[m]qtt_service|[z]enoh_client|[m]qtt_client|[z]enoh_service|[m]qtt_publisher|[m]qtt_subscriber|[z]enoh_publisher|[z]enoh_subscriber|[z]enoh_someip|[s]omeip_" || true`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status / pass-fail: `0` / PASS
- key output lines:
  - no remaining matching processes were listed
- concise conclusion: Scenario started from a clean process state.

### 2) Build binaries and resolve bundled vsomeip library path

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts" && mkdir -p "$REPORT_DIR" && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport && set -- "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib && test -d "$1" && printf 'vsomeip_lib_dir=%s\n' "$1"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.70s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.50s`
  - `vsomeip_lib_dir=/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
- concise conclusion: Required binaries built and bundled vsomeip runtime library path resolved.

### 3) Start streamer

- exact command: `set -e; source ../build/envsetup.sh highest; REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; set -- ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib; VSOMEIP_LIB_DIR="$1"; test -d "$VSOMEIP_LIB_DIR"; export LD_LIBRARY_PATH="$VSOMEIP_LIB_DIR:${LD_LIBRARY_PATH}"; export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"; cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & pid=$!; printf '%s\n' "$pid" > "$REPORT_DIR/streamer.pid"; printf 'streamer_pid=%s\n' "$pid"; printf 'vsomeip_lib_dir=%s\n' "$VSOMEIP_LIB_DIR"`
- working directory: `example-streamer-implementations`
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer_pid=1572863`
  - `vsomeip_lib_dir=../target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
- concise conclusion: `zenoh_someip` streamer started with bundled vsomeip library path injected.

### 4) Start service

- exact command: `set -e; source build/envsetup.sh highest; REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/service.log" 2>&1 & pid=$!; printf '%s\n' "$pid" > "$REPORT_DIR/service.pid"; printf 'service_pid=%s\n' "$pid"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `service.pid` contains `1572959`
- concise conclusion: Zenoh service started and is ready to handle incoming requests.

### 5) Run bounded client

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts" && set -- "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib && VSOMEIP_LIB_DIR="$1" && test -d "$VSOMEIP_LIB_DIR" && export LD_LIBRARY_PATH="$VSOMEIP_LIB_DIR:${LD_LIBRARY_PATH}" && export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `client.exit`: `124`
  - bounded timeout is expected for continuous request loop
- concise conclusion: SOME/IP client executed for the bounded window and exercised sustained request flow.

### 6) Client received OK responses

- exact command: `rg -n -m 3 "UMESSAGE_TYPE_RESPONSE|commstatus: Some\(OK\)" "$REPORT_DIR/client.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `client.log:107: ... type_: UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK) ...`
  - `client.log:108: ... ServiceResponseListener: Received a message ... commstatus: Some(OK) ...`
- concise conclusion: SOME/IP client observed successful response semantics (`UMESSAGE_TYPE_RESPONSE`, `commstatus: Some(OK)`).

### 7) Service handled requests

- exact command: `rg -n -m 3 "ServiceRequestListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `service.log:17: ... Sending Response message:`
  - `service.log:20: ... Sending Response message:`
  - `service.log:23: ... Sending Response message:`
- concise conclusion: Zenoh service processed requests and emitted responses.

### 8) Streamer critical error signature check

- exact command: `rg -n -m 3 "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `1` / PASS
- key output lines:
  - no matches
- concise conclusion: No critical routing/setup failures were observed in streamer logs.

### 9) Structured logging assertion: `egress_send_attempt` with `worker_id`

- exact command: `rg -n -m 3 "egress_send_attempt" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:135: ... event="egress_send_attempt" ... worker_id="019c49b4-82e2-779a-a383-7624d96d9490" ...`
  - `streamer.log:138: ... event="egress_send_attempt" ... worker_id="019c49b4-82cb-714a-a60d-d069b9fe11ea" ...`
- concise conclusion: Required `egress_send_attempt` structured event includes `worker_id`.

### 10) Structured logging assertion: `egress_send_ok` with `worker_id`

- exact command: `rg -n -m 3 "egress_send_ok.*worker_id" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:136: ... event="egress_send_ok" ... worker_id="019c49b4-82e2-779a-a383-7624d96d9490" ...`
  - `streamer.log:166: ... event="egress_send_ok" ... worker_id="019c49b4-82cb-714a-a60d-d069b9fe11ea" ...`
- concise conclusion: Required `egress_send_ok` structured event includes `worker_id`.

### 11) Structured logging assertion: worker create/reuse with `route_label`

- exact command: `rg -n -m 3 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:48: ... event="egress_worker_create" ... route_label="[in.name: host_endpoint, ... out.name: someip_endpoint, ...]" ...`
  - `streamer.log:58: ... event="egress_worker_create" ... route_label="[in.name: someip_endpoint, ... out.name: host_endpoint, ...]" ...`
- concise conclusion: Required worker lifecycle structured event includes `route_label`.

### 12) Lag/closed bounded-run check

- exact command: `rg -n -m 3 "egress_recv_lagged|egress_recv_closed" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `1` / PASS
- key output lines:
  - no matches
- concise conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded run.

### 13) Teardown

- exact command: `REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts" && read -r service_pid < "$REPORT_DIR/service.pid" && read -r streamer_pid < "$REPORT_DIR/streamer.pid" && kill -INT "$service_pid" "$streamer_pid" || true; sleep 1; kill -TERM "$service_pid" "$streamer_pid" || true; pgrep -fa "[z]enoh_someip|[z]enoh_service|[s]omeip_client" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `kill: (1572863) - No such process`
  - follow-up `pgrep` produced no matches
- concise conclusion: Scenario processes were already exited by teardown time; no residual processes remained.

## Final Conclusion

Scenario passed: bounded SOME/IP client request traffic was forwarded to Zenoh service and responses returned to the client through `zenoh_someip`, with required structured egress lifecycle/send logging assertions satisfied.
