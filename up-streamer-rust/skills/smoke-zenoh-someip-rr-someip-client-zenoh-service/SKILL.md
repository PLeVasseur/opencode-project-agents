---
name: smoke-zenoh-someip-rr-someip-client-zenoh-service
description: Validate SOME/IP client to Zenoh service request/response through the zenoh_someip streamer.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: smoke-zenoh-someip-rr
---

## Scope

Run and validate this binary triad:

- Streamer: `up-linux-streamer` bin `zenoh_someip`
- Client: `example-streamer-uses` bin `someip_client`
- Service: `example-streamer-uses` bin `zenoh_service`

## Execution

1. Setup from repo root:
   - `source build/envsetup.sh highest`
   - `export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-rr-someip-client-zenoh-service"`
   - `mkdir -p "$REPORT_DIR"`
   - `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
2. Build binaries:
   - `cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
   - `cargo build -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip"`
   - `cargo build -p example-streamer-uses --bin zenoh_service --features zenoh-transport`
3. Start streamer from `example-streamer-implementations`:
   - `source ../build/envsetup.sh highest`
   - `export LD_LIBRARY_PATH="$(ls -d ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
   - `export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`
   - `cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & echo $! > "$REPORT_DIR/streamer.pid"`
4. Start service from repo root:
   - `source build/envsetup.sh highest`
   - `RUST_LOG=info cargo run -p example-streamer-uses --bin zenoh_service --features zenoh-transport > "$REPORT_DIR/service.log" 2>&1 & echo $! > "$REPORT_DIR/service.pid"`
5. Run client from repo root:
   - `source build/envsetup.sh highest`
   - `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
   - `export RUST_LOG="info,up_transport_vsomeip=trace,example_streamer_uses=debug"`
   - `timeout 45s cargo run -p example-streamer-uses --bin someip_client --features "vsomeip-transport,bundled-vsomeip" > "$REPORT_DIR/client.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/client.exit"`

## Validation

- Client saw responses: `rg -n "UMESSAGE_TYPE_RESPONSE|commstatus: Some\(OK\)" "$REPORT_DIR/client.log"`
- Service handled requests: `rg -n "ServiceResponseListener: Received a message|Sending Response message" "$REPORT_DIR/service.log"`
- Streamer has no critical route/setup error: `rg -n "Routing info for remote service could not be found|Static subscription file not found|panicked" "$REPORT_DIR/streamer.log"`

Pass only when first two checks match and the third check returns no matches.

## Teardown

- `kill -INT "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- If still alive: `kill -TERM "$(cat "$REPORT_DIR/service.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- Verify: `pgrep -fa "zenoh_someip|zenoh_service|someip_client" || true`
