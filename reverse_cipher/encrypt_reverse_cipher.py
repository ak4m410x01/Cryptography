#### reverse_cipher Encryption ####


def encrypt_reverse_cipher(plain: str) -> str:
    cipher = ""

    for i in range(len(plain) - 1, -1, -1):
        cipher += plain[i]

    return cipher


#### reverse_cipher Encryption ####

# plain = "This is program to explain reverse cipher."
# cipher = encrypt_reverse_cipher(plain)

# print(cipher)
