# Reason quality rubric for poor/questionable remediation

## Purpose

- Make every term decision auditable and defensible.
- Prevent low-information justifications such as "looked better" or "seemed right".

## Required reason code (choose exactly one)

- `relocate-conceptual-owner`: moved to a chapter/section that is the concept's canonical home.
- `relocate-first-use-owner`: moved to the chapter/section where the concept is first normatively introduced.
- `retain-conceptual-owner`: kept in current chapter because it is the canonical owner.
- `retain-reordered`: kept in chapter but moved earlier for discoverability/order.
- `retain-link-mitigated`: kept in chapter; first-use discoverability improved with explicit term-linking context.
- `no-change-not-mislocated`: manual review concluded the feedback rating did not indicate a true mislocation.
- `blocked`: cannot resolve now due a concrete blocker (must include blocker ID in `notes`).

## Reason quality minimum bar (`reason_quality=pass`)

- Must cite **before** anchor: baseline `file:line` and `dp_id`.
- Must cite **after** anchor: final `file:line` and `dp_id`.
- Must explain why before was insufficient (1+ concrete issue).
- Must explain why after is better (1+ concrete benefit).
- Must state semantic risk impact (expected: no Rust 2021 meaning change).
- Must be specific to the term (no copy-paste generic sentence).

## Length and specificity guardrails

- `reason_why` minimum length: 80 characters.
- Must mention either ownership, first-use, ordering, or discoverability.
- Must not contain only generic phrases (e.g., "cleaner", "better style", "looks good").

## Pass/fail handling

- If criteria are met: set `reason_quality=pass`.
- If criteria are not met: set `reason_quality=fail` and do not close the checklist item.
- `blocked` decisions cannot be marked `final_quality=resolved-high`.
