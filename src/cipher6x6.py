"""
PlayFair Cipher 6x6 Implementation
Extended PlayFair cipher using a 6x6 matrix that includes both letters and digits.
This allows encryption of alphanumeric text without losing information.
"""

from typing import List, Tuple, Dict


class PlayFairCipher6x6:
    def __init__(self, key: str):
        """
        Initialize the 6x6 PlayFair cipher with a keyword.
        
        Args:
            key: The keyword used to generate the cipher matrix
            
        Raises:
            ValueError: If key is empty or contains no alphanumeric characters
        """
        if not key or not any(c.isalnum() for c in key):
            raise ValueError("Key must contain at least one alphanumeric character")
            
        self.key = key.upper()
        self.matrix = self._generate_matrix()
        self.position_map = self._create_position_map()
    
    def _generate_matrix(self) -> List[List[str]]:
        """
        Generate the 6x6 PlayFair cipher matrix from the key.
        Uses 26 letters (A-Z) + 10 digits (0-9) = 36 characters.
        
        Returns:
            6x6 matrix as a list of lists
        """
        seen = set()
        unique_key = []
        
        # Add unique alphanumeric characters from the key
        for char in self.key:
            if char.isalnum() and char not in seen:
                seen.add(char)
                unique_key.append(char)
        
        # Add remaining letters A-Z
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if char not in seen:
                unique_key.append(char)
                seen.add(char)
        
        # Add digits 0-9
        for char in '0123456789':
            if char not in seen:
                unique_key.append(char)
                seen.add(char)
        
        # Create 6x6 matrix
        matrix = []
        for i in range(6):
            row = unique_key[i*6:(i+1)*6]
            matrix.append(row)
        
        return matrix
    
    def _create_position_map(self) -> Dict[str, Tuple[int, int]]:
        """
        Create a dictionary mapping each character to its (row, col) position.
        
        Returns:
            Maps character to (row, column) tuple
        """
        position_map = {}
        for i in range(6):
            for j in range(6):
                position_map[self.matrix[i][j]] = (i, j)
        return position_map
    
    def get_matrix(self) -> List[List[str]]:
        """Return the cipher matrix."""
        return self.matrix
    
    def print_matrix(self) -> None:
        """Print the cipher matrix in a readable format."""
        print("\n6x6 PlayFair Cipher Matrix:")
        print("─" * 25)
        for row in self.matrix:
            print("│ " + " ".join(row) + " │")
        print("─" * 25)
    
    def _prepare_text(self, text: str) -> List[str]:
        """
        Prepare text for encryption by creating digraphs.
        Inserts 'X' between duplicates and pads odd-length text.
        
        Returns:
            List of digraphs (2-character pairs)
        """
        text = text.upper()
        # Keep only alphanumeric characters
        text = ''.join([char for char in text if char.isalnum()])
        
        digraphs = []
        i = 0
        while i < len(text):
            a = text[i]
            
            if i + 1 >= len(text):
                # Odd length - pad with 'X'
                b = 'X'
                i += 1
            elif text[i] == text[i + 1]:
                # Same character - insert 'X'
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
        
        Rules:
        - Same row: shift horizontally (right for encrypt, left for decrypt)
        - Same column: shift vertically (down for encrypt, up for decrypt)
        - Rectangle: swap columns
        
        Args:
            a: First character of digraph
            b: Second character of digraph
            mode: 'encrypt' or 'decrypt'
            
        Returns:
            Encrypted or decrypted digraph
        """
        row1, col1 = self.position_map[a]
        row2, col2 = self.position_map[b]
        
        if row1 == row2:
            # Same row - shift horizontally
            if mode == 'encrypt':
                col1 = (col1 + 1) % 6
                col2 = (col2 + 1) % 6
            else:
                col1 = (col1 - 1) % 6
                col2 = (col2 - 1) % 6
        
        elif col1 == col2:
            # Same column - shift vertically
            if mode == 'encrypt':
                row1 = (row1 + 1) % 6
                row2 = (row2 + 1) % 6
            else:
                row1 = (row1 - 1) % 6
                row2 = (row2 - 1) % 6
        
        else:
            # Rectangle - swap columns
            col1, col2 = col2, col1
        
        return self.matrix[row1][col1] + self.matrix[row2][col2]
    
    def encrypt(self, plaintext: str, verbose: bool = False) -> str:
        """
        Encrypt plaintext using 6x6 PlayFair cipher.
        
        Args:
            plaintext: Text to encrypt (alphanumeric)
            verbose: If True, print encryption steps
            
        Returns:
            Encrypted ciphertext
        """
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
        """
        Decrypt ciphertext using 6x6 PlayFair cipher.
        
        Args:
            ciphertext: Text to decrypt
            verbose: If True, print decryption steps
            
        Returns:
            Decrypted plaintext
        """
        ciphertext = ciphertext.upper()
        # Keep only alphanumeric characters
        ciphertext = ''.join([char for char in ciphertext if char.isalnum()])
        
        # Split into digraphs
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
