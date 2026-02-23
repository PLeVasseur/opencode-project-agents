# Smoke Skill Report: smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin someip_publisher --features "vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_subscriber --features zenoh-transport`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... up-linux-streamer`
  - `Finished 'dev' profile ... someip_publisher`
  - `Finished 'dev' profile ... zenoh_subscriber`
- Conclusion: Scenario binaries built successfully.

2) Initial startup issue:
- Command pattern: `source ../build/envsetup.sh highest && ... ../target/debug/zenoh_someip --config DEFAULT_CONFIG.json5 ...`
- Exit status: non-zero on first attempt
- Key output:
  - `/bin/bash: line 1: /streamer.pid: Permission denied`
  - a prior run also showed `Unable to initialize Zenoh UTransport` panic in streamer log
- Conclusion: Initial process wrapper/pid handling was unreliable; scenario was reset and rerun cleanly.

3) Remediated streamer launch:
- Command (working directory `example-streamer-implementations`): `../target/debug/zenoh_someip --config DEFAULT_CONFIG.json5 > .../streamer.log 2>&1 &`
- Env: `LD_LIBRARY_PATH=<bundled-vsomeip-lib>:$LD_LIBRARY_PATH`, `RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`
- Exit status: 0 (pass)
- Key output:
  - `UStreamer::up-streamer::UStreamer::new(): UStreamer created`
  - `UStreamer::...::add_route(): Adding route ...`
- Conclusion: Streamer started cleanly and route setup succeeded.

4) Subscriber + publisher commands:
- Subscriber: `RUST_LOG=info timeout 70s target/debug/zenoh_subscriber --uauthority authority-b --uentity 0x5678 --uversion 0x1 --resource 0x1234 --source-authority authority-a --source-uentity 0x5BA0 --source-uversion 0x1 --source-resource 0x8001 > .../subscriber.log 2>&1 &`
- Publisher: `timeout 45s target/debug/someip_publisher > .../publisher.log 2>&1; echo $? > .../publisher.exit`
- Exit status: 0 (commands), publisher exit file: `124`
- Key output:
  - `publisher.exit` captured `124` (expected timeout window)
- Conclusion: Publisher generated traffic during subscriber active window.

5) Validation checks:
- `rg -n -m 3 "Sending Publish message" .../publisher.log`
- `rg -n -m 3 "PublishReceiver: Received a message" .../subscriber.log`
- `rg -n -m 3 "Sending on out_transport succeeded" .../streamer.log`
- Exit status: 0 (all pass)
- Key output:
  - Publisher: `someip_publisher: Sending Publish message:`
  - Subscriber: `zenoh_subscriber::common: PublishReceiver: Received a message`
  - Streamer: `EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: SOME/IP publish traffic was forwarded through streamer and received by Zenoh subscriber.

6) Teardown:
- Commands:
  - `kill -INT <subscriber-pid> <streamer-pid> || true`
  - `pkill -9 -f "zenoh_someip|zenoh_subscriber|someip_publisher" || true`
- Exit status: 0 (pass)
- Key output:
  - no remaining `zenoh_someip|zenoh_subscriber|someip_publisher` processes
- Conclusion: Scenario cleaned up after validation.

## Result

PASS - Required publisher/subscriber/streamer forwarding evidence matched.
