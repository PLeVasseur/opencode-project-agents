# up-rust 0.9 transport upgrade validation

## Target matrix

- `up-rust = 0.9.x`
- `up-transport-zenoh = 0.9.0`
- `up-transport-mqtt5 = 0.4.0`
- `up-transport-vsomeip` pinned to git rev `278ab26415559d6cb61f40facd21de822032cc83`
- Workspace MSRV: Rust `1.88`

## Workspace validation

Commands:

```bash
cargo check --workspace --all-targets
cargo test --workspace
```

Result: pass.

## Canonical smoke A: Zenoh <-> SOME/IP request/response

Setup:

- `source build/envsetup.sh highest`
- Include bundled vsomeip libs in `LD_LIBRARY_PATH`
- Run streamer from `example-streamer-implementations`

Observed sample:

- `routing_miss_count=0`
- `response_count=38`
- `ok_commstatus_count=38`

Pass criteria met.

## Canonical smoke B: Zenoh <-> MQTT5 request/response

Setup:

- Start broker from `utils/mosquitto/docker-compose.yaml`
- Run streamer from `configurable-streamer` with `CONFIG.json5`

Observed sample:

- `request_count=33`
- `response_count=33`
- No transport-level failures in streamer/entity logs

Pass criteria met.

## Follow-up

Replace `up-transport-vsomeip` git pin with the crates.io release when a version with `up-rust 0.9` support is published.
