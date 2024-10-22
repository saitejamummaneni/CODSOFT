import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    # Combine character sets
    all_characters = lowercase + uppercase + digits + special
    
    if len(all_characters) == 0:
        raise ValueError("At least one character type must be selected.")
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# User input
length = int(input("Enter the desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(length, use_uppercase, use_digits, use_special)
print(f"Generated Password: {password}")