# Phase 7 Canonical Transport Matrix (Final Rerun)

## Scenario A (Zenoh <=> SOME/IP)

### Entry A1
- Command: `(source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport && cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip")`
- Working directory: repo root (`/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`)
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.56s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.49s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.45s`
- Conclusion: Scenario A streamer/service/client binaries built successfully.

### Entry A2
- Command: `timeout 45s cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip"`
- Working directory: repo root
- Exit status: 124 (timeout branch accepted)
- Key output lines:
  - `124` (`scenarioA_final_client_phase7.exit`)
- Conclusion: Client loop ran for the full timeout window; pass/fail is determined by log criteria.

### Entry A3
- Command: `rg -n "UMESSAGE_TYPE_RESPONSE|commstatus: Some\(OK\)" "$REPORT_DIR/scenarioA_final_client_phase7.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `... type_: UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK) ...`
  - `ServiceResponseListener: Received a message ...`
- Conclusion: SOME/IP client observed repeated response traffic with `commstatus: Some(OK)`.

### Entry A4
- Command: `rg -n "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/scenarioA_final_service_phase7.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `ServiceResponseListener: Received a message`
  - `Sending Response message:`
- Conclusion: Zenoh service request/response loop remained active and continuous.

### Entry A5
- Command: `rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT_DIR/scenarioA_final_streamer_phase7.log"`
- Working directory: repo root
- Exit status: 1 (pass, no matches)
- Key output lines:
  - none (empty result set)
- Conclusion: No routing-miss/startup-panic signatures were observed in streamer logs.

### Entry A6
- Command: `for pidf in "$REPORT_DIR/scenarioA_final_service_phase7.pid" "$REPORT_DIR/scenarioA_final_streamer_phase7.pid"; do test -f "$pidf" && kill -INT "$(cat "$pidf")" || true; done` then `pgrep -fa "zenoh_someip|zenoh_service|someip_client" || true`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `1078601 target/debug/zenoh_service` (post-SIGINT lingering process)
  - lingering service cleared after `kill -TERM 1078601`
- Conclusion: Teardown completed; non-interactive SIGINT was insufficient for one process, SIGTERM fallback removed leftovers.

## Scenario B (Zenoh <=> MQTT5)

### Entry B1
- Command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d && docker compose -f utils/mosquitto/docker-compose.yaml ps`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1 Started`
  - `0.0.0.0:1883->1883/tcp`
- Conclusion: MQTT broker started and exposed expected listener port.

### Entry B2
- Command: `rg -n "listen:|connect:|endpoints" configurable-streamer/ZENOH_CONFIG.json5`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `6:  listen: {`
  - `7:    endpoints: ["tcp/0.0.0.0:7447"],`
- Conclusion: Local router mode correctly uses `listen.endpoints`.

### Entry B3
- Command: `(source build/envsetup.sh highest && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport && cargo build -p example-streamer-uses --bin mqtt_client --features mqtt-transport)`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.70s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.57s`
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s) in 0.53s`
- Conclusion: Scenario B streamer/service/client binaries built successfully.

### Entry B4
- Command: `timeout 45s cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883`
- Working directory: repo root
- Exit status: 124 (timeout branch accepted)
- Key output lines:
  - `124` (`scenarioB_final_client_phase7.exit`)
- Conclusion: MQTT client loop ran for the full timeout window; criteria validation comes from logs.

### Entry B5
- Command: `rg -n "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/scenarioB_final_client_phase7.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `ServiceResponseListener: Received a message ... type_: UMESSAGE_TYPE_RESPONSE ...`
- Conclusion: MQTT client continuously received response traffic.

### Entry B6
- Command: `rg -n "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/scenarioB_final_service_phase7.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `ServiceResponseListener: Received a message`
  - `Sending Response message:`
- Conclusion: Service-side request handling and response emission remained stable.

### Entry B7
- Command: `rg -n "Sending on out_transport succeeded" "$REPORT_DIR/scenarioB_final_streamer_phase7.log"`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: Streamer forwarding remained active across the full client run.

### Entry B8
- Command: `rg -ni "error|failed|disconnect" "$REPORT_DIR/scenarioB_final_streamer_phase7.log" "$REPORT_DIR/scenarioB_final_client_phase7.log"`
- Working directory: repo root
- Exit status: 1 (pass, no matches)
- Key output lines:
  - none (empty result set)
- Conclusion: No transport-level failure signatures were found in streamer/client logs.

### Entry B9
- Command: `for pidf in "$REPORT_DIR/scenarioB_final_service_phase7.pid" "$REPORT_DIR/scenarioB_final_streamer_phase7.pid"; do test -f "$pidf" && kill -INT "$(cat "$pidf")" || true; done` then `pgrep -fa "configurable-streamer|zenoh_service|mqtt_client" || true` then `docker compose -f utils/mosquitto/docker-compose.yaml down`
- Working directory: repo root
- Exit status: 0 (pass)
- Key output lines:
  - `1079962 ... configurable-streamer --config CONFIG.json5`
  - `1080079 target/debug/zenoh_service`
  - `Container mosquitto-mosquitto-1 Removed`
  - `Network mosquitto_default Removed`
- Conclusion: Scenario B teardown succeeded; SIGTERM fallback was required after SIGINT for non-interactive cleanup.

## Final Matrix Result
- Scenario A outcome: PASS
- Scenario B outcome: PASS
- Overall conclusion: Canonical transport behavior is preserved after modernization; both final reruns meet required pass criteria.
