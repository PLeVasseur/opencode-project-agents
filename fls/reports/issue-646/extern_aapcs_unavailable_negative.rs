extern "aapcs" {
    fn arm_only();
}

fn main() {}

// ExternalBlock derivation (src/ffi.rst:172-175):
// - ExternalBlock -> unsafe? extern AbiKind? { InnerAttributeOrDoc* ExternItem* }.
//   - unsafe? -> empty (line 1).
//   - extern (line 1).
//   - AbiKind -> StringLiteral (src/ffi.rst:48-50).
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153-1155).
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175-1176).
//     - Evidence: line 1: "aapcs".
//   - ExternItem -> ExternalItemWithVisibility (src/ffi.rst:177-178).
//   - ExternalItemWithVisibility -> FunctionDeclaration (src/ffi.rst:180-183).
//
// FunctionDeclaration derivation (src/functions.rst:15-16):
// - FunctionDeclaration -> FunctionQualifierList fn Name GenericParameterList? ( FunctionParameterList? ) ReturnType? WhereClause? ( FunctionBody | ; ).
//   - FunctionQualifierList -> const? async? ItemSafety? AbiSpecification? (src/functions.rst:18-19).
//     - all empty (line 2).
//   - Name -> Identifier (src/entities-and-resolution.rst:20-21).
//     - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435-450).
//     - Evidence: line 2: `arm_only`.
//   - FunctionBody | ; -> ; (line 2).
//
// FLS rubric verification:
// - fls_dbbfqaqa80r8 — "extern \"aapcs\" - The soft-float ABI for 32-bit ARM targets. Only available on 32-bit ARM targets." (src/ffi.rst:112-113)
//   - Evidence: line 1 uses `extern "aapcs"` on a non-ARM target.
//
// Expected result (negative example): rustc rejects `extern "aapcs"` on non-ARM targets.
