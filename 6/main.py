import random
from math import gcd
from sympy import legendre_symbol

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    for i in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


prime_table = sieve_of_eratosthenes(256)
print("Таблица простых чисел меньших 256:", prime_table)

def fermat_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True

def solovay_strassen_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1 or pow(a, (n - 1) // 2, n) != legendre_symbol(a, n) % n:
            return False

    return True

def lehmann_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1 or pow(a, (n - 1) // 2, n) != 1:
            return False

    return True

def miller_rabin_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def is_prime_direct(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

p = 104729  

print(f"Тест Ферма: {fermat_test(p)}")
print(f"Тест Соловея–Штрассена: {solovay_strassen_test(p)}")
print(f"Тест Лемана: {lehmann_test(p)}")
print(f"Тест Рабина–Миллера: {miller_rabin_test(p)}")
print(f"Непосредственная проверка: {is_prime_direct(p)}")