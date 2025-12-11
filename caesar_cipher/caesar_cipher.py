"""
Caesar Security Tool 
Author: Raj Kumar
Date: 12th December 2025
Purpose: Only Encrypt / Decrypt / Brute-force / Exit
"""

import logging

# Optional: install cryptography for the secure example
try:
    from cryptography.fernet import Fernet
    HAS_FERNET = True
except Exception:
    HAS_FERNET = False

LOGFILE = "caesar_security_tool.log"
logging.basicConfig(filename=LOGFILE, level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s")


# ----- Caesar functions -----
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# ----- Brute-force (all 25 shifts) -----
def brute_force(text):
    results = []
    for i in range(1, 26):
        results.append((i, decrypt(text, i)))
    return results

# ----- Simple CLI -----
def run_cli():
    print("🔐 Caesar Cipher Tool — Simplified")
    menu = """
1) Encrypt text
2) Decrypt text
3) Brute-force ciphertext (show all 25 shifts)
4) Exit
"""
    print(menu)

    while True:
        choice = input("Choice: ").strip()

        if choice == "1":
            txt = input("Enter message: ")
            shift = int(input("Enter shift value: "))
            print("\nEncrypted:", encrypt(txt, shift))
            print()

        elif choice == "2":
            txt = input("Enter ciphertext: ")
            shift = int(input("Enter shift value: "))
            print("\nDecrypted:", decrypt(txt, shift))
            print()

        elif choice == "3":
            txt = input("Enter ciphertext to brute-force: ")
            results = brute_force(txt)
            print("\n--- Brute Force Results ---")
            for s, out in results:
                print(f"Shift {s:02}: {out}")
            print()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    run_cli()
