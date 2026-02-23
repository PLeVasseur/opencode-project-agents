# Plan: Section 3 - Security Tooling

## Purpose

Demonstrate automated tooling that detects vulnerabilities and enforces policy.

## Preconditions

- `cargo-audit` and `cargo-deny` are installed.
- Run from the repo root `security-demo`.

## Steps and Expected Results

### 3a. cargo audit

```bash
cd 02-vulnerable-deps
cargo audit
```

Expected:

- Output includes `RUSTSEC-2020-0071` for the `time` crate.
- The command exits with a non-zero status due to vulnerabilities.

### 3b. cargo deny

```bash
cd ../03-cargo-deny
cargo deny check
```

Expected:

- Output includes `RUSTSEC-2020-0071` for `time 0.1.45`.
- The advisories check fails (`advisories FAILED`).

### 3c. (Optional) cargo vet

```bash
cargo vet init
cargo vet
cat supply-chain/config.toml
```

Expected:

- `cargo vet` initializes and reports its status.
- A `supply-chain/config.toml` file is created and can be displayed.

## Gotchas / Prereqs (from docs)

- If `cargo audit` fails, install it via `cargo install cargo-audit` and ensure
  network access to fetch the advisory database.
- If `cargo deny` fails, install it via `cargo install cargo-deny`. First run
  may need `cargo deny fetch`.

## Fix Note

If expected vulnerabilities are not detected, fix the tooling setup or demo
configuration so the vulnerability detection is still shown.
