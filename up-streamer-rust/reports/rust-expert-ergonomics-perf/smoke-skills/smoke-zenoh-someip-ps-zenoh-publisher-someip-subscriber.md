# Smoke Report: smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber

Date: 2026-02-11
Scenario: Zenoh publisher -> SOME/IP subscriber via zenoh_someip streamer
Result: PASS
Artifacts: `$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts/`

## Evidence

### 1) Pre-scenario stale-process cleanup

- exact command: `pkill -INT -f "configurable-streamer|mqtt_service|zenoh_client|mqtt_client|zenoh_service|mqtt_publisher|mqtt_subscriber|zenoh_publisher|zenoh_subscriber|zenoh_someip|someip_" || true; sleep 1; pkill -TERM -f "configurable-streamer|mqtt_service|zenoh_client|mqtt_client|zenoh_service|mqtt_publisher|mqtt_subscriber|zenoh_publisher|zenoh_subscriber|zenoh_someip|someip_" || true; pgrep -fa "[c]onfigurable-streamer|[m]qtt_service|[z]enoh_client|[m]qtt_client|[z]enoh_service|[m]qtt_publisher|[m]qtt_subscriber|[z]enoh_publisher|[z]enoh_subscriber|[z]enoh_someip|[s]omeip_" || true`
- working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- exit status / pass-fail: `0` / PASS
- key output lines:
  - no remaining matching processes were listed
- concise conclusion: Scenario started from a clean process state.

### 2) Build binaries and resolve bundled vsomeip library path

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts" && mkdir -p "$REPORT_DIR" && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport && cargo build -p example-streamer-uses --bin someip_subscriber --features "vsomeip-transport,bundled-vsomeip" && set -- "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib && test -d "$1" && printf 'vsomeip_lib_dir=%s\n' "$1"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 20.26s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.83s`
  - `vsomeip_lib_dir=/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
- concise conclusion: Required binaries built and bundled vsomeip runtime library path resolved.

### 3) Start streamer

- exact command: `set -e; source ../build/envsetup.sh highest; REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts"; set -- ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib; VSOMEIP_LIB_DIR="$1"; test -d "$VSOMEIP_LIB_DIR"; export LD_LIBRARY_PATH="$VSOMEIP_LIB_DIR:${LD_LIBRARY_PATH}"; export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"; cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & pid=$!; printf '%s\n' "$pid" > "$REPORT_DIR/streamer.pid"; printf 'streamer_pid=%s\n' "$pid"; printf 'vsomeip_lib_dir=%s\n' "$VSOMEIP_LIB_DIR"`
- working directory: `example-streamer-implementations`
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer_pid=1569849`
  - `vsomeip_lib_dir=../target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
- concise conclusion: `zenoh_someip` streamer started with bundled vsomeip library path injected.

### 4) Start subscriber

- exact command: `set -e; source build/envsetup.sh highest; REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts"; set -- "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib; VSOMEIP_LIB_DIR="$1"; test -d "$VSOMEIP_LIB_DIR"; export LD_LIBRARY_PATH="$VSOMEIP_LIB_DIR:${LD_LIBRARY_PATH}"; RUST_LOG=info cargo run -p example-streamer-uses --bin someip_subscriber --features "vsomeip-transport,bundled-vsomeip" -- --uauthority authority-a --uentity 0x5678 --uversion 0x1 --resource 0x0 --source-authority authority-b --source-uentity 0x3039 --source-uversion 0x1 --source-resource 0x8001 --remote-authority authority-b --vsomeip-config example-streamer-uses/vsomeip-configs/someip_client.json > "$REPORT_DIR/subscriber.log" 2>&1 & pid=$!; printf '%s\n' "$pid" > "$REPORT_DIR/subscriber.pid"; printf 'subscriber_pid=%s\n' "$pid"; printf 'vsomeip_lib_dir=%s\n' "$VSOMEIP_LIB_DIR"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `subscriber_pid=1569970`
  - `vsomeip_lib_dir=/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
- concise conclusion: SOME/IP subscriber started with expected filter and runtime library configuration.

### 5) Run bounded publisher

- exact command: `source build/envsetup.sh highest && REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts" && export RUST_LOG="info,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`
- working directory: repo root
- exit status / pass-fail: `124` / PASS
- key output lines:
  - `publisher.exit`: `124`
  - bounded timeout is expected for continuous publisher loop
- concise conclusion: Zenoh publisher executed for the bounded window and drove publish traffic.

### 6) Publisher emitted traffic

- exact command: `rg -n -m 3 "Sending Publish message" "$REPORT_DIR/publisher.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `publisher.log:16: Sending Publish message:`
  - `publisher.log:18: Sending Publish message:`
  - `publisher.log:20: Sending Publish message:`
- concise conclusion: Publisher continuously emitted publish messages.

### 7) Subscriber received forwarded traffic

- exact command: `rg -n -m 3 "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `subscriber.log:25: ... PublishReceiver: Received a message ...`
  - `subscriber.log:26: ... PublishReceiver: Received a message ...`
  - `subscriber.log:27: ... PublishReceiver: Received a message ...`
- concise conclusion: SOME/IP subscriber received forwarded publish traffic.

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
  - `streamer.log:122: ... event="egress_send_attempt" ... worker_id="019c49ac-bab2-7062-ae4b-351fcf2fd325" ...`
  - `streamer.log:143: ... event="egress_send_attempt" ... worker_id="019c49ac-bab2-7062-ae4b-351fcf2fd325" ...`
- concise conclusion: Required `egress_send_attempt` structured event includes `worker_id`.

### 10) Structured logging assertion: `egress_send_ok` with `worker_id`

- exact command: `rg -n -m 3 "egress_send_ok.*worker_id" "$REPORT_DIR/streamer.log"`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `streamer.log:141: ... event="egress_send_ok" ... worker_id="019c49ac-bab2-7062-ae4b-351fcf2fd325" ...`
  - `streamer.log:156: ... event="egress_send_ok" ... worker_id="019c49ac-bab2-7062-ae4b-351fcf2fd325" ...`
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

- exact command: `REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/rust-expert-ergonomics-perf/smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber-artifacts" && read -r subscriber_pid < "$REPORT_DIR/subscriber.pid" && read -r streamer_pid < "$REPORT_DIR/streamer.pid" && kill -INT "$subscriber_pid" "$streamer_pid" || true; sleep 1; kill -TERM "$subscriber_pid" "$streamer_pid" || true; pgrep -fa "[z]enoh_someip|[z]enoh_publisher|[s]omeip_subscriber" || true`
- working directory: repo root
- exit status / pass-fail: `0` / PASS
- key output lines:
  - `kill: (1569970) - No such process`
  - `kill: (1569849) - No such process`
  - follow-up `pgrep` produced no matches
- concise conclusion: Scenario processes were already exited by teardown time; no residual processes remained.

## Final Conclusion

Scenario passed: bounded Zenoh publish traffic was forwarded to SOME/IP subscriber through `zenoh_someip`, with required structured egress lifecycle/send logging assertions satisfied.
