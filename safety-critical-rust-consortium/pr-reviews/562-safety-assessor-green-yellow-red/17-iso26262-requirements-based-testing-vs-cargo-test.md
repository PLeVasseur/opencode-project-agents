---
pr: 562
source_feedback: 562-safety-assessor-green-yellow-red.md
comment_type: inline
target_file: iso26262.md
line_start: 116
line_end: 117
context: "Requirements-based test / Interface test: inherent cargo test"
diff_url: "https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R116"
---

`cargo test` is a runner, not requirements-based testing by itself. ISO 26262 expectations include bidirectional requirement-test traceability, documented test specifications, and evidence. This rating seems closer to yellow unless those process elements are in place.
