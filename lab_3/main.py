import argparse
from unittest import TestCase

from asym import *
from sym import *
from work_to_file import *


def menu():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Starts the key generation mode')
    group.add_argument('-enc', '--encryption', action='store_true', help='Starts the encryption mode')
    group.add_argument('-dec', '--decryption', action='store_true', help='Starts the decryption mode')
    group.add_argument('-enc_sym', '--encryption_symmetric', action='store_true',
                       help='Starts symmetric key encryption mode')
    group.add_argument('-dec_sym', '--decryption_symmetric', action='store_true',
                       help='Starts symmetric key decryption mode')
    parser.add_argument("setting", type=str, help="Path to the json file with the settings")

    args = parser.parse_args()

    setting = read_json(args.setting)

    sym = Symmetric()
    asym = Asymmetric()

    if args.generation:
        sym.key_generation(256)
        print("Сгенерирован симметричный ключ длиной 256 бит")
        sym.nonce_generation(128)
        print("Сгенерировано одноразовое случайное число длиной 128 бит")
        sym.key_serialization(setting["symmetric_key"])
        print(f"Симметричный ключ сериализован в {setting['symmetric_key']}")
        sym.nonce_serialization(setting["symmetric_nonce"])
        print(f"Одноразовое случайное число сериализовано в {setting['symmetric_nonce']}")
        asym.generate_keys()
        print("Созданы асимметричные ключи")
        asym.serialization_public(setting["asym_public_key"])
        print(f"Публичный ключ сериализован в {setting['asym_public_key']}")
        asym.serialization_private(setting["asym_private_key"])
        print(f"Приватный ключ сериализован в {setting['asym_private_key']}")
    elif args.encryption:
        sym.key_deserialization(setting["symmetric_key"])
        print(f"Симметричный ключ десериализован из {setting['symmetric_key']}")
        sym.nonce_deserialization(setting["symmetric_nonce"])
        print(f"Одноразовое случайное число десериализовано из {setting['symmetric_nonce']}")
        asym.public_key_deserialization(setting["asym_public_key"])
        print(f"Публичный ключ десериализован из {setting['asym_public_key']}")
        # Encrypt a file using the public key and the symmetric key + nonce
    elif args.decryption:
        sym.key_deserialization(setting["symmetric_key"])
        print(f"Симметричный ключ десериализован из {setting['symmetric_key']}")
        sym.nonce_deserialization(setting["symmetric_nonce"])
        print(f"Одноразовое случайное число десериализовано из {setting['symmetric_nonce']}")
        asym.private_key_deserialization(setting["asym_private_key"])
        print(f"Приватный ключ десериализован из {setting['asym_private_key']}")
        # Decrypt a file using the private key and the symmetric key + nonce
    elif args.encryption_symmetric:
        sym.key_deserialization(setting["symmetric_key"])
        print(f"Симметричный ключ десериализован из {setting['symmetric_key']}")
        sym.nonce_deserialization(setting["symmetric_nonce"])
        print(f"Одноразовое случайное число десериализовано из {setting['symmetric_nonce']}")
        asym.public_key_deserialization(setting["asym_public_key"])
        print(f"Публичный ключ десериализован из {setting['asym_public_key']}")
        encrypted_symmetric_key = asym.encrypt(sym.key)
        print("Симметричный ключ зашифрован публичным ключом")
        write_bytes_text(setting["encrypted_symmetric_key"], encrypted_symmetric_key)
        print(f"Зашифрованный симметричный ключ записан в {setting['encrypted_symmetric_key']}")
    elif args.decryption_symmetric:
        sym.key_deserialization(setting["symmetric_key"])
        print(f"Симметричный ключ десериализован из {setting['symmetric_key']}")
        sym.nonce_deserialization(setting["symmetric_nonce"])
        print(f"Одноразовое случайное число десериализовано из {setting['symmetric_nonce']}")
        asym.private_key_deserialization(setting["asym_private_key"])
        print(f"Приватный ключ десериализован из {setting['asym_private_key']}")
        encrypted_symmetric_key = read_bytes(setting["encrypted_symmetric_key"])
        print(f"Зашифрованный симметричный ключ считан из {setting['encrypted_symmetric_key']}")
        decrypted_symmetric_key = asym.decrypt(encrypted_symmetric_key)
        print("Симметричный ключ расшифрован приватным ключом")
        sym.key_serialization(setting["decrypted_symmetric_key"])
        print(f"Расшифрованный симметричный ключ сериализован в {setting['decrypted_symmetric_key']}")
        return decrypted_symmetric_key


if __name__ == "__main__":
    menu()
