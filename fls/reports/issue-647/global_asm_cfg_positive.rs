#![allow(dead_code)]

#[cfg(any(target_arch = "x86_64", target_arch = "x86"))]
core::arch::global_asm!(
    #[cfg(target_feature = "sse2")]
    "nop",
    "nop",
    #[cfg(target_feature = "sse2")]
    options(raw),
);

#[cfg(not(any(target_arch = "x86_64", target_arch = "x86")))]
const _ASM_CFG_GLOBAL_DUMMY: () = ();

// Argument indices are comma-separated positions inside `global_asm!(...)`.
// Attributes belong to the following argument.
//
// Argument index map:
// - arg[1] (lines 5-6): AssemblyTemplate -> #[cfg(...)] "nop".
// - arg[2] (line 7): AssemblyTemplate -> "nop".
// - arg[3] (lines 8-9): AssemblyAttributeAssemblyOption -> #[cfg(...)] options(raw).
//
// arg[1] expansion:
// - GlobalAsmArguments -> ( AssemblyCodeBlock , AssemblyAttributeRegisterArgument* , AssemblyAttributeAssemblyOption* ) (src/inline-assembly.rst:1633)
//   - Evidence: line 4.
// - AssemblyCodeBlock -> AssemblyTemplate ( , AssemblyTemplate )* (src/inline-assembly.rst:965)
// - AssemblyTemplate -> OuterAttribute* AssemblyInstruction (src/inline-assembly.rst:968)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 5): target_feature = "sse2".
//   - AssemblyInstruction -> StringLiteral (src/inline-assembly.rst:971)
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 5: `#[cfg(target_feature = "sse2")]`.
//     - Line 6: "nop".
//
// arg[2] expansion:
// - AssemblyTemplate -> OuterAttribute* AssemblyInstruction (src/inline-assembly.rst:968)
//   - OuterAttribute* -> empty.
//   - AssemblyInstruction -> StringLiteral (src/inline-assembly.rst:971)
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153)
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175)
//   - Evidence:
//     - Line 7: "nop".
//
// arg[3] expansion:
// - AssemblyAttributeAssemblyOption -> OuterAttribute* AssemblyOption (src/inline-assembly.rst:1642)
//   - OuterAttribute* -> OuterAttribute (src/attributes.rst:30)
//     - OuterAttribute -> # [ AttributeContent ] (src/attributes.rst:30)
//     - AttributeContent -> SimplePath AttributeInput? (src/attributes.rst:33)
//       - SimplePath -> SimplePathSegment -> Identifier (src/entities-and-resolution.rst:241, 244)
//         - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435)
//       - AttributeInput -> ( TokenTree* ) (src/attributes.rst:36)
//         - TokenTree -> DelimitedTokenTree | NonDelimitedToken (src/macros.rst:525-531)
//         - TokenTree* tokens (line 8): target_feature = "sse2".
//   - AssemblyOption -> options ( OptionList ) (src/inline-assembly.rst:1477)
//     - OptionList -> Option ( , Option )* (src/inline-assembly.rst:1480)
//       - Option -> raw (src/inline-assembly.rst:1483)
//   - Evidence:
//     - Line 8: `#[cfg(target_feature = "sse2")]`.
//     - Line 9: `options(raw)`.
//
// FLS rubric verification (Attributes):
// - fls_m0SBtonaNppV — "The :t:`[assembly instruction]s`, :t:`[register argument]s`, :t:`[ABI clobber]s`, and :t:`[assembly option]s` in :s:`AsmArguments` and :s:`GlobalAsmArguments` may be preceded by :t:`outer attribute` instances." (src/inline-assembly.rst:1656)
//   - Evidence:
//     - Lines 5-6: attribute on template.
//     - Lines 8-9: attribute on options.
// - fls_nLBhw2w6uznH — "Only the :t:`attribute` :c:`cfg` and the :t:`attribute` :c:`cfg_attr` are accepted on inline assembly arguments. All other attributes are rejected." (src/inline-assembly.rst:1659)
//   - Evidence:
//     - Lines 5 and 8: `#[cfg(...)]`.
// - fls_xzDPz2zfRfoI — "If a :t:`assembly instruction`, :t:`register argument`, :t:`ABI clobber`, or :t:`assembly option` is annotated with :c:`cfg` or :c:`cfg_attr` and the related :t:`configuration predicate` evaluates to ``false``, the annotated argument is not considered part of the related macro invocation, consistent with :t:`conditional compilation`." (src/inline-assembly.rst:1662)
//   - Evidence:
//     - Lines 5-6 and 8-9: arguments gated by `#[cfg(target_feature = "sse2")]` compile when false.
// - fls_cTEiqjf6haEg — "It is a static error for a :t:`register argument`, :t:`ABI clobber`, or :t:`assembly option` to appear before the first :t:`assembly instruction`, even if the argument is ignored by :t:`conditional compilation`." (src/inline-assembly.rst:1665)
//   - Evidence:
//     - Line 6: first argument is the template string "nop".
