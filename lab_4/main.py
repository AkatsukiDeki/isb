import sys
import hash_func
import work_to_file as file

from PyQt5.QtWidgets import (QApplication, QInputDialog, QFileDialog, QMainWindow,
                             QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Инициализирует класс MainWindow, устанавливает размер окна и заголовок,
        а также создает центральный виджет с различными элементами пользовательского интерфейса.
        """
        super().__init__()

        self.resize(500, 300)
        self.setWindowTitle('ПОИСК НОМЕРА БАНКОВСКОЙ КАРТЫ')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.btn_bins = QLineEdit(placeholderText="Введите список BIN-ов")
        self.btn_bins.setStyleSheet('background-color: #fff;')
        self.btn_hash_card = QLineEdit(placeholderText="Введите хеш")
        self.btn_hash_card.setStyleSheet('background-color: #fff;')
        self.btn_last_number = QLineEdit(placeholderText="Введите последние 4 цифры")
        self.btn_last_number.setStyleSheet('background-color: #fff;')

        self.hash_btn = QPushButton('Найти номер карты по хешу')
        self.hash_btn.setStyleSheet('background-color: #dbdcff;')
        self.hash_btn.clicked.connect(lambda: self.find_number())
        self.luhn_btn = QPushButton('Проверить номер по алгоритму Луна')
        self.luhn_btn.setStyleSheet('background-color: #dbdcff;')
        self.luhn_btn.clicked.connect(self.luna_alg)
        self.graph_btn = QPushButton('Построить график')
        self.graph_btn.setStyleSheet('background-color: #dbdcff;')
        self.graph_btn.clicked.connect(lambda: self.graph_draw())
        self.exit_btn = QPushButton('Выйти')
        self.exit_btn.setStyleSheet('background-color: #dbdcff;')
        self.exit_btn.clicked.connect(lambda: self.close_event())

        hbox = QVBoxLayout()
        hbox.addWidget(self.exit_btn)
        hbox.addWidget(self.hash_btn)
        hbox.addWidget(self.luhn_btn)
        hbox.addWidget(self.graph_btn)
        hbox.addWidget(self.btn_bins)
        hbox.addWidget(self.btn_hash_card)
        hbox.addWidget(self.btn_last_number)
        self.centralWidget.setLayout(hbox)

        self.setStyleSheet('background-color: #B0FFD9;')

        self.show()

    def find_number(self) -> None:
        """
        Обрабатывает логику поиска номера карты на основе предоставленных значений хеша, BIN-ов и последней цифры.
        Если найден действительный номер карты, он сохраняется в файл. Если нет, выводится сообщение.
        """
        bins = self.btn_bins.text().split(",")
        hash_card = self.btn_hash_card.text()
        last_number = self.btn_last_number.text()
        if not bins or not hash_card or not last_number:
            QMessageBox.information(
                None,
                "Не все данные карты были указаны",
                "Заполните все данные карты",
            )
            return
        try:
            last_number = int(last_number)
            bins = [int(item) for item in bins]
        except ValueError:
            QMessageBox.information(
                None,
                "Неверный ввод",
                "Введите действительные значения для последних 4 цифр и BIN-ов",
            )
            return
        card_number = hash_func.get_card_number(hash_card, bins, last_number)
        if card_number:
            directory = QFileDialog.getSaveFileName(
                self, "Выберите файл для сохранения найденного номера:", "", "JSON File(*.json)"
            )[0]
            if directory:
                file.write_file(directory, card_number)
                QMessageBox.information(
                    None, "Успешно", f"Номер карты сохранен в файл: {directory}"
                    )
        else:
            QMessageBox.information(
                None, "Не найдено", "Номер карты не найден на основе предоставленной информации."
            )

    def luna_alg(self) -> None:
        """
        Обрабатывает логику проверки действительности номера карты с помощью алгоритма Луна.
        Пользователю предлагается ввести номер карты,
        и выводится сообщение в зависимости от результата проверки алгоритма Луна.
        """
        card_number = QInputDialog.getText(
            self, "Введите номер карты", "Номер карты:"
        )
        card_number = card_number[0]
        if card_number == "":
            QMessageBox.information(
                None, "Введите номер карты", "Номер карты не был введен"
            )
        result = hash_func.luhn_algorithm(card_number)
        if result is not False:
            QMessageBox.information(
                None, "Результат проверки", "Номер карты действителен"
            )
        else:
            QMessageBox.information(
                None, "Результат проверки", "Номер карты недействителен"
            )

    def graph_draw(self) -> None:
        """
        Обрабатывает логику построения графика, показывающего время выполнения функции `get_card_number`
        в зависимости от количества используемых процессов.
        Пользователь должен предоставить необходимые входные параметры (хеш, BIN-ы, последняя цифра).
        """
        bins = self.btn_bins.text().split(",")
        hash_card = self.btn_hash_card.text()
        last_digit = self.btn_last_number.text()
        if not bins or not hash_card or not last_digit:
            QMessageBox.information(
                None,
                "Не все данные карты были указаны",
                "Заполните все данные карты",
            )
            return
        try:
            last_digit = int(last_digit)
            bins = [int(item) for item in bins]
        except ValueError:
            QMessageBox.information(
                None,
                "Неверный ввод",
                "Введите действительные значения для последних 4 цифр и BIN-ов",
            )
            return
        hash_func.graphing(hash_card, bins, last_digit)

    def close_event(self):
        """
        Обрабатывает логику закрытия приложения, когда пользователь нажимает кнопку "Выйти".
        Пользователю предлагается подтвердить действие выхода.
        """
        reply = QMessageBox.question(self, 'Сообщение', "Вы уверены, что хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.accept()
        else:
            self.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
