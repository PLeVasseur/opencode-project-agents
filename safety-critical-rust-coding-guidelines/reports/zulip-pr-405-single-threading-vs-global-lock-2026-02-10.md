# PR 405: Workflow Concurrency vs Global State Lock

## TL;DR

Yes, that GitHub Actions concurrency doc is relevant. It explains why workflow-level "single-threaded" execution is useful for throttling but is not a durable event-processing guarantee. PR 405 therefore keeps concurrency as a guardrail and adds a durable lock at the shared-state boundary.

## What the GitHub concurrency doc says (and why it matters)

From GitHub docs on workflow concurrency:

- There can be at most **one running and one pending** run per concurrency group.
- When a new run is queued, an existing pending run in that group can be **canceled/replaced**.
- Ordering within a concurrency group is **not guaranteed**.

Implication: even with a single global concurrency group, Actions concurrency is not a FIFO durable queue for "every event must be processed in order" semantics.

## Why this is not enough for our contract

Our requirement is effectively: process every mutating event or fail loudly with diagnostics.

Workflow-level single-threading alone does not enforce that because:

1. Burst events can still collapse at the pending slot.
2. Group ordering is arbitrary, so event ordering assumptions are unsafe.
3. It serializes entire runs (checkout/install/etc.) instead of only the critical section.
4. We mutate shared state from more than one path/workflow, so correctness must live at the shared state boundary itself.

## What "global lock and call it a day" should mean here

It should mean locking the shared state store (issue `#314`) with optimistic concurrency:

1. Read state issue + ETag.
2. Acquire lease via conditional patch (`If-Match`) as compare-and-swap.
3. Retry on conflict (`409`/`412`) with jitter/backoff.
4. Allow stale lock takeover after TTL.
5. Release in `finally` after final `save_state()` attempt.
6. Fail loudly on timeout/persistence failure.

That gives durable serialization where it matters, without over-serializing all non-critical workflow work.

## What PR 405 does

- Adds durable in-repo lease locking with CAS (`ETag` + `If-Match`) on the shared state issue.
- Refactors `save_state()` to stop blind whole-body rewrites and preserve lock/state marker blocks.
- Enforces lock boundary before mutating state reads and until after final save attempt.
- Keeps queue policy permissive (read-level members can still be designated by queue).
- Ensures reviewer-request API `422` does not produce false success claims.
- Adds mandatory triage escalation behavior with idempotent label/comment state.

## Recommended Zulip response (full)

Great pointer, and yes that doc is exactly the key nuance.

Workflow concurrency helps with throttling, but it is not a durable event queue. GitHub explicitly allows only one running + one pending per group, can replace older pending runs with newer ones, and does not guarantee ordering.

So a workflow-level global concurrency group alone does not guarantee "process every event" behavior under burst load. That is why 405 puts the lock on the shared state itself (issue #314) using lease + `ETag`/`If-Match` CAS, conflict retries, stale-lock takeover, and fail-loud handling. We still keep workflow concurrency as a first-line guardrail, but correctness is enforced at the mutation boundary.

## Recommended Zulip response (short)

Good callout. That doc is exactly why we did not rely on workflow-only single-threading: concurrency groups allow one running + one pending, may replace pending runs, and do not guarantee ordering. 405 therefore locks the shared state itself (issue #314) with lease + `ETag`/`If-Match` CAS so we serialize the mutation boundary and preserve event correctness.

## GitHub references

- PR 405: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/405
- Shared state issue (`#314`): https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/314
- Workflow concurrency docs: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
- Reviewer request API status docs (`201`, `403`, `422`): https://docs.github.com/en/rest/pulls/review-requests?apiVersion=2022-11-28#request-reviewers-for-a-pull-request
- REST best practice (avoid concurrent requests): https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#avoid-concurrent-requests

Code links from the PR commit:

- Concurrency note in workflow: https://github.com/PLeVasseur/safety-critical-rust-coding-guidelines/blob/a42580452eea068de9ef8ab670c5a301a8d78711/.github/workflows/reviewer-bot.yml#L38-L42
- Lease lock acquire: https://github.com/PLeVasseur/safety-critical-rust-coding-guidelines/blob/a42580452eea068de9ef8ab670c5a301a8d78711/scripts/reviewer_bot.py#L1069
- Conditional `save_state()` path: https://github.com/PLeVasseur/safety-critical-rust-coding-guidelines/blob/a42580452eea068de9ef8ab670c5a301a8d78711/scripts/reviewer_bot.py#L908
- Lock boundary selector: https://github.com/PLeVasseur/safety-critical-rust-coding-guidelines/blob/a42580452eea068de9ef8ab670c5a301a8d78711/scripts/reviewer_bot.py#L3796
- Reviewer request handling (`422` truthfulness): https://github.com/PLeVasseur/safety-critical-rust-coding-guidelines/blob/a42580452eea068de9ef8ab670c5a301a8d78711/scripts/reviewer_bot.py#L375
