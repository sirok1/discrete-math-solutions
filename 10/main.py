import math
import random


def is_prime_number(num):
    if num <= 1:
        return f"{num} не является простым"
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return f"{num} не является простым"
    return f"{num} является простым"


def random_prime_number(minimum, maximum):
    num = 0
    while is_prime_number(num) != f"{num} является простым":
        num = random.randint(minimum, maximum)
    return num


prime_number1 = random_prime_number(10000, 200000)
prime_number2 = random_prime_number(10000, 200000)

print('Первое простое число:', prime_number1)
print('Второе простое число:', prime_number2)

sum_result = prime_number1 + prime_number2
print('Сумма чисел:', sum_result)

subtraction_result = prime_number2 - prime_number1
print('Разность чисел:', subtraction_result)

multiplication_result = prime_number1 * prime_number2
print('Произведение чисел:', multiplication_result)

division_result = prime_number1 / prime_number2
print('Частное чисел:', division_result)

remainder_result = prime_number1 % prime_number2
print('Остаток от деления:', remainder_result)

power_result = pow(prime_number1, 2) % prime_number2
print('Возведение в степень по модулю:', power_result)
