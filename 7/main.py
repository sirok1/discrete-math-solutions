import string


def preprocess_text(text):
    
    text = text.lower()

    
    text = text.translate(str.maketrans("", "", string.punctuation))

    return text



def simple_substitution_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    encrypted_text = ""

    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + key) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text



def decrypt_simple_substitution_cipher(encrypted_text, key):
    return simple_substitution_cipher(encrypted_text, -key)



def gronsfeld_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    encrypted_text = ""

    for i, char in enumerate(text):
        if char in alphabet:
            key_digit = int(str(key)[i % len(str(key))])
            index = (alphabet.index(char) - key_digit) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text



def decrypt_gronsfeld_cipher(encrypted_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    decrypted_text = ""

    for i, char in enumerate(encrypted_text):
        if char in alphabet:
            key_digit = int(str(key)[i % len(str(key))])
            index = (alphabet.index(char) + key_digit) % len(alphabet)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char

    return decrypted_text


def main():
    original_text = input("Текст для шифрования: ")

    preprocessed_text = preprocess_text(original_text)

    key_simple_substitution = int(input("Ключ простой замены: "))
    key_gronsfeld = int(input("Ключ для шифра Гронсфельда: "))

    encrypted_simple_substitution = simple_substitution_cipher(
        preprocessed_text, key_simple_substitution
    )
    print("Зашифрованный текст (простая замена):", encrypted_simple_substitution)

    decrypted_simple_substitution = decrypt_simple_substitution_cipher(
        encrypted_simple_substitution, key_simple_substitution
    )
    print("Дешифрованный текст (простая замена):", decrypted_simple_substitution)

    encrypted_gronsfeld = gronsfeld_cipher(preprocessed_text, key_gronsfeld)
    print("Зашифрованный текст (шифр Гронсфельда):", encrypted_gronsfeld)

    
    decrypted_gronsfeld = decrypt_gronsfeld_cipher(encrypted_gronsfeld, key_gronsfeld)
    print("Дешифрованный текст (шифр Гронсфельда):", decrypted_gronsfeld)


if __name__ == "__main__":
    main()