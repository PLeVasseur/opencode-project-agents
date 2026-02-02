### Location
File: src/coding-guidelines/expressions/gui_Ncdb5PhhiZyX.rst
Line: 27
Snippet: ``Unbounded or potentially infinite loops are prohibited unless they serve as the main``

### Type
Blocking

### Comment
The guideline currently allows main control loops with external termination, but later it says such loops must still be diagnosed as noncompliant and require deviation. Please make these statements consistent. One option is to move main control loops into the deviation path instead of listing them as compliant conditions.

```suggestion
   Unbounded or potentially infinite loops are prohibited. If a system requires a main control loop with
   external termination mechanisms, it must be handled via a formal deviation with documented justification.
```
