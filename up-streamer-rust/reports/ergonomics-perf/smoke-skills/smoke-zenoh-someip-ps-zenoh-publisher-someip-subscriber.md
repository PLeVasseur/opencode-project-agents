# Smoke Skill Report: smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest && cargo build -p up-linux-streamer --bin zenoh_someip --features "zenoh-transport,vsomeip-transport,bundled-vsomeip" && cargo build -p example-streamer-uses --bin zenoh_publisher --features zenoh-transport && cargo build -p example-streamer-uses --bin someip_subscriber --features "vsomeip-transport,bundled-vsomeip"`
- Exit status: 0 (pass)
- Key output:
  - `Finished 'dev' profile ... up-linux-streamer`
  - `Finished 'dev' profile ... zenoh_publisher`
  - `Finished 'dev' profile ... someip_subscriber`
- Conclusion: Scenario binaries built successfully.

2) Command: launch streamer + subscriber with SOME/IP runtime libs exported
- Streamer command (working directory `example-streamer-implementations`): `../target/debug/zenoh_someip --config "DEFAULT_CONFIG.json5" > .../streamer.log 2>&1 &`
- Subscriber command (repo root): `target/debug/someip_subscriber --uauthority authority-a --uentity 0x5678 --uversion 0x1 --resource 0x0 --source-authority authority-b --source-uentity 0x3039 --source-uversion 0x1 --source-resource 0x8001 --remote-authority authority-b --vsomeip-config example-streamer-uses/vsomeip-configs/someip_client.json > .../subscriber.log 2>&1 &`
- Exit status: 0 (pass)
- Key output:
  - both processes started and logs populated
- Conclusion: Streamer and subscriber were active for pub/sub validation.

3) Command: `source build/envsetup.sh highest && timeout 45s target/debug/zenoh_publisher > .../publisher.log 2>&1; printf '%s\n' "$?" > .../publisher.exit`
- Exit status: 0 (command), publisher exit file: `124`
- Key output:
  - `publisher.exit` captured `124` (expected timeout window)
- Conclusion: Publisher generated traffic during validation window.

4) Command: validation checks
- `rg -n -m 3 "Sending Publish message" .../publisher.log`
- `rg -n -m 3 "PublishReceiver: Received a message" .../subscriber.log`
- `rg -n -m 3 "Sending on out_transport succeeded" .../streamer.log`
- Exit status: 0 (all pass)
- Key output:
  - Publisher: `Sending Publish message:`
  - Subscriber: `someip_subscriber::common: PublishReceiver: Received a message`
  - Streamer: `EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
- Conclusion: Zenoh publish traffic was forwarded through streamer and received by SOME/IP subscriber.

5) Command: teardown
- `kill -INT <subscriber-pid> <streamer-pid> || true`
- `kill -TERM <subscriber-pid> <streamer-pid> || true`
- `pkill -9 -f "target/debug/someip_subscriber ..." || true`
- `pkill -9 -f "target/debug/zenoh_someip --config DEFAULT_CONFIG.json5" || true`
- Exit status: 0 (pass)
- Key output:
  - final `pgrep -fa "zenoh_someip|someip_subscriber"` returned no matches
- Conclusion: Scenario cleaned up; one force-stop remediation was needed due pid files capturing shell-wrapper pids.

## Result

PASS - Required publisher/subscriber/streamer forwarding evidence matched.
