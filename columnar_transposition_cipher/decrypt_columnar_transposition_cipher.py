from math import ceil

#### Columnar Transposition Cipher Decryption ####


def decrypt_columnar_transposition_cipher(cipher: str, key: int) -> str:
    data = [""] * (key - 1)

    column_size = key
    row_size = ceil(len(cipher) / key)
    cipher_idx = 0

    for column_idx in range(column_size):
        for row_idx in range(row_size):
            data[row_idx] += cipher[cipher_idx] if (cipher_idx < len(cipher)) else "?"
            cipher_idx += 1
    print(data)
    plain = ""
    for row_idx in range(row_idx + 1):
        for column_idx in range(column_size):
            if data[row_idx][column_idx] == "?":
                continue

            plain += data[row_idx][column_idx]

    return plain


#### Columnar Transposition Cipher Decryption ####

# cipher = "hore llwdlo"
# key = 4
# plain = decrypt_columnar_transposition_cipher(cipher, key)
# print(f"{plain}:{cipher}")
