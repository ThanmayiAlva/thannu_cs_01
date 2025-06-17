def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            # Non-alphabetical characters remain unchanged
            result += char
    return result


def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    mode = ""
    while mode not in ['encrypt', 'decrypt']:
        mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()

    result = caesar_cipher(message, shift, mode)
    print(f"\nThe {mode}ed message is: {result}")


if __name__ == "__main__":
    main()
