# RISC-V Assembler

> I'm studying how to package a Python project.

## Changelog

| Version | Description     | Author                                             |
| ------- | --------------- | -------------------------------------------------- |
| 0.0.1   | Initial Version | [Nguyen Binh Khiem](https://github.com/khiemnb153) |

## Some WEIRD concepts in the project

- `ICB` - integer-coded-binary: present binary by `int` type. If binary value is number, it is 2's complement. It better than `str`, I think so.

## Supported features

### ISAs

- RVV (32-bit, integer) (See `VECTOR_INSTS` in [`supported_features.py`](./src/supported_features.py))
- RV32I (See `SCALAR_INSTS` in [`supported_features.py`](./src/supported_features.py))

### Sections

- `.text`
- `.data`

### Data types

- `.word`
- `.half`
- `.byte`

### Immediate formats

- Unsigned/Signed decimal
- Binary
- Hexadecimal

### Relocation Functions

- `%hi(symbol)`
- `%lo(symbol)`

### Data parser

- Check overall syntax
- Check supported types
- Check data sequence syntax
- Check data supported formats
- Check overflow data items (TODO)

### Text parser

- Check overall syntax
- Check supported instructions
- Check valid v/x registers
- Check supported immediate formats
