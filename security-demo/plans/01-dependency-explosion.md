# Plan: Section 1 - Dependency Explosion

## Purpose

Demonstrate how adding a single dependency dramatically increases the
transitive dependency graph.

## Preconditions

- Run from the repo root `security-demo`.

## Steps and Expected Results

1. Confirm the starting state.

```bash
cd 01-dependency-explosion
cat Cargo.toml
cargo tree 2>/dev/null | wc -l
```

Expected:

- `Cargo.toml` has no dependencies (only `[package]` and `[dependencies]`).
- Dependency count is `1` (just the root package).

2. Add a popular crate and show the explosion.

```bash
cargo add reqwest
cargo tree | wc -l
cargo tree | head -50
cargo tree --depth 1
```

Expected:

- `reqwest` appears in `Cargo.toml`.
- Dependency count jumps to roughly 150-200 lines (per the guide).
- The tree shows many transitive crates.

3. Reset to the pre-demo state (per DEMO_GUIDE Section 6).

```bash
cat > Cargo.toml << 'EOF'
[package]
name = "dependency-explosion"
version = "0.1.0"
edition = "2021"
license = "MIT OR Apache-2.0"

[dependencies]
# Start with nothing - we'll add reqwest during the demo
EOF
rm -f Cargo.lock
cargo generate-lockfile
```

Expected:

- `Cargo.toml` is back to the empty dependency state.
- A fresh `Cargo.lock` is generated.

## Gotchas / Prereqs (from docs)

- None beyond a working Rust toolchain.

## Fix Note

If any expected output is missing, fix the demo so it still showcases the
dependency explosion. Do not proceed until it matches the documented result.
