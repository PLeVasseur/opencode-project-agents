---
repo: eclipse-uprotocol/up-transport-vsomeip-rust
pr: 42
commit: 3e277e835916b9428d8492ea1ae1383c5131bca6
path: example-utils/hello-world-protos/build.rs
line_start: 52
line_end: 52
comment_type: conversation
inline_on_pr: false
reason_not_inline: file_not_in_pr_diff
---

Fix clippy `double_ended_iterator_last` by replacing `last()` with `next_back()` on the split iterator.

Note: this cannot be left as an inline PR #42 review suggestion because this file is not part of that PR's changed-files diff.

Context snippet:

```rust
let file_name = url.split('/').last().unwrap();
```

Before/after patch:

```diff
- let file_name = url.split('/').last().unwrap();
+ let file_name = url.split('/').next_back().unwrap();
```

Suggested conversation comment text:

```markdown
There is also a clippy failure here (`double_ended_iterator_last`).

Could we use `next_back()` instead of `last()` on the split iterator?

```diff
- let file_name = url.split('/').last().unwrap();
+ let file_name = url.split('/').next_back().unwrap();
```
```
