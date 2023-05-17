#### Monoalphabetic_Cipher Decryption ####


def decrypt_monoalphabetic_cipher(cipher: str, letters: str, key: str) -> str:
    cipher = cipher.lower()
    plain = ""

    for i in cipher:
        idx = key.find(i)

        if idx == -1:
            plain += "?"
        else:
            plain += letters[idx]

    return plain


#### Monoalphabetic_Cipher Decryption ####

# letters = "abcdefghijklmnopqrstuvwxyz"
# key = "qwertyuiopasdmghjklzxcvbnf"
# cipher = "itssg"
# plain = decrypt_monoalphabetic_cipher(cipher, letters, key)
# print(f"{plain}:{cipher}")
