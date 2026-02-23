# Changed paragraph justification for ABI entry (PR 145954)

- Generated UTC: 2026-02-07T14:49:30.658964+00:00
- Source report: /home/pete.levasseur/opencode-project-agents/fls/reports/system-abi-variadic-tooling-restack-20260207T144017Z/integration-abi-dedupe-base.json
- Base ref: 0165ee6ad6e7e6a54705458d491810b0481b7df4
- Release: 1.93.0
- Changed source files: src/ffi.rst, src/glossary.rst
- Changed paragraphs analyzed: 12

## fls_36qrs2fxxvi7
- Location: src/ffi.rst (paragraph 21.1:19, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "cdecl" - The x86_32 ABI of C code.
- After:
  > extern "cdecl" - The x86_32 ABI of C code. Only available on x86_32 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 1da7fe0a23d93d524fed3110b8c116e9b7fe7f1563c51830ffd8b98ce562b9dd -> head_checksum 004d9eeb46c8b8e7fe56e07369710ee3888ff5858adce406211fd1c127589ab2).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_6rtj6rwqxojh
- Location: src/ffi.rst (paragraph 21.1:22, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "fastcall" - The fastcall ABI that corresponds to MSVC’s __fastcall and GCC and clang’s __attribute__((fastcall)).
- After:
  > extern "fastcall" - The fastcall ABI that corresponds to MSVC’s __fastcall and GCC and clang’s __attribute__((fastcall)). Only available on x86_32 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 42ee2288dd6a0bde172c2aa19bdd6c764e4c21913a22a4d9d65065b478aa14ba -> head_checksum d1ab4f75d7570b3dd18b52916d46e7ccc89412dde0c8de590454738da13462fc).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_7t7yxh94wnbl
- Location: src/ffi.rst (paragraph 21.1:24, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "sysv64" - The x86_64 non-Windows ABI of C code.
- After:
  > extern "sysv64" - The x86_64 non-Windows ABI of C code. Only available on x86_64 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum fab1088ce02afa3c8566f0f5033efbd1b6cfec69fc639a64273cc39e32f479e5 -> head_checksum 8c9dd7e26d0ac7848137053e02ff4d1bf697ebeda4fffdf9aecc209b1ac70621).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_CIyK8BYzzo26
- Location: src/ffi.rst (paragraph 21.1:20, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "cdecl-unwind" - The same as extern "cdecl" with the addition that unwinding across FFI is permitted.
- After:
  > extern "cdecl-unwind" - The same as extern "cdecl" with the addition that unwinding across FFI is permitted. Only available on x86_32 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum d0f9c8d00a857e8d69b98fadc01f1222ca7838660e92dbf4c571d07df302a222 -> head_checksum 6daa2acd28b53efb30508470bab25eb295aa4048771de06854e7f59f558ecd8e).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_UippZpUyYpHl
- Location: src/ffi.rst (paragraph 21.1:18, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "aapcs-unwind" - The same as extern "aapcs" with the addition that unwinding across FFI is permitted.
- After:
  > extern "aapcs-unwind" - The same as extern "aapcs" with the addition that unwinding across FFI is permitted. Only available on 32-bit ARM targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 3015fb781cf27af98cfdb17a199fc06a282c4995bf513e4f23460aa87a24fefd -> head_checksum 82d0577c99d015ca068892ae2f3cfb9413aba82cf68db7def1a94223a0643568).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_ccFdnlX5HIYk
- Location: src/ffi.rst (paragraph 21.1:25, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "sysv64-unwind" - The same as extern "sysv64" with the addition that unwinding across FFI is permitted.
- After:
  > extern "sysv64-unwind" - The same as extern "sysv64" with the addition that unwinding across FFI is permitted. Only available on x86_64 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 5d748e814d1f01129f8b66ffb05acc435c309ab75eeff0b4e74925cc1e8b786b -> head_checksum 577037ee9b115680a0388f72007131da469781b7d350d44e4b86ea46bd9e5120).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_d3nmpc5mtg27
- Location: src/ffi.rst (paragraph 21.1:23, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "stdcall" - The x86_32 ABI of the Win32 API.
- After:
  > extern "stdcall" - The x86_32 ABI of the Win32 API. Only available on x86_32 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum a81529042a5b1033d4dfd23dc355a422cafc5e8a94dac4134dcc1cdbe6d6b01d -> head_checksum 0e7d5ec67f95015898b88ba3209a029b1c0ae633f4a1486aa47d31477a6dada8).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_dbbfqaqa80r8
- Location: src/ffi.rst (paragraph 21.1:17, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "aapcs" - The soft-float ABI for 32-bit ARM targets.
- After:
  > extern "aapcs" - The soft-float ABI for 32-bit ARM targets. Only available on 32-bit ARM targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 1454a6149650f43e10f4254d309ba83ae39d3052b579c45d26bed5c429ce1bc4 -> head_checksum f577b535c2c2f8c758a06d1db3504e3712c7eabb74eec1a8d780730fbdfb6ade).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_qwchgvvnp0qe
- Location: src/ffi.rst (paragraph 21.3:3, section fls_yztwtek0y34v)
- Tags: paragraph-changed, role-change, syntax-ref-added
- Before:
  > An external function shall not specify a FunctionQualifierList.
- After:
  > An external function shall not specify a FunctionQualifierList element other than ItemSafety.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 9abb006e22c228a40953b442c54e63fd9a10cc675390d5e7d61b1fb7221ec353 -> head_checksum de9f485f04b3404d7ce4d58216257e17f2de15b1dc952d7dea17a95775c1e60b).
  - role-change: role inventory deltas (s: 1 -> 2).
  - syntax-ref-added: syntax reference count increased by 1.

## fls_sxj4vy39sj4g
- Location: src/ffi.rst (paragraph 21.1:26, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "vectorcall" - The vectorcall ABI that corresponds to MSVC’s __vectorcall and clang’s __attribute__((vectorcall)).
- After:
  > extern "vectorcall" - The vectorcall ABI that corresponds to MSVC’s __vectorcall and clang’s __attribute__((vectorcall)). Only available on x86 and x86_64 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum aa45e16b2c9fb1e7d7ecf23ca38806bc2f369b1d1be518e74d28e24e6b54a8b4 -> head_checksum 8752873f95907d15fb3ed380df983b5911f93d286139708dd8cd0712eec932b3).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_tyjs1x4j8ovp
- Location: src/ffi.rst (paragraph 21.1:27, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "win64" - The x86_64 Windows ABI of C code.
- After:
  > extern "win64" - The x86_64 Windows ABI of C code. Only available on x86_64 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 563032c0e9c472e10f9c487c70925926c24107c3258cc003fb04dd03b00c21af -> head_checksum 9d55689fb18bdcf91b46aba59293dcf50b59a0a72b094d22a4c1ef371881af56).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).

## fls_xrCRprWS13R1
- Location: src/ffi.rst (paragraph 21.1:28, section fls_usgd0xlijoxv)
- Tags: paragraph-changed, normative-shift
- Before:
  > extern "win64-unwind" - The same as extern "win64" with the addition that unwinding across FFI is permitted.
- After:
  > extern "win64-unwind" - The same as extern "win64" with the addition that unwinding across FFI is permitted. Only available on x86_64 targets.
- Why these tags apply:
  - paragraph-changed: paragraph checksum/markup changed (base_checksum 985fd96881b7c12b952e2f2a81cdc5713cd19ec157141a68232ac19172c96907 -> head_checksum b4db1e08fb09bcba2ff6e3fd2a102154976e492b52dd95ad3f010c5751f39ca8).
  - normative-shift: normative keyword counts changed (only: 0 -> 1).
