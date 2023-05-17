#### Multiplicative Cipher Encryption ####


def encrypt_multiplicative_cipher(plain: str, key: int) -> str:
    cipher = ""

    for i in plain:
        if i.islower():
            cipher += chr(((ord(i) - 97) * key) % 26 + 97)

        elif i.isupper():
            cipher += chr(((ord(i) - 65) * key) % 26 + 65)

        else:
            cipher += i

    return cipher


#### Multiplicative Cipher Encryption ####

# plain = "Secret"
# key = 9
# cipher = encrypt_multiplicative_cipher(plain, key)
# print(f"{plain}:{cipher}")
