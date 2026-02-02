### Location
File: src/coding-guidelines/types-and-traits/gui_6JSM7YE7a1KR.rst.inc
Line: 13
Snippet: ``:scope: expression``

### Type
Blocking

### Comment
``scope`` must be one of ``module``, ``crate``, or ``system`` per the style guideline. ``expression`` is not a valid value. Please pick the correct scope; given that initialization/validity can require whole-program reasoning, ``system`` is the safest default.

```suggestion
   :scope: system
```
