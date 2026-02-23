---
pr: 562
source_feedback: 562-safety-assessor-green-yellow-red.md
comment_type: inline
target_file: iso26262.md
line_start: 34
line_end: 34
context: "native compile-time enforcable"
diff_url: "https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R34"
---

Rust provides compile-time prevention of data races, but not deadlocks, priority inversion, or all concurrency hazards considered by ISO 26262. The current rating looks too strong; suggest yellow with an explicit note on what the guarantee actually covers.

Also typo: `enforcable` -> `enforceable`.
