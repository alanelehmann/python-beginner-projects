def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = input("\nChoose an option: ").strip()
message = input("Enter your message: ")
shift = int(input("Enter shift number (1-25): "))

if choice == "1":
    result = encrypt(message, shift)
    print(f"\nEncrypted message: {result}")
elif choice == "2":
    result = decrypt(message, shift)
    print(f"\nDecrypted message: {result}")
else:
    print("Invalid option")