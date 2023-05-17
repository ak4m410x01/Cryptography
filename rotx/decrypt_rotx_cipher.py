#### rotx_cipher Decryption ####


def decrypt_rotx_cipher(cipher: str, key: int = 13) -> str:
    plain = ""

    for i in cipher:
        if i.islower():
            plain += chr(((ord(i) - 97) + key) % 26 + 97)
        elif i.isupper():
            plain += chr(((ord(i) - 65) + key) % 26 + 65)
        else:
            plain += i

    return plain


#### rotx_cipher Decryption ####

# cipher = "Uryyb Jbeyq"
# plain = decrypt_rotx_cipher(cipher)
# print(f"{plain}:{cipher}")
