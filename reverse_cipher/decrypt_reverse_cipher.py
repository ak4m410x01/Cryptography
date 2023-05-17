#### reverse_cipher Decryption ####


def decrypt_reverse_cipher(cipher: str) -> str:
    plain = ""

    for i in range(len(cipher) - 1, -1, -1):
        plain += cipher[i]

    return plain


#### reverse_cipher Decryption ####

# cipher = ".rehpic esrever nialpxe ot margorp si sihT"
# plain = decrypt_reverse_cipher(cipher)

# print(plain)
