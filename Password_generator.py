import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Characters to include in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        print(f"Generated password: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number for the password length.")
