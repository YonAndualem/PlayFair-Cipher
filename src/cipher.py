"""
PlayFair Cipher Implementation
Classical digraph substitution cipher using a 5x5 matrix.
"""

from typing import List, Tuple, Dict


class PlayFairCipher:
    def __init__(self, key: str):
        """
        Initialize the PlayFair cipher with a keyword.
        
        Args:
            key: The keyword used to generate the cipher matrix
            
        Raises:
            ValueError: If key is empty or contains no alphabetic characters
        """
        if not key or not any(c.isalpha() for c in key):
            raise ValueError("Key must contain at least one alphabetic character")
            
        self.key = key.upper().replace('J', 'I')
        self.matrix = self._generate_matrix()
        self.position_map = self._create_position_map()
    
    def _generate_matrix(self) -> List[List[str]]:
        """
        Generate the 5x5 PlayFair cipher matrix from the key.
        
        Returns:
            5x5 matrix as a list of lists
        """
        seen = set()
        unique_key = []
        for char in self.key:
            if char.isalpha() and char not in seen:
                seen.add(char)
                unique_key.append(char)
        
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        for char in alphabet:
            if char not in seen:
                unique_key.append(char)
                seen.add(char)
        
        matrix = []
        for i in range(5):
            row = unique_key[i*5:(i+1)*5]
            matrix.append(row)
        
        return matrix
    
    def _create_position_map(self) -> Dict[str, Tuple[int, int]]:
        """
        Create a dictionary mapping each letter to its (row, col) position.
        
        Returns:
            Maps character to (row, column) tuple
        """
        position_map = {}
        for i in range(5):
            for j in range(5):
                position_map[self.matrix[i][j]] = (i, j)
        return position_map
    
    def get_matrix(self) -> List[List[str]]:
        """Return the cipher matrix."""
        return self.matrix
    
    def print_matrix(self) -> None:
        """Print the cipher matrix in a readable format."""
        print("\nPlayFair Cipher Matrix:")
        print("─" * 21)
        for row in self.matrix:
            print("│ " + " ".join(row) + " │")
        print("─" * 21)
    
    def _prepare_text(self, text: str) -> List[str]:
        """
        Prepare text for encryption by creating digraphs.
        Inserts 'X' between duplicates and pads odd-length text.
        
        Returns:
            List of digraphs (2-letter pairs)
        """
        text = text.upper().replace('J', 'I')
        text = ''.join([char for char in text if char.isalpha()])
        
        digraphs = []
        i = 0
        while i < len(text):
            a = text[i]
            
            if i + 1 >= len(text):
                b = 'X'
                i += 1
            elif text[i] == text[i + 1]:
                b = 'X'
                i += 1
            else:
                b = text[i + 1]
                i += 2
            
            digraphs.append(a + b)
        
        return digraphs
    
    def _apply_rule(self, a: str, b: str, mode: str = 'encrypt') -> str:
        """
        Apply PlayFair cipher rules to a digraph.
        Same row: shift horizontal | Same column: shift vertical | Rectangle: swap columns
        """
        row1, col1 = self.position_map[a]
        row2, col2 = self.position_map[b]
        
        if row1 == row2:
            if mode == 'encrypt':
                col1 = (col1 + 1) % 5
                col2 = (col2 + 1) % 5
            else:
                col1 = (col1 - 1) % 5
                col2 = (col2 - 1) % 5
        
        elif col1 == col2:
            if mode == 'encrypt':
                row1 = (row1 + 1) % 5
                row2 = (row2 + 1) % 5
            else:
                row1 = (row1 - 1) % 5
                row2 = (row2 - 1) % 5
        
        else:
            col1, col2 = col2, col1
        
        return self.matrix[row1][col1] + self.matrix[row2][col2]
    
    def encrypt(self, plaintext: str, verbose: bool = False) -> str:
        """Encrypt plaintext using PlayFair cipher."""
        digraphs = self._prepare_text(plaintext)
        
        if verbose:
            print(f"\nOriginal text: {plaintext}")
            print(f"Prepared digraphs: {' '.join(digraphs)}")
            print("\nEncryption steps:")
        
        ciphertext = []
        for digraph in digraphs:
            encrypted = self._apply_rule(digraph[0], digraph[1], mode='encrypt')
            ciphertext.append(encrypted)
            
            if verbose:
                print(f"  {digraph} → {encrypted}")
        
        result = ''.join(ciphertext)
        
        if verbose:
            print(f"\nCiphertext: {result}")
        
        return result
    
    def decrypt(self, ciphertext: str, verbose: bool = False) -> str:
        """Decrypt ciphertext using PlayFair cipher."""
        ciphertext = ciphertext.upper().replace('J', 'I')
        ciphertext = ''.join([char for char in ciphertext if char.isalpha()])
        
        digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        
        if verbose:
            print(f"\nCiphertext: {ciphertext}")
            print(f"Digraphs: {' '.join(digraphs)}")
            print("\nDecryption steps:")
        
        plaintext = []
        for digraph in digraphs:
            if len(digraph) == 2:
                decrypted = self._apply_rule(digraph[0], digraph[1], mode='decrypt')
                plaintext.append(decrypted)
                
                if verbose:
                    print(f"  {digraph} → {decrypted}")
        
        result = ''.join(plaintext)
        
        if verbose:
            print(f"\nPlaintext: {result}")
        
        return result
