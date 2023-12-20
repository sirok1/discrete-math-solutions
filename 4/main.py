import numpy as np


def hamming_code(data_bits):
    r = 1
    while 2 ** r < r + len(data_bits) + 1:
        r += 1

    G = np.zeros((len(data_bits), len(data_bits) + r))
    for i in range(len(data_bits)):
        G[i, :len(data_bits)] = list(format(i + 1, f'0{len(data_bits)}b'))

    H = np.zeros((r, len(data_bits) + r))
    for i in range(r):
        H[i, i:i + 1] = 1
        H[i, len(data_bits):] = list(format(2 ** i, f'0{r}b'))

    data_vector = np.array(list(map(int, list(data_bits))))
    encoded_vector = np.dot(data_vector, G) % 2

    error_position = np.random.randint(len(encoded_vector))
    encoded_vector[error_position] = 1 - encoded_vector[error_position]

    syndrome = np.dot(encoded_vector, H.T) % 2

    if not np.any(syndrome):
        print("Ошибка не обнаружена.")
    else:
        error_position = int(''.join(map(str, syndrome)), 2)
        encoded_vector[error_position - 1] = 1 - encoded_vector[error_position - 1]
        print(f"Обнаружена и исправлена ошибка в разряде {error_position}.")


if __name__ == "__main__":
    n = int(input("Введите количество информационных разрядов: "))

    data_bits = np.random.randint(2, size=n)

    print("Информационная комбинация:", data_bits)
    hamming_code(data_bits)
