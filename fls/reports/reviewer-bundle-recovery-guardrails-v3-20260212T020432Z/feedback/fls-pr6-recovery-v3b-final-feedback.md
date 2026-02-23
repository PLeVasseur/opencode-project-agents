# Recovery Plan v3b — Final Reviewer Feedback

## Overall

The recovery plan is approved for execution. All prior feedback items are correctly implemented and verified. One known gap remains, documented below with a conditional escalation path.

---

## Known gap: deviation permit approval is forgeable

### The problem

`approve-deviation.py` accepts any `--approved-by` string. The implementer has access to the script and knows the reviewer's name. Nothing prevents them from running:

```
approve-deviation.py --approved-by pete --decision approve --permit ...
```

This is an authentication problem, not an authorization one. An allowlist doesn't help — the implementer knows the allowed values. Any string-based check is forgeable by someone who can run the script.

Solutions that would actually work all require something the implementer doesn't have: a GPG private key (detached signature verification against a pinned public key fingerprint), a protected branch only the reviewer can push to, or an out-of-band approval artifact created from the reviewer's own environment.

### Why we're shipping without fixing it

The risk is low for this specific execution:

1. **The 10 foundational terms cannot use deviation permits at all.** This is hardcoded in the validator. The highest-value targets are locked out of the deviation path entirely.

2. **The 30% concentration cap limits exposure.** At most ~27 of Wave B's 89 terms could have deviations, even with forged approvals.

3. **Anti-monoculture checks constrain the pattern.** If those ~27 all followed the same reasoning, the Jaccard similarity and action-type concentration gates would fire.

4. **Human spot-checks provide a manual catch.** The reviewer examines at least 5 terms per batch and would see deviation permits they didn't sign.

5. **The actual failure mode from the first run wasn't forgery.** It was a blunt mechanical shortcut. Every new guardrail targets that pattern directly. The deviation permit system is a secondary defense for legitimate disagreements with recommendations.

The scenario that would beat all these controls simultaneously — the implementer forges approvals on 15–20 permits with genuinely distinct, well-argued evidence that passes monoculture checks and isn't caught during spot-checks — is qualitatively different from what happened in the first run.

### Conditional escalation

If the first Wave B batch produces more than 3 deviation permits, execution pauses and GPG-based signing is added to `approve-deviation.py` before proceeding. Specifically:

- The reviewer's GPG public key fingerprint is hardcoded in the script.
- `approve-deviation.py` calls `gpg --detach-sign` on the permit file, producing a `.sig` sidecar.
- The validator checks `gpg --verify` against the pinned fingerprint at gate time.
- Unsigned or incorrectly-signed permits fail with `FAILED_DEVIATION_SIGNATURE`.

This threshold (>3 permits in the first WB batch) serves as an automatic tripwire. Below that, the other guardrails provide sufficient coverage.

---

## Summary

| Item | Status |
|---|---|
| Deviation permit lifecycle (file/review/gate split) | ✓ Verified |
| Foundational section enforcement | ✓ Verified |
| Method section correction | ✓ Verified |
| Approval forgery gap | Accepted with conditional GPG escalation |

The plan is ready for the revert, baseline verification, and Wave A execution.
