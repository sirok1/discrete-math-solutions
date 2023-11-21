import math
from collections import Counter


def shannon_fano_coding(freqs):
    if len(freqs) == 1:
        return {list(freqs.keys())[0]: '0'}

    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    total = sum(freqs.values())

    split_idx = 0
    cumulative_freq = 0

    for i, (char, freq) in enumerate(sorted_freqs):
        if cumulative_freq + freq <= total/2:
            cumulative_freq += freq
            split_idx = i
        else:
            break

    left_group = dict(sorted_freqs[:split_idx+1])
    right_group = dict(sorted_freqs[split_idx+1:])

    left_codes = shannon_fano_coding(left_group)
    right_codes = shannon_fano_coding(right_group)

    for char in left_codes:
        left_codes[char] = '0' + left_codes[char]

    for char in right_codes:
        right_codes[char] = '1' + right_codes[char]

    left_codes.update(right_codes)
    return left_codes


text = "ABRACADABRA"

# Single Letter Shannon-Fano Coding
single_freqs = Counter(text)
single_codes = shannon_fano_coding(single_freqs)

encoded_single = ''.join([single_codes[char] for char in text])

# Two Letter Shannon-Fano Coding
two_letter_freqs = Counter([text[i:i + 2] for i in range(0, len(text) - 1, 2)])
two_letter_codes = shannon_fano_coding(two_letter_freqs)

encoded_two_letter = ''.join([two_letter_codes[text[i:i + 2]] for i in range(0, len(text) - 1, 2)])

# Calculate Entropy
entropy = -sum([(freq / len(text)) * math.log2(freq / len(text)) for freq in single_freqs.values()])

# Uniform Code Length
uniform_length = math.ceil(math.log2(len(single_freqs)))

# Redundancy
redundancy = uniform_length - entropy

print("Single Letter Shannon-Fano Encoding:", encoded_single)
print("Two Letter Shannon-Fano Encoding:", encoded_two_letter)
print("Entropy:", entropy)
print("Uniform Code Length:", uniform_length)
print("Redundancy:", redundancy)


# Decoding is done by reversing the dictionary and matching longest prefix
def decode(encoded, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded = ""
    buffer = ""

    for bit in encoded:
        buffer += bit
        if buffer in reverse_codes:
            decoded += reverse_codes[buffer]
            buffer = ""

    return decoded


print("Decoded Single Letter Encoding:", decode(encoded_single, single_codes))
print("Decoded Two Letter Encoding:", decode(encoded_two_letter, two_letter_codes))
