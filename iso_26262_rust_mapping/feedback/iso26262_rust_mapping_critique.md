# Critique: ISO 26262-6:2018 to Rust 1.93.1 Complete Language and Standard Library Mapping (Rev 2)

## Overall Assessment

This document represents a serious and largely well-structured effort to map ISO 26262-6:2018 software-level requirements onto the Rust language. The graded classification system (P/HR/M/R/Q/X/U), the default-deny policy, and the method hazard taxonomy in Section 11.5 are all sound engineering choices that would provide real value to a consortium coding standard. The document's coverage of ISO 26262-6 clauses 5 through 11 and Annex C is broadly correct, and the traceability cross-reference in Section 1.6 is a useful navigational aid.

That said, the document has significant gaps—both in Rust technical accuracy and in ISO 26262 fidelity—that would undermine its credibility if presented to an assessor or adopted as-is by a project. The critique below is organized by theme and then by specific table/row findings.

---

## 1. Structural and Editorial Concerns

### 1.1 Section 2 should be removed or moved to an appendix

Section 2 ("Review Notes and Critiques of Draft v1") is internal editorial housekeeping. It is appropriate in a working draft circulated among subcommittee members, but in a document intended as a "reference for safety-critical Rust coding standards," it reads as unfinished. If the corrections have been applied, the section should either be deleted entirely or converted to a brief change-log appendix. An assessor reading this section will wonder whether the corrections were actually applied or merely noted.

### 1.2 "Complete" claim needs qualification

The title and Section 1 both claim a "complete language and standard library mapping." The inventories in Sections 10–11 are admirably thorough at the module level, but they are not complete at the item level. Several important types, traits, and API patterns are absent (detailed below). The document should either genuinely enumerate every stable public item—feasible via rustdoc JSON as the document itself recommends—or soften the "complete" claim to "module-level inventory with method-level classification rules."

### 1.3 Keyword table padding

The keyword table in Section 10.2 contains dozens of rows with the identical note "Fundamental language construct; apply category-specific rules elsewhere." This is technically correct but adds no information. Keywords like `as`, `break`, `const`, `continue`, `else`, `enum`, `fn`, `for`, `if`, `impl`, `in`, `let`, `loop`, `match`, `mod`, `move`, `mut`, `pub`, `ref`, `return`, `self`, `Self`, `struct`, `super`, `trait`, `true`, `type`, `use`, `where`, and `while` could be grouped into a single row ("Core syntax keywords: P at all ASIL levels; construct-specific restrictions are defined in Sections 10.3–10.8"). This would reduce table size by roughly 30 rows without losing information, and would make the rows that *do* carry restrictions (e.g., `async`, `dyn`, `extern`, `static`, `unsafe`, `union`) much more prominent.

Similarly, all reserved keywords share the identical note about `r#try`. These should be collapsed into a single row.

### 1.4 Rust version baseline

The document pins to "Rust stable 1.93.1 (2026-02-12)." This version identifier should be verified against the actual Rust release history. If this is a projected future version, the document should state that explicitly and flag the risk that the actual 1.93.1 stable API surface may differ. Additionally, the document should specify which target triples are in scope (e.g., `thumbv7em-none-eabihf` for automotive MCUs vs. `x86_64-unknown-linux-gnu` for tooling), since the available standard library surface varies significantly by target.

### 1.5 Missing document versioning strategy

Section 1.1 describes a re-assessment obligation when toolchain versions change, but the document lacks a formal versioning mechanism for itself. It should include a revision history table, a document owner, and a defined review cadence—this is standard practice for safety work products and would be expected by an assessor.

---

## 2. ISO 26262 Fidelity Issues

### 2.1 Missing coverage of Clause 6 (Software Safety Requirements)

The document maps Clauses 5, 7, 8, 9, 10, and 11, but omits Clause 6 entirely. Clause 6 addresses software safety requirements specification—including the derivation of software safety requirements from the technical safety concept, the specification of safety mechanisms, and the definition of hardware-software interface (HSI) requirements. While Clause 6 is less directly about coding guidelines, a coding standard should at minimum address how Rust's type system and trait contracts can be used to express and enforce software safety requirements, and how HSI specifications map to Rust HAL trait interfaces. The absence of Clause 6 is a structural gap that an assessor would notice.

### 2.2 Table 4 ASIL expectation values appear inverted

In Section 4.3, the walk-through method is listed as "++" at ASIL A and "o" at ASIL C/D. In the actual ISO 26262-6:2018 Table 4, walk-throughs are recommended across ASIL levels but are *less sufficient* at higher ASIL (where inspections and formal methods take over). The way the table is worded suggests walk-throughs become unimportant at ASIL C/D, when in reality they remain useful but are supplemented by more rigorous methods. The column values should be reviewed against the standard and the phrasing clarified—"o" typically means "no recommendation for or against," not "do not use."

### 2.3 ASIL decomposition is not addressed

ISO 26262 Part 9 defines ASIL decomposition, which allows splitting a safety requirement across redundant elements at lower ASIL levels. This has direct implications for which language subset applies to a given software element. A component at ASIL B(D) (decomposed from D) must still meet ASIL B coding requirements, but the redundancy argument may allow different profiles for each redundant path. The document should at least acknowledge this and provide guidance on how the ASIL profiles interact with decomposition.

### 2.4 Freedom from interference needs deeper treatment

Section 4.2 (Table 3, principle 1h) mentions spatial isolation and MPU/MMU partitioning, but freedom from interference (as defined in ISO 26262-6, Clause 7.4.11 and Part 9) encompasses spatial interference, temporal interference, and interference through communication. The Rust-specific implications are significant: Rust's memory safety guarantees address spatial interference within a single process, but temporal interference (timing/scheduling) and communication interference (shared buses, IPC) require additional analysis. The document should distinguish these three interference channels explicitly and map Rust mechanisms to each.

### 2.5 Confidence in use of software tools (ISO 26262-8, Clause 11)

Section 12 addresses tool qualification at a high level, but the document does not distinguish between Tool Confidence Level (TCL) 1, 2, and 3, nor between tool impact classes TI1 and TI2. For an assessor, the question is not just "is the tool qualified?" but "what is the TCL, and what evidence is required at that level?" The tool roles table (Section 12.2) should include a column for recommended TCL classification and the corresponding qualification method (increased confidence from use, evaluation, or development per ISO 26262-8 Table 4).

### 2.6 ISO 26262-6 Clause 5.4.3 language suitability argument is missing

Clause 5.4.3 requires an explicit argument for the suitability of the programming language, including consideration of language subsets, tool support, and the ability to model the required functionality. This is arguably the foundational justification for using Rust at all, and the document should include it—or at least reference a companion document that provides it. The language suitability argument should cover Rust's strengths (memory safety, algebraic types, no UB in safe code) and its challenges (no guaranteed WCET, evolving language, limited qualified toolchain ecosystem, no formal language standard in the ISO sense).

### 2.7 Dependent failure analysis is absent

ISO 26262-9 Clause 7 requires analysis of dependent failures (common cause and cascading failures). For Rust codebases, this should address: shared dependencies (crate DAG), shared toolchain components (a single rustc bug affecting all compiled code), and shared runtime behavior (e.g., the global allocator as a single point of failure). The document restricts the allocator to Q at higher ASIL but does not frame this as a dependent failure mitigation.

---

## 3. Rust Technical Accuracy Issues

### 3.1 The `as` keyword is P at all levels—but should not be

The keyword table classifies `as` as P/P/P/P/P with the note "Fundamental language construct; apply category-specific rules elsewhere." But `as` performs potentially lossy, silent truncation casts (e.g., `u32 as u8` truncates without warning), which Section 5.2 (Table 6, principle 1g) explicitly calls out as needing restriction. The keyword table should classify `as` as at least R at ASIL C/D, or the note must cross-reference the restriction in Section 5.2. As written, a reader could look at the keyword table in isolation and conclude that `as` is freely permitted—exactly the misinterpretation a coding standard should prevent.

### 3.2 `loop` as P/P/P/P/P is inconsistent with bounded-execution requirements

An unbounded `loop` without a provable termination condition is a WCET hazard and violates Table 3 principle 1f (scheduling properties) and Table 6 principle 1j (recursion/bounded iteration). The keyword itself is fine—`loop` with a `break` on a known condition is acceptable—but the blanket P classification with no note is misleading. At minimum, the note should state "Requires provable termination or documented infinite-loop justification (e.g., main event loop)" and the ASIL C/D columns should be R.

### 3.3 `try!` macro classified as U—should be X (deprecated, not unstable)

In Section 11.4, `try!` is classified as U ("Unstable; not allowed"). But `try!` is not unstable—it is *deprecated* in Edition 2018+ and is a hard error in Edition 2021+. Since the document's baseline is Edition 2024, `try!` cannot even compile. The classification should be X (Prohibited) with the note "Hard error in Edition 2024; use `?` instead."

### 3.4 The `safe` keyword is listed as U but was stabilized in Edition 2024

The `safe` contextual keyword (used in `extern` blocks to mark safe foreign functions) was stabilized as part of Rust 2024 edition semantics. The document's baseline is Edition 2024, so this keyword should be classified—likely R/R/R/Q/Q to parallel the `extern` block classification—not U. This is an important omission because `safe extern fn` is directly relevant to FFI safety arguments.

### 3.5 `#[repr(C)]` and `#[repr(transparent)]` should not share a row

These are lumped together as R/R/R/Q/Q, but they have very different risk profiles. `#[repr(transparent)]` is a zero-risk layout guarantee used constantly in newtype patterns (which the document itself recommends); restricting it to Q at ASIL C/D would prohibit common safe Rust patterns. `#[repr(C)]` is the one that introduces layout assumptions and FFI coupling. These should be separate rows with different classifications—`repr(transparent)` should be P or at most R, while `repr(C)` can remain Q at ASIL C/D.

### 3.6 Missing constructs in the language inventory

The following language-level constructs are absent from Section 10 and should be classified:

- **Closures (Fn/FnMut/FnOnce):** Closures capture state and can obscure data flow. They deserve a classification row, especially since closure captures changed semantics in Edition 2021 and can interact with lifetimes in non-obvious ways. At higher ASIL, restrictions on what closures may capture (no mutable references to shared state, no unbounded allocations) are warranted.

- **`ManuallyDrop<T>`:** This is a stable, safe-to-construct type that suppresses `Drop`, which has obvious safety implications. It should be classified explicitly—probably R at QM–B and Q at C/D.

- **`PhantomData<T>`:** Used to establish lifetime and variance relationships without runtime cost. Necessary for sound unsafe abstractions. Should be classified, likely P with a note about correct variance.

- **`Drop` trait and drop order guarantees:** The document mentions `Drop` side effects in passing (Section 5.2, principle 1h) but never classifies `Drop` implementations as a construct. Custom `Drop` impls change destruction order and can have visible side effects; they should be at least R at ASIL C/D with a requirement to document side effects.

- **`Deref`/`DerefMut` coercion chains:** The document notes this in Table 6, 1g but does not classify the traits themselves. Implicit deref coercion is a form of hidden data flow and should be restricted in public APIs at higher ASIL.

- **`core::sync::atomic` ordering semantics:** The document classifies `core::sync` as P/R/R/R/R with a brief note. But atomic memory orderings (`Relaxed`, `Release`, `Acquire`, `AcqRel`, `SeqCst`) have profoundly different correctness properties, and `Relaxed` in particular is a common source of subtle bugs. The standard library inventory should break out atomics as a distinct entry and require `SeqCst` by default for ASIL C/D, with weaker orderings permitted only with formal justification.

- **`NonNull<T>`:** A pointer type used extensively in unsafe abstractions. Should be classified as Q at ASIL C/D.

- **`Box::leak` and similar "escape hatch" APIs:** `Box::leak` converts owned allocation into a `&'static mut T`, sidestepping RAII. This should be explicitly X or Q.

- **Numeric literal suffixes and underscores:** Not a safety issue per se, but naming/readability conventions in ISO 26262 Table 1 suggest a rule (e.g., require suffixes on all numeric literals in safety code for clarity).

### 3.7 Debug vs. release behavior divergence is not addressed

Rust's debug builds include integer overflow checks (panicking on overflow) while release builds default to wrapping. This means a test suite run in debug mode exercises different behavior than production code—a serious concern for ISO 26262 verification. The document should require one of: (a) building release with `overflow-checks = true`, (b) using only explicit checked/saturating/wrapping arithmetic, or (c) running the test suite against the release profile. This omission undermines the structural coverage and unit verification arguments in Sections 6 and 7.

### 3.8 Build scripts (build.rs) are not addressed

Cargo build scripts execute arbitrary code at build time and can generate source files, set cfg flags, link native libraries, and affect compilation in ways that are invisible to source-level review. For a safety-critical project, build scripts should be classified and restricted—at minimum R with requirements for review and determinism, and Q or X at ASIL C/D. This is a significant gap in the "completeness" argument.

### 3.9 Missing treatment of `#[track_caller]`

This attribute changes the reported panic location, which is relevant for diagnostic accuracy. It should be classified (likely P with a note about its diagnostic purpose).

---

## 4. Table-by-Table Feedback

### 4.1 Section 3 — Table 1

**Row 1b (Language subsets):** The mapping recommends `#![forbid(unsafe_code)]` at the crate level for application crates. This is correct but should also mention `#![deny(clippy::undocumented_unsafe_blocks)]` in TCB crates to enforce the `// SAFETY:` justification requirement.

**Row 1d (Defensive implementation):** The mapping mentions checked/saturating arithmetic but does not reference the debug-vs-release overflow behavior divergence. Add a note requiring explicit overflow strategy independent of build profile.

**Row 1h (Naming conventions):** "Prohibit shadowing" is stated here, but the keyword table classifies `let` (which enables shadowing) as P at all levels. Cross-reference the restriction in Section 5.2 (Table 6, principle 1d) or add a note to the `let` keyword row.

**Row 1i (Concurrency):** This is one of the strongest rows. Consider adding a note about `core::sync::atomic` ordering restrictions and a requirement for concurrency testing tooling (e.g., Loom or similar model checkers).

### 4.2 Section 4 — Tables 2–4

**Table 3, Row 1f (Scheduling properties):** The note mentions `#[inline(never)]` for WCET analysis, but this is a tool-dependent workaround, not a principled solution. The document should note that Rust currently lacks guaranteed WCET analysis support and that this is a known gap requiring mitigation (e.g., timing measurement, vendor-specific WCET tools adapted for LLVM IR or Rust binaries).

**Table 3, Row 1h (Spatial isolation):** The note "Rust prevents many memory errors but not timing/resource interference" is important and correct. Strengthen this by explicitly listing what Rust does *not* prevent: stack overflow (no guaranteed stack probing on all targets), excessive CPU usage, priority inversion, and resource exhaustion via unbounded allocation.

**Table 4:** As noted in Section 2.2 above, verify all ASIL expectation values against the actual standard. The current values for walk-through appear inverted.

### 4.3 Section 5 — Tables 5–6

**Table 6, Row 1a (One entry/one exit):** The treatment is reasonable but should note that `?` desugars into a hidden match-and-early-return, which means functions using `?` have multiple exit points by definition. The ASIL C/D rule of "only `?` and single success return" is well-considered.

**Table 6, Row 1b (Dynamic objects):** This row conflates heap allocation with online testing. The ISO principle addresses both dynamic object creation *and* online test during production. The Rust mapping should explicitly state that test instrumentation (e.g., `#[cfg(test)]` modules) must not be compiled into production binaries.

**Table 6, Row 1d (No multiple use of variable names):** The restriction against shadowing is good. However, the document should distinguish between type-preserving rebinding (`let x = x.trim()`) and type-changing shadowing (`let x: u32 = x.parse()?`), since the latter is a more significant readability concern.

### 4.4 Section 6 — Tables 7–9

**Table 9 (Structural coverage):** The document correctly notes that monomorphization and inlining complicate coverage measurement, but it does not provide guidance on how to handle this. Recommended additions: require coverage measurement on optimized (release-profile) builds to match production behavior; specify whether generic instantiations must be covered independently; address the interaction between `#[inline(always)]` and coverage instrumentation.

### 4.5 Section 7 — Tables 10–12

**Table 10, Row 1e (Back-to-back model/code comparison):** This row applies only "if model-based design is used," but there is a Rust-specific back-to-back scenario the document misses: comparing debug-build behavior to release-build behavior, since overflow checks and debug assertions differ. This should be explicitly called out.

**Table 12 (Architectural-level structural coverage):** The note about monomorphization and function coverage is important. Add guidance on how to handle dead-code elimination: functions that the linker removes are not in the binary and therefore cannot be covered, but they may still contain safety-relevant logic. A pre-link coverage strategy or explicit `#[used]` annotations may be needed.

### 4.6 Section 8 — Tables 13–15

This section is thin. While it correctly notes that Clause 11 is not Rust-specific, there are Rust-specific considerations for embedded testing that deserve more treatment: cross-compilation fidelity (does the HIL target match the production target?), `no_std` testing strategies, and the fact that Rust's test harness (`libtest`) requires `std` and therefore cannot run on bare-metal targets without a custom test framework.

### 4.7 Section 10 — Language Inventory

**Section 10.1 (Global rules):** The rule "All public safety-related APIs shall have explicit lifetimes (no lifetime elision)" is well-intentioned but potentially counterproductive. Elision rules are deterministic and well-defined; requiring explicit lifetimes on functions like `fn len(&self) -> usize` adds noise without safety benefit. Consider restricting the no-elision rule to functions with multiple reference parameters or lifetime-parameterized return types, where the elision rules are non-obvious.

**Section 10.5 (Control flow):** The `match` construct is correctly classified as HR. The note should additionally state that `#[non_exhaustive]` types from external crates force wildcard arms, which conflicts with the ASIL C/D restriction against wildcard arms. Provide guidance on how to handle this tension (e.g., require a `_ => unreachable!()` with a tracking issue if the upstream type adds variants).

**Section 10.6 (Attributes):** Missing `#[must_use]`—this attribute is a safety-relevant enforcement mechanism and should be classified as HR (encourage its use on Result-returning functions and types with important side effects).

**Section 10.8 (Unsafe Rust):** The row for "Manual Send/Sync impls" is classified X/X/X/Q/Q. The X at QM seems overly restrictive—at QM, which is non-safety-classified, a blanket prohibition on manual Send/Sync impls is hard to justify. Consider R/R/R/Q/Q.

### 4.8 Section 11 — Standard Library Inventory

**`core::fmt` classified P/P/P/P/P:** This seems too permissive at ASIL C/D. Formatting can panic (e.g., positional argument errors in format strings) and may involve non-trivial computation. The std version is correctly restricted at C/D due to allocation, but even core::fmt should be at least R at ASIL D to ensure formatting panics cannot occur in safety-critical paths.

**Missing `std::sync::mpsc`:** The multi-producer single-consumer channel module is not listed. It should be classified—likely R at ASIL B–D due to potential blocking and the fact that `Receiver::recv()` blocks indefinitely.

**Missing `std::sync::OnceLock` / `LazyLock`:** These types are mentioned in the text (Section 5.2, principle 1e) as recommended replacements for `static mut` but are not classified in the library inventory. They should be explicitly classified, probably P/R/R/R/R since they involve one-time initialization with interior mutability.

**`std::collections` as a single row:** This is too coarse. `BTreeMap`/`BTreeSet` have fundamentally different determinism properties than `HashMap`/`HashSet`. The document recommends BTree variants for higher ASIL in Section 11.5.2 but does not reflect this in the module inventory. Consider splitting into ordered collections (more permissive) and hash-based collections (more restricted).

### 4.9 Section 11.5 — Method Hazard Taxonomy

This is one of the strongest parts of the document. The seven-level decision procedure is well-ordered and produces reasonable results for most APIs. However:

- **Step 3 (panicking methods):** "Unless the panic is proven unreachable and justified as a fatal invariant" is vague. Specify what constitutes acceptable proof: formal verification? Static analysis? Code review with documented argument? Test coverage of the non-panicking path? Different evidence levels should apply at different ASIL levels.

- **Step 4 (allocating methods):** "Typically X for ASIL D unless a qualified allocator and determinism argument exists" uses "typically," which introduces ambiguity. Either make it X with an explicit deviation process, or define the criteria for the exception.

- **The taxonomy does not address `const fn` evaluation:** A growing number of standard library functions are `const fn`, meaning they can execute at compile time. Const evaluation cannot panic at runtime (a compile-time panic is a build failure, not a safety hazard). The taxonomy should note that const-evaluated invocations of otherwise-panicking functions are safe and not subject to Step 3.

### 4.10 Section 12 — Tooling

**Missing Miri limitations:** The document recommends Miri for UB checking but does not note its limitations: Miri cannot check all UB (e.g., it does not model hardware-level behavior), it operates on MIR (not machine code), and it does not support all targets. These limitations should be documented so projects do not over-rely on Miri as a single line of defense.

**Missing cargo-vet / supply chain security:** The document mentions `cargo-audit` and `cargo-deny` for vulnerability and license auditing, but does not address `cargo-vet` or similar tools for reviewing the safety of third-party crate code. For ASIL C/D, every dependency crate should undergo some form of code review or qualification, not just vulnerability scanning.

### 4.11 Section 13 — ASIL Profile Summary

**Async/await row:** "Prohibited by default; allow only with qualified runtime and evidence" at ASIL D is reasonable but should define what "qualified runtime" means. Is this a TCL-qualified executor? A formally verified scheduler? The term is too vague for a coding standard.

**Missing row for closures:** Closures are absent from the summary matrix despite being a pervasive language feature with capture semantics that affect data flow analysis.

---

## 5. Additional Topics That Should Be Addressed

### 5.1 Third-party crate governance

The document mentions `cargo-audit` and `cargo-deny` but provides no framework for evaluating, approving, or restricting third-party crates in safety-critical code. ISO 26262-8 Clause 12 (qualification of software components) applies to third-party crates. The coding standard should define a crate approval process (review, testing, ASIL-level classification), maximum dependency depth or complexity limits, and a crate allowlist mechanism analogous to the language-feature allowlist.

### 5.2 Link-time optimization (LTO) and its verification implications

LTO changes the final binary in ways that are not visible at the source level: function inlining across crate boundaries, dead-code elimination, and constant propagation. This affects traceability, structural coverage measurement, and debugging. The coding standard should state whether LTO is permitted and under what conditions, and how coverage evidence should account for LTO transformations.

### 5.3 Test framework limitations on `no_std` targets

Rust's built-in test harness requires `std`. Bare-metal targets cannot use `#[test]` without a custom test framework (which itself requires qualification). The coding standard should acknowledge this and recommend approved testing strategies for `no_std` targets (e.g., `defmt-test`, `embedded-test`, or custom harnesses).

### 5.4 MISRA C/C++ cross-reference

Many teams adopting Rust in automotive are migrating from C/C++ codebases governed by MISRA rules. A cross-reference appendix mapping MISRA C:2023 and MISRA C++:2023 directives to their Rust equivalents (whether enforced by design, by compiler, or by coding rule) would significantly aid adoption and assessor familiarity.

### 5.5 Interaction between editions and safety certification

The document pins Edition 2024 but does not discuss what happens when a project needs to migrate to a future edition. Edition changes can alter semantics (e.g., closure capture rules changed in 2021, `unsafe extern` block semantics changed in 2024). The coding standard should require a safety impact analysis for any edition migration.

---

## 6. Summary of Priority Recommendations

The following items are ranked by their impact on the document's fitness for use as a coding standard input:

1. **Address the debug-vs-release behavior divergence** (overflow checks, debug_assert). This is a Rust-specific verification gap that directly undermines the structural coverage and unit testing arguments. (Sections 6, 7, 10)

2. **Split `#[repr(C)]` and `#[repr(transparent)]`** into separate rows with different classifications. The current grouping would prohibit common safe newtype patterns at ASIL C/D. (Section 10.6)

3. **Reclassify `as` to at least R at ASIL C/D** in the keyword table, or add an explicit cross-reference to the restriction in Section 5.2. (Section 10.2)

4. **Add the missing language constructs** (closures, `ManuallyDrop`, `PhantomData`, `Drop` impls, `Deref`/`DerefMut`, atomic orderings, `NonNull`, `Box::leak`). (Section 10)

5. **Address ISO 26262-6 Clause 6** (software safety requirements) and **Clause 5.4.3** (language suitability argument). (Section structure)

6. **Define what "qualified runtime" and "proven unreachable" mean** in operational terms. Vague phrases undermine enforceability. (Sections 11.5, 13)

7. **Add build.rs / build script governance.** Build scripts are an uncontrolled code execution vector that is invisible to source review. (New subsection in Section 10 or 12)

8. **Expand Section 12** with TCL classifications, Miri limitations, and supply-chain review (cargo-vet). (Section 12)

9. **Add third-party crate governance framework.** Without it, the default-deny policy is bypassed by every `cargo add`. (New section or subsection)

10. **Remove or relegate Section 2** and add a formal revision history table with document owner and review cadence. (Section 2)
