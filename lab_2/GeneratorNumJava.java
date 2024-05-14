import java.security.SecureRandom;

/**
 * Класс GeneratorNumJava генерирует случайные байты с использованием криптографически безопасного генератора случайных чисел.
 */
public class GeneratorNumJava {
    /**
     * Метод main является точкой входа в программу. Он генерирует последовательность случайных байтов и выводит их в двоичном формате на консоль.
     *
     * @param args входные аргументы командной строки (не используются)
     */
    public static void main(String[] args) {
        byte[] sequence = generateSecureRandomBytes();
        System.out.println(bytesToBinaryString(sequence));
    }

    /**
     * Метод generateSecureRandomBytes генерирует массив из 16 криптографически безопасных случайных байтов.
     *
     * @return массив случайных байтов
     */
    private static byte[] generateSecureRandomBytes() {
        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[16];
        random.nextBytes(bytes);
        return bytes;
    }

    /**
     * Метод bytesToBinaryString преобразует массив байтов в строку, представляющую их в двоичном формате.
     *
     * @param bytes массив байтов для преобразования
     * @return строка, представляющая массив байтов в двоичном формате
     */
    private static String bytesToBinaryString(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0'));
        }
        return sb.toString();
    }
}
