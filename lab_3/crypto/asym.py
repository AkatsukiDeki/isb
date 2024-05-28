
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import padding


def generate_key_pair():
    """
    Generates an RSA key pair.
    Returns:
        RSAPrivateKey: The generated RSA private key.
    """
    try:
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def encrypt_symmetric_key(private_key, symmetric_key):
    """
    Encrypts a symmetric key using RSA encryption.
    Args:
        private_key (RSAPrivateKey): The RSA private key used for encryption.
        symmetric_key (bytes): The symmetric key to be encrypted.
    Returns:
        bytes: The encrypted symmetric key.
    """
    try:
        encrypted_key = private_key.public_key().encrypt(symmetric_key,
                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                 algorithm=hashes.SHA256(), label=None))
        return encrypted_key
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def decrypt_symmetric_key(private_key, encrypted_symmetric_key):
    """
    Decrypts an encrypted symmetric key using RSA decryption.
    Args:
        private_key (RSAPrivateKey): The RSA private key used for decryption.
        encrypted_symmetric_key (bytes): The encrypted symmetric key to be decrypted.
    Returns:
        bytes: The decrypted symmetric key.
    """
    try:
        return private_key.decrypt(encrypted_symmetric_key, asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ))
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")