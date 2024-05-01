from read_write import*
from itertools import cycle

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя :.,?/!()- \n"
translation_table = str.maketrans(alphabet, alphabet[len(alphabet)//2:] + alphabet[:len(alphabet)//2])


def read_json(file_path):
    """
        Загружает данные из JSON-файла.

        Args:
            file_path (str): Путь к JSON-файлу.

        Returns:
            dict: Данные, загруженные из JSON-файла.
        """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write_json(data, file_path):
    """
       Сохраняет данные в JSON-файл.

       Args:
           data (dict): Данные, которые нужно записать в JSON-файл.
           file_path (str): Путь к JSON-файлу.
       """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
    except IOError:
        print(f"Error: Unable to write to file {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_files(file_path):
    """
        Читает содержимое файла.

        Args:
            file_path (str): Путь к файлу.

        Returns:
            str: Содержимое файла.
        """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except IOError:
        print(f"Error: Unable to read file {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write_files(file_path, data):
    """
        Записывает данные в файл.

        Args:
            file_path (str): Путь к файлу.
            data (str): Данные, которые нужно записать в файл.
        """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except IOError:
        print(f"Error: Unable to write to file {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def vigenere_cipher(message, key, action):
    """
       Выполняет шифрование или расшифровку сообщения с помощью алгоритма Виженера.

       Args:
           message (str): Сообщение для шифрования или расшифровки.
           key (str): Ключ для шифрования или расшифровки.
           action (str): "encrypt" для шифрования, "decrypt" для расшифровки.

       Returns:
           str: Зашифрованное или расшифрованное сообщение.
       """
    message = message.translate(translation_table)
    key = key.translate(translation_table)
    result = ''.join(alphabet[(alphabet.index(char) + (alphabet.index(key_char) if action == 'encrypt' else -alphabet.index(key_char))) % len(alphabet)] for char, key_char in zip(message, cycle(key)))
    return result


def generate_vigenere_key(message, keyword):
    """
    Генерирует ключ для алгоритма Виженера.

    Args:
        message (str): Сообщение, для которого нужно сгенерировать ключ.
        keyword (str): Ключевое слово для генерации ключа.

    Returns:
        str: Сгенерированный ключ в верхнем регистре.
    """
    key = ''.join(keyword[i % len(keyword)] for i, char in enumerate(message) if char in alphabet)
    return key.upper()


def save_vigenere_key(message, keyword, file_path):
    """
       Сохраняет ключ для алгоритма Виженера в JSON-файл.

       Args:
           message (str): Сообщение, для которого нужно сохранить ключ.
           keyword (str): Ключевое слово для генерации ключа.
           file_path (str): Путь к JSON-файлу, куда нужно сохранить ключ.
       """
    key = generate_vigenere_key(message, keyword)
    write_json({'key': key}, file_path)


def load_vigenere_key(file_path):
    """
        Загружает ключ для алгоритма Виженера из JSON-файла.

        Args:
            file_path (str): Путь к JSON-файлу, откуда нужно загрузить ключ.

        Returns:
            str: Загруженный ключ.
        """
    return read_json(file_path)['key']


def encrypt_file(file_path, key, output_file_path):
    """
       Шифрует содержимое файла с помощью алгоритма Виженера.

       Args:
           file_path (str): Путь к файлу, который нужно зашифровать.
           key (str): Ключ для шифрования.
           output_file_path (str): Путь к файлу, куда нужно сохранить зашифрованные данные.
       """
    message = read_files(file_path)
    encrypted_message = vigenere_cipher(message, key, 'encrypt')
    write_files(output_file_path, encrypted_message)


def decrypt_file(file_path, key, output_file_path):
    """
       Шифрует содержимое файла с помощью алгоритма Виженера.

       Args:
           file_path (str): Путь к файлу, который нужно зашифровать.
           key (str): Ключ для шифрования.
           output_file_path (str): Путь к файлу, куда нужно сохранить зашифрованные данные.
       """
    message = read_files(file_path)
    decrypted_message = vigenere_cipher(message, key, 'decrypt')
    write_files(output_file_path, decrypted_message)

'''
if __name__ == "__main__":
    config = read_json('config.json')
    save_vigenere_key("ПРИВЕТ МИР", "КЛЮЧ", config['path_key_task1'])
    key = load_vigenere_key(config['path_key_task1'])
    encrypt_file(config['path_text_task1'], key, config['path_encrypted_text'])
    decrypt_file(config['path_encrypted_text'], key, config['path_decrypted_text'])
'''