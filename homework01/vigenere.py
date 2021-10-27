plaintext = ''
keyword = ''
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyword *= len(plaintext) // len(keyword) + 1
    for i, j in enumerate(plaintext):
        position = (ord(j) + ord(keyword[i]))
        ciphertext += chr(position % 26 + 65)
    return ciphertext
print(encrypt_vigenere('PYTHON', 'INFORM'))




ciphertext = ''
keyword = ''
def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    keyword *= len(ciphertext) // len(keyword) + 1
    for i, j in enumerate(ciphertext):
        position = (ord(j) - ord(keyword[i]))
        plaintext += chr(position % 26 + 65)
    return plaintext
print(decrypt_vigenere('XLYVFZ', 'INFORM'))
    
