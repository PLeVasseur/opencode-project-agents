# Glossary quality report

Generated terms: 957
Reviewed terms: 957
Missing :t: references: 15 true missing; 226 case mismatches

## Priority index
Rating 0 (missing definitions): assignment, atomic, evaluated, executed, range-full expression, representation
Rating 1 (alias/link-only): none
Rating 2 (low-signal/truncated/fragment): assignee expression, assignee pattern, async block
  code generation attributes, coercion site, coercion-propagating expression, conditional compilation attributes
  constant context, constant expression, Contravariant, Covariant, derivation attributes, diagnostics attributes
  documentation attributes, expected type, foreign function interface attributes, fragment specifier restrictions
  input lifetime, Invariant, Least upper bound coercion, limits attributes, macro attributes, modules attributes
  mutable place expression, mutable place expression context, numeric cast, output lifetime, place expression
  prelude attributes, runtime attributes, specialized cast, testing attributes, type attributes, unifiable
  unnamed lifetime, unsafe block, unsized coercion, while let loop, while loop
Missing legacy See line: none
Regression vs legacy: async closure type, C representation, cast, control flow boundary, indexed operand
  indexing operand, multiplication assignment, range-full expression, signed integer type, trait object type
  unnamed lifetime, use capture
Tautological/circular: none

## Systemic issues
- definition-same-role-change-expected: 247
- low-signal: 7
- missing: 6
- missing-discriminator: 44
- missing-scope: 56
- regression-vs-legacy: 12
- truncated: 32

## Missing :t: references
True missing terms:
- associated type alias
- auto-dereferencing
- bindings
- dynamically-sized type
- extern block
- flexible compound punctuator
- floating point type
- fragment specifier restriction
- if-let expression
- main function
- namespace qualifier
- obligation
- shadowed
- token
- unifiable type

Case mismatches:
- Abstract data type -> abstract data type
- Addition expression -> addition expression
- Alignment -> alignment
- Arithmetic expression -> arithmetic expression
- Array expression -> array expression
- Array type -> array type
- Assembly code block -> assembly code block
- Assembly option -> assembly option
- Assignment expression -> assignment expression
- Associated constant -> associated constant
- Associated function -> associated function
- Associated item -> associated item
- Associated type -> associated type
- associativity -> Associativity
- Atomic type -> atomic type
- Attribute -> attribute
- Attribute macro -> attribute macro
- Await expression -> await expression
- Binding -> binding
- Bit and expression -> bit and expression
- Bit expression -> bit expression
- Bit or expression -> bit or expression
- Bit xor expression -> bit xor expression
- Block comment -> block comment
- Block expression -> block expression
- Borrow expression -> borrow expression
- borrowing -> Borrowing
- Break expression -> break expression
- break type -> Break type
- break value -> Break value
- Built-in attribute -> built-in attribute
- By immutable reference capture -> by immutable reference capture
- By mutable reference capture -> by mutable reference capture
- By unique immutable reference capture -> by unique immutable reference capture
- By value capture -> by value capture
- c signed int type -> C signed int type
- Call expression -> call expression
- Call resolution -> call resolution
- Closure expression -> closure expression
- Closure type -> closure type
- Comparison expression -> comparison expression
- Compound assignment expression -> compound assignment expression
- Configuration predicate -> configuration predicate
- Constant -> constant
- Constant parameter -> constant parameter
- Constant promotion -> constant promotion
- Continue expression -> continue expression
- contravariant -> Contravariant
- covariant -> Covariant
- Crate import -> crate import
- Crate indication -> crate indication
- Declarative macro -> declarative macro
- default representation -> Default representation
- definition site hygiene -> Definition site hygiene
- Dereference expression -> dereference expression
- Derive macro -> derive macro
- destruction -> Destruction
- Diverging expression -> diverging expression
- Division expression -> division expression
- drop order -> Drop order
- Drop scope -> drop scope
- drop scope extension -> Drop scope extension
- dropping -> Dropping
- elaboration -> Elaboration
- Entity -> entity
- Enum -> enum
- Enum field -> enum field
- Enum type -> enum type
- Enum variant -> enum variant
- Error propagation expression -> error propagation expression
- evaluation -> Evaluation
- execution -> Execution
- Expression -> expression
- Expression statement -> expression statement
- External prelude -> external prelude
- Field -> field
- Field access expression -> field access expression
- field resolution -> Field resolution
- Floating-point type -> floating-point type
- foreign function interface -> Foreign Function Interface
- Fragment specifier -> fragment specifier
- Function -> function
- Function item type -> function item type
- Function pointer type -> function pointer type
- Function type -> function type
- Function-like macro -> function-like macro
- Generic argument -> generic argument
- generic conformance -> Generic conformance
- Generic parameter -> generic parameter
- Identifier -> identifier
- identifier pattern matching -> Identifier pattern matching
- If expression -> if expression
- If let expression -> if let expression
- impl header lifetime elision -> Impl header lifetime elision
- Impl trait type -> impl trait type
- Implementation -> implementation
- Index expression -> index expression
- Indirection type -> indirection type
- Inferred type -> inferred type
- Infinite loop expression -> infinite loop expression
- Inherent implementation -> inherent implementation
- inline assembly -> Inline assembly
- Inner block doc -> inner block doc
- Integer type -> integer type
- interior mutability -> Interior mutability
- invariant -> Invariant
- Item statement -> item statement
- Keyword -> keyword
- Label -> label
- Language prelude -> language prelude
- Lazy and expression -> lazy and expression
- Lazy boolean expression -> lazy boolean expression
- Lazy or expression -> lazy or expression
- least upper bound coercion -> Least upper bound coercion
- Let statement -> let statement
- Lifetime -> lifetime
- lifetime elision -> Lifetime elision
- Lifetime parameter -> lifetime parameter
- Line comment -> line comment
- Literal expression -> literal expression
- literal pattern matching -> Literal pattern matching
- Loop expression -> loop expression
- Macro -> macro
- macro expansion -> Macro expansion
- macro matching -> Macro matching
- macro transcription -> Macro transcription
- Match arm -> match arm
- Match expression -> match expression
- Method call expression -> method call expression
- method resolution -> Method resolution
- method resolution implementation candidate lookup -> Method resolution implementation candidate lookup
- method resolution inherent implementation candidate lookup -> Method resolution inherent implementation candidate lookup
- method resolution receiver candidate lookup -> Method resolution receiver candidate lookup
- method resolution trait implementation candidate lookup -> Method resolution trait implementation candidate lookup
- Module -> module
- Multiplication expression -> multiplication expression
- Name -> name
- Negation expression -> negation expression
- Never type -> never type
- Numeric type -> numeric type
- Outer block doc -> outer block doc
- Outlives bound -> outlives bound
- ownership -> Ownership
- Parenthesized expression -> parenthesized expression
- parenthesized pattern matching -> Parenthesized pattern matching
- Parenthesized type -> parenthesized type
- Path expression -> path expression
- path expression resolution -> Path expression resolution
- path expression resolution implementation candidate lookup -> Path expression resolution implementation candidate lookup
- path expression resolution inherent implementation candidate lookup -> Path expression resolution inherent implementation candidate lookup
- path expression resolution trait implementation candidate lookup -> Path expression resolution trait implementation candidate lookup
- path pattern matching -> Path pattern matching
- path resolution -> Path resolution
- pattern matching -> Pattern matching
- Place expression -> place expression
- precedence -> Precedence
- Prelude name -> prelude name
- primitive representation -> Primitive representation
- private visibility -> Private visibility
- Procedural macro -> procedural macro
- public visibility -> Public visibility
- Range expression -> range expression
- range pattern matching -> Range pattern matching
- Raw pointer type -> raw pointer type
- record struct pattern matching -> Record struct pattern matching
- reference pattern matching -> Reference pattern matching
- Reference type -> reference type
- Register -> register
- Remainder expression -> remainder expression
- Return expression -> return expression
- rule matching -> Rule matching
- Scalar type -> scalar type
- Sequence type -> sequence type
- Shadowing -> shadowing
- Shift left expression -> shift left expression
- Shift right expression -> shift right expression
- Signed integer type -> signed integer type
- Size -> size
- slice pattern matching -> Slice pattern matching
- Slice type -> slice type
- Statement -> statement
- Static -> static
- Struct -> struct
- Struct expression -> struct expression
- Struct field -> struct field
- Struct type -> struct type
- Subtraction expression -> subtraction expression
- Subtyping -> subtyping
- Textual type -> textual type
- token matching -> Token matching
- Trait -> trait
- Trait bound -> trait bound
- Trait implementation -> trait implementation
- Trait object type -> trait object type
- Trait type -> trait type
- transparent representation -> Transparent representation
- Tuple expression -> tuple expression
- tuple pattern matching -> Tuple pattern matching
- Tuple struct call expression -> tuple struct call expression
- tuple struct pattern matching -> Tuple struct pattern matching
- Tuple type -> tuple type
- Type -> type
- Type alias -> type alias
- Type bound predicate -> type bound predicate
- Type cast expression -> type cast expression
- type coercion -> Type coercion
- type inference -> Type inference
- Type parameter -> type parameter
- type path resolution -> Type path resolution
- type representation -> Type representation
- type unification -> Type unification
- undefined behavior -> Undefined behavior
- Underscore expression -> underscore expression
- underscore pattern matching -> Underscore pattern matching
- Unify -> unify
- Union field -> union field
- Union type -> union type
- Unsafe block expression -> unsafe block expression
- Unsized coercion -> unsized coercion
- Use capture -> use capture
- variance -> Variance
- visibility -> Visibility
- visible emptiness -> Visible emptiness
- While let loop expression -> while let loop expression
- While loop expression -> while loop expression
- Zero-variant enum type -> zero-variant enum type

## Term reviews

## ABI
Rating: 
Issues: none
Notes: 
Legacy: 

## ABI clobber
Rating: 
Issues: none
Notes: 
Legacy: 

## ABI kind
Rating: 
Issues: none
Notes: 
Legacy: 

## Abort
Rating: 
Issues: none
Notes: 
Legacy: 

## abstract data type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## active
Rating: 
Issues: none
Notes: 
Legacy: 

## active attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## addition assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## addition assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## addition expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## address-to-pointer cast
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## adjusted call operand
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## alignment
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: worse - legacy is shorter or less specific.

## all configuration predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## allocated object
Rating: 
Issues: none
Notes: 
Legacy: 

## anonymous loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## anonymous return type
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## anonymous type parameter
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## any configuration predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## Application Binary Interface
Rating: 
Issues: none
Notes: 
Legacy: 

## argument operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## arithmetic expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## arithmetic operator
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## arithmetic overflow
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: worse - legacy is shorter or less specific.

## arity
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## array
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## array element constructor
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## array expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## array repetition constructor
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## array type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## assembly code block
Rating: 
Issues: none
Notes: 
Legacy: 

## assembly directive
Rating: 
Issues: none
Notes: 
Legacy: 

## assembly instruction
Rating: 
Issues: none
Notes: 
Legacy: 

## assembly option
Rating: 
Issues: none
Notes: 
Legacy: 

## assigned operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## assignee expression
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## assignee operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## assignee pattern
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## assignment
Rating: 0 (missing)
Issues: missing
Notes: No generated definition present.
Legacy: same - same wording and scope.

## assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## associated constant
Rating: 
Issues: none
Notes: 
Legacy: 

## associated function
Rating: 
Issues: none
Notes: 
Legacy: 

## associated implementation constant
Rating: 
Issues: none
Notes: 
Legacy: 

## associated implementation function
Rating: 
Issues: none
Notes: 
Legacy: 

## associated implementation type
Rating: 
Issues: none
Notes: 
Legacy: 

## associated item
Rating: 
Issues: none
Notes: 
Legacy: 

## associated trait constant
Rating: 
Issues: none
Notes: 
Legacy: 

## associated trait function
Rating: 
Issues: none
Notes: 
Legacy: 

## associated trait implementation function
Rating: 
Issues: none
Notes: 
Legacy: 

## associated trait implementation item
Rating: 
Issues: none
Notes: 
Legacy: 

## associated trait item
Rating: 
Issues: none
Notes: 
Legacy: 

## associated trait type
Rating: 
Issues: none
Notes: 
Legacy: 

## associated type
Rating: 
Issues: none
Notes: 
Legacy: 

## associated type projection
Rating: 
Issues: none
Notes: 
Legacy: 

## Associativity
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## async block
Rating: 2 (low-signal)
Issues: low-signal
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## async block expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## async closure expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## async closure type
Rating: 3 (adequate)
Issues: missing-discriminator, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## async control flow boundary
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## async function
Rating: 
Issues: none
Notes: 
Legacy: 

## atomic
Rating: 0 (missing)
Issues: missing
Notes: No generated definition present.
Legacy: same - same wording and scope.

## atomic type
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## att_syntax
Rating: 
Issues: none
Notes: 
Legacy: 

## attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## attribute content
Rating: 
Issues: none
Notes: 
Legacy: 

## attribute macro
Rating: 
Issues: none
Notes: 
Legacy: 

## auto trait
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## automatically_derived
Rating: 
Issues: none
Notes: 
Legacy: 

## await expression
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## base address
Rating: 
Issues: none
Notes: 
Legacy: 

## base initializer
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## basic assignment
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## binary crate
Rating: 
Issues: none
Notes: 
Legacy: 

## binary literal
Rating: 
Issues: none
Notes: 
Legacy: 

## binary operator
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## binding
Rating: 
Issues: none
Notes: 
Legacy: 

## binding argument
Rating: 
Issues: none
Notes: 
Legacy: 

## binding bound argument
Rating: 
Issues: none
Notes: 
Legacy: 

## binding mode
Rating: 
Issues: none
Notes: 
Legacy: 

## binding pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## binding scope
Rating: 
Issues: none
Notes: 
Legacy: 

## bit and assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## bit and assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bit and expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bit expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bit or assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## bit or assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bit or expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bit xor assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## bit xor assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bit xor expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## block comment
Rating: 
Issues: none
Notes: 
Legacy: 

## block expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## bool
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## boolean literal
Rating: 
Issues: none
Notes: 
Legacy: 

## borrow
Rating: 
Issues: none
Notes: 
Legacy: 

## borrow expression
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## borrowed
Rating: 
Issues: none
Notes: 
Legacy: 

## Borrowing
Rating: 
Issues: none
Notes: 
Legacy: 

## bound
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## bound pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## break expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Break type
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## Break value
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## built-in attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## built-in trait
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## by copy
Rating: 
Issues: none
Notes: 
Legacy: 

## by immutable reference capture
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## by move
Rating: 
Issues: none
Notes: 
Legacy: 

## by mutable reference
Rating: 
Issues: none
Notes: 
Legacy: 

## by mutable reference capture
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## by reference
Rating: 
Issues: none
Notes: 
Legacy: 

## by unique immutable reference capture
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## by value
Rating: 
Issues: none
Notes: 
Legacy: 

## by value capture
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## byte literal
Rating: 
Issues: none
Notes: 
Legacy: 

## byte string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## C
Rating: 
Issues: none
Notes: 
Legacy: 

## C representation
Rating: 3 (adequate)
Issues: missing-discriminator, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## C signed int type
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## c string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## call conformance
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## call expression
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## call operand
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## call resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## call site hygiene
Rating: 
Issues: none
Notes: 
Legacy: 

## callee type
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: same - similar scope and detail.

## candidate callee type
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate callee type chain
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate container type
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate container type chain
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate direct entity
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate external prelude entity
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate field
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate indexed field
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate method
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate named field
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate receiver type
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate receiver type chain
Rating: 
Issues: none
Notes: 
Legacy: 

## candidate selected entity
Rating: 
Issues: none
Notes: 
Legacy: 

## capture mode
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## capture target
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## captured
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## capturing
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## capturing environment
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## capturing expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## cast
Rating: 3 (adequate)
Issues: missing-scope, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## cfg
Rating: 
Issues: none
Notes: 
Legacy: 

## cfg_attr
Rating: 
Issues: none
Notes: 
Legacy: 

## char
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## character literal
Rating: 
Issues: none
Notes: 
Legacy: 

## closure body
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## closure expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## closure parameter
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## closure type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## code generation attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## code point
Rating: 
Issues: none
Notes: 
Legacy: 

## coercion site
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## coercion-propagating expression
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## cold
Rating: 
Issues: none
Notes: 
Legacy: 

## collapse_debuginfo
Rating: 
Issues: none
Notes: 
Legacy: 

## comment
Rating: 
Issues: none
Notes: 
Legacy: 

## comparison expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## compilation root
Rating: 
Issues: none
Notes: 
Legacy: 

## compound assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## compound assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## compound punctuator
Rating: 
Issues: none
Notes: 
Legacy: 

## concrete type
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## conditional compilation
Rating: 
Issues: none
Notes: 
Legacy: 

## conditional compilation attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## conditionally-compiled source code
Rating: 
Issues: none
Notes: 
Legacy: 

## configuration predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## const block expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## const register expression
Rating: 
Issues: none
Notes: 
Legacy: 

## constant
Rating: 
Issues: none
Notes: 
Legacy: 

## constant argument
Rating: 
Issues: none
Notes: 
Legacy: 

## constant context
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## constant expression
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## constant function
Rating: 
Issues: none
Notes: 
Legacy: 

## constant initializer
Rating: 
Issues: none
Notes: 
Legacy: 

## constant parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## constant parameter initializer
Rating: 
Issues: none
Notes: 
Legacy: 

## constant promotion
Rating: 
Issues: none
Notes: 
Legacy: 

## constrain
Rating: 
Issues: none
Notes: 
Legacy: 

## construct
Rating: 
Issues: none
Notes: 
Legacy: 

## constructee
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## container operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## continue expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## Contravariant
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## control flow boundary
Rating: 4 (mostly-clear)
Issues: regression-vs-legacy
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: better - legacy is more detailed.

## copy type
Rating: 
Issues: none
Notes: 
Legacy: 

## core prelude
Rating: 
Issues: none
Notes: 
Legacy: 

## Covariant
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## crate
Rating: 
Issues: none
Notes: 
Legacy: 

## crate import
Rating: 
Issues: none
Notes: 
Legacy: 

## crate indication
Rating: 
Issues: none
Notes: 
Legacy: 

## crate public modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## crate root
Rating: 
Issues: none
Notes: 
Legacy: 

## crate root module
Rating: 
Issues: none
Notes: 
Legacy: 

## crate type
Rating: 
Issues: none
Notes: 
Legacy: 

## crate_name
Rating: 
Issues: none
Notes: 
Legacy: 

## crate_type
Rating: 
Issues: none
Notes: 
Legacy: 

## dangling
Rating: 
Issues: none
Notes: 
Legacy: 

## data race
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## decimal literal
Rating: 
Issues: none
Notes: 
Legacy: 

## declaration
Rating: 
Issues: none
Notes: 
Legacy: 

## declarative macro
Rating: 
Issues: none
Notes: 
Legacy: 

## deconstructee
Rating: 
Issues: none
Notes: 
Legacy: 

## Default representation
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## Definition site hygiene
Rating: 
Issues: none
Notes: 
Legacy: 

## dereference
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## dereference expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## dereference type
Rating: 
Issues: none
Notes: 
Legacy: 

## dereference type chain
Rating: 
Issues: none
Notes: 
Legacy: 

## derivation attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## derive
Rating: 
Issues: none
Notes: 
Legacy: 

## derive helper attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## derive macro
Rating: 
Issues: none
Notes: 
Legacy: 

## Destruction
Rating: 
Issues: none
Notes: 
Legacy: 

## destructor
Rating: 
Issues: none
Notes: 
Legacy: 

## destructuring assignment
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: same - similar scope and detail.

## diagnostics attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## direction modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## discriminant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## discriminant initializer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## discriminant type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## diverging expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## diverging type variable
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## division assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## division assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## division expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## doc
Rating: 
Issues: none
Notes: 
Legacy: 

## doc comment
Rating: 
Issues: none
Notes: 
Legacy: 

## documentation attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## drop construct
Rating: 
Issues: none
Notes: 
Legacy: 

## Drop order
Rating: 
Issues: none
Notes: 
Legacy: 

## drop scope
Rating: 
Issues: none
Notes: 
Legacy: 

## Drop scope extension
Rating: 
Issues: none
Notes: 
Legacy: 

## drop type
Rating: 
Issues: none
Notes: 
Legacy: 

## dropped
Rating: 
Issues: none
Notes: 
Legacy: 

## Dropping
Rating: 
Issues: none
Notes: 
Legacy: 

## dynamically sized type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Elaboration
Rating: 
Issues: none
Notes: 
Legacy: 

## element type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## elided
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## elided lifetime
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## else expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## empty statement
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## entity
Rating: 
Issues: none
Notes: 
Legacy: 

## enum
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## enum cast
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## enum field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## enum type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## enum value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## enum variant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## enum variant value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## equals expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## error propagation expression
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## escaped character
Rating: 
Issues: none
Notes: 
Legacy: 

## evaluated
Rating: 0 (missing)
Issues: missing
Notes: No generated definition present.
Legacy: same - same wording and scope.

## Evaluation
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## exclusive range pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## executed
Rating: 0 (missing)
Issues: missing
Notes: No generated definition present.
Legacy: same - same wording and scope.

## Execution
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## expected type
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## explicit register argument
Rating: 
Issues: none
Notes: 
Legacy: 

## explicit register name
Rating: 
Issues: none
Notes: 
Legacy: 

## explicitly declared entity
Rating: 
Issues: none
Notes: 
Legacy: 

## export_name
Rating: 
Issues: none
Notes: 
Legacy: 

## exported function
Rating: 
Issues: none
Notes: 
Legacy: 

## exported static
Rating: 
Issues: none
Notes: 
Legacy: 

## expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## expression statement
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## expression-with-block
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## expression-without-block
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## extending expression
Rating: 
Issues: none
Notes: 
Legacy: 

## extending pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## extern C ABI
Rating: 
Issues: none
Notes: 
Legacy: 

## external block
Rating: 
Issues: none
Notes: 
Legacy: 

## external function
Rating: 
Issues: none
Notes: 
Legacy: 

## external function item type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## external prelude
Rating: 
Issues: none
Notes: 
Legacy: 

## external static
Rating: 
Issues: none
Notes: 
Legacy: 

## f32
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## f64
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## false
Rating: 
Issues: none
Notes: 
Legacy: 

## fat pointer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## fat pointer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## FFI
Rating: 
Issues: none
Notes: 
Legacy: 

## field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## field access expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## field index
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## field list
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## Field resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## field selector
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## final match arm
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## fixed sized type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## flexible compound punctuators
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## float literal
Rating: 
Issues: none
Notes: 
Legacy: 

## float suffix
Rating: 
Issues: none
Notes: 
Legacy: 

## floating-point type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## floating-point type variable
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## floating-point value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## for loop
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## for loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Foreign Function Interface
Rating: 
Issues: none
Notes: 
Legacy: 

## foreign function interface attributes
Rating: 2 (low-signal)
Issues: missing-discriminator, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## fragment specifier
Rating: 
Issues: none
Notes: 
Legacy: 

## fragment specifier restrictions
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## full range expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## function
Rating: 
Issues: none
Notes: 
Legacy: 

## function body
Rating: 
Issues: none
Notes: 
Legacy: 

## function item type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Function lifetime elision
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## function parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## function pointer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## function pointer type parameter
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## function qualifier
Rating: 
Issues: none
Notes: 
Legacy: 

## function signature
Rating: 
Issues: none
Notes: 
Legacy: 

## function type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## function-like macro
Rating: 
Issues: none
Notes: 
Legacy: 

## function-pointer-to-address cast
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## function-pointer-to-pointer cast
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## fundamental
Rating: 
Issues: none
Notes: 
Legacy: 

## future
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## future operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## generic argument
Rating: 
Issues: none
Notes: 
Legacy: 

## generic associated type
Rating: 
Issues: none
Notes: 
Legacy: 

## Generic conformance
Rating: 
Issues: none
Notes: 
Legacy: 

## generic enum
Rating: 
Issues: none
Notes: 
Legacy: 

## generic function
Rating: 
Issues: none
Notes: 
Legacy: 

## generic implementation
Rating: 
Issues: none
Notes: 
Legacy: 

## generic parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## generic parameter scope
Rating: 
Issues: none
Notes: 
Legacy: 

## generic struct
Rating: 
Issues: none
Notes: 
Legacy: 

## generic substitution
Rating: 
Issues: none
Notes: 
Legacy: 

## generic trait
Rating: 
Issues: none
Notes: 
Legacy: 

## generic type
Rating: 
Issues: none
Notes: 
Legacy: 

## generic type alias
Rating: 
Issues: none
Notes: 
Legacy: 

## generic union
Rating: 
Issues: none
Notes: 
Legacy: 

## glob import
Rating: 
Issues: none
Notes: 
Legacy: 

## global path
Rating: 
Issues: none
Notes: 
Legacy: 

## global type variable
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## global_allocator
Rating: 
Issues: none
Notes: 
Legacy: 

## greater-than expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## greater-than-or-equals expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## half-open range pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## hexadecimal literal
Rating: 
Issues: none
Notes: 
Legacy: 

## higher-ranked trait bound
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## hygiene
Rating: 
Issues: none
Notes: 
Legacy: 

## hygienic
Rating: 
Issues: none
Notes: 
Legacy: 

## i128
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## i16
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## i32
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## i64
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## i8
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## identifier
Rating: 
Issues: none
Notes: 
Legacy: 

## identifier pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Identifier pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## if expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## if let expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## ignore
Rating: 
Issues: none
Notes: 
Legacy: 

## immutable
Rating: 
Issues: none
Notes: 
Legacy: 

## immutable borrow
Rating: 
Issues: none
Notes: 
Legacy: 

## immutable borrow expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## immutable place expression
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: worse - legacy is shorter or less specific.

## immutable place expression context
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: worse - legacy is shorter or less specific.

## immutable raw borrow expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## immutable raw pointer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## immutable reference
Rating: 
Issues: none
Notes: 
Legacy: 

## immutable static
Rating: 
Issues: none
Notes: 
Legacy: 

## immutable variable
Rating: 
Issues: none
Notes: 
Legacy: 

## Impl header lifetime elision
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## impl trait type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## implementation
Rating: 
Issues: none
Notes: 
Legacy: 

## implementation body
Rating: 
Issues: none
Notes: 
Legacy: 

## implementation coherence
Rating: 
Issues: none
Notes: 
Legacy: 

## implementation conformance
Rating: 
Issues: none
Notes: 
Legacy: 

## implemented trait
Rating: 
Issues: none
Notes: 
Legacy: 

## implementing type
Rating: 
Issues: none
Notes: 
Legacy: 

## implicit borrow
Rating: 
Issues: none
Notes: 
Legacy: 

## implicitly declared entity
Rating: 
Issues: none
Notes: 
Legacy: 

## implied bound
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: same - similar scope and detail.

## import path prefix
Rating: 
Issues: none
Notes: 
Legacy: 

## in scope
Rating: 
Issues: none
Notes: 
Legacy: 

## inclusive range pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## incomplete associated constant
Rating: 
Issues: none
Notes: 
Legacy: 

## incomplete associated function
Rating: 
Issues: none
Notes: 
Legacy: 

## incomplete associated type
Rating: 
Issues: none
Notes: 
Legacy: 

## index expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## indexable type
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## indexed deconstructor
Rating: 
Issues: none
Notes: 
Legacy: 

## indexed field selector
Rating: 
Issues: none
Notes: 
Legacy: 

## indexed initializer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## indexed operand
Rating: 4 (mostly-clear)
Issues: regression-vs-legacy
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: better - legacy is more detailed.

## indexing operand
Rating: 3 (adequate)
Issues: missing-discriminator, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## indirection type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## inert attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## inferred constant
Rating: 
Issues: none
Notes: 
Legacy: 

## inferred type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## infinite loop
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## infinite loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## inherent implementation
Rating: 
Issues: none
Notes: 
Legacy: 

## Initialization
Rating: 
Issues: none
Notes: 
Legacy: 

## initialization expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## initialization type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## initialized
Rating: 
Issues: none
Notes: 
Legacy: 

## inline
Rating: 
Issues: none
Notes: 
Legacy: 

## Inline assembly
Rating: 
Issues: none
Notes: 
Legacy: 

## inline module
Rating: 
Issues: none
Notes: 
Legacy: 

## inlined
Rating: 
Issues: none
Notes: 
Legacy: 

## inlining
Rating: 
Issues: none
Notes: 
Legacy: 

## inner attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## inner block doc
Rating: 
Issues: none
Notes: 
Legacy: 

## inner doc comment
Rating: 
Issues: none
Notes: 
Legacy: 

## inner line doc
Rating: 
Issues: none
Notes: 
Legacy: 

## input lifetime
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## input register
Rating: 
Issues: none
Notes: 
Legacy: 

## input register expression
Rating: 
Issues: none
Notes: 
Legacy: 

## input-output register expression
Rating: 
Issues: none
Notes: 
Legacy: 

## integer literal
Rating: 
Issues: none
Notes: 
Legacy: 

## integer suffix
Rating: 
Issues: none
Notes: 
Legacy: 

## integer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## integer type variable
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Interior mutability
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## intermediate match arm
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Invariant
Rating: 2 (low-signal)
Issues: low-signal
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## irrefutable constant
Rating: 
Issues: none
Notes: 
Legacy: 

## irrefutable pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## isize
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## item
Rating: 
Issues: none
Notes: 
Legacy: 

## item scope
Rating: 
Issues: none
Notes: 
Legacy: 

## item statement
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## iteration expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## keyword
Rating: 
Issues: none
Notes: 
Legacy: 

## label
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## label block
Rating: 
Issues: none
Notes: 
Legacy: 

## label indication
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## label namespace
Rating: 
Issues: none
Notes: 
Legacy: 

## label scope
Rating: 
Issues: none
Notes: 
Legacy: 

## language prelude
Rating: 
Issues: none
Notes: 
Legacy: 

## layout
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## lazy and expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## lazy boolean expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## lazy or expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Least upper bound coercion
Rating: 2 (low-signal)
Issues: missing-discriminator, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## left operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## less-than expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## less-than-or-equals expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## let binding
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## let initializer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## let statement
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## lexical element
Rating: 
Issues: none
Notes: 
Legacy: 

## library crate
Rating: 
Issues: none
Notes: 
Legacy: 

## lifetime
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## lifetime argument
Rating: 
Issues: none
Notes: 
Legacy: 

## lifetime bound
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## lifetime bound predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## Lifetime elision
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## lifetime namespace
Rating: 
Issues: none
Notes: 
Legacy: 

## lifetime parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## lifetime variable
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## limits attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## line
Rating: 
Issues: none
Notes: 
Legacy: 

## line comment
Rating: 
Issues: none
Notes: 
Legacy: 

## link
Rating: 
Issues: none
Notes: 
Legacy: 

## link_name
Rating: 
Issues: none
Notes: 
Legacy: 

## link_ordinal
Rating: 
Issues: none
Notes: 
Legacy: 

## link_section
Rating: 
Issues: none
Notes: 
Legacy: 

## literal
Rating: 
Issues: none
Notes: 
Legacy: 

## literal expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## literal pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Literal pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## local trait
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## local type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## local variable
Rating: 
Issues: none
Notes: 
Legacy: 

## loop
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## loop body
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## macro
Rating: 
Issues: none
Notes: 
Legacy: 

## macro attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## Macro expansion
Rating: 
Issues: none
Notes: 
Legacy: 

## macro implementation function
Rating: 
Issues: none
Notes: 
Legacy: 

## macro invocation
Rating: 
Issues: none
Notes: 
Legacy: 

## macro match
Rating: 
Issues: none
Notes: 
Legacy: 

## macro matcher
Rating: 
Issues: none
Notes: 
Legacy: 

## Macro matching
Rating: 
Issues: none
Notes: 
Legacy: 

## macro namespace
Rating: 
Issues: none
Notes: 
Legacy: 

## macro repetition
Rating: 
Issues: none
Notes: 
Legacy: 

## macro repetition in matching
Rating: 
Issues: none
Notes: 
Legacy: 

## macro repetition in transcription
Rating: 
Issues: none
Notes: 
Legacy: 

## macro rule
Rating: 
Issues: none
Notes: 
Legacy: 

## macro statement
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## macro transcriber
Rating: 
Issues: none
Notes: 
Legacy: 

## Macro transcription
Rating: 
Issues: none
Notes: 
Legacy: 

## macro_export
Rating: 
Issues: none
Notes: 
Legacy: 

## macro_use
Rating: 
Issues: none
Notes: 
Legacy: 

## macro_use prelude
Rating: 
Issues: none
Notes: 
Legacy: 

## main function signature
Rating: 
Issues: none
Notes: 
Legacy: 

## match arm
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## match arm body
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## match arm guard
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## match arm matcher
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## match expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## matched argument operand
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## matched indexed deconstructor
Rating: 
Issues: none
Notes: 
Legacy: 

## matched indexed initializer
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## matched named deconstructor
Rating: 
Issues: none
Notes: 
Legacy: 

## matched named initializer
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## matched shorthand deconstructor
Rating: 
Issues: none
Notes: 
Legacy: 

## matched shorthand initializer
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## matched tuple struct subpattern
Rating: 
Issues: none
Notes: 
Legacy: 

## matched tuple subpattern
Rating: 
Issues: none
Notes: 
Legacy: 

## memory size
Rating: 
Issues: none
Notes: 
Legacy: 

## metavariable
Rating: 
Issues: none
Notes: 
Legacy: 

## metavariable indication
Rating: 
Issues: none
Notes: 
Legacy: 

## method
Rating: 
Issues: none
Notes: 
Legacy: 

## method call expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## method operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Method resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## Method resolution implementation candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## Method resolution inherent implementation candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## Method resolution receiver candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## Method resolution trait implementation candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## mixed site hygiene
Rating: 
Issues: none
Notes: 
Legacy: 

## modifying operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## module
Rating: 
Issues: none
Notes: 
Legacy: 

## module path
Rating: 
Issues: none
Notes: 
Legacy: 

## modules attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## move type
Rating: 
Issues: none
Notes: 
Legacy: 

## multi segment path
Rating: 
Issues: none
Notes: 
Legacy: 

## multiplication assignment
Rating: 3 (adequate)
Issues: missing-scope, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy intentionally uses alias-only.

## multiplication assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## multiplication expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## mutability
Rating: 
Issues: none
Notes: 
Legacy: 

## mutable
Rating: 
Issues: none
Notes: 
Legacy: 

## mutable assignee expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## mutable binding
Rating: 
Issues: none
Notes: 
Legacy: 

## mutable borrow
Rating: 
Issues: none
Notes: 
Legacy: 

## mutable borrow expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## mutable place expression
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## mutable place expression context
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## mutable raw borrow expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## mutable raw pointer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## mutable reference
Rating: 
Issues: none
Notes: 
Legacy: 

## mutable reference type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## mutable static
Rating: 
Issues: none
Notes: 
Legacy: 

## mutable variable
Rating: 
Issues: none
Notes: 
Legacy: 

## naked
Rating: 
Issues: none
Notes: 
Legacy: 

## name
Rating: 
Issues: none
Notes: 
Legacy: 

## named block expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## named deconstructor
Rating: 
Issues: none
Notes: 
Legacy: 

## named field selector
Rating: 
Issues: none
Notes: 
Legacy: 

## named initializer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## named loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## named register argument
Rating: 
Issues: none
Notes: 
Legacy: 

## namespace
Rating: 
Issues: none
Notes: 
Legacy: 

## namespace context
Rating: 
Issues: none
Notes: 
Legacy: 

## NaN-boxing
Rating: 
Issues: none
Notes: 
Legacy: 

## negation expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## nesting import
Rating: 
Issues: none
Notes: 
Legacy: 

## never type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## no_builtins
Rating: 
Issues: none
Notes: 
Legacy: 

## no_implicit_prelude
Rating: 
Issues: none
Notes: 
Legacy: 

## no_link
Rating: 
Issues: none
Notes: 
Legacy: 

## no_main
Rating: 
Issues: none
Notes: 
Legacy: 

## no_mangle
Rating: 
Issues: none
Notes: 
Legacy: 

## no_std
Rating: 
Issues: none
Notes: 
Legacy: 

## non-exhaustive type
Rating: 
Issues: none
Notes: 
Legacy: 

## non-exhaustive variant
Rating: 
Issues: none
Notes: 
Legacy: 

## non-reference pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## non_exhaustive
Rating: 
Issues: none
Notes: 
Legacy: 

## not configuration predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## not-equals expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## null
Rating: 
Issues: none
Notes: 
Legacy: 

## numeric cast
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## numeric literal
Rating: 
Issues: none
Notes: 
Legacy: 

## numeric literal pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## numeric type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## object safe
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Object safety
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## obligations
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## obsolete range pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## octal literal
Rating: 
Issues: none
Notes: 
Legacy: 

## operand
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## operator expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## opt-out trait bound
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## or-pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## outer attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## outer block doc
Rating: 
Issues: none
Notes: 
Legacy: 

## outer doc comment
Rating: 
Issues: none
Notes: 
Legacy: 

## outer line doc
Rating: 
Issues: none
Notes: 
Legacy: 

## outline module
Rating: 
Issues: none
Notes: 
Legacy: 

## outlives bound
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## output lifetime
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## output register
Rating: 
Issues: none
Notes: 
Legacy: 

## output register expression
Rating: 
Issues: none
Notes: 
Legacy: 

## overlap
Rating: 
Issues: none
Notes: 
Legacy: 

## owner
Rating: 
Issues: none
Notes: 
Legacy: 

## Ownership
Rating: 
Issues: none
Notes: 
Legacy: 

## panic
Rating: 
Issues: none
Notes: 
Legacy: 

## panic_handler
Rating: 
Issues: none
Notes: 
Legacy: 

## parenthesized expression
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## parenthesized pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Parenthesized pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## parenthesized type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## partially hygienic
Rating: 
Issues: none
Notes: 
Legacy: 

## passing convention
Rating: 
Issues: none
Notes: 
Legacy: 

## path
Rating: 
Issues: none
Notes: 
Legacy: 

## path attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## path expression
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## Path expression resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## Path expression resolution implementation candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## Path expression resolution inherent implementation candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## Path expression resolution trait implementation candidate lookup
Rating: 
Issues: none
Notes: 
Legacy: 

## path pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Path pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## path prefix
Rating: 
Issues: none
Notes: 
Legacy: 

## Path resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## path segment
Rating: 
Issues: none
Notes: 
Legacy: 

## pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## pattern-without-alternation
Rating: 
Issues: none
Notes: 
Legacy: 

## pattern-without-range
Rating: 
Issues: none
Notes: 
Legacy: 

## place
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## place expression
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## place expression context
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## plane
Rating: 
Issues: none
Notes: 
Legacy: 

## pointer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## pointer type
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## pointer-to-address cast
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## positional register argument
Rating: 
Issues: none
Notes: 
Legacy: 

## Precedence
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## prelude
Rating: 
Issues: none
Notes: 
Legacy: 

## prelude attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## prelude entity
Rating: 
Issues: none
Notes: 
Legacy: 

## prelude name
Rating: 
Issues: none
Notes: 
Legacy: 

## Primitive representation
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## primitive-to-integer cast
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## principal trait
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## Private visibility
Rating: 
Issues: none
Notes: 
Legacy: 

## proc-macro crate
Rating: 
Issues: none
Notes: 
Legacy: 

## proc_macro
Rating: 
Issues: none
Notes: 
Legacy: 

## proc_macro_attribute
Rating: 
Issues: none
Notes: 
Legacy: 

## proc_macro_derive
Rating: 
Issues: none
Notes: 
Legacy: 

## procedural macro
Rating: 
Issues: none
Notes: 
Legacy: 

## program entry point
Rating: 
Issues: none
Notes: 
Legacy: 

## Public visibility
Rating: 
Issues: none
Notes: 
Legacy: 

## punctuator
Rating: 
Issues: none
Notes: 
Legacy: 

## pure identifier
Rating: 
Issues: none
Notes: 
Legacy: 

## qualified fn trait
Rating: 
Issues: none
Notes: 
Legacy: 

## qualified path expression
Rating: 
Issues: none
Notes: 
Legacy: 

## qualified type
Rating: 
Issues: none
Notes: 
Legacy: 

## qualified type path
Rating: 
Issues: none
Notes: 
Legacy: 

## qualifying trait
Rating: 
Issues: none
Notes: 
Legacy: 

## range expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range expression high bound
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range expression low bound
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## range pattern bound
Rating: 
Issues: none
Notes: 
Legacy: 

## range pattern high bound
Rating: 
Issues: none
Notes: 
Legacy: 

## range pattern low bound
Rating: 
Issues: none
Notes: 
Legacy: 

## Range pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## range-from expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range-from-to expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range-full expression
Rating: 0 (missing)
Issues: missing, regression-vs-legacy
Notes: No generated definition present.
Legacy: better - legacy is more detailed.

## range-inclusive expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range-to expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## range-to-inclusive expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## raw
Rating: 
Issues: none
Notes: 
Legacy: 

## raw borrow expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## raw byte string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## raw c string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## raw pointer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## raw pointer type
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## raw string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## reachable control flow path
Rating: 
Issues: none
Notes: 
Legacy: 

## receiver operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## receiver type
Rating: 
Issues: none
Notes: 
Legacy: 

## record enum variant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## record struct
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## record struct field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## record struct pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Record struct pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## record struct type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## record struct value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## recursion_limit
Rating: 
Issues: none
Notes: 
Legacy: 

## recursive type
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: worse - legacy is shorter or less specific.

## reference
Rating: 
Issues: none
Notes: 
Legacy: 

## reference identifier pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## reference pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Reference pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## reference type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## referent
Rating: 
Issues: none
Notes: 
Legacy: 

## refutability
Rating: 
Issues: none
Notes: 
Legacy: 

## refutable constant
Rating: 
Issues: none
Notes: 
Legacy: 

## refutable pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## refutable type
Rating: 
Issues: none
Notes: 
Legacy: 

## register
Rating: 
Issues: none
Notes: 
Legacy: 

## register argument
Rating: 
Issues: none
Notes: 
Legacy: 

## register class
Rating: 
Issues: none
Notes: 
Legacy: 

## register class argument
Rating: 
Issues: none
Notes: 
Legacy: 

## register class name
Rating: 
Issues: none
Notes: 
Legacy: 

## register expression
Rating: 
Issues: none
Notes: 
Legacy: 

## register name
Rating: 
Issues: none
Notes: 
Legacy: 

## register parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## register parameter modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## remainder assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## remainder assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## remainder expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## renaming
Rating: 
Issues: none
Notes: 
Legacy: 

## repeat operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## repetition index
Rating: 
Issues: none
Notes: 
Legacy: 

## repetition operator
Rating: 
Issues: none
Notes: 
Legacy: 

## repr
Rating: 
Issues: none
Notes: 
Legacy: 

## representation
Rating: 0 (missing)
Issues: missing
Notes: No generated definition present.
Legacy: same - same wording and scope.

## representation modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## reserved keyword
Rating: 
Issues: none
Notes: 
Legacy: 

## resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## resolution context
Rating: 
Issues: none
Notes: 
Legacy: 

## rest pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## return expression
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## return type
Rating: 
Issues: none
Notes: 
Legacy: 

## right operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Rule matching
Rating: 
Issues: none
Notes: 
Legacy: 

## runtime attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## Rust ABI
Rating: 
Issues: none
Notes: 
Legacy: 

## rustc
Rating: 
Issues: none
Notes: 
Legacy: 

## safety invariant
Rating: 
Issues: none
Notes: 
Legacy: 

## scalar type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## scope
Rating: 
Issues: none
Notes: 
Legacy: 

## scope hierarchy
Rating: 
Issues: none
Notes: 
Legacy: 

## scoping construct
Rating: 
Issues: none
Notes: 
Legacy: 

## selected field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Self
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## self input lifetime
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## self parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## self public modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## Self scope
Rating: 
Issues: none
Notes: 
Legacy: 

## send type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## separator
Rating: 
Issues: none
Notes: 
Legacy: 

## sequence type
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## shadowing
Rating: 
Issues: none
Notes: 
Legacy: 

## shared borrow
Rating: 
Issues: none
Notes: 
Legacy: 

## shared reference
Rating: 
Issues: none
Notes: 
Legacy: 

## shared reference type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## shift left assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## shift left assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## shift left expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## shift right assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## shift right assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## shift right expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## shorthand deconstructor
Rating: 
Issues: none
Notes: 
Legacy: 

## shorthand initializer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## should_panic
Rating: 
Issues: none
Notes: 
Legacy: 

## signed integer type
Rating: 3 (adequate)
Issues: missing-discriminator, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## simple byte string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## simple c string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## simple import
Rating: 
Issues: none
Notes: 
Legacy: 

## simple import path
Rating: 
Issues: none
Notes: 
Legacy: 

## simple path
Rating: 
Issues: none
Notes: 
Legacy: 

## simple path prefix
Rating: 
Issues: none
Notes: 
Legacy: 

## simple path public modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## simple path resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## simple public modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## simple punctuator
Rating: 
Issues: none
Notes: 
Legacy: 

## simple register expression
Rating: 
Issues: none
Notes: 
Legacy: 

## simple string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## single segment path
Rating: 
Issues: none
Notes: 
Legacy: 

## size
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: worse - legacy is shorter or less specific.

## size operand
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## sized type
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## slice
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## slice pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Slice pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## slice type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## source file
Rating: 
Issues: none
Notes: 
Legacy: 

## specialized cast
Rating: 2 (low-signal)
Issues: missing-discriminator, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## statement
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## static
Rating: 
Issues: none
Notes: 
Legacy: 

## static initializer
Rating: 
Issues: none
Notes: 
Legacy: 

## static lifetime elision
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## str
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## strict keyword
Rating: 
Issues: none
Notes: 
Legacy: 

## string literal
Rating: 
Issues: none
Notes: 
Legacy: 

## struct
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## struct expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## struct field
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## struct pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## struct type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## struct value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## structurally equal
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subexpression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subject expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subject let expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subpattern
Rating: 
Issues: none
Notes: 
Legacy: 

## subtraction assignment
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## subtraction assignment expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subtraction expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subtrait
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## subtype
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## subtyping
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## suffixed float
Rating: 
Issues: none
Notes: 
Legacy: 

## suffixed integer
Rating: 
Issues: none
Notes: 
Legacy: 

## super public modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## supertrait
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## sym path expression
Rating: 
Issues: none
Notes: 
Legacy: 

## sync type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## syntactic category
Rating: 
Issues: none
Notes: 
Legacy: 

## tail expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## target type
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## target_feature
Rating: 
Issues: none
Notes: 
Legacy: 

## temporary
Rating: 
Issues: none
Notes: 
Legacy: 

## terminated
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## terminated macro invocation
Rating: 
Issues: none
Notes: 
Legacy: 

## test
Rating: 
Issues: none
Notes: 
Legacy: 

## testing attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## testing function
Rating: 
Issues: none
Notes: 
Legacy: 

## textual macro scope
Rating: 
Issues: none
Notes: 
Legacy: 

## textual type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## thin pointer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## thin pointer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Token matching
Rating: 
Issues: none
Notes: 
Legacy: 

## Tokens
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## track_caller
Rating: 
Issues: none
Notes: 
Legacy: 

## trait
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## trait body
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## trait bound
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## trait implementation
Rating: 
Issues: none
Notes: 
Legacy: 

## Trait object lifetime elision
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: missing - not in legacy glossary.

## trait object type
Rating: 3 (adequate)
Issues: missing-discriminator, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## trait type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Transparent representation
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## trivial predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## true
Rating: 
Issues: none
Notes: 
Legacy: 

## tuple
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple enum variant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple enum variant value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple initializer
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Tuple pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## tuple struct
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple struct call expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple struct field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple struct pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Tuple struct pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## tuple struct type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple struct value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## tuple type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## type alias
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## type argument
Rating: 
Issues: none
Notes: 
Legacy: 

## type ascription
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## type attributes
Rating: 2 (low-signal)
Issues: missing-scope, truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: missing - not in legacy glossary.

## type bound predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## type cast expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Type coercion
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## Type inference
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## type inference root
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: same - similar scope and detail.

## type namespace
Rating: 
Issues: none
Notes: 
Legacy: 

## type parameter
Rating: 
Issues: none
Notes: 
Legacy: 

## type parameter initializer
Rating: 
Issues: none
Notes: 
Legacy: 

## type parameter type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## type path
Rating: 
Issues: none
Notes: 
Legacy: 

## Type path resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## Type representation
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## type specification
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Type unification
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## type variable
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## type_length_limit
Rating: 
Issues: none
Notes: 
Legacy: 

## u128
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## u16
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## u32
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## u64
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## u8
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## u8-to-char cast
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## unary operator
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## Undefined behavior
Rating: 
Issues: none
Notes: 
Legacy: 

## under resolution
Rating: 
Issues: none
Notes: 
Legacy: 

## underscore expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## underscore pattern
Rating: 
Issues: none
Notes: 
Legacy: 

## Underscore pattern matching
Rating: 
Issues: none
Notes: 
Legacy: 

## unhygienic
Rating: 
Issues: none
Notes: 
Legacy: 

## Unicode
Rating: 
Issues: none
Notes: 
Legacy: 

## unifiable
Rating: 2 (low-signal)
Issues: low-signal
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## unifiable types
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## unified type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unify
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## uninitialized
Rating: 
Issues: none
Notes: 
Legacy: 

## union
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## union field
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## union type
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## union value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unique immutable reference
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit enum variant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit struct
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit struct constant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit struct type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit struct value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit tuple
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unit value
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unnamed constant
Rating: 
Issues: none
Notes: 
Legacy: 

## unnamed lifetime
Rating: 2 (low-signal)
Issues: low-signal, regression-vs-legacy
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: better - legacy is more detailed.

## unqualified path expression
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe block
Rating: 2 (low-signal)
Issues: low-signal
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## unsafe block expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unsafe context
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe external block
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe function
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe function item type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unsafe function pointer type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## unsafe operation
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe Rust
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafe trait
Rating: 3 (adequate)
Issues: missing-scope
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## unsafe trait implementation
Rating: 
Issues: none
Notes: 
Legacy: 

## unsafety
Rating: 
Issues: none
Notes: 
Legacy: 

## unsigned integer type
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: same - similar scope and detail.

## unsized coercion
Rating: 2 (low-signal)
Issues: truncated
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## unsized type
Rating: 3 (adequate)
Issues: missing-discriminator
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: worse - legacy is shorter or less specific.

## unsuffixed float
Rating: 
Issues: none
Notes: 
Legacy: 

## unsuffixed integer
Rating: 
Issues: none
Notes: 
Legacy: 

## use capture
Rating: 3 (adequate)
Issues: missing-discriminator, regression-vs-legacy
Notes: Definition states the core relationship but lacks discriminators or edge cases.
Legacy: better - legacy is more detailed.

## use import
Rating: 
Issues: none
Notes: 
Legacy: 

## used
Rating: 
Issues: none
Notes: 
Legacy: 

## usize
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: same - similar scope and detail.

## validity invariant
Rating: 
Issues: none
Notes: 
Legacy: 

## value
Rating: 
Issues: none
Notes: 
Legacy: 

## value expression
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: worse - legacy is shorter or less specific.

## value expression context
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## value namespace
Rating: 
Issues: none
Notes: 
Legacy: 

## value operand
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## variable
Rating: 
Issues: none
Notes: 
Legacy: 

## variadic function
Rating: 
Issues: none
Notes: 
Legacy: 

## variadic part
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## Variance
Rating: 5 (clear)
Issues: none
Notes: Definition is clear, scoped, and self-contained with discriminators.
Legacy: missing - not in legacy glossary.

## Visibility
Rating: 
Issues: none
Notes: 
Legacy: 

## visibility modifier
Rating: 
Issues: none
Notes: 
Legacy: 

## Visible emptiness
Rating: 4 (mostly-clear)
Issues: none
Notes: Definition is clear and mostly scoped with at least one discriminator.
Legacy: missing - not in legacy glossary.

## visible empty enum variant
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## visible empty type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## weak keyword
Rating: 
Issues: none
Notes: 
Legacy: 

## where clause
Rating: 
Issues: none
Notes: 
Legacy: 

## where clause predicate
Rating: 
Issues: none
Notes: 
Legacy: 

## while let loop
Rating: 2 (low-signal)
Issues: low-signal
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## while let loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## while loop
Rating: 2 (low-signal)
Issues: low-signal
Notes: Definition is short or fragmentary and lacks usable scope.
Legacy: worse - legacy is shorter or less specific.

## while loop expression
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## whitespace character
Rating: 
Issues: none
Notes: 
Legacy: 

## whitespace string
Rating: 
Issues: none
Notes: 
Legacy: 

## windows_subsystem
Rating: 
Issues: none
Notes: 
Legacy: 

## zero-sized type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).

## zero-variant enum type
Rating: 5 (clear)
Issues: definition-same-role-change-expected
Notes: Generated definition matches legacy with :dt: -> :t: role-only change.
Legacy: same - role-only change (:dt: to :t:).
