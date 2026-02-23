# Smoke Report: smoke-zenoh-someip-rr-zenoh-client-someip-service

## Result

- Status: PASS
- Scope: Zenoh client -> zenoh_someip streamer -> SOME/IP service (request/response)
- Log directory: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/smoke-zenoh-someip-rr-zenoh-client-someip-service`

## Command Evidence

1. Command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="...vsomeip-install/lib" && cargo build ...`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Finished 'dev' profile ...`
   - Conclusion: binaries prepared for scenario.

2. Command: `source ../build/envsetup.sh highest && ... cargo run --bin zenoh_someip ... &`
   - Working directory: `example-streamer-implementations`
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: streamer launched.

3. Command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="..." && cargo run -p example-streamer-uses --bin someip_service ... &`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: SOME/IP service launched.

4. Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin zenoh_client ...`
   - Working directory: repo root
   - Exit status: 0 (pass command wrapper)
   - Key output:
     - client exit file: `124`
   - Conclusion: client exercised request/response loop.

5. Command: `rg -n -m 5 "ServiceResponseListener: Received a message|UMESSAGE_TYPE_RESPONSE" "$REPORT_DIR/client.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `zenoh_client::common: ServiceResponseListener: Received a message ... UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK) ...`
   - Conclusion: client received valid responses.

6. Command: `rg -n -m 5 "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `someip_service::common: ServiceResponseListener: Received a message ...`
     - `someip_service::common: Sending Response message:`
   - Conclusion: service handled requests and responded.

7. Command: `rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT_DIR/streamer.log" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `(no matches)`
   - Conclusion: no critical streamer route/setup errors.

8. Command: `kill ... && pgrep -fa "zenoh_someip|zenoh_client|someip_service" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - no lingering scenario process beyond `pgrep` self line
   - Conclusion: teardown clean.

## Pass/Fail Decision

- Client response evidence: PASS
- Service request/response evidence: PASS
- Critical streamer-error check: PASS
- Final verdict: PASS
