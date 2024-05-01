from NIST import *


if __name__ == "__main__":
    config = read_json("config_file.json")
    sequences = read_json(config["From"])
    sequences_cpp = sequences["C++"]
    sequences_java = sequences["Java"]
    bit_frequency_test(sequences_cpp, config["To"], "C++")
    bit_frequency_test(sequences_java, config["To"], "Java")
    consecutive_bits_test(sequences_cpp, config["To"], "C++")
    consecutive_bits_test(sequences_java, config["To"], "Java")
    longest_sequence_of_ones_test(sequences_cpp, config["To"], "C++")
    longest_sequence_of_ones_test(sequences_java, config["To"], "Java")