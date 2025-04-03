from cryptography.fernet import Fernet
import os

# Generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Save the key to a file (optional for reuse)
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

# Load the key from a file
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Encrypt a file
def encrypt_file(file_path, key, encrypted_file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)

    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{file_path}' has been encrypted and saved as '{encrypted_file_path}'")

# Decrypt a file
def decrypt_file(encrypted_file_path, key, decrypted_file_path):
    fernet = Fernet(key)
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File '{encrypted_file_path}' has been decrypted and saved as '{decrypted_file_path}'")

#if __name__ == "__main__":
    # Generate a new key (run this only once, or load an existing key)
   # key = generate_key()

    # Save the key to a file for future use
   # save_key(key, "secret.key")

    # Load the key from a file (to be used for encryption/decryption)
   # key = load_key("secret.key")

    # Example: Encrypt a file
   # file_name = input("Enter the path to the file: ")
    #file_to_encrypt = f"{file_name}.txt"  # Path to the file you want to encrypt
    #encrypted_file = f"{file_name}_encrypted.enc"  # Path to save the encrypted file
    #encrypt_file(file_to_encrypt, key, encrypted_file)

    # Example: Decrypt a file
    #decrypted_file = f"{file_name}_decrypted.txt"  # Path to save the decrypted file
    #decrypt_file(encrypted_file, key, decrypted_file)
