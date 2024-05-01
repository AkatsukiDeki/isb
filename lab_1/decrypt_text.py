from read_write import *


def decrypt_task_2(path: str, encoded_text: str, decryption_key: dict) -> None:
    """
    Decrypts the encoded text using a simple substitution cipher decryption key from a JSON file.

    Args:
        path (str): The path to decrypted text.
        encoded_text (str): The text to decrypt.
        decryption_key (dict): The path to the JSON file containing the decryption key.
    """
    decrypted_text = ''
    for char in encoded_text:
        if char in decryption_key:
            decrypted_text += decryption_key[char]
        else:
            decrypted_text += char
    write_file(path, decrypted_text)