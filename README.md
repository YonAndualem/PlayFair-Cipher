# PlayFair Cipher

Python implementation of the PlayFair cipher, a classical digraph substitution cipher developed in 1854.

## Overview

The PlayFair cipher encrypts pairs of letters using a 5×5 matrix generated from a keyword. It was one of the first practical digraph substitution ciphers and was notably used in military communications.
![Tests](https://github.com/YonAndualem/PlayFair-Cipher/actions/workflows/python-app.yml/badge.svg)

## Installation

```bash
git clone https://github.com/YonAndualem/PlayFair-Cipher.git
cd PlayFair-Cipher
```

No external dependencies required for core functionality. GUI requires `tkinter` (usually included with Python).

## Usage

### Graphical Interface

```bash
python3 main.py gui
```

### Command Line Interface

```bash
python3 main.py cli
```

### Run Tests

```bash
python3 main.py test
```

### Programmatic Usage

```python
from src.cipher import PlayFairCipher

cipher = PlayFairCipher("KEYWORD")
ciphertext = cipher.encrypt("HELLO WORLD")
plaintext = cipher.decrypt(ciphertext)
```

## Algorithm

### Matrix Generation

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
│   ├── cipher.py       # Core algorithm implementation
│   ├── gui/
│   │   └── app.py      # Graphical interface
│   └── cli/
│       └── demo.py     # Command-line interface
├── tests/
│   └── test_cipher.py  # Test suite
├── main.py             # Application entry point
└── README.md
```

## Features

- **Core Implementation**: Clean, well-documented cipher algorithm
- **GUI Application**: Interactive visual interface with real-time encryption
- **CLI Tool**: Command-line demonstration and interactive mode
- **Test Suite**: Comprehensive unit tests

## Technical Details

### Text Preprocessing

- Converts to uppercase
- Replaces J with I
- Removes non-alphabetic characters
- Splits into digraphs (letter pairs)
- Inserts 'X' between duplicate letters
- Pads with 'X' if odd length

### Matrix Properties

- 5×5 grid containing 25 letters (I and J share a position)
- Generated deterministically from keyword
- Unique letter positioning ensures reversible encryption

## Examples

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

## Testing

Run the test suite to verify implementation:

```bash
python3 main.py test
```

Tests cover:
- Matrix generation
- Position mapping
- Text preparation
- Encryption/decryption reversibility
- Individual cipher rules
- Edge cases

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
