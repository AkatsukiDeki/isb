import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives import padding
from work_no_walk_yes_files import *


class Symmetric:
    """
    A class that implements symmetric encryption using the ChaCha20 algorithm.

    Attributes:
        key: encryption key (256 bits)
        nonce: one-time random number (128 bits)
    """

    def __init__(self):
        self.key = None
        self.nonce = None

    def generate_key_and_nonce(self) -> tuple[bytes, bytes]:
        """
        Generates a random 32 byte encryption key and a random 16 byte nonce.

        Returns:
            A tuple containing the generated encryption key and nonce.
        """
        self.key = os.urandom(32)
        self.nonce = os.urandom(16)
        return self.key, self.nonce

    def key_deserialization(self, file_name: str) -> None:
        """
        Deserializes the encryption key from a file.

        Parameters:
            file_name: The path to the file containing the encryption key.
        """
        try:
            with open(file_name, "rb") as file:
                self.key = file.read()
        except FileNotFoundError:
            print("The file was not found")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

    def nonce_deserialization(self, file_name: str) -> None:
        """
        Deserializes the nonce from a file.

        Parameters:
            file_name: The path to the file containing the nonce.
        """
        try:
            with open(file_name, "rb") as file:
                self.nonce = file.read()
        except FileNotFoundError:
            print("The file was not found")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

    def serialize_key(self, path: str) -> None:
        """
        Serializes the encryption key to a file.

        Parameters:
            path: The path to the file where the encryption key will be saved.
        """
        try:
            with open(path, 'wb') as key_file:
                key_file.write(self.key)
            print(f"The symmetric key has been successfully written to the file '{path}'.")
        except FileNotFoundError:
            print("The file was not found")
        except Exception as e:
            print(f"An error occurred while writing the file: {str(e)}")

    def serialize_nonce(self, path: str) -> None:
        """
        Serializes the nonce to a file.

        Parameters:
            path: The path to the file where the nonce will be saved.
        """
        try:
            with open(path, 'wb') as nonce_file:
                nonce_file.write(self.nonce)
            print(f"The nonce has been successfully written to the file '{path}'.")
        except FileNotFoundError:
            print("The file was not found")
        except Exception as e:
            print(f"An error occurred while writing the file: {str(e)}")

    def encrypt(self, path_text: str, encrypted_path_text: str) -> bytes:
        """
        Encrypts data from a file using the ChaCha20 algorithm.

        Parameters:
            path_text: The path to the file with the source data.
            encrypted_path_text: The path to the file where the encrypted data will be written.
        Returns:
            The encrypted data.
        """
        text = read_bytes(path_text)
        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None)
        encryptor = cipher.encryptor()
        padder = padding.ANSIX923(128).padder()
        padded_text = padder.update(text) + padder.finalize()
        encrypt_sym_key = encryptor.update(padded_text) + encryptor.finalize()
        write_bytes_text(encrypted_path_text, encrypt_sym_key)
        return encrypt_sym_key

    def decrypt(self, encrypted_path_text: str, decrypted_path_text: str) -> str:
        """
        Decrypts data from a file using the ChaCha20 algorithm.

        Parameters:
            encrypted_path_text: The path to the file with the encrypted data.
            decrypted_path_text: The path to the file where the decrypted data will be written.
        Returns:
            The decrypted data as a string.
        """
        encrypted_text = read_bytes(encrypted_path_text)
        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None)
        decryptor = cipher.decryptor()
        decrypt_sym_key = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.ANSIX923(128).unpadder()
        unpadded_dc_text = unpadder.update(decrypt_sym_key) + unpadder.finalize()
        decrypt_sym_key = unpadded_dc_text.decode('UTF-8')
        write_file(decrypted_path_text, decrypt_sym_key)
        return decrypt_sym_key
