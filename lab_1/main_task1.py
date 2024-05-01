from encrypt_text import read_json, save_vigenere_key, encrypt_file, decrypt_file


def main():
    # Загружаем конфигурацию из файла config.json
    config = read_json('config.json')

    # Генерируем и сохраняем ключ Виженера
    save_vigenere_key("ПРИВЕТ МИР", "КЛЮЧ", config['path_key_task1'])
    key = load_vigenere_key(config['path_key_task1'])

    # Шифруем текст из файла, указанного в config['path_text_task1'], и сохраняем результат в файл, указанный в config['path_encrypted_text']
    encrypt_file(config['path_text_task1'], key, config['path_encrypted_text'])

    # Расшифровываем текст из файла, указанного в config['path_encrypted_text'], и сохраняем результат в файл, указанный в config['path_decrypted_text']
    decrypt_file(config['path_encrypted_text'], key, config['path_decrypted_text'])


def load_vigenere_key(file_path):
    # Загружаем ключ Виженера из JSON-файла по указанному пути
    return read_json(file_path)['key']


if __name__ == "__main__":
    main()
