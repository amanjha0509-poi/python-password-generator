import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "Error: No character types selected."

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("Secure Password Generator")
print("--------------------------")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Length must be greater than 0.")
        exit()

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    print("\nGenerated Password:")
    print(password)

except ValueError:
    print("Invalid input. Please enter a valid number.")
