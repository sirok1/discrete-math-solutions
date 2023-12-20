import re

encrypted_text = "Привет мир"
encrypted_text = encrypted_text.replace(" ", "").lower()
encrypted_text = re.sub(r"[ \s\d]|[^\w\s]", "", encrypted_text)

char_probabilities = {
    'а': 0.0801,
    'б': 0.0159,
    'в': 0.0454,
    'г': 0.0170,
    'д': 0.0298,
    'е': 0.0845,
    'ё': 0.0004,
    'ж': 0.0094,
    'з': 0.0165,
    'и': 0.0735,
    'й': 0.0121,
    'к': 0.0349,
    'л': 0.0440,
    'м': 0.0321,
    'н': 0.0670,
    'о': 0.1097,
    'п': 0.0281,
    'р': 0.0473,
    'с': 0.0547,
    'т': 0.0632,
    'у': 0.0262,
    'ф': 0.0026,
    'х': 0.0097,
    'ц': 0.0048,
    'ч': 0.0144,
    'ш': 0.0073,
    'щ': 0.0036,
    'ъ': 0.0004,
    'ы': 0.0190,
    'ь': 0.0174,
    'э': 0.0032,
    'ю': 0.0064,
    'я': 0.0201
}


def analyze_text(text):
    char_count = {}
    total_chars = 0
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
        total_chars += 1
    char_frequencies = {}
    for char, count in char_count.items():
        char_frequencies[char] = count / total_chars
    return char_frequencies


def decrypt_text(encrypted_text, char_probabilities):
    decrypted_text = ""
    for char in encrypted_text:
        if char in char_probabilities:
            possible_chars = char_probabilities.keys()
            min_difference = float('inf')
            best_match = ''
            for possible_char in possible_chars:
                difference = abs(char_probabilities[char] - char_probabilities[possible_char])
                if difference < min_difference:
                    min_difference = difference
                    best_match = possible_char
            decrypted_text += best_match
        else:
            decrypted_text += char
    return decrypted_text


char_frequencies = analyze_text(encrypted_text)
decrypted_text = decrypt_text(encrypted_text, char_probabilities)
print("Статистика символов:", char_frequencies)
print("Дешифрованный текст:", decrypted_text)
