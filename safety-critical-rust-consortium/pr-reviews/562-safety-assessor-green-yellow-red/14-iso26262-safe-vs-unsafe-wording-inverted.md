---
pr: 562
source_feedback: 562-safety-assessor-green-yellow-red.md
comment_type: inline
target_file: iso26262.md
line_start: 92
line_end: 92
context: "disallow safe rust - pointer usage discouraged"
diff_url: "https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R92"
---

This appears inverted: it currently says to disallow safe Rust. I think the intended guidance is to disallow or tightly restrict `unsafe` Rust and raw-pointer usage.
