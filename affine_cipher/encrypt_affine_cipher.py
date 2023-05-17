#### Affine Cipher Encryption ####


def encrypt_affine_cipher(plain: str, key1: int, key2: int) -> str:
    cipher = ""
    for i in plain:
        if i.islower():
            cipher += chr(((((ord(i) - 97) * key1) + key2) % 26) + 97)

        elif i.isupper():
            cipher += chr(((((ord(i) - 65) * key1) + key2) % 26) + 65)

        else:
            cipher += i

    return cipher


#### Affine Cipher Encryption ####

# plain = "hello world"
# key1 = 7
# key2 = 2
# cipher = encrypt_affine_cipher(plain, key1, key2)

# print(f"{plain}:{cipher}")
