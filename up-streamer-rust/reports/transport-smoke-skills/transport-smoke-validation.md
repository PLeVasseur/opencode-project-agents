# Smoke Report: transport-smoke-validation

## Result

- Status: PASS
- Scope: Canonical transport smoke coverage across Zenoh<->MQTT and Zenoh<->SOME/IP pairs
- Scenario reports:
  - `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber.md`
  - `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber.md`
  - `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service.md`
  - `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service.md`
  - `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber.md`
  - `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber.md`
  - `smoke-zenoh-someip-rr-zenoh-client-someip-service.md`
  - `smoke-zenoh-someip-rr-someip-client-zenoh-service.md`

## Prerequisite Evidence

1. Command: `source build/envsetup.sh highest`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Set GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
     - `Set ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`
   - Conclusion: expected env bootstrap applied.

2. Command: `docker compose -f utils/mosquitto/docker-compose.yaml up -d`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `Container mosquitto-mosquitto-1  Started`
   - Conclusion: MQTT broker prerequisite available for MQTT smoke scenarios.

3. Command: `ls /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/target/debug/build/vsomeip-sys-196dbe50abf320ee/out/vsomeip/vsomeip-install/lib`
   - Working directory: repo root
   - Exit status: 0 (pass)
   - Key output:
     - `libvsomeip3.so`
     - `libvsomeip3-sd.so`
     - `libvsomeip3-cfg.so`
   - Conclusion: SOME/IP runtime libraries available for LD_LIBRARY_PATH.

## Aggregate Outcomes

- MQTT pub/sub (Zenoh->MQTT): PASS
- MQTT pub/sub (MQTT->Zenoh): PASS
- MQTT request/response (Zenoh client->MQTT service): PASS
- MQTT request/response (MQTT client->Zenoh service): PASS
- SOME/IP pub/sub (Zenoh->SOME/IP): PASS
- SOME/IP pub/sub (SOME/IP->Zenoh): PASS
- SOME/IP request/response (Zenoh client->SOME/IP service): PASS
- SOME/IP request/response (SOME/IP client->Zenoh service): PASS

## Conclusion

Mandatory smoke matrix executed successfully. All required scenario skill reports are present and passed with command/log evidence.
