# PR-32 Remediation Run Summary

- Date (UTC): 2026-02-13T20:49:27Z
- Repo: /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust
- Source branch: cleanup/refactor-upstream-main
- Base SHA (upstream/main): b6bc245ceaf2ae94b9272c3be86a2502c8fdac81
- Source SHA: 1ed5614e8850b32115a465356b92bf52c94e97f1

## Timeline

- phase1: initialized run artifacts and progress seed.
- phase1: created rollback refs `backup/pr-32-restack-20260213T204953Z` and `backup-pr-32-restack-20260213T204953Z` and verified on origin.
- rollback: If any step fails, `git switch cleanup/refactor-upstream-main && git reset --hard backup/pr-32-restack-20260213T204953Z`, then restart Phase 2.
- phase2: resolved rewrite branch `pr-32-restack-work`, reset to base, and captured pre-rewrite inventories (`pr-32-restack-pre-*.txt`).
- phase2: Commit 0 classification completed with Strategy A; source-file finalizable set is exactly 4 files and deferred inventory is recorded in `pr-32-commit0-deferred-files.txt`.
- phase3-setup: initialized overlap artifacts (`pr-32-overlap-*.txt`, `pr-32-overlap-audit.md`) and shared target cache `/tmp/pr32-shared-target`.
- c0 fb49056: PASS staged-scope + detached `cargo check --workspace --all-targets` + overlap(disallowed=0); tag `pr-32-restack-20260213T204927Z-c0`.
- c1 cd436ae: PASS staged-scope + detached `cargo check --workspace --all-targets` + overlap(disallowed=0); tag `pr-32-restack-20260213T204927Z-c1`.
- c2 dff00a3: FAIL detached gate `cargo check --workspace --all-targets` in `/tmp/pr32-c2-UcumPe`; key failures were unresolved `log` imports and async-constructor API mismatches in existing `up-streamer/tests/*` files. Remediation: rebuild c2 from c1 with required compile-safe test API churn included (mechanical old-test compatibility updates), then re-run c2 gates before advancing.
- c2 remediation: added explicit approved overlap exceptions for five legacy `up-streamer/tests/*` files in `pr-32-approved-source-overlap.txt` so commit 3 can finalize deterministic test refactors without violating overlap policy.
- c2 cbef885: PASS staged-scope + subscription-cache manifest-path check + detached `cargo check --workspace --all-targets` + overlap(disallowed=0); tag `pr-32-restack-20260213T204927Z-c2`.
- restart 2026-02-13T21:33:46Z: resume-mode recovery loaded `PROGRESS_FILE`/`SUMMARY_REPORT`; detected `HEAD=75610d5` vs `LAST_SHA=cbef885`; nearest checkpoint `pr-32-restack-20260213T204927Z-c2`; no in-flight rebase/cherry-pick/merge; continuing from consistent post-c2 state by validating existing c3 commit before further mutations.
- c3 75610d5: PASS commit-scope inspection + detached `cargo check --workspace --all-targets` + detached `cargo test --workspace` + overlap(disallowed=0, overlap=8); tag `pr-32-restack-20260213T204927Z-c3`.
- c4 bdb4151: PASS staged-scope + detached `cargo check -p criterion-guardrail --all-targets` + detached `cargo test -p criterion-guardrail --all-targets` + detached `cargo check -p up-streamer --benches` + overlap(disallowed=0, overlap=4); tag `pr-32-restack-20260213T204927Z-c4`.
- c5 ca9368e: PASS staged-scope + detached `cargo check --workspace --all-targets` + detached `cargo check -p transport-smoke-suite --all-targets` + detached `cargo test -p transport-smoke-suite --tests` + detached `cargo check -p example-streamer-uses --all-targets` (no-op due required-feature-gated bins only) + overlap(disallowed=0, overlap=3); tag `pr-32-restack-20260213T204927Z-c5`.
- phase3: completed c0..c5 reconstruction with checkpoint tags through `pr-32-restack-20260213T204927Z-c5`.
- overlap-final: disallowed overlap count is 0 across c0..c5; commit-file matrix recorded at `pr-32-commit-file-overlap-final.txt`.
- phase4: `git diff --stat SOURCE_SHA..HEAD` returned empty output (content identity preserved).
- phase4: commit body audit across c0..c5 shows all commits with non-empty bodies containing reviewer guidance.
- phase4: no standalone copyright/header-fixup commit detected in reconstructed stack.
- phase5 PR-A: PASS `source build/envsetup.sh highest && cargo build`, `cargo clippy --all-targets -- -W warnings -D warnings`, `cargo fmt -- --check`, and `cargo test --workspace`.
- phase5 PR-A bundled matrix: PASS `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport` and matching clippy command.
- phase5 PR-A unbundled matrix: SKIP (`VSOMEIP_INSTALL_PATH` is unset after `envsetup.sh highest`, so unbundled vsomeip install tree is unavailable in this environment).
- phase5 PR-B targeted: PASS `cargo check -p criterion-guardrail --all-targets`, `cargo test -p criterion-guardrail --all-targets`, and `cargo check -p up-streamer --benches`.
- phase5 PR-C targeted: PASS `cargo check --workspace --all-targets`, `cargo check -p transport-smoke-suite --all-targets`, `cargo test -p transport-smoke-suite --tests`, and `cargo check -p example-streamer-uses --all-targets` (no-op because all bins are required-feature gated).
- phase6: fork base verification PASS (`origin/main` == `BASE_SHA` == `b6bc245ceaf2ae94b9272c3be86a2502c8fdac81`).
- phase6: created/pushed stacked branches on origin only: `cleanup/refactor-upstream-main-prA-architecture` -> `75610d5`, `cleanup/refactor-upstream-main-prB-benchmark` -> `bdb4151`, `cleanup/refactor-upstream-main-prC-smoke` -> `8670bca` (cherry-pick of reconstructed `ca9368e` onto PR-A base).
- phase6: PR A https://github.com/PLeVasseur/up-streamer-rust/pull/33 (base `main`), PR B https://github.com/PLeVasseur/up-streamer-rust/pull/34 (base `cleanup/refactor-upstream-main-prA-architecture`), PR C https://github.com/PLeVasseur/up-streamer-rust/pull/35 (base `cleanup/refactor-upstream-main-prA-architecture`).
- phase6 stack proof: `PRA..PRB` contains only `bdb4151`; `PRA..PRC` contains only `8670bca`.
- R5 note: `SOURCE_SHA` does not contain `.gitattributes` linguist rules; remediation preserved exact source content identity, so fixture-collapsing `.gitattributes` remains an explicit open item in the plan checklist.
