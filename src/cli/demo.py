"""
PlayFair Cipher - Command Line Interface
Interactive demonstration tool
"""

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.cipher import PlayFairCipher


def print_header(text):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)


def print_section(text):
    """Print a section divider."""
    print(f"\n{'-'*60}")
    print(f"  {text}")
    print('-'*60)


def demonstrate_matrix_creation(keyword):
    """Demonstrate cipher matrix creation."""
    print_header("MATRIX CREATION")
    
    print(f"\nKeyword: '{keyword}'")
    print("\nProcess:")
    print("  1. Remove duplicate letters from keyword")
    print("  2. Fill remaining with alphabet (A-Z, no J)")
    print("  3. Arrange in 5×5 grid")
    
    cipher = PlayFairCipher(keyword)
    cipher.print_matrix()
    
    return cipher


def demonstrate_text_preparation(cipher, text):
    """Demonstrate text preparation."""
    print_header("TEXT PREPARATION")
    
    print(f"\nOriginal message: '{text}'")
    
    print("\nPreparation steps:")
    print("  1. Convert to uppercase and remove spaces")
    clean_text = text.upper().replace(' ', '')
    print(f"     → {clean_text}")
    
    print("  2. Replace J with I")
    clean_text = clean_text.replace('J', 'I')
    print(f"     → {clean_text}")
    
    print("  3. Split into pairs (digraphs)")
    print("  4. Insert 'X' between duplicate letters")
    print("  5. Add 'X' at end if odd length")
    
    digraphs = cipher._prepare_text(text)
    print(f"\nDigraphs: {' '.join(digraphs)}")
    
    return digraphs


def demonstrate_encryption_rules():
    """Explain the encryption rules."""
    print_header("CIPHER RULES")
    
    print("\nRule 1: Same Row")
    print("  → Replace with letter to the right (wrap around)")
    
    print("\nRule 2: Same Column")
    print("  → Replace with letter below (wrap around)")
    
    print("\nRule 3: Rectangle")
    print("  → Swap columns")


def demonstrate_encryption(cipher, plaintext):
    """Demonstrate encryption."""
    print_header("ENCRYPTION")
    
    print(f"\nEncrypting: '{plaintext}'")
    time.sleep(0.5)
    
    ciphertext = cipher.encrypt(plaintext, verbose=True)
    
    return ciphertext


def demonstrate_decryption(cipher, ciphertext):
    """Demonstrate decryption."""
    print_header("DECRYPTION")
    
    print("\nDecryption uses reverse rules:")
    print("  • Same row: shift left")
    print("  • Same column: shift up")
    print("  • Rectangle: swap columns (same)")
    
    time.sleep(0.5)
    
    plaintext = cipher.decrypt(ciphertext, verbose=True)
    
    return plaintext


def interactive_mode():
    """Interactive demonstration mode."""
    print_header("INTERACTIVE MODE")
    
    keyword = input("\nEnter keyword (default: MONARCHY): ").strip()
    if not keyword:
        keyword = "MONARCHY"
    
    cipher = PlayFairCipher(keyword)
    cipher.print_matrix()
    
    while True:
        print("\n" + "-"*60)
        message = input("\nEnter message to encrypt (or 'quit'): ").strip()
        
        if message.lower() == 'quit':
            break
        
        if not message:
            continue
        
        print_section("Encrypting...")
        ciphertext = cipher.encrypt(message, verbose=True)
        
        print_section("Decrypting...")
        decrypted = cipher.decrypt(ciphertext, verbose=True)


def full_presentation():
    """Complete demonstration."""
    print_header("PLAYFAIR CIPHER DEMONSTRATION")
    
    keyword = "MONARCHY"
    message = "HELLO WORLD"
    
    input("\nPress Enter to start...")
    
    cipher = demonstrate_matrix_creation(keyword)
    input("\nPress Enter to continue...")
    
    digraphs = demonstrate_text_preparation(cipher, message)
    input("\nPress Enter to continue...")
    
    demonstrate_encryption_rules()
    input("\nPress Enter to continue...")
    
    ciphertext = demonstrate_encryption(cipher, message)
    input("\nPress Enter to continue...")
    
    plaintext = demonstrate_decryption(cipher, ciphertext)
    
    print_header("SUMMARY")
    print(f"\nKeyword:    {keyword}")
    print(f"Plaintext:  {message}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {plaintext}")


def quick_examples():
    """Show quick examples."""
    print_header("EXAMPLES")
    
    examples = [
        ("MONARCHY", "BALLOON"),
        ("PLAYFAIR", "HIDE THE GOLD"),
        ("KEYWORD", "MEET ME AT NOON"),
    ]
    
    for keyword, message in examples:
        print_section(f"Keyword: {keyword}")
        cipher = PlayFairCipher(keyword)
        cipher.print_matrix()
        
        ciphertext = cipher.encrypt(message, verbose=False)
        print(f"\nPlaintext:  {message}")
        print(f"Ciphertext: {ciphertext}")
        
        decrypted = cipher.decrypt(ciphertext, verbose=False)
        print(f"Decrypted:  {decrypted}")
        
        time.sleep(0.5)


def run_demo():
    """Main demo entry point."""
    while True:
        print("\n" + "="*60)
        print("  PLAYFAIR CIPHER")
        print("="*60)
        print("\nOptions:")
        print("  1. Full demonstration")
        print("  2. Quick examples")
        print("  3. Interactive mode")
        print("  4. Exit")
        
        choice = input("\nChoice (1-4): ").strip()
        
        if choice == "1":
            full_presentation()
        elif choice == "2":
            quick_examples()
        elif choice == "3":
            interactive_mode()
        elif choice == "4":
            break
        else:
            print("\nInvalid choice")
