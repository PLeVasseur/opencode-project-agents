# smoke-zenoh-someip-rr-someip-client-zenoh-service

## Result

- Status: PASS

## Evidence

- Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)` for all binaries
- Conclusion: scenario binaries compiled.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; source ../build/envsetup.sh highest && libdirs=(../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test -d "${libdirs[0]}" && export LD_LIBRARY_PATH="$(realpath "${libdirs[0]}"):${LD_LIBRARY_PATH}" && export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug" && cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$ART/streamer.log" 2>&1 & printf '%s\n' "$!" > "$ART/streamer.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: 0 (pass)
- Key output lines:
  - `Running .../target/debug/zenoh_someip --config DEFAULT_CONFIG.json5`
- Conclusion: streamer started for SOME/IP <-> Zenoh RR forwarding.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$ART/service.log" 2>&1 & printf '%s\n' "$!" > "$ART/service.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Running target/debug/zenoh_service`
  - `ServiceResponseListener: Received a message`
- Conclusion: service started and handled requests.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; source build/envsetup.sh highest && libdirs=("$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib) && test -d "${libdirs[0]}" && export LD_LIBRARY_PATH="${libdirs[0]}:${LD_LIBRARY_PATH}" && export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" > "$ART/client.log" 2>&1; printf '%s\n' "$?" > "$ART/client.exit"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass), workload exit code recorded as `124` (expected timeout-bounded run)
- Key output lines:
  - `Running target/debug/someip_client`
  - `UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK)`
- Conclusion: client received continuous request/response traffic.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; rg -n -m 1 "Routing info for remote service could not be found|Static subscription file not found|panicked" "$ART/streamer.log"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 1 (pass for negative check)
- Key output lines:
  - none
- Conclusion: no critical SOME/IP route/setup errors observed.

## Structured logging assertions

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; rg -n -m 1 "egress_send_attempt.*worker_id|worker_id.*egress_send_attempt" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_attempt" ... worker_id="019c490c-7f3c-7f7e-8620-472d6f99cd0e"`
- Conclusion: attempt event includes `worker_id`.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; rg -n -m 1 "egress_send_ok.*worker_id|worker_id.*egress_send_ok" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_ok" ... worker_id="019c490c-7f3c-7f7e-8620-472d6f99cd0e"`
- Conclusion: success event includes `worker_id`.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; rg -n -m 1 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_worker_create" ... route_label="[in.name: host_endpoint, in.authority: \"authority-b\" ; out.name: someip_endpoint, out.authority: \"authority-a\"]"`
- Conclusion: worker-route correlation is grepable via `route_label`.

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; rg -n -m 1 "egress_recv_lagged|egress_recv_closed" "$ART/streamer.log"`
- Exit status: 1 (not observed)
- Key output lines:
  - none
- Conclusion: `egress_recv_lagged` / `egress_recv_closed` not observed in bounded healthy run.

## Teardown

- Command: `ART="$OPENCODE_CONFIG_DIR/reports/structured-tracing-commonization/smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service-artifacts"; kill -INT "$(cat "$ART/service.pid")" "$(cat "$ART/streamer.pid")" || true; kill -TERM "$(cat "$ART/service.pid")" "$(cat "$ART/streamer.pid")" || true; pkill -f "target/debug/(zenoh_someip|zenoh_service|someip_client)" || true`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `no matching processes after cleanup`
- Conclusion: scenario processes were fully stopped.
