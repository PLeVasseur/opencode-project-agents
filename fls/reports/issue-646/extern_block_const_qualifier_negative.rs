unsafe extern "C" {
    const fn const_api();
}

fn main() {}

// ExternalBlock derivation (src/ffi.rst:172-175):
// - ExternalBlock -> unsafe? extern AbiKind? { InnerAttributeOrDoc* ExternItem* }.
//   - unsafe? -> unsafe (line 1).
//   - extern (line 1).
//   - AbiKind -> StringLiteral (src/ffi.rst:48-50).
//     - StringLiteral -> SimpleStringLiteral (src/lexical-elements.rst:1153-1155).
//     - SimpleStringLiteral -> " SimpleStringContent* " (src/lexical-elements.rst:1175-1176).
//     - Evidence: line 1: "C".
//   - ExternItem -> ExternalItemWithVisibility (src/ffi.rst:177-178).
//   - ExternalItemWithVisibility -> FunctionDeclaration (src/ffi.rst:180-183).
//
// FunctionDeclaration derivation (src/functions.rst:15-16):
// - FunctionDeclaration -> FunctionQualifierList fn Name GenericParameterList? ( FunctionParameterList? ) ReturnType? WhereClause? ( FunctionBody | ; ).
//   - FunctionQualifierList -> const? async? ItemSafety? AbiSpecification? (src/functions.rst:18-19).
//     - const? -> const (line 2).
//   - Name -> Identifier (src/entities-and-resolution.rst:20-21).
//     - Identifier -> NonKeywordIdentifier -> PureIdentifier (src/lexical-elements.rst:435-450).
//     - Evidence: line 2: `const_api`.
//   - FunctionBody | ; -> ; (line 2).
//
// FLS rubric verification:
// - fls_qwchgvvnp0qe — "An external function shall not specify a FunctionQualifierList element other than ItemSafety." (src/ffi.rst:235-236)
//   - Evidence: line 2 specifies `const` in the qualifier list.
//
// Expected result (negative example): rustc rejects `const fn` in an extern block.
