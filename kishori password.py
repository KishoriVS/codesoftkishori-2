import random
import string


def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    print("Password Generator")


    while True:
        length = input("Enter password length (8-128): ")


        if length.isdigit() and 8 <= int(length) <= 128:
            length = int(length)
            break


        else:
            print("Invalid length. Please enter a number between 8 and 128.")


    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'


    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()


