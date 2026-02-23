# smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber

## Result

- Status: PASS

## Evidence

- Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin someip_publisher --features "vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `Finished 'dev' profile [unoptimized + debuginfo] target(s)` for all binaries
- Conclusion: binaries compiled.

- Command: `source ../build/envsetup.sh highest; export LD_LIBRARY_PATH="$(ls -d ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"; export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"; cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$ART/streamer.log" 2>&1 & echo $! > "$ART/streamer.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/example-streamer-implementations`
- Exit status: 0 (pass)
- Key output lines:
  - streamer logs include route setup and forwarding events
- Conclusion: streamer started.

- Command: `source build/envsetup.sh highest && RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport -- --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001 > "$ART/subscriber.log" 2>&1 & echo $! > "$ART/subscriber.pid"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - `PublishReceiver: Received a message`
- Conclusion: zenoh subscriber consumed forwarded publishes.

- Command: `source build/envsetup.sh highest; export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"; export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug"; timeout 45s cargo run -p example-streamer-uses --bin someip_publisher --features "vsomeip-transport,bundled-vsomeip" > "$ART/publisher.log" 2>&1; printf '%s\n' "$?" > "$ART/publisher.exit"`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass), workload exit code recorded as `124` (expected timeout-bounded run)
- Key output lines:
  - `Sending Publish message`
- Conclusion: SOME/IP publisher emitted traffic.

## Structured logging assertions

- Command: `rg -n -m 1 "egress_send_attempt.*worker_id|worker_id.*egress_send_attempt" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_attempt" ... worker_id="019c4901-d78f-712e-ac27-e88780a6a65e"`

- Command: `rg -n -m 1 "egress_send_ok.*worker_id|worker_id.*egress_send_ok" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_send_ok" ... worker_id="019c4901-d78f-712e-ac27-e88780a6a65e"`

- Command: `rg -n -m 1 "egress_worker_create.*route_label|egress_worker_reuse.*route_label" "$ART/streamer.log"`
- Exit status: 0 (pass)
- Key output line:
  - `event="egress_worker_create" ... route_label="[in.name: host_endpoint, in.authority: \"authority-b\" ; out.name: someip_endpoint, out.authority: \"authority-a\"]"`

- Command: `rg -n -m 1 "egress_recv_lagged|egress_recv_closed" "$ART/streamer.log"`
- Exit status: 1 (not observed)
- Key output lines:
  - none
- Conclusion: lag/closed events not observed in bounded healthy run.

## Teardown

- Command: `kill -INT ...; kill -TERM ...; pkill ...`
- Working directory: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
- Exit status: 0 (pass)
- Key output lines:
  - no matching processes after cleanup
- Conclusion: scenario cleaned up.
