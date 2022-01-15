def encrypt_ceasar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for symbol in plaintext:
        if symbol.isalpha():
            if symbol.isupper():
                ciphertext += chr((ord(symbol) - ord("A") + shift) % 26 + ord("A"))
            else:
                ciphertext += chr((ord(symbol) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_ceasar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for symbol in ciphertext:
        if symbol.isalpha():
            if symbol.isupper():
                plaintext += chr((ord(symbol) - ord("A") - shift) % 26 + ord("A"))
            else:
                plaintext += chr((ord(symbol) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += symbol
    return plaintext
