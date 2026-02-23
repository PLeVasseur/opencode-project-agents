# Smoke Report: smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber

## Result

- Status: PASS
- Scope: Zenoh publisher -> configurable-streamer -> MQTT subscriber (pub/sub)
- Log directory: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`

## Command Evidence

1. Command: `source build/envsetup.sh highest && ... && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Finished 'dev' profile ...`
     - `Container mosquitto-mosquitto-1  Running`
   - Conclusion: prerequisites and binaries prepared.

2. Command: `source ../build/envsetup.sh highest && ... cargo run -- --config "CONFIG.json5" ... &`
   - Working directory: `configurable-streamer`
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: streamer launched with log+pid capture.

3. Command: `source build/envsetup.sh highest && ... cargo run -p example-streamer-uses --bin mqtt_subscriber ... &`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: subscriber launched with log+pid capture.

4. Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher ...`
   - Working directory: repo root
   - Exit status: 0 (pass command wrapper)
   - Key output:
     - publisher exit file: `124`
   - Conclusion: publisher ran under bounded timeout window (expected long-running publisher behavior).

5. Command: `rg -n "Sending Publish message" "$REPORT_DIR/publisher.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `19:Sending Publish message:`
     - `21:Sending Publish message:`
   - Conclusion: publisher emitted publish traffic.

6. Command: `rg -n "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `... mqtt_subscriber::common: PublishReceiver: Received a message ...`
   - Conclusion: subscriber received forwarded messages.

7. Command: `rg -n "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
   - Conclusion: streamer forwarded traffic successfully.

8. Command: `kill ... && docker compose ... down && pgrep -fa "configurable-streamer|zenoh_publisher|mqtt_subscriber" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - docker stack stopped/removed
     - only the `pgrep` command line itself remained in match output
   - Conclusion: scenario teardown succeeded.

## Pass/Fail Decision

- Publisher emitted traffic: PASS
- Subscriber received traffic: PASS
- Streamer forwarded traffic: PASS
- Final verdict: PASS
