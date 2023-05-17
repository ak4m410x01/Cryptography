#### rotx_cipher Encryption ####


def encrypt_rotx_cipher(plain: str, key: int = 13) -> str:
    cipher = ""

    for i in plain:
        if i.islower():
            cipher += chr(((ord(i) - 97) + key) % 26 + 97)
        elif i.isupper():
            cipher += chr(((ord(i) - 65) + key) % 26 + 65)
        else:
            cipher += i

    return cipher


#### rotx_cipher Encryption ####

# plain = "Hello World"
# cipher = encrypt_rotx_cipher(plain)
# print(f"{plain}:{cipher}")
