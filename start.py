"""
Caesar Cipher Encryption and Decryption Tool

This script allows users to encrypt or decrypt text using the Caesar Cipher method.
This script is intended for educational purposes and simple use cases in classical cryptography.

Author: Ikmal Thaufan Mahdi
last Update: 2025-06-24
GitHub: https://github.com/ElfnnXI
"""

def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  
    return result

def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid option. Please choose 'E' or 'D'.")
        return
    text = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift amount (e.g. 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return
    if choice == 'e':
        result = encrypt(text, shift)
        print(f"\nEncrypted message: {result}")
    else:
        result = decrypt(text, shift)
        print(f"\nDecrypted message: {result}")

if __name__ == "__main__":
    main()
