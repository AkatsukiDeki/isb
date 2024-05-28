
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


def encrypt_data(symmetric_key, plaintext):
    """
    Encrypts plaintext using the ChaCha20 symmetric encryption algorithm.
    Args:
        symmetric_key (bytes): The symmetric key used for encryption.
        plaintext (bytes): The plaintext to be encrypted.
    Returns:
        bytes: The ciphertext resulting from the encryption process.
    """
    try:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return iv + ciphertext
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def decrypt_data(symmetric_key, ciphertext, iv):
    """
    Decrypts ciphertext using the ChaCha20 symmetric encryption algorithm.
    Args:
        symmetric_key (bytes): The symmetric key used for decryption.
        ciphertext (bytes): The ciphertext to be decrypted.
        iv (bytes): The initialization vector used for encryption.
    Returns:
        bytes: The decrypted plaintext.
    """
    try:
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")
