---
name: transport-smoke-validation
description: Execute and assess canonical Zenoh<->SOME/IP and Zenoh<->MQTT5 request/response smoke validations.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: transport-validation
---

## When to use

Use this skill for transport migration work, forwarding/routing behavior changes, or CI regressions involving transports.

## Per-scenario skills (binaries fixed to one smoke test each)

Use these targeted skills when you need one exact binary pairing per run:

- `smoke-zenoh-someip-rr-someip-client-zenoh-service`
- `smoke-zenoh-someip-rr-zenoh-client-someip-service`
- `smoke-zenoh-someip-ps-someip-publisher-zenoh-subscriber`
- `smoke-zenoh-someip-ps-zenoh-publisher-someip-subscriber`
- `smoke-zenoh-mqtt-rr-mqtt-client-zenoh-service`
- `smoke-zenoh-mqtt-rr-zenoh-client-mqtt-service`
- `smoke-zenoh-mqtt-ps-mqtt-publisher-zenoh-subscriber`
- `smoke-zenoh-mqtt-ps-zenoh-publisher-mqtt-subscriber`

Each targeted skill includes build, launch order, validation regexes, and teardown commands.

## Scenario A: Zenoh <-> SOME/IP

1. Setup:
   - `source build/envsetup.sh highest`
   - Include bundled vsomeip libs in `LD_LIBRARY_PATH` when needed.
2. Start streamer from `example-streamer-implementations` with `zenoh_someip`.
3. Start `zenoh_service` and then run `someip_client`.
4. Pass criteria:
   - No repeating `Routing info for remote service could not be found`
   - `UMESSAGE_TYPE_RESPONSE` seen with `commstatus: Some(OK)`

## Scenario B: Zenoh <-> MQTT5

1. Start broker: `utils/mosquitto/docker-compose.yaml`.
2. Start `configurable-streamer` with `CONFIG.json5`.
3. Start `zenoh_service`, then run `mqtt_client` (or inverse pairing).
4. Router mode caveat:
   - In `configurable-streamer/ZENOH_CONFIG.json5`, use `listen.endpoints` for local router setup.
5. Pass criteria:
   - Stable continuous request/response
   - No transport-level failures in streamer/entity logs

## Logging profile

- `RUST_LOG="up_transport_vsomeip=trace,up_streamer=debug,up_linux_streamer=debug,example_streamer_uses=debug"`

## Report template

Always include:

1. Commands executed
2. Relevant environment variables
3. Key counters/evidence from logs
4. Pass/fail against each criterion
5. Follow-up actions if any criterion is not met
