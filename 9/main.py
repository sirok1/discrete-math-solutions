def generate_key(length, a, b, m, initial):
    key = [0] * length
    key[0] = initial
    for i in range(1, length):
        key[i] = (a * key[i - 1] + b) % m
    return key


def encrypt(text, key):
    encrypted_text = []
    for i in range(len(text)):
        encrypted_char = ord(text[i]) ^ key[i % len(key)]
        encrypted_text.append(encrypted_char)
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = []
    for i in range(len(encrypted_text)):
        decrypted_char = chr(encrypted_text[i] ^ key[i % len(key)])
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)


original_text = "Это девятое задание по дискретной математике"

a = 5
b = 7
m = 256
initial = 13

gamma_length = len(original_text)
gamma_key = generate_key(gamma_length, a, b, m, initial)

encrypted_text = encrypt(original_text, gamma_key)

decrypted_text = decrypt(encrypted_text, gamma_key)

print(f"Открытый текст: {original_text}")
print(f"Гамма: {gamma_key}")
print(f"Зашифрованный текст: {encrypted_text}")
print(f"Дешифрованный текст: {decrypted_text}")
