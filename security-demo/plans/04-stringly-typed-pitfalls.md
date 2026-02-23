# Plan: Section 4 - Stringly-Typed API Pitfalls

## Purpose

Demonstrate logic bugs and OS interface hazards that are not prevented by Rust
memory safety alone.

## Preconditions

- Run from the repo root `security-demo`.

## Steps and Expected Results

### 4a. TOCTOU race condition

Terminal 1:

```bash
cd 04-toctou
cargo run
```

Terminal 2 (during the 5-second countdown):

```bash
touch /tmp/toctou_demo.txt
```

Expected in Terminal 1:

- File creation fails with `File exists`.
- Output includes `RACE CONDITION DEMONSTRATED`.

### 4b. Safe Rust accessing dangerous resources

```bash
cd ../05-proc-self-mem
cargo run
```

Expected:

- `/proc/self/mem` opens for reading and writing.
- Output warns that writing would corrupt process memory.

## Gotchas / Prereqs (from docs)

- After verification, remove `/tmp/toctou_demo.txt` as part of reset.

## Fix Note

If the race or `/proc/self/mem` output does not appear, fix the demo so the
intended Rust security issue is still demonstrated.
