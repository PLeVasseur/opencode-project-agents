# Smoke Skill Report: transport-smoke-validation

Date: 2026-02-10

## Evidence

1) Command: `source build/envsetup.sh highest`
- Exit status: 0 (pass)
- Key output:
  - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
- Conclusion: Environment bootstrap completed for transport scenarios.

2) Command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
- Exit status: 0 (pass)
- Key output:
  - `Container mosquitto-mosquitto-1  Started`
- Conclusion: MQTT broker prerequisite was available for MQTT transport scenarios.

3) Command: `ls -d target/debug/build/vsomeip-sys-*/out/vsomeip/vsomeip-install/lib`
- Exit status: 0 (pass)
- Key output:
  - `.../target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
- Conclusion: SOME/IP runtime libraries were available and exported on `LD_LIBRARY_PATH` for SOME/IP scenarios.

4) Command: `rg -n "^## Result|^PASS" "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/smoke-skills"/*.md`
- Exit status: 0 (pass)
- Key output:
  - `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md ... PASS`
  - `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md ... PASS`
  - `smoke-zenoh-someip-rr-someip-client-zenoh-service.md ... PASS`
  - `smoke-zenoh-someip-rr-zenoh-client-someip-service.md ... PASS`
  - `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md ... PASS`
  - `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md ... PASS`
  - `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md ... PASS`
  - `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md ... PASS`
- Conclusion: All mandatory transport smoke scenario reports completed with PASS outcomes.

5) Command: scenario-specific log validations from each per-scenario report
- Exit status: 0 (pass)
- Key output:
  - RR scenarios show `UMESSAGE_TYPE_RESPONSE` and service request/response handling lines.
  - Pub/sub scenarios show `Sending Publish message`, `PublishReceiver: Received a message`, and streamer forward success lines.
- Conclusion: Canonical Zenoh<->MQTT and Zenoh<->SOME/IP forwarding paths validated end-to-end.

6) Command: teardown checks (`docker compose ... down`, `pkill/pgrep` per scenario)
- Exit status: 0 (pass)
- Key output:
  - broker networks removed after MQTT scenarios
  - no lingering streamer/entity processes after final cleanup
- Conclusion: Smoke execution left no active scenario processes.

## Result

PASS - Transport smoke validation skill criteria met across all mandatory scenario reports.
