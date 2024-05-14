#include <iostream>
#include <random>
#include <bitset>

/*!
 * \brief Преобразует массив байтов в строку, представляющую их в двоичном формате.
 *
 * \param bytes Указатель на массив байтов для преобразования.
 * \param length Длина массива байтов.
 * \return std::string Строка, представляющая массив байтов в двоичном формате.
 */

std::string bytesToBinaryString(const unsigned char* bytes, size_t length) {
    std::string binaryString;
    for (size_t i = 0; i < length; ++i) {
        binaryString += std::bitset<8>(bytes[i]).to_string();
    }
    return binaryString;
}

/*!
 * \brief Точка входа программы.
 *
 * Программа генерирует 16 случайных байтов с использованием криптографически безопасного генератора случайных чисел и выводит их в двоичном формате на консоль.
 *
 * \return int Код возврата программы (0 в случае успешного завершения).
 */

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
