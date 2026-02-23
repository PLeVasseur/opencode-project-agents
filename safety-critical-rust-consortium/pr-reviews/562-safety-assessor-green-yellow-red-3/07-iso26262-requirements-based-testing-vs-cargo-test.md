---
pr: 562
comment_type: inline
target_file: arewesafetycriticalyet.org/docs/main/iso26262.md
line_start: 116
line_end: 117
context: "Requirements-based test / Interface test: inherent cargo test"
---

`cargo test` is a runner, not requirements-based testing by itself. ISO 26262 expectations typically include requirement-to-test traceability, documented test specifications, and auditable evidence. This likely needs a yellow rating unless those process elements are explicitly covered.
