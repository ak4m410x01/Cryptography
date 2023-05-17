# from vigenere_cipher_generate_key import generate_key

### Vigenere_Cipher Encryption ####


def encrypt_vigenere_cipher(plain: str, key: str) -> str:
    cipher = ""
    key_idx = 0

    for i in plain:
        if i == " ":
            cipher += i

        else:
            plain_chr_state = 97 if i.islower() else 65
            key_chr_state = 97 if key[key_idx].islower() else 65

            cipher += chr(
                ((ord(i) - plain_chr_state) + (ord(key[key_idx]) - key_chr_state)) % 26
                + plain_chr_state
            )

            key_idx += 1

    return cipher


### Vigenere_Cipher Encryption ####

# plain = "Hello There"
# key = generate_key(plain, "iteam")
# cipher = encrypt_vigenere_cipher(plain, key)
# print(f"{plain}:{cipher}:{key}")
