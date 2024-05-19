import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.Qt import QFile, QIODevice
from sym_asym.sym import Symmetric
from sym_asym.asym import Asymmetric
from sym_asym.work_no_walk_yes_files import *

class SymmetricEncryptionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Symmetric Encryption")
        self.setGeometry(100, 100, 400, 400)

        self.symmetric = Symmetric()
        self.asymmetric = Asymmetric()

        self.file_paths = {
            "initial_file": "text/text.txt",
            "encrypted_file": "text/encrypt_text.txt",
            "decrypted_file": "text/decrypt_text.txt",
            "symmetric_key": "key/sym.txt",
            "encrypted_symmetric_key": "key/encrypt_sym_key.txt",
            "public_key": "key/asym_public_key.pem",
            "private_key": "key/asym_private_key.pem",
            "decrypted_symmetric_key": "key/decrypt_sym_key.txt"
        }

        self.init_ui()

    def init_ui(self):
        # Add your PyQt5 UI components and event handlers here
        pass

    def encrypt_file(self):
        # Generate symmetric key and nonce
        self.symmetric.generate_key_and_nonce()
        self.symmetric.serialize_key(self.file_paths["symmetric_key"])
        self.symmetric.serialize_nonce(self.file_paths["symmetric_key"])

        # Encrypt the file using the symmetric key
        self.symmetric.encrypt(self.file_paths["initial_file"], self.file_paths["encrypted_file"])

        # Encrypt the symmetric key using the public key
        encrypted_symmetric_key = self.asymmetric.encrypt(self.symmetric.key)
        write_bytes_text(self.file_paths["encrypted_symmetric_key"], encrypted_symmetric_key)

    def decrypt_file(self):
        # Deserialize the symmetric key and nonce
        self.symmetric.key_deserialization(self.file_paths["symmetric_key"])
        self.symmetric.nonce_deserialization(self.file_paths["symmetric_key"])

        # Decrypt the symmetric key using the private key
        encrypted_symmetric_key = read_bytes(self.file_paths["encrypted_symmetric_key"])
        decrypted_symmetric_key = self.asymmetric.decrypt(encrypted_symmetric_key)
        write_file(self.file_paths["decrypted_symmetric_key"], decrypted_symmetric_key.decode())

        # Decrypt the file using the symmetric key
        self.symmetric.decrypt(self.file_paths["encrypted_file"], self.file_paths["decrypted_file"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SymmetricEncryptionGUI()
    gui.show()
    sys.exit(app.exec_())
