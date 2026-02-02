# PR 305 Review Summary

Verdict: Request changes

CI status:
- build: success
- check_typos: success
- check_rust_examples: success (Test Guidelines Nightly skipped)
- Netlify header/redirect checks: neutral (informational)

Blocking issues:
1. ``:scope: function`` is not an allowed value; must be ``module``, ``crate``, or ``system``.
2. The guideline text allows main control loops with external termination, but a later noncompliant example says such loops must be treated as noncompliant and require deviation. This is internally inconsistent.
3. The normative termination requirement and loop-variant rules lack citations to authoritative sources or standards in the amplification.

Notes:
- PR body does not include a ``closes #<id>`` reference.
