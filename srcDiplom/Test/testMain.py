#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
# import sys
# from srcDiplom.Controllers.UserController import *
# from srcDiplom.Test.testReg import TestReg  # Импортируем класс TestReg из файла registration.py
# from PyQt5 import QtWidgets
#
# class TaxiApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Служба такси")
#         self.setGeometry(100, 100, 1355, 715)
#
#         self.labelMainWindow = QLabel(self)
#         self.labelMainWindow.setGeometry(360, 10, 591, 61)
#         self.labelMainWindow.setText("Добро пожаловать в приложение \"Служба такси\"")
#         self.labelMainWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
#         from PyQt5 import QtCore
#         self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.ButtonReg = QPushButton(self)
#         self.ButtonReg.setGeometry(340, 210, 101, 26)
#         self.ButtonReg.setText("Регистрация")
#         self.ButtonReg.clicked.connect(self.registration)
#
#         self.ButtonAuth = QPushButton(self)
#         self.ButtonAuth.setGeometry(450, 210, 101, 26)
#         self.ButtonAuth.setText("Авторизация")
#         self.ButtonAuth.clicked.connect(self.auth)
#
#         self.textLogin = QTextEdit(self)
#         self.textLogin.setGeometry(280, 90, 131, 31)
#         self.textLogin.setPlaceholderText("Введите логин")
#
#         self.textPassword = QTextEdit(self)
#         self.textPassword.setGeometry(280, 140, 131, 31)
#         self.textPassword.setPlaceholderText("Введите пароль")
#
#     def registration(self):
#         self.hide()  # Скрываем текущее окно
#         self.registration_window = QtWidgets.QMainWindow()  # Создаем новое окно
#         self.ui = TestReg()  # Создаем экземпляр класса TestReg
#         self.ui.setupUi(self.registration_window)  # Настраиваем интерфейс для нового окна
#         self.registration_window.show()  # Показываем новое окно
#
#     def auth(self):
#         login = self.textLogin.toPlainText()
#         password = self.textPassword.toPlainText()
#         if UserController.auth(login, password):
#             print("Авторизация успешна")
#         else:
#             print("Ошибка авторизации")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = TaxiApp()
#     window.show()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
import sys
from srcDiplom.Controllers.UserController import *
from srcDiplom.Test.testReg import TestReg  # Импортируем класс TestReg из файла registration.py
from PyQt5 import QtWidgets

class TaxiApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Устанавливаем цвет фона на черный
        self.setStyleSheet("background-color: black;")

        self.setWindowTitle("Служба такси")
        self.setGeometry(100, 100, 1355, 715)

        self.labelMainWindow = QLabel(self)
        self.labelMainWindow.setGeometry(360, 10, 591, 61)
        self.labelMainWindow.setText("Добро пожаловать в приложение \"Служба такси\"")
        self.labelMainWindow.setStyleSheet("background-color: rgb(255, 172, 0);")
        from PyQt5 import QtCore
        self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)

        self.ButtonReg = QPushButton(self)
        self.ButtonReg.setGeometry(340, 210, 101, 26)
        self.ButtonReg.setText("Регистрация")
        self.ButtonReg.clicked.connect(self.registration)
        # Устанавливаем цвет кнопки на оранжевый
        self.ButtonReg.setStyleSheet("background-color: orange; color: black;")

        self.ButtonAuth = QPushButton(self)
        self.ButtonAuth.setGeometry(450, 210, 101, 26)
        self.ButtonAuth.setText("Авторизация")
        self.ButtonAuth.clicked.connect(self.auth)
        # Устанавливаем цвет кнопки на оранжевый
        self.ButtonAuth.setStyleSheet("background-color: orange; color: black;")

        self.textLogin = QTextEdit(self)
        self.textLogin.setGeometry(280, 90, 131, 31)
        self.textLogin.setPlaceholderText("Введите логин")
        # Устанавливаем стиль для поля ввода логина
        self.textLogin.setStyleSheet("background-color: white; color: black;")

        self.textPassword = QTextEdit(self)
        self.textPassword.setGeometry(280, 140, 131, 31)
        self.textPassword.setPlaceholderText("Введите пароль")
        # Устанавливаем стиль для поля ввода пароля
        self.textPassword.setStyleSheet("background-color: white; color: black;")

    def registration(self):
        self.hide()  # Скрываем текущее окно
        self.registration_window = QtWidgets.QMainWindow()  # Создаем новое окно
        self.ui = TestReg()  # Создаем экземпляр класса TestReg
        self.ui.setupUi(self.registration_window)  # Настраиваем интерфейс для нового окна
        self.registration_window.show()  # Показываем новое окно

    def auth(self):
        login = self.textLogin.toPlainText()
        password = self.textPassword.toPlainText()
        if UserController.auth(login, password):
            print("Авторизация успешна")
        else:
            print("Ошибка авторизации")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaxiApp()
    window.show()
    sys.exit(app.exec_())



