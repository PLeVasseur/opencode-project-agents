# Five Representative Queries and Returned Evidence

All cases below were captured in `hybrid` mode (`degraded=false`) with
`top_k=8` and `candidate_limit=200`.

## 1) RET-RESOLVE-001

Query:

`How should Rust code handle defensive error paths safely?`

Top evidence:

1. `doc::unsafe-keyword.md::section:0003::statement:007`
   - Anchor: `https://doc.rust-lang.org/reference/unsafe-keyword.html#unsafe-blocks-unsafe`
   - Relevance: `0.6785419612712817`
   - Text: Rust's type system is a conservative approximation of the dynamic
     safety requirements, so in some cases there is a performance cost to using
     safe code.
2. `doc::panic.md::section:0001::statement:001`
   - Anchor: `https://doc.rust-lang.org/reference/panic.html#panic`
   - Relevance: `0.609430950599742`
   - Text: Rust provides a mechanism to panic as a response to error conditions
     that are typically not expected in normal operation.
3. `doc::crates-and-source-files.md::section:0003::statement:001`
   - Anchor: `https://doc.rust-lang.org/reference/crates-and-source-files.html#uncaught-foreign-unwinding`
   - Relevance: `0.5804349691853016`
   - Text: Uncaught foreign unwinding that propagates beyond `main` causes the
     process to abort.

Artifact file:

- `query_outputs/20260222T001709Z__ret-resolve-001__hybrid.json`

## 2) RET-RESOLVE-002

Query:

`Which Rust features enforce strong typing in design decisions?`

Top evidence:

1. `doc::influences.md::section:0001::statement:001`
   - Anchor: `https://doc.rust-lang.org/reference/influences.html#influences`
   - Relevance: `0.799264585618337`
   - Text: Rust is not a particularly original language and draws design
     elements from many sources.
2. `doc::unsafe-keyword.md::section:0003::statement:007`
   - Anchor: `https://doc.rust-lang.org/reference/unsafe-keyword.html#unsafe-blocks-unsafe`
   - Relevance: `0.7`
   - Text: Rust's type system conservatively approximates dynamic safety
     requirements.
3. `doc::items::unions.md::section:0015::statement:002`
   - Anchor: `https://doc.rust-lang.org/reference/items/unions.html#union-myunion-f1-u32-f2-f32-5`
   - Relevance: `0.6740803924003049`
   - Text: A number of language aspects (including type inference and traits)
     are discussed in the Rust Reference context for soundness rules.

Artifact file:

- `query_outputs/20260222T001709Z__ret-resolve-002__hybrid.json`

## 3) RET-RESOLVE-003

Query:

`How do ownership and lifetimes mitigate memory safety concerns?`

Top evidence:

1. `doc::types::trait-object.md::section:0002::statement:003`
   - Anchor: `https://doc.rust-lang.org/reference/types/trait-object.html#trait-object-lifetime-bounds`
   - Relevance: `0.6902807650409863`
   - Text: Trait object lifetime bounds have defaults that are often inferable.
2. `doc::lifetime-elision.md::section:0013::statement:003`
   - Anchor: `https://doc.rust-lang.org/reference/lifetime-elision.html#const-and-static-elision`
   - Relevance: `0.6469689201380828`
   - Text: If the compiler cannot resolve lifetimes by elision rules, it
     produces an error.
3. `doc::behavior-considered-undefined.md::section:0001::statement:011`
   - Anchor: `https://doc.rust-lang.org/reference/behavior-considered-undefined.html#behavior-considered-undefined`
   - Relevance: `0.5567024357496362`
   - Text: Reference liveness is bounded by borrow-checker-assigned lifetimes,
     with constraints relevant to undefined behavior.

Artifact file:

- `query_outputs/20260222T001709Z__ret-resolve-003__hybrid.json`

## 4) RET-RESOLVE-004

Query:

`What practices keep unsafe code boundaries controlled?`

Top evidence:

1. `doc::behavior-considered-undefined.md::section:0001::statement:002`
   - Anchor: `https://doc.rust-lang.org/reference/behavior-considered-undefined.html#behavior-considered-undefined`
   - Relevance: `0.9626683663176756`
   - Text: Undefined behavior constraints apply to code within `unsafe` blocks
     and `unsafe` functions.
2. `doc::behavior-considered-undefined.md::section:0001::statement:004`
   - Anchor: `https://doc.rust-lang.org/reference/behavior-considered-undefined.html#behavior-considered-undefined`
   - Relevance: `0.9573507584803991`
   - Text: `unsafe` code that cannot be misused by safe code is called sound;
     otherwise it is unsound.
3. `doc::unsafe-keyword.md::section:0001::statement:002`
   - Anchor: `https://doc.rust-lang.org/reference/unsafe-keyword.html#the-unsafe-keyword`
   - Relevance: `0.9448647992083893`
   - Text: `unsafe` marks code that defines extra safety conditions to be
     upheld elsewhere.

Artifact file:

- `query_outputs/20260222T001709Z__ret-resolve-004__hybrid.json`

## 5) RET-RESOLVE-005

Query:

`Which Rust constraints help avoid data races?`

Top evidence:

1. `doc::behavior-considered-undefined.md::section:0001::statement:007`
   - Anchor: `https://doc.rust-lang.org/reference/behavior-considered-undefined.html#behavior-considered-undefined`
   - Relevance: `0.6730541509962827`
   - Text: The undefined-behavior list does not guarantee stable semantics for
     all future versions, but represents current constraints.
2. `doc::items::static-items.md::section:0003::statement:002`
   - Anchor: `https://doc.rust-lang.org/reference/items/static-items.html#mutable-statics`
   - Relevance: `0.6642960903848549`
   - Text: Mutable statics are a major source of race-condition risk; Rust
     treats access as requiring `unsafe` due to concurrency hazards.
3. `doc::type-layout.md::section:0016::statement:005`
   - Anchor: `https://doc.rust-lang.org/reference/type-layout.html#repr-c-field-less-enums`
   - Relevance: `0.532417895412544`
   - Text: For fieldless enum layout constraints, out-of-range discriminants
     can trigger undefined behavior.

Artifact file:

- `query_outputs/20260222T001709Z__ret-resolve-005__hybrid.json`
