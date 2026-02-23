---
repo: eclipse-uprotocol/up-transport-vsomeip-rust
pr: 42
commit: 3e277e835916b9428d8492ea1ae1383c5131bca6
comment_type: review_summary
review_state: request_changes
---

Thanks for the fix here - it resolves the downstream streamer use-case issue we were seeing.

I do need to request changes for CI:

1. `up-transport-vsomeip/tests/point_to_point.rs`
   - Update point-to-point listener registration source filter to match the new streamer-use-case detection behavior.

2. `example-utils/hello-world-protos/build.rs`
   - Address clippy `io_other_error` in the build script.

3. `example-utils/hello-world-protos/build.rs`
   - Address clippy `double_ended_iterator_last` in the URL filename extraction line.

Note: these files are outside this PR's changed-files diff, so I cannot leave line-level GitHub suggestion comments directly on this PR for them.

Detailed before/after snippets are prepared in:

- `reviews/pr-42-ci-fixes/01-point-to-point-source-filter.md`
- `reviews/pr-42-ci-fixes/02-build-rs-io-other-error.md`
- `reviews/pr-42-ci-fixes/03-build-rs-next-back.md`
