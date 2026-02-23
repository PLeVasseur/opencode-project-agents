# Smoke Report: smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber

## Result

- Status: PASS
- Scope: MQTT publisher -> configurable-streamer -> Zenoh subscriber (pub/sub)
- Log directory: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`

## Command Evidence

1. Command: `source build/envsetup.sh highest && ... && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Finished 'dev' profile ...`
     - `Container mosquitto-mosquitto-1  Started`
   - Conclusion: prerequisites and binaries prepared.

2. Command: `source ../build/envsetup.sh highest && ... cargo run -- --config "CONFIG.json5" ... &`
   - Working directory: `configurable-streamer`
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: streamer launched.

3. Command: `source build/envsetup.sh highest && ... cargo run -p example-streamer-uses --bin zenoh_subscriber ... &`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: subscriber launched.

4. Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin mqtt_publisher ...`
   - Working directory: repo root
   - Exit status: 0 (pass command wrapper)
   - Key output:
     - publisher exit file: `124`
   - Conclusion: publisher ran in bounded window.

5. Command: `rg -n -m 5 "Sending Publish message" "$REPORT_DIR/publisher.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `mqtt_publisher: Sending Publish message:`
   - Conclusion: publisher emitted traffic.

6. Command: `rg -n -m 5 "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `zenoh_subscriber::common: PublishReceiver: Received a message ...`
   - Conclusion: subscriber received forwarded messages.

7. Command: `rg -n -m 5 "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
   - Conclusion: streamer forwarding confirmed.

8. Command: `kill ... && docker compose ... down && pgrep -fa "configurable-streamer|mqtt_publisher|zenoh_subscriber" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - broker stack removed cleanly
     - no lingering scenario process found beyond `pgrep` self line
   - Conclusion: teardown clean.

## Pass/Fail Decision

- Publisher emitted traffic: PASS
- Subscriber received traffic: PASS
- Streamer forwarded traffic: PASS
- Final verdict: PASS
