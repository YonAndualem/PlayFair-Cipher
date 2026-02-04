"""
PlayFair Cipher 6x6 - Command Line Interface
Interactive demonstration tool for 6x6 matrix (alphanumeric support)
"""

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.cipher6x6 import PlayFairCipher6x6


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
    print_header("6x6 MATRIX CREATION")
    
    print(f"\nKeyword: '{keyword}'")
    print("\nProcess:")
    print("  1. Remove duplicate characters from keyword")
    print("  2. Fill remaining with alphabet (A-Z)")
    print("  3. Add digits (0-9)")
    print("  4. Arrange in 6×6 grid (36 characters)")
    
    cipher = PlayFairCipher6x6(keyword)
    cipher.print_matrix()
    
    return cipher


def demonstrate_text_preparation(cipher, text):
    """Demonstrate text preparation."""
    print_header("TEXT PREPARATION")
    
    print(f"\nOriginal message: '{text}'")
    
    print("\nPreparation steps:")
    print("  1. Convert to uppercase and remove non-alphanumeric")
    clean_text = text.upper()
    clean_text = ''.join([c for c in clean_text if c.isalnum()])
    print(f"     → {clean_text}")
    
    print("  2. Split into pairs (digraphs)")
    print("  3. Insert 'X' between duplicate characters")
    print("  4. Add 'X' at end if odd length")
    
    digraphs = cipher._prepare_text(text)
    print(f"\nDigraphs: {' '.join(digraphs)}")
    
    return digraphs


def demonstrate_encryption_rules():
    """Explain the encryption rules."""
    print_header("CIPHER RULES")
    
    print("\nRule 1: Same Row")
    print("  → Replace with character to the right (wrap around)")
    
    print("\nRule 2: Same Column")
    print("  → Replace with character below (wrap around)")
    
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
    
    keyword = input("\nEnter keyword (default: CRYPTO): ").strip()
    if not keyword:
        keyword = "CRYPTO"
    
    cipher = PlayFairCipher6x6(keyword)
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
    print_header("PLAYFAIR CIPHER 6x6 DEMONSTRATION")
    
    keyword = "CRYPTO2026"
    message = "PASSWORD123"
    
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
        ("CRYPTO", "AGENT007"),
        ("SECURE", "PASSWORD123"),
        ("SECRET", "ROOM404"),
        ("2026KEY", "CODE2026"),
    ]
    
    for keyword, message in examples:
        print_section(f"Keyword: {keyword}")
        cipher = PlayFairCipher6x6(keyword)
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
        print("  PLAYFAIR CIPHER 6x6")
        print("  Alphanumeric Support (A-Z, 0-9)")
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


if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nExiting...")
