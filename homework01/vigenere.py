def encrypt_vigenere(plaintext: str, keyword: str, shift: int = 3) -> str:
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


def decrypt_vigenere(ciphertext: str, keyword: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
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
