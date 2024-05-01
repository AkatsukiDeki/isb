from collections import Counter
from read_write import *


def frequency_analysis(path: str, info: str) -> None:
    """
    Performs a frequency analysis of the text and returns a dictionary with character frequencies.

    Args:
        path (str): The path to frequencies.
        info (str): The text to analyze.
    """
    total = len(info)
    frequencies = {char: count / total for char, count in Counter(info).items()}
    write_json(path, frequencies)


def compare_frequencies(path: str, frequencies: dict, alphabet_frequencies: dict) -> None:
    """
    Compares the frequencies dictionary with the letter frequencies of the Russian alphabet
    and creates a decryption key.

    Args:
        path (str): The path to decryption key.
        frequencies (dict): The dictionary of character frequencies to compare.
        alphabet_frequencies (dict): The dictionary of alphabet letter frequencies.
    """
    sorted_frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    # sorted_alphabet_frequencies = dict(sorted(alphabet_frequencies.items(), key=lambda x: x[1], reverse=True))

    decryption_key = {}
    for char, freq in sorted_frequencies.items():
        for alpha_char, alpha_freq in alphabet_frequencies.items():
            if alpha_char not in decryption_key.values() and alpha_char not in decryption_key.keys():
                decryption_key[char] = alpha_char
                break
    write_json(path, decryption_key)