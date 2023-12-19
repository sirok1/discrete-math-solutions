import string

def preprocess_text(text):
    # Привести все слова к нижнему регистру и удалить знаки препинания
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def simple_substitution_cipher(text, key):
    # Зашифровать текст методом простой замены
    alphabet = string.ascii_lowercase
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            index = (alphabet.index(char) + key) % 26
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text

def simple_substitution_decipher(encrypted_text, key):
    # Дешифровать текст методом простой замены
    return simple_substitution_cipher(encrypted_text, -key)

def complex_substitution_cipher(text, key):
    # Зашифровать текст методом сложной замены
    mapping = {char: key[i % len(key)] for i, char in enumerate(string.ascii_lowercase)}
    encrypted_text = "".join(mapping[char] if char.isalpha() else char for char in text)
    return encrypted_text

def complex_substitution_decipher(encrypted_text, key):
    # Дешифровать текст методом сложной замены
    reverse_mapping = {value: char for char, value in zip(string.ascii_lowercase, key)}
    decrypted_text = "".join(reverse_mapping[char] if char.isalpha() else char for char in encrypted_text)
    return decrypted_text

def main():
    # Ввод текста
    original_text = input("Введите текст для шифрования: ")

    # Предварительная обработка текста
    processed_text = preprocess_text(original_text)

    # Запрос ключа шифрования
    key_simple = int(input("Введите ключ для простого метода замены: "))
    key_complex = input("Введите ключ для сложного метода замены: ")

    # Шифрование и дешифрование
    encrypted_simple = simple_substitution_cipher(processed_text, key_simple)
    decrypted_simple = simple_substitution_decipher(encrypted_simple, key_simple)

    encrypted_complex = complex_substitution_cipher(processed_text, key_complex)
    decrypted_complex = complex_substitution_decipher(encrypted_complex, key_complex)

    # Вывод результатов
    print("\nРезультаты:")
    print(f"Оригинальный текст: {original_text}")
    print(f"Обработанный текст: {processed_text}")
    print(f"Зашифрованный (простой метод): {encrypted_simple}")
    print(f"Дешифрованный (простой метод): {decrypted_simple}")
    print(f"Зашифрованный (сложный метод): {encrypted_complex}")
    print(f"Дешифрованный (сложный метод): {decrypted_complex}")

if __name__ == "__main__":
    main()
