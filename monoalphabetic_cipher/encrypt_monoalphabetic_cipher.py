#### Monoalphabetic_Cipher Encryption ####


def encrypt_monoalphabetic_cipher(plain: str, letters: str, key: str) -> str:
    plain = plain.lower()
    cipher = ""

    for i in plain:
        idx = letters.find(i)

        if idx == -1:
            cipher += "?"
        else:
            cipher += key[idx]

    return cipher


#### Monoalphabetic_Cipher Encryption ####

# letters = "abcdefghijklmnopqrstuvwxyz"
# key = "qwertyuiopasdmghjklzxcvbnf"
# plain = "Hello"
# cipher = encrypt_monoalphabetic_cipher(plain, letters, key)
# print(f"{plain}:{cipher}")
