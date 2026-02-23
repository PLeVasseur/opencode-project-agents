---
pr: 562
source_feedback: 562-safety-assessor-green-yellow-red.md
comment_type: inline
target_file: iso26262.md
line_start: 29
line_end: 29
context: "possible e.g. Option'<T'>, Result<T, E>"
diff_url: "https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R29"
---

The apostrophes in `Option'<T'>` are causing the Netlify failure. MDX parses `<T'>` as JSX and errors on the `'` character.

Suggested fix:

```md
| **1d** | Use of defensive implementation techniques | possible e.g. `Option<T>`, `Result<T, E>` | green |
```

It is also worth auditing other bare angle brackets (for example `<T>`) and wrapping them in backticks so MDX does not parse them as JSX.
