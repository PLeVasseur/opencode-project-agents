---
repo: eclipse-uprotocol/up-transport-vsomeip-rust
pr: 42
commit: 3e277e835916b9428d8492ea1ae1383c5131bca6
path: up-transport-vsomeip/tests/point_to_point.rs
line_start: 356
line_end: 356
comment_type: conversation
inline_on_pr: false
reason_not_inline: file_not_in_pr_diff
---

Use a non-wildcard source authority for this point-to-point listener registration so it matches the new streamer-use-case detection rule.

Note: this cannot be left as an inline PR #42 review suggestion because this file is not part of that PR's changed-files diff.

Context snippet:

```rust
let source = UUri::any();
let sink = any_from_authority(PTP_AUTHORITY_NAME);
```

Before/after patch:

```diff
- let source = UUri::any();
+ let source = any_from_authority(PTP_AUTHORITY_NAME);
```

Suggested conversation comment text:

```markdown
CI regression on `point_to_point` appears tied to the new streamer-use-case detection behavior: this test still registers the listener with wildcard source authority.

Could we update this registration to use `any_from_authority(PTP_AUTHORITY_NAME)`?

```diff
- let source = UUri::any();
+ let source = any_from_authority(PTP_AUTHORITY_NAME);
```
