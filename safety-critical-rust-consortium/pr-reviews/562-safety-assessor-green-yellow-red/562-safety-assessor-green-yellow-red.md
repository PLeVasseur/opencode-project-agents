Right, that's line 29 column 80 of `iso26262.md`. It's the `Option'<T'>` thing I already flagged. MDX is parsing those apostrophes as JSX attribute syntax and choking on it. So the Netlify failure isn't a routing issue or `sidebar_position` conflict, it's that one line.

Here's the updated review with that corrected:

---

# PR #562 Review

Thanks for putting this up, @fried-gluttony.

The target audience (Functional Safety Manager deciding if Rust is viable) is the right one for this site, and the traffic-light scale communicates well for that audience.

I chair the Coding Guidelines Subcommittee. We already have ISO 26262-to-Rust language mapping work in progress that overlaps a lot with the gap analysis here. I'd like to coordinate rather than end up with parallel documents. More on that at the end.

Comments below anchored to lines in the diff.

---

## `intro.md`

### [Line 9 - `"...is defined by it's context."`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-a32db9c25999c2994e12a57575391694804b01e296fb588b705b0106c6ef569f-R9)

`it's` -> `its` (possessive).

### [Line 12 - `"...generally stems from malfcuntions..."`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-a32db9c25999c2994e12a57575391694804b01e296fb588b705b0106c6ef569f-R12)

`malfcuntions` -> `malfunctions`. Also `delimit` is awkward here, "to distinguish from Cybersecurity" reads better.

### [Line 23 - `"There might are also indirect requirements..."`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-a32db9c25999c2994e12a57575391694804b01e296fb588b705b0106c6ef569f-R23)

Grammar. Try: "There are also indirect requirements, e.g. that certain test coverage metrics need to be achieved - here we judge how well the existing toolchain and ecosystem can be used to satisfy these requirements."

### [Lines 32-46 - Standards overview section with TODOs](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-a32db9c25999c2994e12a57575391694804b01e296fb588b705b0106c6ef569f-R32)

The intro sets up ISO 26262, IEC 61508, and DO-178C, but only 26262 has content. I'd rather not land TODO stubs on the live site. A safety manager clicking through and hitting empty sections undermines confidence. Scope the intro to what's ready and expand later.

---

## `iso26262.md`

### [Line 2 - `sidebar_position: 1`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R2)

Both this and `intro.md` have `sidebar_position: 1`. One needs to change or the ordering breaks.

### [Line 11 - `"...requirement can't be met literally (ior doesn't make sense..."`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R11)

`(ior` -> `(or`, `apriori` -> `a priori`.

### [Line 26 - `clippy::cyclomatic_complexity`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R26)

Renamed to `clippy::cognitive_complexity`.

### [Line 29 - `"possible e.g. Option'<T'>, Result<T, E>"` (this is also the Netlify build failure)](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R29)

The apostrophes in `Option'<T'>` are what's breaking the deploy. MDX (Docusaurus uses it under the hood) is parsing the `<T'>` as a JSX tag and choking on the `'` character at column 80. The fix is to remove the apostrophes so it reads `Option<T>`, and then wrap it in backticks so MDX doesn't try to parse the angle brackets as JSX:

```
| **1d** | Use of defensive implementation techniques | possible e.g. `Option<T>`, `Result<T, E>` | 🟢 |
```

The Netlify error:

```
Cause: Unexpected character `'` (U+0027) in name, expected a name character
  such as letters, digits, `$`, or `_`; whitespace before attributes;
  or the end of the tag
```

You'll also want to audit the rest of the markdown for bare angle brackets (e.g. any `<T>` not wrapped in backticks) since MDX will try to parse those as JSX too.

### [Line 34 - Concurrency: `"native compile-time enforcable"` 🟢](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R34)

Rust prevents *data races* at compile time. It does not prevent deadlocks, priority inversions, or the broader class of concurrency hazards 26262 cares about. A safety manager seeing 🟢 here will assume more coverage than exists. Should be 🟡 with an explanation of what the compile-time guarantee actually covers.

`enforcable` -> `enforceable`. Appears throughout the doc.

### [Lines 67-70 - Table 4 items 1a-1d marked `"n.A. for Rust"`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R67)

Walk-throughs, inspections, simulation, prototyping are process methods, not language-specific. You do them the same way in Rust as in C. Marking them "n.A. for Rust" is wrong, and it's a conformity risk: an assessor could read this as the project deciding these activities don't apply. These should be 🟢.

### [Line 71 - `"creusat"`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R71)

**Creusot**. Also Kani, Verus, and Prusti should be listed here. The formal verification landscape for Rust is broader than one tool.

### [Line 87 - 1a: One entry and one exit point](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R87)

TBD is right here. Early returns, `?`, and panic paths all create multiple exit points. We've been working through what a sound tailoring argument looks like for this in the Coding Guidelines Subcommittee. Get in touch and we can share what we have.

### [Line 90 - 1d: `"shadowing possible, TBD clippy enforcable"`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R90)

`clippy::shadow_unrelated`, `shadow_reuse`, and `shadow_same` exist and are directly relevant. We've been evaluating which to recommend at different ASIL levels in the Coding Guidelines work.

### [Line 92 - 1f: `"disallow safe rust - pointer usage discouraged"` 🟢](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R92)

Inverted. This should say "disallow **unsafe** Rust" (restrict `unsafe` blocks and raw pointer usage). As written it says to disallow *safe* Rust, i.e. everything must be `unsafe`. Please fix this one.

### [Lines 107-109 - Table 7 items 1a-1c marked `"n.A. for Rust"`](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R107)

Same issue as Table 4. Walk-throughs, inspections, pair-programming are language-agnostic.

### [Lines 110-115 - Table 7 items 1d-1i using `+` and `o` symbols](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R110)

Inconsistent with the 🟢/🟡/🔴 scale used everywhere else.

### [Lines 116-117 - Requirements-based test / Interface test: `"inherent cargo test"` 🟢](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R116)

`cargo test` is a test runner. Requirements-based testing under 26262 means bidirectional traceability between safety requirements and test cases, documented test specs, coverage evidence. That's process + tooling, not something you get out of the box. Should be 🟡. (You mention `mantra` for traceability in 6-6, relevant here too.)

### [Line 128 - MC/DC: `"no tool support yet"` 🔴](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R128)

There's been active LLVM-level MC/DC instrumentation work and Rust nightly has experimental coverage improvements building on it. Check the current state before publishing, this is probably 🟡 now.

### [Lines 172-175 - Part 8 Supporting Processes / Tool Qualification 🔴](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562/files#diff-ec7fe1094871c324566fcbe9fe279dffd6bc16d03c0394528f15f8cfa36ff43e-R172)

Tool qualification is one of the biggest topics for Rust in safety-critical and it gets a single bullet. Qualifying `rustc`, `cargo`, `clippy`, LLVM is a massive effort and often the first thing a safety manager asks about. Ferrocene has already achieved ISO 26262 qualification, so qualified toolchains exist. This section needs real content, or at minimum a link to consortium resources and a mention of Ferrocene.

---

## General

### Spellcheck

Per Dale's comment, run a spellchecker. Additional catches: `enforcable` -> `enforceable` (multiple), `lifecylce` -> `lifecycle`, `requiremets` -> `requirements`, `ressources` -> `resources`.

### Coordination with existing work

The Coding Guidelines Subcommittee has ISO 26262 language mapping work in progress that overlaps heavily with this gap analysis. I'd like to get you involved in that rather than maintaining separate docs.
