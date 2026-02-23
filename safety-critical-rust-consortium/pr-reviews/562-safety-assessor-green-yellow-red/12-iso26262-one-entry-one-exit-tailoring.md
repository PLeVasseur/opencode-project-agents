---
pr: 562
source_feedback: 562-safety-assessor-green-yellow-red.md
comment_type: inline
target_file: iso26262.md
line_start: 87
line_end: 87
context: "1a: One entry and one exit point"
diff_url: "https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R87"
---

TBD seems reasonable here. Early returns, `?`, and panic paths can create multiple exits, so this likely needs a tailored compliance argument rather than a blanket green assessment.
