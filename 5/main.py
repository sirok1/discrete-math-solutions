def generate_hamming_code(data_bits):
    r = 1
    while 2 ** r < data_bits + r + 1:
        r += 1
    print(f"{r} проверочных бита")
    total_bits = data_bits + r

    code_table = [[0] * total_bits for _ in range(r)]
    for i in range(r):
        for j in range(total_bits):
            code_table[i][j] = (j + 1) & (1 << i) != 0
    return code_table


def encode_data(data, code_table):
    data_bits = len(data)
    r = len(code_table)

    encoded_data = [0] * (data_bits + r)
    for i in range(r):
        for j in range(data_bits):
            encoded_data[2 ** i - 1] ^= int(data[j]) & code_table[i][j]
        encoded_data[data_bits + i] = encoded_data[2 ** i - 1]

    return encoded_data


def introduce_error(encoded_data):
    error_position = 3
    encoded_data[error_position - 1] ^= 1


def calculate_syndrome(encoded_data, code_table):
    r = len(code_table)
    syndrome = [0] * r

    for i in range(r):
        for j in range(len(encoded_data)):
            syndrome[i] ^= encoded_data[j] & code_table[i][j]

    return syndrome


def correct_error(encoded_data, syndrome):
    error_position = sum([s * 2 ** i for i, s in enumerate(syndrome)]) - 1

    if error_position >= 0:
        encoded_data[error_position] ^= 1
        print(f"Ошибка в разряде {error_position + 1}, исправлено.")

    return encoded_data


def print_hamming_matrix(code_table):
    for row in code_table:
        for i in range(0, len(row)):
            row[i] = 1 if row[i] else 0
    print('[')
    print('\n'.join(map(str, code_table)))
    print(']')


def main():
    data_bits = int(input("Введите количество информационных разрядов: "))

    code_table = generate_hamming_code(data_bits)
    print_hamming_matrix(code_table)

    data = input(f"Введите информационную комбинацию из {data_bits} бит: ")

    encoded_data = encode_data(data, code_table)
    print(encoded_data)
    introduce_error(encoded_data)

    syndrome = calculate_syndrome(encoded_data, code_table)
    print(f"Синдром: {syndrome}")

    corrected_data = correct_error(encoded_data, syndrome)
    print(f"Исправленная комбинация: {''.join(map(str, corrected_data))}")


if __name__ == "__main__":
    main()
