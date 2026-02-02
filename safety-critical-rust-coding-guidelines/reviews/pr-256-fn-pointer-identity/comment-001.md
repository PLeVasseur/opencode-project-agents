### Location
File: src/coding-guidelines/types-and-traits/gui_QbvIknd9qNF6.rst
Line: 21
Snippet: ``**Exception**``

### Type
Blocking

### Comment
The Rust Reference does not guarantee that ``#[no_mangle]`` functions have a single instance; it only fixes the symbol name. Duplicate symbols can also be link errors. Unless you can cite a source that guarantees unique instantiation, please remove or rephrase this exception.

```suggestion
   **Exception**

   None. Function pointer identity is not guaranteed by Rust, even for functions with stable symbol names.
```
