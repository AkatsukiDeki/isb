import os
import json


def vigenere_cipher(message, key, action):
    """
    Шифрует или дешифрует сообщение с помощью шифра Виженера.

    Параметры:
    message (str): Сообщение, которое нужно зашифровать/дешифровать.
    key (str): Ключевое слово для шифрования/дешифрования.
    action (str): 'encrypt' для шифрования, 'decrypt' для дешифрования.

    Возвращает:
    str: Зашифрованное или дешифрованное сообщение.
    """

    # Приводим сообщение и ключ к верхнему регистру
    message = message.upper()
    key = key.upper()

    result = ''
    key_index = 0

    for char in message:
        if char.isalpha():
            # Если символ является буквой, применяем шифр Виженера
            shift = ord(key[key_index]) - ord('A')
            if action == 'encrypt':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            # Если символ не является буквой, оставляем его без изменений
            result += char

    return result


def generate_vigenere_key(message, keyword):
    """
    Генерирует ключ для шифра Виженера.

    Параметры:
    message (str): Сообщение, для которого нужно сгенерировать ключ.
    keyword (str): Ключевое слово для генерации ключа.

    Возвращает:
    str: Сгенерированный ключ.
    """
    key = ''
    message_index = 0
    for char in message:
        if char.isalpha():
            key += keyword[message_index % len(keyword)]
            message_index += 1
        else:
            key += ' '
    return key.upper()


# Пример использования
message = "HELLO WORLD"
keyword = "KEY"
key = generate_vigenere_key(message, keyword)
print(key)  # Выведет: KEY KEY KEY

encrypted_message = vigenere_cipher(message, key, 'encrypt')
print(encrypted_message)  # Выведет: FIELD RYVQX

decrypted_message = vigenere_cipher(encrypted_message, key, 'decrypt')
print(decrypted_message)  # Выведет: HELLO WORLD

key_folder = 'path_key_task1'
text_folder = 'path_text_task1'
folder_path = 'path_folder_text'


def save_vigenere_key(message, keyword, folder_path):
    """
    Сохраняет ключ для шифра Виженера в файл JSON.

    Параметры:
    message (str): Сообщение, для которого нужно сохранить ключ.
    keyword (str): Ключевое слово для генерации ключа.
    folder_path (str): Путь к папке, в которой нужно сохранить ключ.
    """
    key = generate_vigenere_key(message, keyword)
    file_path = os.path.join(folder_path, 'vigenere_key.json')
    with open(file_path, 'w') as file:
        json.dump({'key': key}, file)


def load_vigenere_key(folder_path):
    """
    Загружает ключ для шифра Виженера из файла JSON.

    Параметры:
    folder_path (str): Путь к папке, в которой хранится ключ.

    Возвращает:
    str: Загруженный ключ.
    """
    file_path = os.path.join(folder_path, 'vigenere_key.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['key']


def encrypt_file(file_path, key):
    """
    Шифрует текстовый файл с помощью шифра Виженера.

    Параметры:
    file_path (str): Путь к файлу, который нужно зашифровать.
    key (str): Ключ для шифрования.
    """
    with open(file_path, 'r') as file:
        message = file.read().replace('\n', ' ').upper()
    encrypted_message = vigenere_cipher(message, key, 'encrypt')
    encrypted_file_path = os.path.join(text_folder, 'encrypted_' + os.path.basename(file_path))
    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted_message)


key_folder = 'path_key_task1'
text_folder = 'path_texts_task1'
folder_path = 'path_folder_texts'

# Пример использования
save_vigenere_key("HELLO WORLD", "KEY", key_folder)
key = load_vigenere_key(key_folder)
encrypt_file(os.path.join(text_folder, 'input.txt'), key)