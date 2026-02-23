# Smoke Skill Report: smoke-zenoh-someip-rr-someip-client-zenoh-service

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... up-linux-streamer`
  - `Finished 'dev' profile ... someip_client`
  - `Finished 'dev' profile ... zenoh_service`
- Conclusion: Scenario binaries built successfully.

2) Streamer startup command:
- Working directory: `example-streamer-implementations`
- Command: `../target/debug/zenoh_someip --config DEFAULT_CONFIG.json5 > .../streamer.log 2>&1 &`
- Env: `LD_LIBRARY_PATH=<bundled-vsomeip-lib>:$LD_LIBRARY_PATH`, `RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`
- Exit status: 0 (pass)
- Key output:
  - `UStreamer::...::add_route(): Adding route ...`
- Conclusion: Streamer started cleanly with expected route setup.

3) Service and client commands:
- Service: `RUST_LOG=info target/debug/zenoh_service > .../service.log 2>&1 &`
- Client: `timeout 45s target/debug/someip_client > .../client.log 2>&1; echo $? > .../client.exit`
- Exit status: 0 (commands), client exit file: `124`
- Key output:
  - `client.exit` captured `124` (expected timeout window)
- Conclusion: Request/response traffic window executed.

4) Validation checks:
- `rg -n -m 3 "UMESSAGE_TYPE_RESPONSE|commstatus: Some\(OK\)" .../client.log`
- `rg -n -m 3 "ServiceResponseListener: Received a message|Sending Response message" .../service.log`
- `if rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" .../streamer.log; then ...; else ...; fi`
- Exit status: 0 (all pass)
- Key output:
  - Client: `UMESSAGE_TYPE_RESPONSE` and `commstatus: Some(OK)`
  - Service: `ServiceResponseListener: Received a message` and `Sending Response message`
  - Streamer: `CRITICAL_STREAMER_ERROR=none`
- Conclusion: End-to-end RR forwarding succeeded with no critical streamer routing/setup errors.

5) Teardown:
- Commands:
  - `kill -INT <service-pid> <streamer-pid> || true`
  - `pkill -9 -f "zenoh_someip|someip_client|zenoh_service" || true`
- Exit status: 0 (pass)
- Key output:
  - no remaining `zenoh_someip|someip_client|zenoh_service` processes
- Conclusion: Scenario cleaned up.

## Result

PASS - Required RR response evidence and streamer health criteria matched.
