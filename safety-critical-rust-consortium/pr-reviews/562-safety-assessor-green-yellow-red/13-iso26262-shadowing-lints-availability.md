---
pr: 562
source_feedback: 562-safety-assessor-green-yellow-red.md
comment_type: inline
target_file: iso26262.md
line_start: 90
line_end: 90
context: "shadowing possible, TBD clippy enforcable"
diff_url: "https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R90"
---

Relevant lints already exist: `clippy::shadow_unrelated`, `clippy::shadow_reuse`, and `clippy::shadow_same`. This can reference concrete checks instead of staying open-ended.
