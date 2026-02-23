---
repo: eclipse-uprotocol/up-transport-vsomeip-rust
pr: 42
commit: 3e277e835916b9428d8492ea1ae1383c5131bca6
path: example-utils/hello-world-protos/build.rs
line_start: 36
line_end: 36
comment_type: conversation
inline_on_pr: false
reason_not_inline: file_not_in_pr_diff
---

Fix clippy `io_other_error` in the build script by using `std::io::Error::other`.

Note: this cannot be left as an inline PR #42 review suggestion because this file is not part of that PR's changed-files diff.

Context snippet:

```rust
return Err(std::io::Error::new(std::io::ErrorKind::Other, error_message));
```

Before/after patch:

```diff
- return Err(std::io::Error::new(std::io::ErrorKind::Other, error_message));
+ return Err(std::io::Error::other(error_message));
```

Suggested conversation comment text:

```markdown
I think one CI failure here is from a clippy lint in `hello-world-protos/build.rs`.

Could we switch to `std::io::Error::other`?

```diff
- return Err(std::io::Error::new(std::io::ErrorKind::Other, error_message));
+ return Err(std::io::Error::other(error_message));
```
```
