# Policy decisions v2

## Conceptual-home-first policy

- Foundational terms are owned by their conceptual home sections, not by first incidental use sites.
- Analyzer destination recommendations are diagnostic signals and not binding destinations.
- Controlled forward references are acceptable when conceptual-home placement improves specification coherence.

## Canonical home criteria

Canonical section selection follows this order:

1. The chapter/section whose scope names the concept directly (for example, `Values`, `Expressions`, `Traits`, `Implementations`, `Modules`, `Statements`).
2. The section that introduces the normative rules governing the concept across later uses.
3. If ties remain, the location with the clearest standalone definition prose and least contextual coupling.

## Displaced definition handling

- When moving canonical `:dt:` away from a previous site, replace the previous defining use with `:t:` where possible.
- If reader flow needs a bridge, retain a sentence-level forward reference in the form `For :dt:\`<term>\`, see ...`.
- Keep exactly one canonical chapter-side `:dt:` per concept in scoped remediation rows.

## Analyzer recommendation handling

- `recommended_location` from placement fitness input is treated as non-binding evidence.
- Deviations are expected when conceptual ownership outranks first-use locality.
- Ledger `decision_detail` must state chosen chapter/section ownership explicitly.

## Forward-reference debt rule

- Forward references introduced by conceptual-home placement are accepted when they remove context-local overfitting.
- Such cases should use `reason_code=retain-link-mitigated` or `relocate-conceptual-owner` with explicit rationale.

## Missing-term findings decision

- `crate import` is canonically satisfied by `[crate import]s`.
- `declaration` is canonically satisfied by `[declaration]s`.
- Closure criterion: no singular duplicate `:dt:` is required when plural canonical forms are present and role-usage remains semantically equivalent.
