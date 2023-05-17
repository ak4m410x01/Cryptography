#### Multiplicative Cipher Decryption ####


def decrypt_multiplicative_cipher(cipher: str, key: int) -> str:
    plain = ""

    for i in cipher:
        if i.islower():
            plain += chr(((ord(i) - 97) * key) % 26 + 97)

        elif i.isupper():
            plain += chr(((ord(i) - 65) * key) % 26 + 65)

        else:
            plain += i

    return plain


#### Multiplicative Cipher Decryption ####

# cipher = "Gksxkp"
# key = 3
# plain = decrypt_multiplicative_cipher(cipher, key)
# print(f"{plain}:{cipher}")
