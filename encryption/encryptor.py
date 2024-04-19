import random
import string
import getpass
import hashlib

MAX_ATTEMPTS = 3

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def save_to_file(filename, data, password):
    with open(filename, 'w') as file:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        encrypted_data = encrypt(data, len(password))
        file.write(hashed_password + '\n')
        file.write(encrypted_data)

def load_from_file(filename, password):
    attempts = 0
    with open(filename, 'r') as file:
        stored_password = file.readline().strip()
        while attempts < MAX_ATTEMPTS:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if stored_password == hashed_password:
                encrypted_data = file.readline()
                return decrypt(encrypted_data, len(password))
            else:
                attempts += 1
                print(f"Incorrect password. {MAX_ATTEMPTS - attempts} attempts remaining.")
                password = getpass.getpass("Enter the password to decrypt the text: ")
    print("Max attempts reached. Exiting program.")
    return None

def main():
    text = input("Enter the text you want to encrypt: ")
    shift = int(input("Enter the shift value (a number between 1 and 25): "))
    
    password = getpass.getpass("Enter a password to protect your data: ")
    encrypted_text = encrypt(text, shift)
    save_to_file('encrypted_data.txt', encrypted_text, password)
    print("Text encrypted and saved to file.")

    decrypt_option = input("Do you want to decrypt the text later? (yes/no): ").lower()
    if decrypt_option == "yes":
        password = getpass.getpass("Enter the password to decrypt the text: ")
        decrypted_text = load_from_file('encrypted_data.txt', password)
        if decrypted_text:
            print("Decrypted text:", decrypted_text)
    else:
        print("Exiting program.")

if __name__ == "__main__":
    main()
