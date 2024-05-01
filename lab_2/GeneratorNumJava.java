import java.security.SecureRandom;

public class GeneratorNumJava {
    public static void main(String[] args) {

        byte[] sequence = generateSecureRandomBytes();
        System.out.println(bytesToBinaryString(sequence));
    }

    private static byte[] generateSecureRandomBytes() {
        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[16];
        random.nextBytes(bytes);
        return bytes;
    }

    private static String bytesToBinaryString(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0'));
        }
        return sb.toString();
    }
}
