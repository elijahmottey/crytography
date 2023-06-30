
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class AdvanceEncryptionStandard:
     @staticmethod
     def encryption():
            # Define the encryption key (128 bits = 16 bytes)
            key = b'Secretkey1234567'

            # Get plaintext from user input and convert to bytes
            plaintext=input("Enter your plaintext: ").encode()
            # Create an AES cipher object
            cipher = AES.new(key, AES.MODE_ECB)

            # Pad the plaintext to match the block size
            padded_plaintext = pad(plaintext, AES.block_size)

        # Encrypt the padded plaintext
            ciphertext = cipher.encrypt(padded_plaintext)
            print("Ciphertext:", ciphertext.hex())


     @staticmethod
     def decryption():
        
        # Define the encryption key (128 bits = 16 bytes)
        key = b'SecretKey1234567'

        # Define the ciphertext
        ciphertext = bytes.fromhex(input("Enter your encrypted message: "))

        # Create an AES cipher object
        cipher = AES.new(key, AES.MODE_ECB)

        # Decrypt the ciphertext
        decrypted_data = cipher.decrypt(ciphertext)

        # Unpad the decrypted data
        plaintext = unpad(decrypted_data, AES.block_size)

        print("Plaintext:", plaintext.decode())


#instantiation
aes=AdvanceEncryptionStandard()


#running encryption
aes.encryption()
aes.decryption()
