from encrypt_text import encrypt_vigenere, decrypt_vigenere
from read_write import read_json

# Загрузка ключа из файла конфигурации
config = read_json("texts/task1/vigenere_key.json")
VIGENERE_KEY = config["vigenere_key"]

# Пример использования
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = "path_texts_task1!"
encrypted_text = encrypt_vigenere(text, VIGENERE_KEY, alphabet)
decrypted_text = decrypt_vigenere(encrypted_text, VIGENERE_KEY, alphabet)


