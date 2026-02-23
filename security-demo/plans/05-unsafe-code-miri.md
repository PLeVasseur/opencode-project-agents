# Plan: Section 5 - Unsafe Code and Miri

## Purpose

Show undefined behavior in unsafe Rust and how tools detect it.

## Preconditions

- Run from the repo root `security-demo`.
- Nightly toolchain and Miri are installed.
- Clippy is installed.

## Steps and Expected Results

### 5a. Undefined behavior examples (normal run)

```bash
cd 06-unsafe-miri
cargo +stable run 2>/dev/null || cargo run
```

Expected:

- Program runs and prints a "Read uninitialized value" line.

### 5b. Miri catches UB

```bash
cargo miri run
```

Expected:

- Miri aborts with `Undefined Behavior` and mentions uninitialized data.

### 5c. Clippy lints for unsafe

```bash
cd ../07-clippy-unsafe
cargo clippy
```

Expected:

- Clippy reports lint errors for unsafe code practices.

To show the specific lint failures, remove the allow attributes and re-run:

```bash
sed -i 's/#\[allow(clippy::undocumented_unsafe_blocks)\]//' src/main.rs
sed -i 's/#\[allow(clippy::unsafe_op_in_unsafe_fn)\]//' src/main.rs
cargo clippy
```

Expected:

- `unsafe block missing a safety comment`.
- `unsafe operation in unsafe fn body`.

Restore the file after verification:

```bash
git checkout src/main.rs
```

## Gotchas / Prereqs (from docs)

- If Miri fails, install nightly and the Miri component:
  `rustup toolchain install nightly` and `rustup +nightly component add miri`.
- If Clippy is missing, run `rustup component add clippy`.

## Fix Note

If the UB or lint errors do not appear, fix the demo or toolchain so the unsafe
code issues are still demonstrated.
