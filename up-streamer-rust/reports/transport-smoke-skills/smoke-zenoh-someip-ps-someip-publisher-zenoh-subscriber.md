# Smoke Report: smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber

## Result

- Status: PASS
- Scope: SOME/IP publisher -> zenoh_someip streamer -> Zenoh subscriber (pub/sub)
- Log directory: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`

## Command Evidence

1. Command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="...vsomeip-install/lib" && cargo build ...`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Finished 'dev' profile ...`
   - Conclusion: required binaries built.

2. Command: `source ../build/envsetup.sh highest && ... cargo run --bin zenoh_someip ... &`
   - Working directory: `example-streamer-implementations`
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: streamer launched.

3. Command: `source build/envsetup.sh highest && ... cargo run -p example-streamer-uses --bin zenoh_subscriber ... &`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: Zenoh subscriber launched.

4. Command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="..." && timeout 45s cargo run -p example-streamer-uses --bin someip_publisher ...`
   - Working directory: repo root
   - Exit status: 0 (pass command wrapper)
   - Key output:
     - publisher exit file: `124`
   - Conclusion: SOME/IP publisher ran in bounded window.

5. Command: `rg -n -m 5 "Sending Publish message" "$REPORT_DIR/publisher.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `someip_publisher: Sending Publish message:`
   - Conclusion: publisher emitted traffic.

6. Command: `rg -n -m 5 "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `zenoh_subscriber::common: PublishReceiver: Received a message ...`
   - Conclusion: subscriber observed forwarded messages.

7. Command: `rg -n -m 5 "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
   - Conclusion: streamer forwarding confirmed.

8. Command: `kill ... && pgrep -fa "zenoh_someip|zenoh_subscriber|someip_publisher" || true`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - no lingering scenario process beyond `pgrep` self line
   - Conclusion: teardown clean.

## Pass/Fail Decision

- Publisher emitted traffic: PASS
- Subscriber received traffic: PASS
- Streamer forwarded traffic: PASS
- Final verdict: PASS
