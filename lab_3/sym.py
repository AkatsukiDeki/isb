import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from work_to_file import *


class Symmetric:
    """
    A class that implements symmetric encryption using the ChaCha20 algorithm.

    Attributes:
        key: encryption key
        nonce: one-time random number
    """

    def __init__(self):
        self.key = None
        self.nonce = None

    def key_generation(self) -> bytes:
        """
        Generates a random encryption key of 256 bits.

        Returns:
            The generated encryption key.
        """
        self.key = os.urandom(32)  # 256 bits
        return self.key

    def nonce_generation(self) -> bytes:
        """
        Generates a random one-time number (nonce) of 128 bits.

        Returns:
            The generated nonce.
        """
        self.nonce = os.urandom(16)  # 128 bits
        return self.nonce

    def key_serialization(self, key_path: str, nonce_path: str) -> None:
        """
        Serializes the encryption key and nonce to separate files.

        Args:
            key_path: The path to the file where the encryption key will be saved.
            nonce_path: The path to the file where the nonce will be saved.
        """
        try:
            with open(key_path, 'wb') as key_file:
                key_file.write(self.key)
            with open(nonce_path, 'wb') as nonce_file:
                nonce_file.write(self.nonce)
        except FileNotFoundError:
            print(f"Ошибка! Файл не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def key_deserialization(self, key_path: str, nonce_path: str) -> None:
        """
        Deserializes the encryption key and nonce from separate files.

        Args:
            key_path: The path to the file containing the encryption key.
            nonce_path: The path to the file containing the nonce.
        """
        try:
            with open(key_path, "rb") as key_file:
                self.key = key_file.read()
            with open(nonce_path, "rb") as nonce_file:
                self.nonce = nonce_file.read()
        except FileNotFoundError:
            print(f"Ошибка! Файл не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def encrypt(self, path: str, encrypted_path: str) -> bytes:
        """
        Encrypts data from a file using the ChaCha20 algorithm.

        Args:
            path: The path to the file with the source data.
            encrypted_path: The path to the file where the encrypted data will be written.
        Returns:
            The encrypted data.
        """
        text = read_bytes_from_text(path)
        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(text) + padder.finalize()
        cipher_text = encryptor.update(padded_text) + encryptor.finalize()
        write_bytes_text(encrypted_path, cipher_text)
        return cipher_text

    def decrypt(self, encrypted_path: str, decrypted_path: str) -> str:
        """
        Decrypts data from a file using the ChaCha20 algorithm.

        Args:
            encrypted_path: The path to the file with the encrypted data.
            decrypted_path: The path to the file where the decrypted data will be written.
        Returns:
            The decrypted data as a string.
        """
        encrypted_text = read_bytes(encrypted_path)
        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        decrypt_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_dc_text = unpadder.update(decrypt_text) + unpadder.finalize()
        decrypt_text = unpadded_dc_text.decode('UTF-8')
        write_file(decrypted_path, decrypt_text)
        return decrypt_text
