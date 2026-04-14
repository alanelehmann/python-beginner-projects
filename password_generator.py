import random
import string

def generate_password(length, use_upper, use_numbers, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    
    all_characters = lower
    
    if use_upper:
        all_characters += upper
    if use_numbers:
        all_characters += numbers
    if use_symbols:
        all_characters += symbols
        
    password = [random.choice(all_characters) for _ in range(length)]
    random.shuffle(password)
    
    return "".join(password)
    
print("Welcome to the Password Generator!")

length = int(input("How long should the password be? "))
use_upper = input("Include uppercase letters? (yes/no): ").lower() =="yes"
use_numbers = input("Include numbers? (yes/no): ").lower() =="yes"
use_symbols = input("Include symbols? (yes/no):").lower() =="yes"

password = generate_password(length, use_upper, use_numbers, use_symbols)

print(f"\nYour generated password is: {password}")
