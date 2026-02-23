# Smoke Skill Report: smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && ... && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport && cargo build -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... configurable-streamer`
  - `Finished 'dev' profile ... zenoh_publisher`
  - `Finished 'dev' profile ... mqtt_subscriber`
  - `Container mosquitto-mosquitto-1  Running`
- Conclusion: Scenario prerequisites and binaries were ready.

2) Command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > <scenario-log>/streamer.log 2>&1 &`
- Working directory: `configurable-streamer`
- Exit status: non-zero on first attempt (pid-file write path typo), then remediated
- Key output:
  - `/bin/bash: line 1: /streamer.pid: Permission denied`
  - Remediation command: `printf '1373625' > <scenario-log>/streamer.pid`
- Conclusion: Streamer process started successfully and was tracked after remediation.

3) Command: `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport -- --uauthority authority-a --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-b --source-uentity 0x3039 --source-uversion 0x1 --source-resource 0x8001 --broker-uri localhost:1883 > <scenario-log>/subscriber.log 2>&1 &`
- Exit status: non-zero on first attempt (pid-file write path typo), then remediated
- Key output:
  - `/bin/bash: line 1: /subscriber.pid: Permission denied`
  - Remediation command: `printf '1373960' > <scenario-log>/subscriber.pid`
- Conclusion: Subscriber process started successfully and was tracked after remediation.

4) Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport > <scenario-log>/publisher.log 2>&1; printf '%s\n' "$?" > <scenario-log>/publisher.exit`
- Exit status: 0 (command), publisher exit file: `124`
- Key output:
  - `publisher.exit` captured `124` (expected timeout termination window)
- Conclusion: Publisher ran for the scenario window and emitted traffic.

5) Command: validation grep checks
- `rg -n -m 3 "Sending Publish message" <scenario-log>/publisher.log`
- `rg -n -m 3 "PublishReceiver: Received a message" <scenario-log>/subscriber.log`
- `rg -n -m 3 "Sending on out_transport succeeded" <scenario-log>/streamer.log`
- Exit status: 0 (all pass)
- Key output:
  - Publisher: `19:Sending Publish message:`
  - Subscriber: `PublishReceiver: Received a message: UMessage { ... }`
  - Streamer: `Sending on out_transport succeeded`
- Conclusion: Publish traffic was produced, forwarded through streamer, and received by MQTT subscriber.

6) Command: teardown
- `kill -INT "$(cat <scenario-log>/subscriber.pid)" "$(cat <scenario-log>/streamer.pid)" || true`
- `docker compose -f utils/mosquitto/docker-compose.yaml down`
- `pgrep -fa "configurable-streamer|zenoh_publisher|mqtt_subscriber" || true`
- Exit status: 0 (pass)
- Key output:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: Scenario processes and broker were torn down.

## Result

PASS - Required publisher/subscriber/streamer forwarding evidence matched.
