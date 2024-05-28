from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def serialize_private_key(private_key):
    """
    Serialize a private key to PEM format.
    Args:
        private_key (cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey): The private key to serialize.
    Returns:
        bytes: The serialized private key in PEM format.
    """
    try:
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def serialize_public_key(public_key):
    """
    Serialize a public key to PEM format.
    Args:
        public_key: The public key to serialize.
    Returns:
        bytes: The serialized public key in PEM format.
    """
    try:
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def load_private_key(private_key_bytes):
    """
    Load a private key from its byte representation.
    Args:
        private_key_bytes (bytes): The byte representation of the private key.
    Returns:
        bytes: The loaded private key.
    """
    try:
        return serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")
