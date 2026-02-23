---
pr: 562
comment_type: inline
target_file: arewesafetycriticalyet.org/docs/main/iso26262.md
line_start: 34
line_end: 34
context: "native compile-time enforcable"
---

Rust gives strong compile-time data-race guarantees, but ISO 26262 concurrency risks also include deadlocks, priority inversion, and scheduling effects. This rating looks too strong as green; suggest yellow with a scoped explanation of what is and is not covered.
