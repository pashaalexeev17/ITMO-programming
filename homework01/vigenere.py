def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    j = 0

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if alph.index(plaintext[i].lower()) + alph.index(keyword[j].lower()) >= len(alph):
                g = alph.index(plaintext[i].lower()) + alph.index(keyword[j].lower()) - len(alph)
            else:
                g = alph.index(plaintext[i].lower()) + alph.index(keyword[j].lower())
            if plaintext[i].isupper():
                ciphertext += alph[g].upper()
            else:
                ciphertext += alph[g]
            if j == len(keyword) - 1:
                j = 0
            else:
                j += 1
        else:
            ciphertext += plaintext[i]
            if j == len(keyword) - 1:
                j = 0
            else:
                j += 1

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
    alph = "abcdefghijklmnopqrstuvwxyz"
    j = 0

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if alph.index(ciphertext[i].lower()) - alph.index(keyword[j].lower()) < 0:
                g = alph.index(ciphertext[i].lower()) - alph.index(keyword[j].lower()) + len(alph)
            else:
                g = alph.index(ciphertext[i].lower()) - alph.index(keyword[j].lower())
            if ciphertext[i].isupper():
                plaintext += alph[g].upper()
            else:
                plaintext += alph[g]
            if j == len(keyword) - 1:
                j = 0
            else:
                j += 1
        else:
            plaintext += ciphertext[i]
            if j == len(keyword) - 1:
                j = 0
            else:
                j += 1
    return plaintext
