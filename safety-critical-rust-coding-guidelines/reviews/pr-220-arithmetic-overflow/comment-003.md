### Location
File: src/coding-guidelines/expressions/gui_dCquvqE1csI3.rst.inc
Line: 16
Snippet: `Any wraparound behavior must be explicitly specified to ensure the same behavior in both debug and release modes.`

### Type
Blocking

### Comment
The PR description says this guideline covers CERT INT30-C and INT32-C, but the guideline body does not state or cite this. Please add explicit traceability in the guideline text with citations.

```suggestion
    Eliminate arithmetic overflow :cite:`gui_dCquvqE1csI3:FLS-ARITHMETIC-OVERFLOW` of both signed and unsigned integer types.
    Any wraparound behavior must be explicitly specified to ensure the same behavior in both debug and release modes.
    This guideline aligns with :cite:`gui_dCquvqE1csI3:CERT-INT30-C` and :cite:`gui_dCquvqE1csI3:CERT-INT32-C`.
```
