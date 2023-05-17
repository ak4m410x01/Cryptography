# from vigenere_cipher_generate_key import generate_key

### Vigenere_Cipher Encryption ####


def decrypt_vigenere_cipher(cipher: str, key: str) -> str:
    plain = ""
    key_idx = 0

    for i in cipher:
        if i == " ":
            plain += i

        else:
            cipher_chr_state = 97 if i.islower() else 65
            key_chr_state = 97 if key[key_idx].islower() else 65

            plain += chr(
                ((ord(i) - cipher_chr_state) - (ord(key[key_idx]) - key_chr_state)) % 26
                + cipher_chr_state
            )

            key_idx += 1

    return plain


### Vigenere_Cipher Encryption ####

# cipher = "Pxpla Bairq"
# key = generate_key(cipher, "iteam")
# plain = decrypt_vigenere_cipher(cipher, key)
# print(f"{plain}:{cipher}:{key}")
