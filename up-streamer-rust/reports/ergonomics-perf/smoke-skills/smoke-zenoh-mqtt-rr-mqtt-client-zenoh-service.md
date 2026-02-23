# Smoke Skill Report: smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin mqtt_client --features mqtt-transport && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... configurable-streamer`
  - `Finished 'dev' profile ... mqtt_client`
  - `Finished 'dev' profile ... zenoh_service`
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: Scenario prerequisites and binaries were ready.

2) First streamer start attempt:
- Command: `target/debug/configurable-streamer --config configurable-streamer/CONFIG.json5`
- Exit status: non-zero
- Key output:
  - `Error: UStatus { code: INVALID_ARGUMENT, message: Some("Unable to load MQTT transport details: ... No such file or directory") }`
- Conclusion: Initial attempt used wrong working-directory/config path pairing.

3) Remediated start command and process launch:
- Streamer command (working directory `configurable-streamer`): `../target/debug/configurable-streamer --config CONFIG.json5 > .../streamer.log 2>&1 &`
- Service command (repo root): `target/debug/zenoh_service > .../service.log 2>&1 &`
- Exit status: 0 (pass)
- Key output:
  - streamer log shows route setup (no startup panic)
- Conclusion: Streamer and service were running for client request/response window.

4) Client run command:
- `source build/envsetup.sh highest && timeout 45s target/debug/mqtt_client --broker-uri localhost:1883 > .../client.log 2>&1; printf '%s\n' "$?" > .../client.exit`
- Exit status: 0 (command), client exit file: `124`
- Key output:
  - `client.exit` captured `124` (expected timeout window)
- Conclusion: Client generated repeated request flow during validation window.

5) Validation checks:
- `rg -n -m 3 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" .../client.log`
- `rg -n -m 3 "ServiceResponseListener: Received a message|Sending Response message" .../service.log`
- `rg -n -m 3 "Sending on out_transport succeeded" .../streamer.log`
- Exit status: 0 (all pass)
- Key output:
  - Client: `mqtt_client::common: ServiceResponseListener: Received a message ... UMESSAGE_TYPE_RESPONSE`
  - Service: `zenoh_service::common: ServiceResponseListener: Received a message` and `Sending Response message`
  - Streamer: `EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: End-to-end request/response forwarding succeeded through streamer.

6) Failure signature check:
- Command: `if rg -ni -m 5 "error|failed|disconnect" .../client.log .../streamer.log; then ...; else ...; fi`
- Exit status: 0 (pass)
- Key output:
  - `FAILURE_SIGNATURES=none`
- Conclusion: No transport failure signatures matched in client/streamer logs.

7) Teardown:
- Commands:
  - `kill -INT <service-pid> <streamer-pid> || true`
  - `kill -TERM <service-pid> <streamer-pid> || true`
  - `docker compose -f utils/mosquitto/docker-compose.yaml down`
  - `pkill -9` remediation for stale wrapper-pid mismatch
- Exit status: 0 (pass)
- Key output:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Scenario cleaned up; one force-stop remediation was needed due wrapper-vs-child pid mismatch.

## Result

PASS - Required RR response, service handling, and forwarding evidence matched.
