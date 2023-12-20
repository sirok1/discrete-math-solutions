import heapq
import re
from collections import Counter
import math


def calculate_entropy(text):
    frequencies = Counter(text)  
    total_symbols = len(text)
    entropy = -sum((count / total_symbols) * ((math.log2(count / total_symbols))) for count in frequencies.values())
    return entropy


def huffman_coding(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)  
    while len(heap) > 1:
        lo = heapq.heappop(heap)  
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]  
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]  
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0][1:]


def calculate_code_length_and_efficiency(codes, frequencies):
    total_length = sum(len(code) * frequencies[symbol] for symbol, code in
                       codes)  
    average_length = total_length / sum(frequencies.values())
    efficiency = 1 - (average_length / 8)
    return average_length, efficiency


def encode_text(text, encoding_dict):
    return ''.join(encoding_dict[symbol] for symbol in text)  


def decode_text(encoded_text, decoding_dict):
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        for code, symbol in decoding_dict.items():
            if current_code == code:
                decoded_text += symbol
                current_code = ""
                break  
    return decoded_text



text = "Русский язык является одним из наиболее сложных в современном мире, но он не так распространен как многие другие. Особенностью русского языка является невероятная выразительность и возможность составлять слова, меняя склонения и падежи. Такой вариабельности не существует во многих других языках. На протяжении довольно длительного периода русский язык впитывал в себя огромное количество других языков. Собственно такой процесс является вполне нормальным, но русский язык в современном мире явно отличается от такого языка, на котором говорили наши далекие предки."

processed_text = text.lower()
processed_text = re.sub(r"[ \s\d]|[^\w\s]", "", processed_text)
print("Обработанный текст:", processed_text)


entropy = calculate_entropy(processed_text)
print("Энтропия:", entropy)


uniform_code_length = math.log2(len(set(processed_text)))
redundancy = uniform_code_length - entropy
print("Длина кода при равномерном кодировании:", uniform_code_length)
print("Избыточность:", redundancy)


frequencies = Counter(processed_text)
huffman_codes = huffman_coding(frequencies)
average_length, efficiency = calculate_code_length_and_efficiency(huffman_codes, frequencies)
print("Схема алфавитного кодирования для однобуквенных сочетаний (метод Хаффмана):", huffman_codes)
print("Средняя длина элементарного кода:", average_length)
print("Эффективность сжатия:", efficiency)


encoded_text = encode_text(processed_text, dict(huffman_codes))
decoded_text = decode_text(encoded_text, {code: symbol for symbol, code in huffman_codes})
print("Закодированный текст:", encoded_text)
print("Декодированный текст:", decoded_text)



frequencies = Counter(processed_text)
huffman_codes = huffman_coding(frequencies)
average_length, efficiency = calculate_code_length_and_efficiency(huffman_codes, frequencies)
print("Схема алфавитного кодирования для двухбуквенных сочетаний (метод Хаффмана):", huffman_codes)
print("Средняя длина элементарного кода:", average_length)
print("Эффективность сжатия:", efficiency)

encoded_text = encode_text(processed_text, dict(huffman_codes))
decoded_text = decode_text(encoded_text, {code: symbol for symbol, code in huffman_codes})
print("Закодированный текст:", encoded_text)
print("Декодированный текст:", decoded_text)
