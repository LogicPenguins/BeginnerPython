import time

def encrypt(plain):
    even = ""
    odd = ""

    count = 0
    for char in plain:
        if count % 2 == 0:
            even += char
        else:
            odd += char
        count += 1
    cipher = odd + even

    return cipher


def decrypt(cipher):
    half = len(cipher) // 2
    odd = cipher[:half]
    even = cipher[half:]

    plain = " "

    for i in range(half):
        plain += even[i]
        plain += odd[i]

    if len(even) > len(odd):
        plain += even[-1]

    return plain


message_encrypt = input("Message: ")
print(f'Your message is being encrypted...')
time.sleep(3)
message_encrypt = encrypt(message_encrypt)
print(message_encrypt)
print('Encryption complete.')


message_decrypt = decrypt(message_encrypt)
print(f'Here is your original message: {message_decrypt}')
