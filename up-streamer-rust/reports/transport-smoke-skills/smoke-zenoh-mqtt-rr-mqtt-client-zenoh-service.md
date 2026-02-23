# Smoke Report: smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service

## Result

- Status: PASS
- Scope: MQTT client -> configurable-streamer -> Zenoh service (request/response)
- Log directory: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`

## Command Evidence

1. Command: `source build/envsetup.sh highest && ... && docker compose -f utils/mosquitto/docker-compose.yaml up -d`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - broker started
   - Conclusion: prerequisites and binaries prepared.

2. Command: `source ../build/envsetup.sh highest && ... cargo run -- --config "CONFIG.json5" ... &`
   - Working directory: `configurable-streamer`
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: streamer launched.

3. Command: `source build/envsetup.sh highest && ... cargo run -p example-streamer-uses --bin zenoh_service ... &`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: service launched.

4. Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin mqtt_client ...`
   - Working directory: repo root
   - Exit status: 0 (pass command wrapper)
   - Key output:
     - client exit file: `124`
   - Conclusion: client exercised request/response flow under timeout.

5. Command: `rg -n -m 5 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/client.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `mqtt_client::common: ServiceResponseListener: Received a message ... UMESSAGE_TYPE_RESPONSE ...`
   - Conclusion: client received responses.

6. Command: `rg -n -m 5 "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `zenoh_service::common: ServiceResponseListener: Received a message ...`
     - `zenoh_service::common: Sending Response message:`
   - Conclusion: service processed requests and emitted responses.

7. Command: `rg -n -m 5 "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
   - Conclusion: streamer forwarded request/response traffic.

8. Command: `rg -ni -m 5 "error|failed|disconnect" "$REPORT_DIR/client.log" "$REPORT_DIR/streamer.log" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: no transport-level failure signature detected.

9. Command: `kill ... && docker compose ... down && pgrep -fa "configurable-streamer|zenoh_service|mqtt_client" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - broker stopped and removed
   - Conclusion: teardown clean.

## Pass/Fail Decision

- Client response evidence: PASS
- Service request/response evidence: PASS
- Streamer forwarding evidence: PASS
- Failure-signature check: PASS
- Final verdict: PASS
