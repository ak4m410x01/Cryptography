#### Caesar_Cipher Encryption ####


def encrypt_caesar_cipher(plain: str, key: int) -> str:
    cipher = ""

    for i in plain:
        if i.islower():
            cipher += chr(((ord(i) - 97) + key) % 26 + 97)

        elif i.isupper():
            cipher += chr(((ord(i) - 65) + key) % 26 + 65)

        else:
            cipher += i

    return cipher


#### Caesar_Cipher Encryption ####

# plain = "Caesar Cipher"
# key = 7
# cipher = encrypt_caesar_cipher(plain, key)

# print(cipher)
