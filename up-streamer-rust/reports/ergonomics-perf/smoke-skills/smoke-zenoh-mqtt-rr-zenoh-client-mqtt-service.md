# Smoke Skill Report: smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin zenoh_client --features zenoh-transport && cargo build -p example-streamer-uses --bin mqtt_service --features mqtt-transport && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... configurable-streamer`
  - `Finished 'dev' profile ... zenoh_client`
  - `Finished 'dev' profile ... mqtt_service`
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: Scenario prerequisites and binaries were ready.

2) Command: launch background streamer and service
- Streamer command (working directory `configurable-streamer`): `cargo run -- --config "CONFIG.json5" > .../streamer.log 2>&1 &`
- Service command (repo root): `cargo run -p example-streamer-uses --bin mqtt_service --features mqtt-transport -- --broker-uri localhost:1883 > .../service.log 2>&1 &`
- Exit status: 0 (pass)
- Key output:
  - PID files generated in scenario log directory
- Conclusion: Streamer and MQTT service were running for the client request/response window.

3) Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin zenoh_client --features zenoh-transport > .../client.log 2>&1; printf '%s\n' "$?" > .../client.exit`
- Exit status: 0 (command), client exit file: `124`
- Key output:
  - `client.exit` captured `124` (expected timeout window)
- Conclusion: Client executed long enough to generate repeated RR traffic.

4) Command: response/forwarding validation checks
- `rg -n -m 3 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" .../client.log`
- `rg -n -m 3 "ServiceResponseListener: Received a message|Sending Response message" .../service.log`
- `rg -n -m 3 "Sending on out_transport succeeded" .../streamer.log`
- Exit status: 0 (all pass)
- Key output:
  - Client: `ServiceResponseListener: Received a message ... UMESSAGE_TYPE_RESPONSE`
  - Service: `ServiceResponseListener: Received a message` and `Sending Response message`
  - Streamer: `EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: End-to-end request/response forwarding succeeded through streamer.

5) Command: failure-signature check
- `rg -ni -m 5 "error|failed|disconnect" .../client.log .../streamer.log; printf 'RG_EXIT=%s\n' "$?"`
- Exit status: 0 (pass)
- Key output:
  - `RG_EXIT=1`
- Conclusion: No failure signatures matched in client/streamer logs.

6) Command: teardown
- `kill -INT <service-pid> <streamer-pid> || true`
- `kill -TERM <service-pid> <streamer-pid> || true`
- `docker compose -f utils/mosquitto/docker-compose.yaml down`
- `kill -9 1376928 1377058` (remediation)
- Exit status: 0 (pass)
- Key output:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Scenario cleaned up; one force-stop remediation was needed because pid files captured wrapper shell pids.

## Result

PASS - Required RR response, service handling, and forwarding evidence matched.
