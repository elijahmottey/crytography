from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import tkinter as tk
from tkinter import ttk



class AESEncryptionUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AES")
        self.root.configure(bg="#1f497d")

        # Create header label
        self.header_label = tk.Label(root, text="Group 8", font=("Arial", 20, "bold"), fg="white", bg="#1f497d")
        self.header_label.pack(pady=10)

        self.header_label = tk.Label(root, text="ADVANCE ENCRYPTION STANDARD, AES", font=("Arial", 20, "bold"), fg="white", bg="#1f497d")
        self.header_label.pack(pady=10)


        # Create input label and entry for plaintext
        self.plaintext_label = tk.Label(root, text="Enter your plaintext:", font=("Arial", 14), bg="#1f497d", fg="white")
        self.plaintext_label.pack()
        self.plaintext_entry = tk.Entry(root, font=("Arial", 14))
        self.plaintext_entry.pack(pady=5)

        # Create encrypt button
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt, font=("Arial", 14))
        self.encrypt_button.pack(pady=10)

        # Create input label and text field for ciphertext
        self.ciphertext_label = tk.Label(root, text="Ciphertext:", font=("Arial", 14), bg="#1f497d", fg="white")
        self.ciphertext_label.pack()
        self.ciphertext_textfield = tk.Text(root, font=("Arial", 14), height=5, width=40)
        self.ciphertext_textfield.pack(pady=5)

        # Create decrypt button
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt, font=("Arial", 14))
        self.decrypt_button.pack(pady=10)

        # Create output label
        self.output_label = tk.Label(root, text="", font=("Arial", 14), bg="#1f497d", fg="white")
        self.output_label.pack()

    


    def encrypt(self):
        # Define the encryption key (128 bits = 16 bytes)
        key = b'SecretKey1234567'

        # Get the plaintext from the input entry and convert to bytes
        plaintext = self.plaintext_entry.get().encode()

        # Create an AES cipher object
        cipher = AES.new(key, AES.MODE_ECB)

        # Pad the plaintext to match the block size
        padded_plaintext = pad(plaintext, AES.block_size)

        # Encrypt the padded plaintext
        ciphertext = cipher.encrypt(padded_plaintext)

        # Display the ciphertext
        self.ciphertext_textfield.delete(1.0, tk.END)
        self.ciphertext_textfield.insert(tk.END, ciphertext.hex())

    def decrypt(self):
        # Define the encryption key (128 bits = 16 bytes)
        key = b'SecretKey1234567'

        # Get the ciphertext from the text field
        ciphertext = bytes.fromhex(self.ciphertext_textfield.get("1.0", tk.END).strip())

        # Create an AES cipher object
        cipher = AES.new(key, AES.MODE_ECB)

        try:
            # Decrypt the ciphertext
            decrypted_data = cipher.decrypt(ciphertext)

            # Unpad the decrypted data
            plaintext = unpad(decrypted_data, AES.block_size)

            # Display the plaintext
            self.output_label.config(text="Plaintext: " + plaintext.decode())
        except ValueError:
            self.output_label.config(text="Decryption failed.")

if __name__ == "__main__":
    root = tk.Tk()
    encryption_ui = AESEncryptionUI(root)
    root.mainloop()