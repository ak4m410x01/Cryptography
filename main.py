# import <Dir_Name>.<File_Name>
# from <Dir_Name>.<File Name> import <Func_Name>
# from <Dir_Name> import <File Name>.<Func_Name>


from caesar_cipher.encrypt_caesar_cipher import encrypt_caesar_cipher
from caesar_cipher.decrypt_caesar_cipher import decrypt_caesar_cipher

plain = "Abdullah Kamal"
key = 2

# import <Dir_Name>.<File_Name>
cipher = encrypt_caesar_cipher(plain, key)

print(f"Cipher:'{cipher}'")

_plain = decrypt_caesar_cipher(cipher, key)

print(f"Plain:'{_plain}'")
