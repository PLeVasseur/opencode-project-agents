# Policy decisions v2

- Decision model: conceptual-home-first for foundational terms and placement-priority terms.
- Canonical home criteria: prefer section that owns the normative rule semantics; if tied, prefer earliest first-use rule in the same chapter.
- Displaced definition handling: when canonical `:dt:` moves, replace prior definitional prose with `:t:` usage or explicit "For :dt:`<term>`, see ..." forward reference.
- Analyzer recommendations: treated as diagnostic input only; final destination is manual adjudication against conceptual ownership.
- Forward-reference debt: acceptable when conceptual-home placement is materially better than local-first placement; debt must be explicit in ledger rationale.

## Missing-term closures

- `crate import` is canonically satisfied by `[crate import]s`.
- `declaration` is canonically satisfied by `[declaration]s`.
- Closure rationale: pluralized canonical glossary entries satisfy singular diagnostics where stem and semantics are unchanged.
- Closure criteria: diagnostic item is closed only when chapter coverage includes the canonical pluralized term entry and no distinct singular concept is introduced.
