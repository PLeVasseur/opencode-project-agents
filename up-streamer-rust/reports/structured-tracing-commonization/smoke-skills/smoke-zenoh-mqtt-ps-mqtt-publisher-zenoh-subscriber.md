# smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber

## Result

- Status: PASS

## Evidence

- Command: `source build/envsetup.sh highest && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport && cargo build -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)` (all three builds)
- Conclusion: required binaries compiled.

- Command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: MQTT broker started.

- Command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$ART/streamer.log" 2>&1 & echo $! > "$ART/streamer.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/configurable-streamer`
- Exit status: 0 (pass)
- Key output lines (from `streamer.log`):
  - `Running .../target/debug/configurable-streamer --config CONFIG.json5`
- Conclusion: streamer started.

- Command: `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001 > "$ART/subscriber.log" 2>&1 & echo $! > "$ART/subscriber.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `PublishReceiver: Received a message`
- Conclusion: subscriber consumed forwarded publishes.

- Command: `source build/envsetup.sh highest && export RUST_LOG="info,up_transport_mqtt5=debug,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin mqtt_publisher --features mqtt-transport -- --broker-uri localhost:1883 > "$ART/publisher.log" 2>&1; printf '%s\n' "$?" > "$ART/publisher.exit"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass), workload exit code recorded as `124` (expected timeout-bounded run)
- Key output lines:
  - `Sending Publish message`
- Conclusion: publisher emitted traffic.

## Structured logging assertions

- Command: `rg -n -m 1 "egress_send_attempt.*worker_id|worker_id.*egress_send_attempt" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_attempt" ... worker_id="019c48ec-6a1f-7571-bac9-c6289b7c5a70"`
- Conclusion: attempt event includes `worker_id`.

- Command: `rg -n -m 1 "egress_send_ok.*worker_id|worker_id.*egress_send_ok" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_ok" ... worker_id="019c48ec-6a1f-7571-bac9-c6289b7c5a70"`
- Conclusion: success event includes `worker_id`.

- Command: `rg -n -m 1 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, in.authority: \"authority-b\" ; out.name: endpoint_mqtt_1, out.authority: \"authority-a\"]"`
- Conclusion: worker-route correlation event emitted.

- Command: `rg -n -m 1 "egress_recv_lagged|egress_recv_closed" "$ART/streamer.log"`
- Exit status: 1 (not observed)
- Key output lines:
  - none
- Conclusion: lag/closed events not observed in bounded healthy run.

## Teardown

- Command: `kill -INT ...; kill -TERM ...; docker compose -f utils/mosquitto/docker-compose.yaml down; pkill ...`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - broker/network removed successfully
- Conclusion: scenario cleaned up.
