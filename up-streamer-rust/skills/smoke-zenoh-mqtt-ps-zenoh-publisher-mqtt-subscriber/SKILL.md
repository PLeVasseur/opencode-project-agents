---
name: smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber
description: Validate Zenoh publisher to MQTT subscriber pub/sub forwarding through configurable-streamer.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: smoke-zenoh-mqtt-pubsub
---

## Scope

Run and validate this binary set:

- Broker: `utils/mosquitto/docker-compose.yaml`
- Streamer: `configurable-streamer`
- Publisher: `example-streamer-uses` bin `zenoh_publisher`
- Subscriber: `example-streamer-uses` bin `mqtt_subscriber`

## Execution

1. Setup from repo root:
   - `source build/envsetup.sh highest`
   - `export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber"`
   - `mkdir -p "$REPORT_DIR"`
2. Build binaries:
   - `cargo build -p configurable-streamer`
   - `cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport`
   - `cargo build -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport`
3. Start broker:
   - `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
4. Start streamer from `configurable-streamer`:
   - `source ../build/envsetup.sh highest`
   - `RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & echo $! > "$REPORT_DIR/streamer.pid"`
5. Start subscriber from repo root (aligned with static subscription sink URI):
   - `source build/envsetup.sh highest`
   - `RUST_LOG=info cargo run -p example-streamer-uses --bin mqtt_subscriber --features mqtt-transport -- --uauthority authority-a --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-b --source-uentity 0x3039 --source-uversion 0x1 --source-resource 0x8001 --broker-uri localhost:1883 > "$REPORT_DIR/subscriber.log" 2>&1 & echo $! > "$REPORT_DIR/subscriber.pid"`
6. Run publisher from repo root:
   - `source build/envsetup.sh highest`
   - `export RUST_LOG="info,example_streamer_uses=debug"`
   - `timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`

## Validation

- Publisher emitted traffic: `rg -n "Sending Publish message" "$REPORT_DIR/publisher.log"`
- Subscriber received traffic: `rg -n "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- Streamer forwarded traffic: `rg -n "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`

Pass only when all three checks match.

## Teardown

- `kill -INT "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- If still alive: `kill -TERM "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- `docker compose -f utils/mosquitto/docker-compose.yaml down`
- Verify: `pgrep -fa "configurable-streamer|zenoh_publisher|mqtt_subscriber" || true`
