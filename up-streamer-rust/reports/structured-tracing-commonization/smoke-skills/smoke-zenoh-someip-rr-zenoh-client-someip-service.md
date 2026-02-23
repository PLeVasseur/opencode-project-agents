# smoke-zenoh-someip-rr-zenoh-client-someip-service

## Result

- Status: PASS

## Evidence

- Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_client --features zenoh-transport && cargo build -p example-streamer-uses --bin someip_service --features "vsomeip-transport,bundled-vsomeip"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)` for all binaries
- Conclusion: binaries compiled.

- Command: `source ../build/envsetup.sh highest; export LD_LIBRARY_PATH="$(ls -d ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"; export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"; cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$ART/streamer.log" 2>&1 & echo $! > "$ART/streamer.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: 0 (pass)
- Key output lines:
  - streamer initialized without panic/signature errors
- Conclusion: zenoh_someip streamer started.

- Command: `source build/envsetup.sh highest; export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"; RUST_LOG=info cargo run -p example-streamer-uses --bin someip_service --features "vsomeip-transport,bundled-vsomeip" > "$ART/service.log" 2>&1 & echo $! > "$ART/service.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `ServiceResponseListener: Received a message`
- Conclusion: SOME/IP service handled requests.

- Command: `source build/envsetup.sh highest && export RUST_LOG="info,example_streamer_uses=debug" && timeout 45s cargo run -p example-streamer-uses --bin zenoh_client --features zenoh-transport > "$ART/client.log" 2>&1; printf '%s\n' "$?" > "$ART/client.exit"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass), workload exit code recorded as `124` (expected timeout-bounded run)
- Key output lines:
  - `ServiceResponseListener: Received a message: ... UMESSAGE_TYPE_RESPONSE ... commstatus: Some(OK)`
- Conclusion: client received valid response traffic.

## Structured logging assertions

- Command: `rg -n -m 1 "egress_send_attempt.*worker_id|worker_id.*egress_send_attempt" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_attempt" ... worker_id="019c4904-7f89-73d8-8e14-da16ca4e30c5"`

- Command: `rg -n -m 1 "egress_send_ok.*worker_id|worker_id.*egress_send_ok" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_ok" ... worker_id="019c4904-7f89-73d8-8e14-da16ca4e30c5"`

- Command: `rg -n -m 1 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_worker_create" ... route_label="[in.name: host_endpoint, in.authority: \"authority-b\" ; out.name: someip_endpoint, out.authority: \"authority-a\"]"`

- Command: `rg -n -m 1 "egress_recv_lagged|egress_recv_closed" "$ART/streamer.log"`
- Exit status: 1 (not observed)
- Key output lines:
  - none
- Conclusion: lag/closed events not observed in bounded healthy run.

- Command: `rg -n -m 1 "Routing info for remote service could not be found|Static subscription file not found|panicked" "$ART/streamer.log"`
- Exit status: 1 (pass for negative check)
- Key output lines:
  - none
- Conclusion: no critical SOME/IP route/setup errors observed.

## Teardown

- Command: `kill -INT ...; kill -TERM ...; pkill ...`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - no matching processes after cleanup
- Conclusion: scenario cleaned up.
