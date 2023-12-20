import random
from sympy import isprime, primerange


def eratosthenes_sieve(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes


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
        if pow(a, (n - 1) // 2, n) != legendre_symbol(a, n) % n:
            return False
    return True


def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)


def lehman_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        d = pow(a, (n - 1) // 2, n)
        if d != 1 and d != n - 1:
            return False
    return True


def rabin_miller_test(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def prime_factorization(n):
    factors = []
    for prime in primerange(2, n + 1):
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)
    return factors


limit = 256
primes_table = eratosthenes_sieve(limit)
print("Таблица простых чисел меньших 256:", primes_table)

large_prime = int(input("Введите число для проверки: "))
if fermat_test(large_prime):
    print(f"{large_prime} является простым числом.")
else:
    print(f"{large_prime} составное число. Разложение на множители:", prime_factorization(large_prime))

print(f"\nПроверка простоты числа {large_prime}:")
print("Тест Соловея–Штрассена:", solovay_strassen_test(large_prime))
print("Тест Лемана:", lehman_test(large_prime))
print("Тест Рабина–Миллера:", rabin_miller_test(large_prime))
print("Непосредственная проверка с помощью sympy:", isprime(large_prime))
