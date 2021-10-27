import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    alfavit_ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
    alfavit_eng = 'abcdefghijklmnopqrstuvwxyzabc'
    for i in plaintext:
        if i.isupper():
            position = alfavit_ENG.find(i)
            new_position = position + shift
            if i in alfavit_ENG:
                ciphertext += alfavit_ENG[new_position]
            else:
                ciphertext += i
        else:
            position = alfavit_eng.find(i)
            new_position = position + shift
            if i in alfavit_eng:
                ciphertext += alfavit_eng[new_position]
            else:
                ciphertext += i
    return ciphertex


print(caesar("Pyton", 3))


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    alfavit_ENG = 'XYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_eng = 'xyzabcdefghijklmnopqrstuvwxyz'
    for i in ciphertex:
        if i.isupper():
            position = alfavit_ENG.find(i)
            new_position = position - shift
            if i in alfavit_ENG:
                plaintext += alfavit_ENG[new_position]
            else:
                plaintext += i
        else:
            position = alfavit_eng.find(i)
            new_position = position - shift
            if i in alfavit_eng:
                plaintext += alfavit_eng[new_position]
            else:
                plaintext += i

    return plaintext


print(caesar("Sbwkrq", 3))


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
