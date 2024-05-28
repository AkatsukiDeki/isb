import sys
sys.path.append('crypto')

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton, QMessageBox
from crypto.file import generate_keys, encrypt_file, decrypt_file

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

        # Создание виджетов выбора действия
        self.mode_label = QLabel('Choose action:')
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(['Key Generation', 'Encryption', 'Decryption'])

        self.start_button = QPushButton('Start Action')

        # Создание макета для выбора действия
        layout = QVBoxLayout()
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Подключение сигналов к слотам
        self.start_button.clicked.connect(self.start_selected_action)

    def start_selected_action(self):
        selected_action = self.mode_combo.currentText().lower()

        if selected_action == 'key generation':
            self.generate_keys()
        elif selected_action == 'encryption':
            self.encrypt_data()
        elif selected_action == 'decryption':
            self.decrypt_data()

    def generate_keys(self):
        generate_keys(self.settings["asym_private_key"], self.settings["asym_public_key"], self.settings["symmetric_key"])
        QMessageBox.information(self, 'Key Generation', 'Keys were generated successfully!')

    def encrypt_data(self):
        encrypt_file(self.settings["initial_file"], self.settings["asym_private_key"], self.settings["symmetric_key"], self.settings["encrypted_file"])
        QMessageBox.information(self, 'Encryption', 'Data was encrypted successfully!')

    def decrypt_data(self):
        decrypt_file(self.settings["encrypted_file"], self.settings["asym_private_key"], self.settings["symmetric_key"], self.settings["decrypted_file"])
        QMessageBox.information(self, 'Decryption', 'Decrypted text was saved to file.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    enc_app = EncryptionApp()
    enc_app.show()
    sys.exit(app.exec_())
