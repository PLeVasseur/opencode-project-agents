# smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service

## Result

- Status: PASS

## Evidence

- Command: `source build/envsetup.sh highest && cargo build -p configurable-streamer && cargo build -p example-streamer-uses --bin mqtt_client --features mqtt-transport && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)` (all three builds)
- Conclusion: scenario binaries built.

- Command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: broker started.

- Command: `source ../build/envsetup.sh highest && RUST_LOG="up_streamer=debug,up_transport_mqtt5=debug" cargo run -- --config "CONFIG.json5" > "$ART/streamer.log" 2>&1 & echo $! > "$ART/streamer.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/configurable-streamer`
- Exit status: 0 (pass)
- Key output lines:
  - `Running .../target/debug/configurable-streamer --config CONFIG.json5`
- Conclusion: streamer started.

- Command: `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$ART/service.log" 2>&1 & echo $! > "$ART/service.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `ServiceResponseListener: Received a message`
- Conclusion: service processed requests.

- Command: `source build/envsetup.sh highest && export RUST_LOG="info,up_transport_mqtt5=debug,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin mqtt_client --features mqtt-transport -- --broker-uri localhost:1883 > "$ART/client.log" 2>&1; printf '%s\n' "$?" > "$ART/client.exit"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass), workload exit code recorded as `124` (expected timeout-bounded run)
- Key output lines:
  - `ServiceResponseListener: Received a message: ... UMESSAGE_TYPE_RESPONSE`
- Conclusion: client received responses continuously.

## Structured logging assertions

- Command: `rg -n -m 1 "egress_send_attempt.*worker_id|worker_id.*egress_send_attempt" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_attempt" ... worker_id="019c48fb-cede-780f-a48b-f051fc607b4f"`
- Conclusion: attempt event includes `worker_id`.

- Command: `rg -n -m 1 "egress_send_ok.*worker_id|worker_id.*egress_send_ok" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_ok" ... worker_id="019c48fb-cede-780f-a48b-f051fc607b4f"`
- Conclusion: success event includes `worker_id`.

- Command: `rg -n -m 1 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_worker_create" ... route_label="[in.name: endpoint_zenoh_1, in.authority: \"authority-b\" ; out.name: endpoint_mqtt_1, out.authority: \"authority-a\"]"`
- Conclusion: route-label correlation event emitted.

- Command: `rg -n -m 1 "egress_recv_lagged|egress_recv_closed" "$ART/streamer.log"`
- Exit status: 1 (not observed)
- Key output lines:
  - none
- Conclusion: lag/closed events not observed in bounded healthy run.

- Command: `rg -n -m 1 -i "error|failed|disconnect" "$ART/client.log" "$ART/streamer.log"`
- Exit status: 1 (pass for negative check)
- Key output lines:
  - none
- Conclusion: no transport-level failure signatures detected.

## Teardown

- Command: `kill -INT ...; kill -TERM ...; docker compose -f utils/mosquitto/docker-compose.yaml down; pkill ...`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Container mosquitto-mosquitto-1  Removed`
  - `Network mosquitto_default  Removed`
- Conclusion: scenario cleaned up.
