import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length_str = input("Enter the length of the password you want to generate: ")
        if length_str.isdigit():
            length = int(length_str)
            if length > 0:
                break
            else:
                print("Please enter a positive integer.")
        else:
            print("Please enter a valid integer.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
20