# Smoke Skill Report: smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport && cargo build -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... configurable-streamer`
  - `Finished 'dev' profile ... mqtt_publisher`
  - `Finished 'dev' profile ... zenoh_subscriber`
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: Scenario prerequisites and binaries were ready.

2) Command: launch background streamer and subscriber
- Streamer command (working directory `configurable-streamer`): `cargo run -- --config "CONFIG.json5" > .../streamer.log 2>&1 &`
- Subscriber command (repo root): `cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- ... > .../subscriber.log 2>&1 &`
- Exit status: 0 (pass)
- Key output:
  - PID files created in scenario log directory
- Conclusion: Streamer and Zenoh subscriber processes were active for validation window.

3) Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --broker-uri localhost:1883 > .../publisher.log 2>&1; printf '%s\n' "$?" > .../publisher.exit`
- Exit status: 0 (command), publisher exit file: `124`
- Key output:
  - `publisher.exit` captured `124` (expected timeout window)
- Conclusion: Publisher ran long enough to emit repeated traffic.

4) Command: validation grep checks
- `rg -n -m 3 "Sending Publish message" .../publisher.log`
- `rg -n -m 3 "PublishReceiver: Received a message" .../subscriber.log`
- `rg -n -m 3 "Sending on out_transport succeeded" .../streamer.log`
- Exit status: 0 (all pass)
- Key output:
  - Publisher: `mqtt_publisher: Sending Publish message:`
  - Subscriber: `zenoh_subscriber::common: PublishReceiver: Received a message`
  - Streamer: `EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: MQTT publish traffic was forwarded through streamer and consumed by Zenoh subscriber.

5) Command: teardown
- `kill -INT <subscriber-pid> <streamer-pid> || true`
- `kill -TERM <subscriber-pid> <streamer-pid> || true`
- `docker compose -f utils/mosquitto/docker-compose.yaml down`
- `kill -9 <leftover-pids>` (required once)
- Exit status: 0 (pass)
- Key output:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Scenario was cleaned up; lingering processes required one explicit force-stop.

## Result

PASS - Required publisher/subscriber/streamer forwarding evidence matched.
