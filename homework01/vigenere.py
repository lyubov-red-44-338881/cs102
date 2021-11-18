def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    for element in range(len(plaintext)):
        letter = plaintext[element]
        keyword = keyword.upper()
        shift = ord(keyword[element % len(keyword)]) - 65
        element = 0
        if letter.islower():
            ciphertext += chr(97 + ((ord(letter) - 97 + shift) % 26))
        elif letter.isupper():
            ciphertext += chr(65 + ((ord(letter) - 65 + shift) % 26))
        else:
            ciphertext += letter
        element += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
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
    for element in range(len(ciphertext)):
        letter = ciphertext[element]
        keyword = keyword.upper()
        shift = ord(keyword[element % len(keyword)]) - 65
        element = 0
        if letter.islower():
            plaintext += chr(97 + ((ord(letter) - 97 - shift) % 26))
        elif letter.isupper():
            plaintext += chr(65 + ((ord(letter) - 65 - shift) % 26))
        else:
            plaintext += letter
        element += 1
    return plaintext
