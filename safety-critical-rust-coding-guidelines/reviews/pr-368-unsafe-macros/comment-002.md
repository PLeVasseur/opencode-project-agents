### Location
File: src/coding-guidelines/macros/gui_FRLaMIMb4t3S.rst
Line: 19
Snippet: ``Do not hide unsafe code in macro definitions.``

### Type
Blocking

### Comment
The normative amplification and rationale are currently uncited. Please add authoritative sources (and a bibliography section) to support the claims about unsafe visibility and auditability, or move any unverifiable statements into non-normative rationale with appropriate sourcing.

```suggestion
   Do not hide unsafe code in macro definitions :cite:`gui_FRLaMIMb4t3S:<SOURCE-KEY>`.
   Macros that expand to unsafe code should preserve the ``unsafe`` token visibility :cite:`gui_FRLaMIMb4t3S:<SOURCE-KEY>`.
```
