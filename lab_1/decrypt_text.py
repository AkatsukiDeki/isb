from read_write import *


def decrypt_task_2(path: str, encoded_text: str, decryption_key: dict) -> None:
    """
     Расшифровывает закодированный текст с использованием ключа простой подстановочной шифровки из JSON-файла.

    Args:
        path (str): Путь к файлу, в который будет записан расшифрованный текст.
        encoded_text (str): Текст, который нужно расшифровать.
        decryption_key (dict): Ключ для расшифровки, представляющий собой словарь, отображающий каждый символ в закодированном тексте на его соответствующий расшифрованный символ.

    Returns:
        None
    """

    decrypted_text = ''
    for char in encoded_text:
        if char in decryption_key:
            decrypted_text += decryption_key[char]
        else:
            decrypted_text += char
    write_file(path, decrypted_text)