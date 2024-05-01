from decrypt_text import *
from frequency_analysis import *
from read_write import *


if __name__ == "__main__":
    config = read_json("config.json")
    text = read_file(config["path_text_task2"])

    frequency_analysis(config["path_frequencies"], text)
    frequency = read_json(config["path_frequency"])
    alphabet = read_json(config["path_alphabet"])
    compare_frequencies(config["path_frequencies"], frequency, alphabet)

    key = read_json(config["path_key_task2"])
    decrypt_task_2(config["path_decryption_text"], text, key)