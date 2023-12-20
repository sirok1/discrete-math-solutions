import math
import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_large_prime_number(min_value):
    while True:
        p = random.randint(min_value, min_value + 1000)
        if is_prime(p):
            return p


p = generate_large_prime_number(1000000)
q = generate_large_prime_number(1000000)

n = p * q
phi = (p - 1) * (q - 1)

e = random.randint(1, phi - 1)
while gcd(e, phi) != 1:
    e = random.randint(1, phi - 1)

d = multiplicative_inverse(e, phi)

plaintext = "Hello, World!"

block_size = n.bit_length() // 8
blocks = [
    plaintext.encode()
    for plaintext in [
        plaintext[i : i + block_size] for i in range(0, len(plaintext), block_size)
    ]
]

ciphertext_blocks = []
for block in blocks:
    m = int.from_bytes(block, byteorder="big")
    c = pow(m, e, n)
    ciphertext_blocks.append(c)

decrypted_blocks = []
for ciphertext_block in ciphertext_blocks:
    m = pow(ciphertext_block, d, n)
    decrypted_block = m.to_bytes((n.bit_length() + 7) // 8, byteorder="big").decode(
        "utf-8", "ignore"
    )
    decrypted_blocks.append(decrypted_block)

decrypted_text = "".join(decrypted_blocks)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)
print("Открытый текст:", plaintext)
print("Зашифрованный текст:", ciphertext_blocks)
print("Расшифрованный текст:", decrypted_text)