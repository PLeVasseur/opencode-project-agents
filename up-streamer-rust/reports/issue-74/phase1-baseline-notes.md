# Phase 1 Baseline Reproduction Notes

Date: 2026-02-08

## Bootstrap confirmation

- Plan source: `$OPENCODE_CONFIG_DIR/plans/issue-74-pubsub-subscription-mapping-debug-plan.md`
- Issue context fetched: `gh issue view 74 --repo eclipse-uprotocol/up-streamer-rust --json number,title,body,state,url`
- Branch: `bugfix/issue-74-left-topic-authority`
- Hotspot files had no local edits before work:
  - `up-streamer/src/ustreamer.rs`
  - `subscription-cache/src/lib.rs`
  - `utils/usubscription-static-file/src/lib.rs`

## Baseline reproduction setup (pre-fix)

Artifacts created under `$OPENCODE_CONFIG_DIR/reports/issue-74/`:

- `CONFIG.baseline.json5`
- `subscription_data.baseline.json`
- `baseline_streamer.log`
- `baseline_mqtt_subscriber.log`
- `baseline_zenoh_publisher.log`

Subscription mapping intentionally used only left authority `authority-a`:

```json
{
  "//authority-a/3039/1/8001": ["//authority-a/5678/1/1234"]
}
```

Runtime command sequence:

```bash
docker compose -f utils/mosquitto/docker-compose.yaml up -d
RUST_LOG="up_streamer=debug,configurable_streamer=debug" target/debug/configurable-streamer --config "$OPENCODE_CONFIG_DIR/reports/issue-74/CONFIG.baseline.json5"
RUST_LOG=info target/debug/mqtt_subscriber
RUST_LOG=info target/debug/zenoh_publisher
```

## Baseline evidence

- Streamer registered a publish listener using in-authority `authority-b` even though the subscription map topic authority was `authority-a`.
  - See `baseline_streamer.log` line with:
    - `in authority: authority-b, out authority: authority-a, source URI filter: ... authority_name: "authority-b"`
- Subscriber received publish messages from `authority-b` repeatedly.
  - See `baseline_mqtt_subscriber.log` repeated lines:
    - `PublishReceiver: Received a message ... source ... authority_name: "authority-b"`

This confirms left-side/topic authority in the subscription mapping is not enforced in publish forwarding prior to the fix.
