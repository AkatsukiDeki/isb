import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from sym import encrypt_data
from asym import generate_key_pair, encrypt_symmetric_key, decrypt_symmetric_key
from serializ import serialize_private_key, serialize_public_key, load_private_key


def generate_keys(private_key_path, public_key_path, symmetric_key_path):
    """
    Generates key pairs for asymmetric encryption and a symmetric key for hybrid encryption.
    Args:
        private_key_path (str): The path to save the private key.
        public_key_path (str): The path to save the public key.
        symmetric_key_path (str): The path to save the symmetric key.
    """
    try:
        private_key = generate_key_pair()
        public_key = private_key.public_key()
        symmetric_key = os.urandom(32)
        with open(public_key_path, "wb") as f:
            f.write(serialize_public_key(public_key))
        with open(private_key_path, "wb") as f:
            f.write(serialize_private_key(private_key))
        with open(symmetric_key_path, "wb") as f:
            f.write(symmetric_key)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def encrypt_file(initial_file_path, private_key_path, symmetric_key_path, encrypted_file_path):
    """
    Encrypts a file using hybrid encryption.
    Args:
        initial_file_path (str): The path to the file to be encrypted.
        private_key_path (str): The path to the private key.
        symmetric_key_path (str): The path to the symmetric key.
        encrypted_file_path (str): The path to save the encrypted file.
    """
    try:
        private_key_bytes = open(private_key_path, "rb").read()
        private_key = load_private_key(private_key_bytes)
        symmetric_key = open(symmetric_key_path, "rb").read()
        encrypted_symmetric_key = encrypt_symmetric_key(private_key, symmetric_key)
        with open(symmetric_key_path, "wb") as f:
            f.write(encrypted_symmetric_key)
        with open(initial_file_path, "rb") as f_in, open(encrypted_file_path, "wb") as f_out:
            plaintext = f_in.read()
            ciphertext = encrypt_data(symmetric_key, plaintext)
            f_out.write(ciphertext)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def decrypt_file(encrypted_file_path, private_key_path, symmetric_key_path, decrypted_file_path):
    """
    Decrypts a file encrypted using hybrid encryption.
    Args:
        encrypted_file_path (str): The path to the encrypted file.
        private_key_path (str): The path to the private key.
        symmetric_key_path (str): The path to the symmetric key.
        decrypted_file_path (str): The path to save the decrypted file.
    """
    try:
        private_key_bytes = open(private_key_path, "rb").read()
        private_key = load_private_key(private_key_bytes)
        encrypted_symmetric_key = open(symmetric_key_path, "rb").read()
        symmetric_key = decrypt_symmetric_key(private_key, encrypted_symmetric_key)
        with open(encrypted_file_path, "rb") as f_in, open(decrypted_file_path, "wb") as f_out:
            iv = f_in.read(16)
            cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
            decryptor = cipher.decryptor()
            while chunk := f_in.read(128):
                decrypted_chunk = decryptor.update(chunk)
                f_out.write(decrypted_chunk)
            f_out.write(decryptor.finalize())
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")
