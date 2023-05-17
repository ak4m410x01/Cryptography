#### Affine Cipher Decryption ####


def decrypt_affine_cipher(cipher: str, key1: int, key2: int) -> str:
    plain = ""
    for i in cipher:
        if i.islower():
            plain += chr(((((ord(i) - 97) - key2) * key1) % 26) + 97)

        elif i.isupper():
            plain += chr(((((ord(i) - 65) - key2) * key1) % 26) + 65)

        else:
            plain += i

    return plain


#### Affine Cipher Decryption ####

# cipher = "hello world"
# key1 = 15
# key2 = 2
# plain = decrypt_affine_cipher(cipher, key1, key2)

# print(f"{plain}:{cipher}")
