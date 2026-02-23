Execute the migration plan at:

`plans/up-rust-0.9-transport-upgrade-plan.md`

You appear to have blown the context window last time. Be careful. You were part way complete. Ensure you complete the entire plan.

Execution requirements:

1. Follow phases in order and update the plan file as you work.
2. Tick each task checkbox from `[ ]` to `[x]` immediately after completing it.
3. Keep all work in one branch and open a single PR.
4. Use logical commits exactly aligned to the plan's commit chunks.
5. Do not squash commits locally.

Technical targets:

- Rust MSRV `1.88`
- `up-rust = 0.9.x`
- `up-transport-zenoh = 0.9.0`
- `up-transport-mqtt5 = 0.4.0`
- `up-transport-vsomeip` pinned to git rev `278ab26415559d6cb61f40facd21de822032cc83` until crates.io release catches up

Implementation notes:

- Migrate zenoh transport usage to the `up-transport-zenoh 0.9` builder API.
- Update lockfile and any impacted docs.
- Preserve existing behavior wherever possible.

Validation requirements:

- Run workspace compile/test checks.
- Run canonical smoke test A (Zenoh <-> SOME/IP request/response) per project AGENTS guidance.
- Run canonical smoke test B (Zenoh <-> MQTT5 request/response) per project AGENTS guidance.
- Capture commands and key results for the PR description.

Final deliverables to return at the end of execution:

1. Final commit list (hash + subject).
2. PR URL.
3. Validation summary.
4. Explicit follow-up note to replace vsomeip git pin with crates.io release when available.
