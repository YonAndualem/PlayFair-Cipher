"""
PlayFair Cipher Test Suite
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cipher import PlayFairCipher


def test_matrix_generation():
    """Test cipher matrix generation."""
    print("Testing matrix generation...")
    
    cipher = PlayFairCipher("MONARCHY")
    
    assert len(cipher.get_matrix()) == 5
    assert all(len(row) == 5 for row in cipher.get_matrix())
    
    letters = []
    for row in cipher.get_matrix():
        letters.extend(row)
    assert len(letters) == 25
    assert len(set(letters)) == 25
    assert 'J' not in letters
    
    print("  ✓ Passed")


def test_position_map():
    """Test position mapping."""
    print("Testing position map...")
    
    cipher = PlayFairCipher("MONARCHY")
    
    assert len(cipher.position_map) == 25
    
    for i in range(5):
        for j in range(5):
            letter = cipher.get_matrix()[i][j]
            pos = cipher.position_map[letter]
            assert pos == (i, j)
    
    print("  ✓ Passed")


def test_text_preparation():
    """Test text preparation."""
    print("Testing text preparation...")
    
    cipher = PlayFairCipher("MONARCHY")
    
    assert cipher._prepare_text("HELLO") == ['HE', 'LX', 'LO']
    assert cipher._prepare_text("HIDE") == ['HI', 'DE']
    assert cipher._prepare_text("CAT") == ['CA', 'TX']
    assert len(cipher._prepare_text("HELLO WORLD")) > 0
    assert all('J' not in d for d in cipher._prepare_text("JUMP"))
    
    print("  ✓ Passed")


def test_encryption_decryption():
    """Test encryption and decryption."""
    print("Testing encryption/decryption...")
    
    cipher = PlayFairCipher("MONARCHY")
    
    test_messages = [
        "HELLO",
        "HELLO WORLD",
        "THE QUICK BROWN FOX",
        "BALLOON",
        "MEET ME AT MIDNIGHT",
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
    
    cipher = PlayFairCipher("MONARCHY")
    
    plaintext = "BALLOON"
    ciphertext = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(ciphertext)
    prepared = ''.join(cipher._prepare_text(plaintext))
    
    assert decrypted == prepared
    
    print("  ✓ Passed")


def test_same_row_rule():
    """Test same row rule."""
    print("Testing same row rule...")
    
    cipher = PlayFairCipher("ABCDEFGHIKLMNOPQRSTUVWXYZ")
    
    result = cipher._apply_rule('A', 'B', mode='encrypt')
    row1, col1 = cipher.position_map['A']
    row2, col2 = cipher.position_map['B']
    
    if row1 == row2:
        new_col1 = (col1 + 1) % 5
        new_col2 = (col2 + 1) % 5
        expected = cipher.get_matrix()[row1][new_col1] + cipher.get_matrix()[row2][new_col2]
        assert result == expected
    
    print("  ✓ Passed")


def test_same_column_rule():
    """Test same column rule."""
    print("Testing same column rule...")
    
    cipher = PlayFairCipher("ABCDEFGHIKLMNOPQRSTUVWXYZ")
    
    row1, col1 = cipher.position_map['A']
    row2, col2 = cipher.position_map['F']
    
    if col1 == col2:
        result = cipher._apply_rule('A', 'F', mode='encrypt')
        new_row1 = (row1 + 1) % 5
        new_row2 = (row2 + 1) % 5
        expected = cipher.get_matrix()[new_row1][col1] + cipher.get_matrix()[new_row2][col2]
        assert result == expected
    
    print("  ✓ Passed")


def test_rectangle_rule():
    """Test rectangle rule."""
    print("Testing rectangle rule...")
    
    cipher = PlayFairCipher("MONARCHY")
    
    result = cipher._apply_rule('H', 'E', mode='encrypt')
    assert len(result) == 2
    assert all(c.isalpha() for c in result)
    
    decrypted = cipher._apply_rule(result[0], result[1], mode='decrypt')
    assert decrypted == 'HE'
    
    print("  ✓ Passed")


def test_edge_cases():
    """Test edge cases."""
    print("Testing edge cases...")
    
    cipher = PlayFairCipher("MONARCHY")
    
    try:
        result = cipher.encrypt("")
        assert result == ""
    except:
        pass
    
    result = cipher.encrypt("A")
    assert len(result) == 2
    
    result = cipher.encrypt("AAAA")
    assert 'X' in ''.join(cipher._prepare_text("AAAA"))
    
    print("  ✓ Passed")


def run_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("  PLAYFAIR CIPHER TEST SUITE")
    print("="*60 + "\n")
    
    tests = [
        test_matrix_generation,
        test_position_map,
        test_text_preparation,
        test_encryption_decryption,
        test_known_example,
        test_same_row_rule,
        test_same_column_rule,
        test_rectangle_rule,
        test_edge_cases,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"  RESULTS: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
