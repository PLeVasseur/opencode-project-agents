---
name: smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service
description: Validate MQTT client to Zenoh service request/response through configurable-streamer.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: smoke-zenoh-mqtt-rr
---

## Scope

Run and validate this binary set:

- Broker: `utils/mosquitto/docker-compose.yaml`
- Streamer: `configurable-streamer`
- Client: `example-streamer-uses` bin `mqtt_client`
- Service: `example-streamer-uses` bin `zenoh_service`

## Execution

1. Setup from repo root:
   - `source build/envsetup.sh highest`
   - `export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service"`
   - `mkdir -p "$REPORT_DIR"`
2. Build binaries:
   - `cargo build -p configurable-streamer`
   - `cargo build -p example-streamer-uses --bin mqtt_client --features mqtt-transport`
   - `cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
3. Start broker:
   - `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
4. Start streamer from `configurable-streamer`:
   - `source ../build/envsetup.sh highest`
   - `RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & echo $! > "$REPORT_DIR/streamer.pid"`
5. Start service from repo root:
   - `source build/envsetup.sh highest`
   - `RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/service.log" 2>&1 & echo $! > "$REPORT_DIR/service.pid"`
6. Run client from repo root:
   - `source build/envsetup.sh highest`
   - `export RUST_LOG="info,up_transport_mqtt5=debug,example_streamer_uses=debug"`
   - `timeout 45s cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883 > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`

## Validation

- Client saw responses: `rg -n "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/client.log"`
- Service handled requests: `rg -n "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- Streamer forwarded messages: `rg -n "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`
- No transport failure signatures: `rg -ni "error|failed|disconnect" "$REPORT_DIR/client.log" "$REPORT_DIR/streamer.log"`

Pass only when the first three checks match and the failure-signature check returns no matches.

## Teardown

- `kill -INT "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- If still alive: `kill -TERM "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- `docker compose -f utils/mosquitto/docker-compose.yaml down`
- Verify: `pgrep -fa "configurable-streamer|zenoh_service|mqtt_client" || true`
