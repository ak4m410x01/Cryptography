#### Vigenere_Cipher Generate Key ####


def generate_key(msg: str, key: str) -> str:
    key_idx = 0
    new_key = ""

    for i in msg:
        if i == " ":
            continue

        new_key += key[key_idx % len(key)]
        key_idx += 1

    return new_key


#### Vigenere_Cipher Generate Key ####

# msg = "hello there"
# key = "iteam"
# print(generate_key(msg, key))
