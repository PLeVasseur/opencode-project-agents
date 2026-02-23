## CI parity results

Date: 2026-02-09
Branch: `bugfix/issue-74-left-topic-authority`

### Environment prep

- `source build/envsetup.sh highest` -> success
- Exported by script:
  - `GENERIC_CPP_STDLIB_PATH=/usr/include/c++/14`
  - `ARCH_SPECIFIC_CPP_STDLIB_PATH=/usr/include/x86_64-linux-gnu/c++/14`

### Base matrix (no transport features)

- `cargo build` -> pass
- `cargo clippy --all-targets -- -W warnings -D warnings` -> pass
- `cargo fmt -- --check` -> pass (after running `cargo fmt` once to apply formatting)

### Bundled feature matrix

- `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport` -> pass
- `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings` -> pass

### Unbundled feature matrix

- `VSOMEIP_INSTALL_PATH` was not set in this environment (`printenv VSOMEIP_INSTALL_PATH` returned empty).
- No usable local unbundled vsomeip install tree was available to point `VSOMEIP_INSTALL_PATH` at.
- Per plan requirement, unbundled matrix commands were **skipped** with explicit reason:
  - skipped `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
  - skipped `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`

### Workspace sanity

- `cargo check --workspace --all-targets` -> pass
- `cargo test --workspace` -> pass
