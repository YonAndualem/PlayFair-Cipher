"""
PlayFair Cipher - Graphical User Interface
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.cipher import PlayFairCipher


class PlayFairGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PlayFair Cipher")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        self.root.minsize(900, 650)
        
        self.cipher = None
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface."""
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        title_label = tk.Label(
            main_frame,
            text="PlayFair Cipher",
            font=('Arial', 24, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(
            main_frame,
            text="Demonstration",
            font=('Arial', 10, 'italic'),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        subtitle_label.pack(pady=(0, 20))
        
        content_frame = tk.Frame(main_frame, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        left_frame = tk.Frame(content_frame, bg='#f0f0f0')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        right_frame = tk.Frame(content_frame, bg='#f0f0f0')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        
        keyword_frame = tk.LabelFrame(
            left_frame,
            text="Keyword",
            font=('Arial', 11, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10
        )
        keyword_frame.pack(fill=tk.X, pady=(0, 10))
        
        keyword_input_frame = tk.Frame(keyword_frame, bg='#ffffff')
        keyword_input_frame.pack(fill=tk.X)
        
        self.keyword_entry = tk.Entry(
            keyword_input_frame,
            font=('Arial', 12),
            width=30
        )
        self.keyword_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.keyword_entry.insert(0, "MONARCHY")
        
        generate_btn = tk.Button(
            keyword_input_frame,
            text="Generate Matrix",
            command=self.generate_matrix,
            bg='#3498db',
            fg='white',
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=5
        )
        generate_btn.pack(side=tk.LEFT)
        
        message_frame = tk.LabelFrame(
            left_frame,
            text="Message",
            font=('Arial', 11, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10
        )
        message_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        tk.Label(
            message_frame,
            text="Plaintext:",
            font=('Arial', 10),
            bg='#ffffff'
        ).pack(anchor=tk.W)
        
        self.plaintext_box = scrolledtext.ScrolledText(
            message_frame,
            height=4,
            font=('Arial', 11),
            wrap=tk.WORD
        )
        self.plaintext_box.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        self.plaintext_box.insert('1.0', "HELLO WORLD")
        
        button_frame = tk.Frame(message_frame, bg='#ffffff')
        button_frame.pack(fill=tk.X)
        
        encrypt_btn = tk.Button(
            button_frame,
            text="⬇ Encrypt",
            command=self.encrypt_message,
            bg='#27ae60',
            fg='white',
            font=('Arial', 11, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        encrypt_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        
        decrypt_btn = tk.Button(
            button_frame,
            text="⬆ Decrypt",
            command=self.decrypt_message,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 11, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        decrypt_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        
        tk.Label(
            message_frame,
            text="Ciphertext:",
            font=('Arial', 10),
            bg='#ffffff'
        ).pack(anchor=tk.W, pady=(10, 0))
        
        self.ciphertext_box = scrolledtext.ScrolledText(
            message_frame,
            height=4,
            font=('Arial', 11),
            wrap=tk.WORD
        )
        self.ciphertext_box.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        log_frame = tk.LabelFrame(
            left_frame,
            text="Process",
            font=('Arial', 11, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10
        )
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.process_log = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            font=('Courier', 9),
            wrap=tk.WORD,
            bg='#f8f9fa'
        )
        self.process_log.pack(fill=tk.BOTH, expand=True)
        
        matrix_frame = tk.LabelFrame(
            right_frame,
            text="Cipher Matrix",
            font=('Arial', 11, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10
        )
        matrix_frame.pack(fill=tk.BOTH, pady=(0, 10))
        
        self.matrix_display = tk.Frame(matrix_frame, bg='#ffffff')
        self.matrix_display.pack()
        
        info_frame = tk.LabelFrame(
            right_frame,
            text="Algorithm Rules",
            font=('Arial', 11, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10
        )
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        info_text = """
Encryption Rules:

1. Same Row
   → Shift right
   
2. Same Column
   → Shift down
   
3. Rectangle
   → Swap columns

Note: I/J share position
Padding: X inserted
        """
        
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=('Arial', 9),
            bg='#ffffff',
            fg='#34495e',
            justify=tk.LEFT,
            anchor=tk.NW
        )
        info_label.pack(fill=tk.BOTH, expand=True)
        
        self.generate_matrix()
    
    def generate_matrix(self):
        """Generate the cipher matrix from the keyword."""
        keyword = self.keyword_entry.get().strip()
        
        if not keyword:
            messagebox.showwarning("Warning", "Please enter a keyword")
            return
        
        try:
            self.cipher = PlayFairCipher(keyword)
            self.display_matrix()
            self.log_message(f"Matrix generated: {keyword}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate matrix: {str(e)}")
    
    def display_matrix(self):
        """Display the cipher matrix visually."""
        for widget in self.matrix_display.winfo_children():
            widget.destroy()
        
        if not self.cipher:
            return
        
        for i in range(5):
            for j in range(5):
                letter = self.cipher.get_matrix()[i][j]
                label = tk.Label(
                    self.matrix_display,
                    text=letter,
                    font=('Courier', 16, 'bold'),
                    width=3,
                    height=1,
                    bg='#3498db',
                    fg='white',
                    relief=tk.RAISED,
                    borderwidth=2
                )
                label.grid(row=i, column=j, padx=2, pady=2)
    
    def encrypt_message(self):
        """Encrypt the plaintext message."""
        if not self.cipher:
            messagebox.showwarning("Warning", "Generate matrix first")
            return
        
        plaintext = self.plaintext_box.get('1.0', tk.END).strip()
        
        if not plaintext:
            messagebox.showwarning("Warning", "Enter message to encrypt")
            return
        
        try:
            self.process_log.delete('1.0', tk.END)
            
            self.log_message("ENCRYPTION")
            self.log_message("="*40 + "\n")
            self.log_message(f"Input: {plaintext}\n")
            
            digraphs = self.cipher._prepare_text(plaintext)
            self.log_message(f"Digraphs: {' '.join(digraphs)}\n")
            
            ciphertext_parts = []
            for digraph in digraphs:
                encrypted = self.cipher._apply_rule(digraph[0], digraph[1], mode='encrypt')
                ciphertext_parts.append(encrypted)
                self.log_message(f"{digraph} → {encrypted}")
            
            ciphertext = ''.join(ciphertext_parts)
            self.log_message(f"\nOutput: {ciphertext}")
            
            self.ciphertext_box.delete('1.0', tk.END)
            self.ciphertext_box.insert('1.0', ciphertext)
            
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
    
    def decrypt_message(self):
        """Decrypt the ciphertext message."""
        if not self.cipher:
            messagebox.showwarning("Warning", "Generate matrix first")
            return
        
        ciphertext = self.ciphertext_box.get('1.0', tk.END).strip()
        
        if not ciphertext:
            messagebox.showwarning("Warning", "Enter message to decrypt")
            return
        
        try:
            self.process_log.delete('1.0', tk.END)
            
            self.log_message("DECRYPTION")
            self.log_message("="*40 + "\n")
            
            clean_ciphertext = ciphertext.upper().replace('J', 'I')
            clean_ciphertext = ''.join([c for c in clean_ciphertext if c.isalpha()])
            
            self.log_message(f"Input: {clean_ciphertext}\n")
            
            digraphs = [clean_ciphertext[i:i+2] for i in range(0, len(clean_ciphertext), 2)]
            self.log_message(f"Digraphs: {' '.join(digraphs)}\n")
            
            plaintext_parts = []
            for digraph in digraphs:
                if len(digraph) == 2:
                    decrypted = self.cipher._apply_rule(digraph[0], digraph[1], mode='decrypt')
                    plaintext_parts.append(decrypted)
                    self.log_message(f"{digraph} → {decrypted}")
            
            plaintext = ''.join(plaintext_parts)
            self.log_message(f"\nOutput: {plaintext}")
            
            self.plaintext_box.delete('1.0', tk.END)
            self.plaintext_box.insert('1.0', plaintext)
            
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
    
    def log_message(self, message):
        """Add a message to the process log."""
        self.process_log.insert(tk.END, message + "\n")
        self.process_log.see(tk.END)


def launch():
    """Launch the GUI application."""
    root = tk.Tk()
    app = PlayFairGUI(root)
    root.mainloop()
