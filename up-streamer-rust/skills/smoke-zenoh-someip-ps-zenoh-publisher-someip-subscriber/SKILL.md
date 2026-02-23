---
name: smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber
description: Validate Zenoh publisher to SOME/IP subscriber pub/sub forwarding through the zenoh_someip streamer.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: smoke-zenoh-someip-pubsub
---

## Scope

Run and validate this binary triad:

- Streamer: `up-linux-streamer` bin `zenoh_someip`
- Publisher: `example-streamer-uses` bin `zenoh_publisher`
- Subscriber: `example-streamer-uses` bin `someip_subscriber`

## Execution

1. Setup from repo root:
   - `source build/envsetup.sh highest`
   - `export REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/transport-smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber"`
   - `mkdir -p "$REPORT_DIR"`
   - `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
2. Build binaries:
   - `cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip"`
   - `cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport`
   - `cargo build -p example-streamer-uses --bin someip_subscriber --features "vsomeip-transport,bundled-vsomeip"`
3. Start streamer from `example-streamer-implementations`:
   - `source ../build/envsetup.sh highest`
   - `export LD_LIBRARY_PATH="$(ls -d ../target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
   - `export RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`
   - `cargo run --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" -- --config "DEFAULT_CONFIG.json5" > "$REPORT_DIR/streamer.log" 2>&1 & echo $! > "$REPORT_DIR/streamer.pid"`
4. Start subscriber from repo root (aligned with static subscription topic and SOME/IP local-URI requirements):
   - `source build/envsetup.sh highest`
   - `export LD_LIBRARY_PATH="$(ls -d "$PWD"/target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib | head -n1):${LD_LIBRARY_PATH}"`
   - `RUST_LOG=info cargo run -p example-streamer-uses --bin someip_subscriber --features "vsomeip-transport,bundled-vsomeip" -- --uauthority authority-a --uentity 0x5678 --uversion 0x1 --resource 0x0 --source-authority authority-b --source-uentity 0x3039 --source-uversion 0x1 --source-resource 0x8001 --remote-authority authority-b --vsomeip-config example-streamer-uses/vsomeip-configs/someip_client.json > "$REPORT_DIR/subscriber.log" 2>&1 & echo $! > "$REPORT_DIR/subscriber.pid"`
5. Run publisher from repo root:
   - `source build/envsetup.sh highest`
   - `export RUST_LOG="info,example_streamer_uses=debug"`
   - `timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport > "$REPORT_DIR/publisher.log" 2>&1; printf '%s\n' "$?" > "$REPORT_DIR/publisher.exit"`

## Validation

- Publisher emitted traffic: `rg -n "Sending Publish message" "$REPORT_DIR/publisher.log"`
- Subscriber received traffic: `rg -n "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
- Streamer forwarded traffic: `rg -n "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`

Pass only when all three checks match.

## Teardown

- `kill -INT "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- If still alive: `kill -TERM "$(cat "$REPORT_DIR/subscriber.pid")" "$(cat "$REPORT_DIR/streamer.pid")" || true`
- Verify: `pgrep -fa "zenoh_someip|zenoh_publisher|someip_subscriber" || true`
