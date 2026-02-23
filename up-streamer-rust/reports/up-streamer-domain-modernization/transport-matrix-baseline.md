# Phase 1 Canonical Transport Matrix Baseline

## Scenario A: Zenoh <=> SOME/IP request/response

### Entry A1
- Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: 0 (pass)
- Key output lines:
  - `Compiling up-streamer v0.1.0`
  - `Compiling up-linux-streamer v0.1.0`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 2m 24s`
- Conclusion: Terminal A bootstrap and required binary build succeeded.

### Entry A2
- Command: `source ../build/envsetup.sh highest && export LD_LIBRARY_PATH="$(ls -d /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: 0 (pass; process started and logs captured)
- Key output lines (from `scenarioA_streamer.log`):
  - `Running .../target/debug/zenoh_someip --config DEFAULT_CONFIG.json5`
  - `UStreamer::...::new(): UStreamer created`
  - `ForwardingListeners::insert: able to register request listener`
- Conclusion: Streamer launched with expected routing/listener initialization.

### Entry A3
- Command: `source build/envsetup.sh highest && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- Working directory: repo root
- Exit status: 0 (pass; process started)
- Key output lines (from `scenarioA_service.log`):
  - `Running 'target/debug/zenoh_service'`
- Conclusion: Zenoh service process started for scenario.

### Entry A4
- Command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="$(ls -d /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip"`
- Working directory: repo root
- Exit status: 0 (pass; process started)
- Key output lines (from `scenarioA_client.log`):
  - `Running 'target/debug/someip_client'`
  - `type_: UMESSAGE_TYPE_RESPONSE`
  - `commstatus: Some(OK)`
- Conclusion: SOME/IP client produced continuous request/response traffic.

### Entry A5
- Command: `rg -c "commstatus: Some\(OK\)" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioA_client.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `54`
- Conclusion: Client observed many successful response statuses.

### Entry A6
- Command: `rg -n "Routing info for remote service could not be found" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioA_"*.log || true`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - no matches
- Conclusion: No repeating routing-info missing warnings were observed.

### Entry A7
- Command: `rg -c "me_client@i=" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioA_client.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `108`
- Conclusion: Request/response progression is continuous and stable over many iterations.

### Entry A8
- Command: `rg -c "ServiceResponseListener: Received a message" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioA_service_rerun.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `44`
- Conclusion: Zenoh service request handling was explicitly observed in Scenario A (rerun with `RUST_LOG=info`).

### Entry A9
- Command: `kill -INT 971563 971277 971189` and later `kill -INT 977089 977010 976921`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - process checks after signals returned no `zenoh_someip`, `zenoh_service`, or `someip_client` binaries running
- Conclusion: Scenario A processes were stopped cleanly before Scenario B and after Scenario A log-verification rerun.

## Scenario B: Zenoh <=> MQTT5 request/response

### Entry B1
- Command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: MQTT broker prerequisite was started successfully.

### Entry B2
- Command: `rg -n "listen|connect|endpoints" configurable-streamer/ZENOH_CONFIG.json5`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `6:  listen: {`
  - `7:    endpoints: ["tcp/0.0.0.0:7447"],`
- Conclusion: Local router configuration uses `listen.endpoints` (not `connect.endpoints`).

### Entry B3
- Command: `source ../build/envsetup.sh highest && export RUST_LOG="debug" && cargo run -- --config "CONFIG.json5"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/configurable-streamer`
- Exit status: 0 (pass; process started)
- Key output lines (from `scenarioB_streamer_rerun.log`):
  - `Started up-linux-streamer-configurable`
  - `UStreamer::...::new(): UStreamer created`
  - `TransportForwarder::message_forwarding_loop(): Sending on out_transport succeeded`
- Conclusion: Configurable streamer bridged Zenoh<=>MQTT with active forwarding.

### Entry B4
- Command: `source build/envsetup.sh highest && export RUST_LOG="info" && cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- Working directory: repo root
- Exit status: 0 (pass; process started)
- Key output lines (from `scenarioB_service_rerun.log`):
  - `Started zenoh_service`
  - `ServiceResponseListener: Received a message`
  - `Sending Response message`
- Conclusion: Zenoh service handled bridged requests and emitted responses.

### Entry B5
- Command: `source build/envsetup.sh highest && export RUST_LOG="info,up_transport_mqtt5=debug" && cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883`
- Working directory: repo root
- Exit status: 0 (pass; process started)
- Key output lines (from `scenarioB_client_rerun.log`):
  - `Started mqtt_client.`
  - `Sending Request message:`
  - `ServiceResponseListener: Received a message: UMessage { ... type_: UMESSAGE_TYPE_RESPONSE ... }`
- Conclusion: MQTT client observed continuous request/response behavior.

### Entry B6
- Command: `rg -c "ServiceResponseListener: Received a message" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioB_client_rerun.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `53`
- Conclusion: Dozens of responses were received without interruption.

### Entry B7
- Command: `rg -n "disconnect|transport-level|ERROR|failed" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioB_client_rerun.log" "/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/up-streamer-domain-modernization/scenarioB_streamer_rerun.log" || true`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - no matches
- Conclusion: No transport-level failure/disconnect signatures were found in client or streamer logs.

### Entry B8
- Command: `kill -INT 975813 975743 975671 && docker compose -f utils/mosquitto/docker-compose.yaml down`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Scenario B processes and broker were stopped and cleaned up successfully.

## Gate 1 Result
- Status: PASS
- Scenario A: PASS (`UMESSAGE_TYPE_RESPONSE` and `commstatus: Some(OK)` with no routing-miss spam)
- Scenario B: PASS (stable request/response loop with no disconnect/failure signatures)
- Progression decision: eligible to proceed to Phase 2.
