def generate_hamming_table(data_bits):
    
    hamming_bits = 2 ** data_bits - 1

    
    table = [[0] * hamming_bits for _ in range(data_bits)]

    
    for i in range(data_bits):
        for j in range(hamming_bits):
            table[i][j] = (j + 1) & (2 ** i) != 0

    return table

def hamming_encode(data, hamming_table):
    
    encoded_data = [0] * len(hamming_table[0])

    for i, bit in enumerate(data, start=1):
        if bit:
            for j in range(len(hamming_table)):
                encoded_data[j] ^= hamming_table[j][i - 1]

    return encoded_data

def introduce_error(encoded_data):
    
    import random
    error_position = random.randint(0, len(encoded_data) - 1)
    encoded_data[error_position] ^= 1
    return error_position

def hamming_decode(encoded_data, hamming_table):
    
    syndrome = [0] * len(hamming_table)

    for i in range(len(hamming_table)):
        for j in range(len(encoded_data)):
            syndrome[i] ^= encoded_data[j] * hamming_table[i][j]

    
    error_position = sum([bit * (2 ** i) for i, bit in enumerate(syndrome)])

    if error_position > 0:
        print(f"Ошибка обнаружена в разряде {error_position}")
        encoded_data[error_position - 1] ^= 1
    else:
        print("Ошибок не обнаружено")

    
    return [encoded_data[i] for i in range(len(encoded_data)) if i + 1 not in hamming_table]

def main():
    
    data_bits = int(input("Введите количество информационных разрядов: "))

    
    hamming_table = generate_hamming_table(data_bits)

    
    data = [int(bit) for bit in input("Введите информационную комбинацию (биты через пробел): ").split()]

    
    encoded_data = hamming_encode(data, hamming_table)

    
    error_position = introduce_error(encoded_data)

    
    decoded_data = hamming_decode(encoded_data, hamming_table)

    print(f"Исходная информация: {data}")
    print(f"Закодированная информация: {encoded_data}")
    print(f"Исправленная информация: {decoded_data}")

if __name__ == "__main__":
    main()
