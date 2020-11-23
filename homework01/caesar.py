
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
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            j = alph.index(plaintext[i].lower()) + shift
            if alph.index(plaintext[i].lower()) + shift >= len(alph):
                j -= len(alph)
            if plaintext[i].isupper():
                ciphertext += alph[j].upper()
            else:
                ciphertext += alph[j]   
        else:
            ciphertext += plaintext[i] 
    return ciphertexеt


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
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            j = alph.index(ciphertext[i].lower()) - shift
            if alph.index(ciphertext[i].lower()) - shift < 0:
                j += len(alph)
            if ciphertext[i].isupper():
                plaintext += alph[j].upper()
            else:
                plaintext += alph[j]   
        else:
            plaintext += ciphertext[i]
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:

    """

    Brute force breaking a Caesar cipher.

    """

    best_shift = 0

    # PUT YOUR CODE HERE

    return best_shift

