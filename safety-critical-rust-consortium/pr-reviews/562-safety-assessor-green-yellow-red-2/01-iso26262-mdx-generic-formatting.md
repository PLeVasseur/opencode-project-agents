---
pr: 562
comment_type: inline
target_file: arewesafetycriticalyet.org/docs/main/iso26262.md
line_start: 29
line_end: 29
context: "possible e.g. Option'<T'>, Result<T, E>"
---

This generic type formatting is currently malformed (`Option'<T'>`) and can be parsed as invalid MDX/JSX. Please rewrite this as inline code (for example, `` `Option<T>` and `Result<T, E>` ``) so the docs render reliably.
