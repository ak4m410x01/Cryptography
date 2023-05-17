from math import ceil

#### Columnar Transposition Cipher Encryption ####


def encrypt_columnar_transposition_cipher(plain: str, key: int) -> str:
    data = []

    column_size = key
    row_size = ceil(len(plain) / key)
    plain_idx = 0

    for row_idx in range(row_size):
        row_data = ""

        for column_idx in range(column_size):
            row_data += plain[plain_idx] if plain_idx < len(plain) else "?"
            plain_idx += 1

        data.append(row_data)

    cipher = ""

    for i in range(column_size):
        for j in range(row_size):
            cipher += data[j][i]

    return cipher


#### Columnar Transposition Cipher Encryption ####

# plain = "hello world"
# key = 4
# cipher = encrypt_columnar_transposition_cipher(plain, key)
# print(f"{plain}:{cipher}")
