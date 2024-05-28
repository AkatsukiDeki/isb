
import os
import sys
sys.path.append("crypto")


from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton, QMessageBox
from crypto.asym import Asymmetric
from crypto.sym import Symmetric
from crypto.serializ import *
from crypto.file import Work


class EncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = {
            "initial_file": "texts/text.txt",
            "encrypted_file": "texts/encrypted_text.txt",
            "decrypted_file": "texts/decrypted_text.txt",
            "symmetric_key": "keys/symmetric_key.txt",
            "asym_public_key": "keys/public_key.pem",
            "asym_private_key": "keys/private_key.pem",
            "nonce": "keys/sym_nonce.txt",
            "encrypted_symmetric_key": "keys/encrypted_symmetric_key.txt",
            "decrypted_symmetric_key": "keys/decrypted_symmetric_key.txt"
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Encryption App')
        self.setGeometry(100, 100, 400, 300)

        # Create widgets
        self.mode_label = QLabel('Choose mode:')
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(['Key Generation', 'Encryption', 'Decryption'])

        self.start_button = QPushButton('Start')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connections
        self.start_button.clicked.connect(self.start_operation)

    def start_operation(self):
        mode = self.mode_combo.currentText().lower()

        if mode == 'key generation':
            self.generate_keys()
        elif mode == 'encryption':
            self.encrypt_data()
        elif mode == 'decryption':
            self.decrypt_data()

    def generate_keys(self):
        symmetric_key = Symmetric.key_generation(32)
        Serialization.symmetric_key_serialization(self.settings["symmetric_key"], symmetric_key)
        public_key, private_key = Asymmetric.key_generation()
        Serialization.public_key_serialization(self.settings["asym_public_key"], public_key)
        Serialization.private_key_serialization(self.settings["asym_private_key"], private_key)
        Serialization.nonce_serialization(self.settings["nonce"], os.urandom(16))
        QMessageBox.information(self, 'Key Generation', 'Keys were generated successfully!')

    def encrypt_data(self):
        encrypted_text = Symmetric.encryption(
            self.settings["initial_file"],
            self.settings["symmetric_key"],
            self.settings["nonce"],
            self.settings["encrypted_file"]
        )
        Asymmetric.encrypt(
            self.settings["asym_public_key"],
            self.settings["symmetric_key"],
            self.settings["encrypted_symmetric_key"]
        )
        QMessageBox.information(self, 'Encryption', 'Data was encrypted successfully!')

    def decrypt_data(self):
        Asymmetric.decrypt(
            self.settings["asym_private_key"],
            self.settings["encrypted_symmetric_key"],
            self.settings["decrypted_symmetric_key"]
        )
        decrypted_text = Symmetric.decryption(
            self.settings["symmetric_key"],
            self.settings["nonce"],
            self.settings["encrypted_file"],
            self.settings["decrypted_file"]
        )
        QMessageBox.information(self, 'Decryption', f'Decrypted text: {decrypted_text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    enc_app = EncryptionApp()
    enc_app.show()
    sys.exit(app.exec_())
