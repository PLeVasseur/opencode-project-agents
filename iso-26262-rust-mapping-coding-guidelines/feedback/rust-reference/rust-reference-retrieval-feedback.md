# Feedback: Rust Reference Retrieval (“Queryable Rust Reference”) Review

This feedback is based on the review bundle `query-review-handoff-20260222`, specifically:

- `PROCESS_OVERVIEW.md`
- `FIVE_QUERIES_AND_OUTPUTS.md`
- Five captured retrieval payloads in `query_outputs/*__hybrid.json` (prompt IDs `RET-RESOLVE-001` … `RET-RESOLVE-005`)

The intent here is **quality review of retrieval behavior** for *ISO 26262 Part 6, Table 1*-style prompts: whether the returned evidence is practically useful, and whether the “row projection” is trustworthy.

---

## Snapshot of the capture setup (for context)

From the bundle:

- Corpus style: **statement-first**
- Corpus size: **2,896 statements**
- Mode: `hybrid` (non-degraded), `top_k=8`, `candidate_limit=200`
- Embeddings model: `Qwen/Qwen3-Embedding-4B`
- Reranker model: `BAAI/bge-reranker-v2-m3`

---

## Executive summary

- **Strong foundation for auditability:** statement IDs + stable anchors are great for building a traceable evidence trail (important for safety cases).
- **Retrieval is best when the question matches Rust-Reference-native concepts** (e.g., “unsafe boundaries”, UB, soundness).
- **Several Table 1 topics cannot be covered well using the Rust Reference alone** (style, naming, “design principles”, graphical modeling, defensive programming patterns).
- **Row projection / row markers are currently too noisy to trust**: 70% of returned rows across these samples are marked as `1i` (Concurrency aspects), even when the underlying statement is not about concurrency.
- **Latency is high for interactive use** in these runs (~23.5s–50.1s/query with `candidate_limit=200` and reranking).

---

## What’s working well

### 1) Traceability and “evidence hygiene”
Each hit includes a `statement_id` and `source_anchor`, which makes it straightforward to:
- cite precise text,
- build claim → evidence mappings,
- reproduce and audit where each claim came from.

This is a real advantage for ISO 26262 work where reviewers want verifiable, stable references.

### 2) “Statement-first” granularity supports claim-by-claim mapping
Having atomic statements allows you to:
- avoid citing entire pages,
- align specific ISO table rows with specific language guarantees.

### 3) Retrieval quality is strong on “unsafe boundary control”
`RET-RESOLVE-004` (“What practices keep unsafe code boundaries controlled?”) is a good example: top hits correctly land on **UB constraints**, **soundness/unsoundness**, and the meaning of `unsafe` as “extra safety conditions.” This is exactly the kind of normative material the Rust Reference is good at.

### 4) `row_projection` explainability is a good idea
The `row_projection` includes an `evidence_trace` with per-statement contributions. This is the right direction for “why are you saying this supports row X?”—even though the current row-marker assignment needs work.

---

## What doesn’t seem to work well (or needs improvement)

### 1) Some prompts are not answerable from the Rust Reference alone
Several Table 1 intents map to *coding practice*, not *language definition*.

Examples from the captured prompts:

- `RET-RESOLVE-001` (“defensive error paths safely”) retrieves `panic`/unwinding semantics and `unsafe` cost tradeoffs. Those are relevant *facts*, but **they don’t answer “how should code handle defensive error paths”** as a guideline question.
- `RET-RESOLVE-002` (“features enforce strong typing”) retrieves a high-ranking statement from `influences` (“Rust is not a particularly original language…”). That’s a sign that the corpus **doesn’t contain enough “strong typing” phrasing**, and the query isn’t being rewritten into Rust-native terms (types, traits, coercions, casts, inference, etc.).

In short: **retrieval can only be as good as the match between the question language and the corpus language.**

### 2) Statement chunking is inconsistent (too small *and* too large)
Across the five runs, statement text sizes vary widely (e.g., minimum ~65–140 chars, maximum ~919–1012 chars depending on the prompt). This inconsistency tends to create two failure modes:

- **Too small:** contextless fragments that are semantically “nearby” but not directly actionable.
- **Too large:** big multi-bullet blocks that dilute the embedding signal and are hard to cite cleanly.

A consistent “concept chunk” (paragraph-sized, with a small context window) is often more reliable.

### 3) Row markers are heavily biased toward `1i` (concurrency)
Across the 5 captured queries (40 returned rows total), row marker assignments are skewed:

| Row marker | Count | % of all returned rows (n=40) |
|---|---:|---:|
| 1i | 28 | 70.0% |
| 1h | 6 | 15.0% |
| 1e | 2 | 5.0% |
| 1b | 1 | 2.5% |
| 1g | 1 | 2.5% |

This bias makes `row_projection` unreliable as an ISO Table 1 mapping aid right now: it will frequently claim “concurrency aspects” evidence where there isn’t any.

### 4) Scoring instrumentation is hard to interpret in places
In at least three cases, `lexical_score=1` while `bm25_raw=0`, `token_overlap_count=0`, and `phrase_match=0` (e.g., `RET-RESOLVE-002` rank 1, `RET-RESOLVE-004` rank 1). That makes it hard to reason about *why* something ranked well and to tune the system.

If these fields are meant for debugging/tuning, they should tell a consistent story (or be renamed to clarify what they measure).

### 5) Latency is likely too high for an interactive “guideline authoring tool”
Observed `duration_ms` in these five `hybrid` captures:

| Prompt | Duration (s) |
|---|---:|
| RET-RESOLVE-001 | 43.7 |
| RET-RESOLVE-002 | 50.1 |
| RET-RESOLVE-003 | 34.3 |
| RET-RESOLVE-004 | 23.5 |
| RET-RESOLVE-005 | 48.6 |

For interactive use, this will feel slow unless caching / candidate reduction / rerank optimization is applied.

---

## Would this help address ISO 26262-6 Part 6 Table 1 row-by-row?

### Where it can help (with the Rust Reference corpus)
- **1b — Use of language subsets:** *Potentially strong.* Safe Rust vs `unsafe` boundaries and UB constraints can be positioned as a “subset” story.
- **1c — Enforcement of strong typing:** *Potentially useful, but needs query rewriting +/or corpus expansion.* The Reference has type-system material, but the system should translate ISO phrasing into Rust terminology.
- **1i — Concurrency aspects:** *Potentially useful.* The Reference does include relevant constraints (e.g., data races as UB, `static mut` requiring `unsafe`).

### Where it’s only weakly helpful (needs more sources)
- **1d — Defensive implementation techniques:** The Reference explains panic/unwind and some error semantics, but it does not provide “defensive coding techniques” guidance. This needs additional “best practice” sources.

### Where it’s mostly the wrong corpus
- **1a — Low complexity:** typically enforced via coding rules, linting policy, architecture constraints.
- **1e — Well-trusted design principles:** mostly design guidance, not the Reference.
- **1f — Unambiguous graphical representation:** modeling/diagramming topic.
- **1g — Style guides / 1h — Naming conventions:** the Reference isn’t the style/naming guide.

**Bottom line:** this is a good *evidence source* for language guarantees, but not sufficient as “the tool” for Table 1 coverage without expanding the indexed sources and fixing row marker quality.

---

## Observations per captured prompt (top hits)

### RET-RESOLVE-001 — “defensive error paths safely”
- Returns `unsafe` cost tradeoff and `panic` semantics.
- Useful facts, but doesn’t directly produce guideline-ready advice about defensive error path patterns (Result/Option usage, error types, retry strategies, etc.).

Top 3 hits (abridged):
- `doc::unsafe-keyword.md::section:0003::statement:007` — Rust's type system is a conservative approximation of the dynamic safety requirements, so in some cases there is a performance cost to using safe code.
- `doc::panic.md::section:0001::statement:001` — r[panic.intro] Rust provides a mechanism to prevent a function from returning normally, and instead "panic," which is a response to an error condition that is typically not expected to be recoverable within the context in which the error is encountered. r[panic.lang-ops] Some language constructs, such as out-of-bounds [array indexing], panic automatically. r[panic.control] There are also language features that provide a level of control over panic behavior: * A [_panic handler_][panic handler] defines the behavior of a panic. * [FFI ABIs](items/functions.md#unwinding) may alter how panics behave. > [!NOTE] > The standard library provides the capability to explicitly panic via the [`panic!` macro][panic!]. r[panic.panic_handler]
- `doc::crates-and-source-files.md::section:0003::statement:001` — When a "foreign" unwind (e.g. an exception thrown from C++ code, or a `panic!` in Rust code using a different panic handler) propagates beyond the `main` function, the process will be safely terminated.

### RET-RESOLVE-002 — “strong typing”
- Top hit from `influences` suggests mismatch between ISO phrasing and corpus language.
- Consider query rewriting toward “type checking / trait bounds / coercions / casts / inference / exhaustiveness”.

Top 3 hits (abridged):
- `doc::influences.md::section:0001::statement:001` — Rust is not a particularly original language, with design elements coming from a wide range of sources.
- `doc::unsafe-keyword.md::section:0003::statement:007` — Rust's type system is a conservative approximation of the dynamic safety requirements, so in some cases there is a performance cost to using safe code.
- `doc::items::unions.md::section:0015::statement:002` — This is also true for many unmentioned aspects of Rust language (such as privacy, name resolution, type inference, generics, trait implementations, inherent implementations, coherence, pattern checking, etc etc etc).

### RET-RESOLVE-003 — “ownership and lifetimes mitigate memory safety”
- Hits are directionally relevant (lifetimes, UB constraints), but the top result is a narrow fact about lifetime defaults for trait objects. This is “true” but not the best summary evidence for “ownership mitigates memory safety concerns.”
- Suggest adding chunk context and query rewriting toward “borrow checker”, “aliasing”, “use-after-free”, “data race UB”, etc.

Top 3 hits (abridged):
- `doc::types::trait-object.md::section:0002::statement:003` — There are [defaults] that allow this lifetime to usually be inferred with a sensible choice.
- `doc::lifetime-elision.md::section:0013::statement:003` — If it is unable to resolve the lifetimes by its usual rules, then it will error.
- `doc::behavior-considered-undefined.md::section:0001::statement:011` — The exact liveness duration is not specified, but some bounds exist: * For references, the liveness duration is upper-bounded by the syntactic lifetime assigned by the borrow checker; it cannot be live any *longer* than that lifetime. * Each time a reference or box is dereferenced or reborrowed, it is considered live. * Each time a reference or box is passed to or returned from a function, it is considered live. * When a reference (but not a `Box`!) is passed to a function, it is live at least as long as that function call, again except if the `&T` contains an [`UnsafeCell<U>`].

### RET-RESOLVE-004 — “control unsafe boundaries”
- Best of the five: top results align with `unsafe` meaning, UB constraints, and soundness.
- This is a strong “yes” case for the approach.

Top 3 hits (abridged):
- `doc::behavior-considered-undefined.md::section:0001::statement:002` — This includes code within `unsafe` blocks and `unsafe` functions.
- `doc::behavior-considered-undefined.md::section:0001::statement:004` — `unsafe` code that satisfies this property for any safe client is called *sound*; if `unsafe` code can be misused by safe code to exhibit undefined behavior, it is *unsound*. > [!WARNING] > The following list is not exhaustive; it may grow or shrink.
- `doc::unsafe-keyword.md::section:0001::statement:002` — Specifically: - It is used to mark code that *defines* extra safety conditions that must be upheld elsewhere. - This includes `unsafe fn`, `unsafe static`, and `unsafe trait`. - It is used to mark code that the programmer *asserts* satisfies safety conditions defined elsewhere. - This includes `unsafe {}`, `unsafe impl`, `unsafe fn` without [`unsafe_op_in_unsafe_fn`], `unsafe extern`, and `#[unsafe(attr)]`.

### RET-RESOLVE-005 — “avoid data races”
- Contains a clearly relevant hit about `static mut` being a race-risk and requiring `unsafe`—good.
- The top hit about “UB list not guaranteeing stable semantics” is true, but not the strongest “data race avoidance” evidence.

Top 3 hits (abridged):
- `doc::behavior-considered-undefined.md::section:0001::statement:007` — In other words, this list does not say that anything will *definitely* always be undefined in all future Rust version (but we might make such commitments for some list items in the future). > > Please read the [Rustonomicon] before writing unsafe code. r[undefined.race] * Data races. r[undefined.pointer-access] * Accessing (loading from or storing to) a place that is [dangling] or [based on a misaligned pointer]. r[undefined.place-projection] * Performing a place projection that violates the requirements of [in-bounds pointer arithmetic](pointer#method.offset).
- `doc::items::static-items.md::section:0003::statement:002` — One of Rust's goals is to make concurrency bugs hard to run into, and this is obviously a very large source of race conditions or other bugs. r[items.static.mut.safety] For this reason, an `unsafe` block is required when either reading or writing a mutable static variable.
- `doc::type-layout.md::section:0016::statement:005` — In contrast, Rust’s [field-less enums] can only legally hold the discriminant values, everything else is [undefined behavior].

---

## What I would change (prioritized)

### 1) Fix row marker assignment before relying on `row_projection`
If the goal is “help me address each Table 1 row,” row markers need higher precision.

Concrete suggestions:
- Introduce **thresholding** and allow “no row marker” when the evidence is weak.
- Make row marker classification **semantic**, not lexical (Table 1 rows are categories, not keywords).
- Validate row markers with a **small hand-labeled set** and track precision/recall per row.

### 2) Retrieve context windows (while keeping atomic IDs)
Keep `statement_id` for citation, but retrieve:
- the statement,
- ±1–2 neighboring statements,
- section heading + page title.

This reduces contextless hits without losing traceability.

### 3) Clean the embedded text representation
For embedding/reranking, consider normalizing:
- admonition markers,
- heavy bullet formatting,
- reference-only artifacts.

Keep raw text for display, but embed a cleaner text view.

### 4) Add row-specific query rewriting (“ISO → Rust vocabulary”)
Example: “strong typing” → “type checking”, “trait bounds”, “generics”, “coercions”, “casts”, “exhaustive match”, etc.

Do this per Table 1 row to bridge terminology gaps.

### 5) Expand the indexed corpus for Table 1 completeness
To cover Table 1 meaningfully, add sources such as:
- Rust API Guidelines (naming, design, conventions)
- rustfmt + style guidance
- Clippy lint docs (complexity, correctness, pedantic rules)
- Rustonomicon (unsafe best practices)
- The Rust Book (idiomatic error handling, defensive patterns)
- Your internal modeling/coding guideline docs (so the system can answer “what do we require?”)

### 6) Reduce interactive latency
Potential options:
- Lower `candidate_limit` and rerank only the top-N semantic hits.
- Cache embeddings and rerank results per query.
- Consider a faster reranker or only rerank on-demand.

---

## Suggested next-step evaluation (lightweight)
Before “Table 1 mapping” becomes a dependency, consider:
- A labeled set of ~10–20 prompts per Table 1 row.
- Track: top-3 evidence precision, “row marker correctness,” and median latency.
- Iterate on query rewriting + row marker classifier until row projection is reliable enough to trust.

---
