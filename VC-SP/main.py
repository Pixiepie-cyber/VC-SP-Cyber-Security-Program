from os import system
from password_generator import *
from web_scrapper import *
from file_encryptor import *


system("cls")
print("____   _____________             ___________________ ")
print("\   \ /   /\_   ___ \           /   _____/\______   \ ")
print(" \   Y   / /    \  \/   ______  \_____  \  |     ___/ ")
print("  \     /  \     \____ /_____/  /        \ |    |    ")
print("   \___/    \______  /         /_______  / |____|    ")
print("                   \/                  \/            ") 

username = input("Enter your name: ")

while True:

    system("cls")

    print("____   _____________             ___________________ ")
    print("\   \ /   /\_   ___ \           /   _____/\______   \ ")
    print(" \   Y   / /    \  \/   ______  \_____  \  |     ___/ ")
    print("  \     /  \     \____ /_____/  /        \ |    |    ")
    print("   \___/    \______  /         /_______  / |____|    ")
    print("                   \/                  \/            ") 


        
    cmd = input(f"[{username}]@[VC-SP]# ")

    if cmd == "help":
        print("Welcome to VC-SP, Choose an option; to use a service, type the number assigned to it..")
        print("[1] Password Generator")
        print("[2] Computer Security Information")
        print("[3] File Encryptor")
        print("[4] Malware Analysis and Demo")
        system("pause")

    elif cmd == "1":
        passwd = PasswordGenerator()
        system("pause")

    elif cmd == "2":
        url = "https://en.wikipedia.org/wiki/Computer_security"  # Replace with the actual URL of the website you want to scrape
        scraper = WebScraper(url)
        scraper.run()
        system("pause")
    
    elif cmd == "3":
        # Generate a new key (run this only once, or load an existing key)
        key = generate_key()

        # Save the key to a file for future use
        save_key(key, "secret.key")

        # Load the key from a file (to be used for encryption/decryption)
        key = load_key("secret.key")

        # Example: Encrypt a file
        file_name = input("Enter the path to the file: ")
        file_to_encrypt = f"{file_name}.txt"  # Path to the file you want to encrypt
        encrypted_file = f"{file_name}_encrypted.enc"  # Path to save the encrypted file
        encrypt_file(file_to_encrypt, key, encrypted_file)

        # Example: Decrypt a file
        decrypted_file = f"{file_name}_decrypted.txt"  # Path to save the decrypted file
        decrypt_file(encrypted_file, key, decrypted_file)
        system("pause")



    
    