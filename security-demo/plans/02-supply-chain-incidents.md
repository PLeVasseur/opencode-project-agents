# Plan: Section 2 - Real Supply Chain Incidents

## Purpose

Show real-world Rust ecosystem incidents that highlight supply chain risk.

## Preconditions

- Browser access to external URLs.

## Steps and Expected Results

1. Open the documented browser tabs.

- https://crates.io/crates/liblzma-sys/versions
- https://blog.rust-lang.org/2022/05/10/malicious-crate-rustdecimal/
- https://blog.rust-lang.org/2025/09/12/crates-io-phishing-campaign/
- https://rustsec.org/

Expected:

- liblzma-sys shows yanked versions for the XZ backdoor window.
- rustdecimal blog explains the typosquatting incident.
- phishing campaign blog explains credential theft risks.
- rustsec.org loads as the advisory database home.

## Gotchas / Prereqs (from docs)

- URLs must be reachable; the verification report notes they should be
  accessible.

## Fix Note

If any URL is inaccessible or content is missing, fix access (network, proxy,
or cached pages) so the incident can still be demonstrated.
