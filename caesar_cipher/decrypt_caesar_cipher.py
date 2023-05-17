#### Caesar_Cipher Decryption ####


def decrypt_caesar_cipher(cipher: str, key: int) -> str:
    plain = ""

    for i in cipher:
        if i.islower():
            plain += chr(((ord(i) - 97) - key) % 26 + 97)

        elif i.isupper():
            plain += chr(((ord(i) - 65) - key) % 26 + 65)

        else:
            plain += i

    return plain


#### Caesar_Cipher Decryption ####

# cipher = "Jhlzhy Jpwoly"
# key = 7
# plain = decrypt_caesar_cipher(cipher, key)

# print(plain)
