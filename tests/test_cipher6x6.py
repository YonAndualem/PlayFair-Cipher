"""
PlayFair Cipher 6x6 Test Suite
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cipher6x6 import PlayFairCipher6x6


def test_matrix_generation():
    """Test cipher matrix generation."""
    print("Testing 6x6 matrix generation...")
    
    cipher = PlayFairCipher6x6("CRYPTO")
    
    assert len(cipher.get_matrix()) == 6
    assert all(len(row) == 6 for row in cipher.get_matrix())
    
    chars = []
    for row in cipher.get_matrix():
        chars.extend(row)
    assert len(chars) == 36
    assert len(set(chars)) == 36
    
    print("  ✓ Passed")


def test_position_map():
    """Test position mapping."""
    print("Testing position map...")
    
    cipher = PlayFairCipher6x6("CRYPTO")
    
    assert len(cipher.position_map) == 36
    
    for i in range(6):
        for j in range(6):
            char = cipher.get_matrix()[i][j]
            pos = cipher.position_map[char]
            assert pos == (i, j)
    
    print("  ✓ Passed")


def test_alphanumeric_support():
    """Test that matrix contains letters and digits."""
    print("Testing alphanumeric support...")
    
    cipher = PlayFairCipher6x6("SECRET")
    
    chars = []
    for row in cipher.get_matrix():
        chars.extend(row)
    char_set = set(chars)
    
    # Check all letters present
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        assert letter in char_set
    
    # Check all digits present
    for digit in '0123456789':
        assert digit in char_set
    
    print("  ✓ Passed")


def test_text_preparation():
    """Test text preparation."""
    print("Testing text preparation...")
    
    cipher = PlayFairCipher6x6("CRYPTO")
    
    assert cipher._prepare_text("HELLO") == ['HE', 'LX', 'LO']
    assert cipher._prepare_text("HIDE") == ['HI', 'DE']
    assert cipher._prepare_text("CAT") == ['CA', 'TX']
    assert len(cipher._prepare_text("AGENT007")) > 0
    
    print("  ✓ Passed")


def test_encryption_decryption():
    """Test encryption and decryption."""
    print("Testing encryption/decryption...")
    
    cipher = PlayFairCipher6x6("CRYPTO2026")
    
    test_messages = [
        "HELLO",
        "PASSWORD123",
        "AGENT007",
        "ROOM404",
        "CODE2026",
    ]
    
    for message in test_messages:
        ciphertext = cipher.encrypt(message)
        decrypted = cipher.decrypt(ciphertext)
        prepared = ''.join(cipher._prepare_text(message))
        assert decrypted == prepared
    
    print("  ✓ Passed")


def test_known_example():
    """Test against known example."""
    print("Testing known example...")
    
    cipher = PlayFairCipher6x6("SECRET")
    
    plaintext = "PASSWORD123"
    ciphertext = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(ciphertext)
    prepared = ''.join(cipher._prepare_text(plaintext))
    
    assert decrypted == prepared
    
    print("  ✓ Passed")


def test_same_row_rule():
    """Test same row rule."""
    print("Testing same row rule...")
    
    cipher = PlayFairCipher6x6("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    result = cipher._apply_rule('A', 'B', mode='encrypt')
    row1, col1 = cipher.position_map['A']
    row2, col2 = cipher.position_map['B']
    
    if row1 == row2:
        new_col1 = (col1 + 1) % 6
        new_col2 = (col2 + 1) % 6
        expected = cipher.get_matrix()[row1][new_col1] + cipher.get_matrix()[row2][new_col2]
        assert result == expected
    
    print("  ✓ Passed")


def test_same_column_rule():
    """Test same column rule."""
    print("Testing same column rule...")
    
    cipher = PlayFairCipher6x6("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    row1, col1 = cipher.position_map['A']
    row2, col2 = cipher.position_map['G']
    
    if col1 == col2:
        result = cipher._apply_rule('A', 'G', mode='encrypt')
        new_row1 = (row1 + 1) % 6
        new_row2 = (row2 + 1) % 6
        expected = cipher.get_matrix()[new_row1][col1] + cipher.get_matrix()[new_row2][col2]
        assert result == expected
    
    print("  ✓ Passed")


def test_rectangle_rule():
    """Test rectangle rule."""
    print("Testing rectangle rule...")
    
    cipher = PlayFairCipher6x6("CRYPTO")
    
    result = cipher._apply_rule('H', 'E', mode='encrypt')
    assert len(result) == 2
    assert all(c.isalnum() for c in result)
    
    decrypted = cipher._apply_rule(result[0], result[1], mode='decrypt')
    assert decrypted == 'HE'
    
    print("  ✓ Passed")


def test_different_keys():
    """Test that different keys produce different results."""
    print("Testing different keys...")
    
    cipher1 = PlayFairCipher6x6("KEY1")
    cipher2 = PlayFairCipher6x6("KEY2")
    
    plaintext = "TEST123"
    ciphertext1 = cipher1.encrypt(plaintext)
    ciphertext2 = cipher2.encrypt(plaintext)
    
    assert ciphertext1 != ciphertext2
    
    print("  ✓ Passed")


def test_digit_encryption():
    """Test encryption of messages with digits."""
    print("Testing digit encryption...")
    
    cipher = PlayFairCipher6x6("SECURE")
    
    messages_with_digits = [
        "PASSWORD123",
        "AGENT007",
        "ROOM404",
        "PORT8080",
        "CODE2026",
    ]
    
    for message in messages_with_digits:
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        prepared = ''.join(cipher._prepare_text(message))
        assert decrypted == prepared
        assert encrypted.isalnum()
    
    print("  ✓ Passed")


def test_case_insensitive():
    """Test case insensitivity."""
    print("Testing case insensitivity...")
    
    cipher = PlayFairCipher6x6("SECRET")
    
    plaintext_upper = "PASSWORD123"
    plaintext_lower = "password123"
    plaintext_mixed = "PaSsWoRd123"
    
    encrypted_upper = cipher.encrypt(plaintext_upper)
    encrypted_lower = cipher.encrypt(plaintext_lower)
    encrypted_mixed = cipher.encrypt(plaintext_mixed)
    
    assert encrypted_upper == encrypted_lower == encrypted_mixed
    
    print("  ✓ Passed")


def test_special_characters_ignored():
    """Test that special characters are ignored."""
    print("Testing special character handling...")
    
    cipher = PlayFairCipher6x6("SECRET")
    
    plaintext_clean = "HELLO123"
    plaintext_dirty = "HE!!LL##O--1@2@3"
    
    encrypted_clean = cipher.encrypt(plaintext_clean)
    encrypted_dirty = cipher.encrypt(plaintext_dirty)
    
    assert encrypted_clean == encrypted_dirty
    
    print("  ✓ Passed")


def test_invalid_key():
    """Test error handling for invalid keys."""
    print("Testing invalid key handling...")
    
    try:
        cipher = PlayFairCipher6x6("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        cipher = PlayFairCipher6x6("!@#$%^")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("  ✓ Passed")


def test_verbose_output():
    """Test verbose encryption/decryption."""
    print("Testing verbose mode...")
    
    cipher = PlayFairCipher6x6("TEST")
    
    # Should not raise errors
    cipher.encrypt("HELLO123", verbose=True)
    cipher.decrypt("ABCD1234", verbose=True)
    
    print("  ✓ Passed")


def run_all_tests():
    """Run all test functions."""
    print("\n" + "="*60)
    print("  PLAYFAIR CIPHER 6x6 TEST SUITE")
    print("="*60 + "\n")
    
    test_functions = [
        test_matrix_generation,
        test_position_map,
        test_alphanumeric_support,
        test_text_preparation,
        test_encryption_decryption,
        test_known_example,
        test_same_row_rule,
        test_same_column_rule,
        test_rectangle_rule,
        test_different_keys,
        test_digit_encryption,
        test_case_insensitive,
        test_special_characters_ignored,
        test_invalid_key,
        test_verbose_output,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ Failed: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ Error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"  Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
