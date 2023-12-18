from cryptography.fernet import Fernet


def encrypt_decrypt_text(text, key, encrypt=True):
    cipher = Fernet(key)
    if encrypt:
        return cipher.encrypt(text.encode()).decode()

    else:
        return cipher.decrypt(text.encode()).decode()


key = Fernet.generate_key()
text_to_encrypt = "London is the capital of the Greate Britain"
encrypted_text = encrypt_decrypt_text(text_to_encrypt, key)
print(f"Encrypted Text: {encrypted_text}")
decrypted_text = encrypt_decrypt_text(encrypted_text, key, encrypt=False)
print(f"Decrypted Text: {decrypted_text}")
