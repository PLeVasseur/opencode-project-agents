# Smoke Report: smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber

## Result

- Status: PASS
- Scope: Zenoh publisher -> zenoh_someip streamer -> SOME/IP subscriber (pub/sub)
- Log directory: `/home/pete.levasseur/opencode-project-agents/up-streamer-rust/reports/transport-smoke-skills/smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`

## Command Evidence

1. Command: `source build/envsetup.sh highest && export LD_LIBRARY_PATH="...vsomeip-install/lib" && cargo build ...`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Finished 'dev' profile ...`
   - Conclusion: SOME/IP binaries built with bundled vsomeip.

2. Command: `ls /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `libvsomeip3.so`
     - `libvsomeip3-sd.so`
   - Conclusion: runtime SOME/IP shared libraries available.

3. Command: `source ../build/envsetup.sh highest && ... cargo run --bin zenoh_someip ... &`
   - Working directory: `example-streamer-implementations`
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: zenoh_someip streamer launched.

4. Command: `source build/envsetup.sh highest && ... cargo run -p example-streamer-uses --bin someip_subscriber ... &`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - envsetup variables exported
   - Conclusion: SOME/IP subscriber launched.

5. Command: `source build/envsetup.sh highest && timeout 45s cargo run -p example-streamer-uses --bin zenoh_publisher ...`
   - Working directory: repo root
   - Exit status: 0 (pass command wrapper)
   - Key output:
     - publisher exit file: `124`
   - Conclusion: publisher exercised pub flow in bounded run.

6. Command: `rg -n -m 5 "Sending Publish message" "$REPORT_DIR/publisher.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Sending Publish message:`
   - Conclusion: publisher emitted publish traffic.

7. Command: `rg -n -m 5 "PublishReceiver: Received a message" "$REPORT_DIR/subscriber.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `someip_subscriber::common: PublishReceiver: Received a message ...`
   - Conclusion: SOME/IP subscriber received forwarded messages.

8. Command: `rg -n -m 5 "Sending on out_transport succeeded" "$REPORT_DIR/streamer.log"`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `... EgressRouteWorker::run_loop(): Sending on out_transport succeeded`
   - Conclusion: streamer forwarding confirmed.

9. Command: `kill ... && pgrep -fa "zenoh_someip|zenoh_publisher|someip_subscriber" || true`
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
