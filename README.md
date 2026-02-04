# PlayFair Cipher

Python implementation of the PlayFair cipher, a classical digraph substitution cipher developed in 1854.

## Overview

The PlayFair cipher encrypts pairs of letters using a matrix generated from a keyword. It was one of the first practical digraph substitution ciphers and was notably used in military communications.

This repository contains **two implementations**:
- **5×5 Traditional**: Classic PlayFair with 25 letters (I and J share position)
- **6×6 Extended**: Modern variant supporting alphanumeric text (A-Z, 0-9)

![Tests](https://github.com/YonAndualem/PlayFair-Cipher/actions/workflows/python-app.yml/badge.svg)

## Installation

```bash
git clone https://github.com/YonAndualem/PlayFair-Cipher.git
cd PlayFair-Cipher
```

No external dependencies required for core functionality. GUI requires `tkinter` (usually included with Python).

## Usage

### 5×5 Traditional Version

#### Graphical Interface

```bash
python3 main.py gui
```

#### Command Line Interface

```bash
python3 main.py cli
```

#### Run Tests

```bash
python3 main.py test
```

#### Programmatic Usage

```python
from src.cipher import PlayFairCipher

cipher = PlayFairCipher("KEYWORD")
ciphertext = cipher.encrypt("HELLO WORLD")
plaintext = cipher.decrypt(ciphertext)
```

### 6×6 Extended Version

#### Graphical Interface

```bash
python3 main6x6.py gui
```

#### Command Line Interface

```bash
python3 main6x6.py cli
```

#### Run Tests

```bash
python3 main6x6.py test
```

#### Programmatic Usage

```python
from src.cipher6x6 import PlayFairCipher6x6

cipher = PlayFairCipher6x6("CRYPTO2026")
ciphertext = cipher.encrypt("PASSWORD123")
plaintext = cipher.decrypt(ciphertext)
```

## Algorithm

### 5×5 Matrix Generation

1. Remove duplicate letters from keyword
2. Fill remaining spaces with alphabet (A-Z, excluding J)
3. Arrange in 5×5 grid

Example with keyword "MONARCHY":
```
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
```

### 6×6 Matrix Generation

1. Remove duplicate characters from keyword
2. Fill remaining spaces with unused letters (A-Z)
3. Add remaining digits (0-9)
4. Arrange in 6×6 grid

Example with keyword "CRYPTO2026":
```
C R Y P T O
2 6 A B D E
F G H I J K
L M N Q S U
V W X Z 0 1
3 4 5 7 8 9
```

### Encryption Rules

For each pair of letters:

1. **Same Row**: Replace with letters to the right (wrap around)
2. **Same Column**: Replace with letters below (wrap around)
3. **Rectangle**: Swap the columns of each letter

### Decryption

Apply inverse operations:
- Same row: shift left
- Same column: shift up
- Rectangle: swap columns (same operation)

## Project Structure

```
PlayFair-Cipher/
├── src/
│   ├── cipher.py       # 5×5 core algorithm
│   ├── cipher6x6.py    # 6×6 extended algorithm
│   ├── gui/
│   │   ├── app.py      # 5×5 graphical interface
│   │   └── app6x6.py   # 6×6 graphical interface
│   └── cli/
│       ├── demo.py     # 5×5 command-line interface
│       └── demo6x6.py  # 6×6 command-line interface
├── tests/
│   ├── test_cipher.py     # 5×5 test suite
│   └── test_cipher6x6.py  # 6×6 test suite
├── main.py             # 5×5 application entry point
├── main6x6.py          # 6×6 application entry point
└── README.md
```

## Features

### 5×5 Traditional Version
- **Core Implementation**: Clean, well-documented cipher algorithm
- **GUI Application**: Interactive visual interface with real-time encryption
- **CLI Tool**: Command-line demonstration and interactive mode
- **Test Suite**: Comprehensive unit tests
- **Historical Accuracy**: Implements the original PlayFair cipher

### 6×6 Extended Version
- **Alphanumeric Support**: Encrypt messages containing both letters and numbers
- **36-Character Matrix**: All 26 letters (A-Z) + 10 digits (0-9)
- **No Information Loss**: No character merging (unlike J→I in 5×5)
- **Modern Use Cases**: Perfect for passwords, codes, and alphanumeric messages
- **Same Interfaces**: GUI, CLI, and programmatic API

## Comparison: 5×5 vs 6×6

| Feature | 5×5 Traditional | 6×6 Extended |
|---------|----------------|--------------|
| Characters | 25 (A-Z, no J) | 36 (A-Z, 0-9) |
| Digit Support | ❌ No | ✅ Yes |
| Character Merging | J → I | None |
| Historical | ✅ Original | Modern variant |
| Use Cases | Text only | Alphanumeric |

## Technical Details

### 5×5 Text Preprocessing

- Converts to uppercase
- Replaces J with I
- Removes non-alphabetic characters
- Splits into digraphs (letter pairs)
- Inserts 'X' between duplicate letters
- Pads with 'X' if odd length

### 6×6 Text Preprocessing

- Converts to uppercase
- Removes non-alphanumeric characters
- Splits into digraphs (character pairs)
- Inserts 'X' between duplicate characters
- Pads with 'X' if odd length

### Matrix Properties

**5×5:**
- 5×5 grid containing 25 letters (I and J share a position)
- Generated deterministically from keyword
- Unique letter positioning ensures reversible encryption

**6×6:**
- 6×6 grid containing 36 characters (26 letters + 10 digits)
- Generated deterministically from keyword
- All alphanumeric characters supported
- No character sharing or merging

## Examples

### 5×5 Traditional

```python
from src.cipher import PlayFairCipher

# Create cipher
cipher = PlayFairCipher("SECRET")

# Encrypt
encrypted = cipher.encrypt("MEET AT NOON")
print(encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)
print(decrypted)
```

### 6×6 Extended

```python
from src.cipher6x6 import PlayFairCipher6x6

# Create cipher
cipher = PlayFairCipher6x6("CRYPTO2026")

# Encrypt with digits
encrypted = cipher.encrypt("PASSWORD123")
print(encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)
print(decrypted)

# Verbose mode (shows steps)
cipher.encrypt("AGENT007", verbose=True)
```

## Testing

Run the test suites to verify implementations:

**5×5 Version:**
```bash
python3 main.py test
```

**6×6 Version:**
```bash
python3 main6x6.py test
```

Tests cover:
- Matrix generation
- Position mapping
- Text preparation
- Encryption/decryption reversibility
- Individual cipher rules
- Edge cases
- Alphanumeric support (6×6 only)

## Security Note

This is a classical cipher for educational and historical purposes. It is not secure for modern cryptographic use and is vulnerable to:
- Frequency analysis
- Known-plaintext attacks
- Chosen-plaintext attacks

## License

MIT License

## References

- Wheatstone, Charles (1854). Original cipher design
- Playfair, Lyon (1854). Promotion and popularization
- Historical military usage in Boer War and WWI

## Contributing

Contributions welcome. Please ensure:
- Code follows existing style
- Tests pass
- New features include tests
- Documentation is updated
