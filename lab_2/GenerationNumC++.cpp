#include <iostream>
#include <random>
#include <bitset>

std::string bytesToBinaryString(const unsigned char* bytes, size_t length) {
    std::string binaryString;
    for (size_t i = 0; i < length; ++i) {
        binaryString += std::bitset<8>(bytes[i]).to_string();
    }
    return binaryString;
}

int main() {

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<unsigned char> dis(0, 255);

    unsigned char sequence[16];
    for (size_t i = 0; i < 16; ++i) {
        sequence[i] = dis(gen);
    }

    std::cout << bytesToBinaryString(sequence, 16) << std::endl;

    return 0;
}
