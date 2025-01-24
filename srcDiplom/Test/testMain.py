
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit
# import sys
# from srcDiplom.Controllers.UserController import *
# from srcDiplom.Test.testReg import TestReg
# from PyQt5 import QtWidgets
#
# class TaxiApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Устанавливаем цвет фона на черный
#         self.setStyleSheet("background-color: black;")
#
#         self.setWindowTitle("Служба такси")
#         self.setGeometry(100, 100, 1355, 715)
#
#         self.labelMainWindow = QLabel(self)
#         self.labelMainWindow.setGeometry(360, 10, 591, 61)
#         self.labelMainWindow.setText("Добро пожаловать в приложение \"Служба такси\"")
#         self.labelMainWindow.setStyleSheet("background-color: rgb(255, 172, 0); font-size: 24px;")  # Увеличен размер текста
#         from PyQt5 import QtCore
#         self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.ButtonReg = QPushButton(self)
#         self.ButtonReg.setGeometry(340, 210, 101, 26)
#         self.ButtonReg.setText("Регистрация")
#         self.ButtonReg.clicked.connect(self.registration)
#         # Устанавливаем цвет кнопки на оранжевый и увеличиваем размер текста
#         self.ButtonReg.setStyleSheet("background-color: orange; color: black; font-size: 14px;")
#
#         self.ButtonAuth = QPushButton(self)
#         self.ButtonAuth.setGeometry(450, 210, 101, 26)
#         self.ButtonAuth.setText("Авторизация")
#         self.ButtonAuth.clicked.connect(self.auth)
#         # Устанавливаем цвет кнопки на оранжевый и увеличиваем размер текста
#         self.ButtonAuth.setStyleSheet("background-color: orange; color: black; font-size: 14px;")
#
#         self.textLogin = QTextEdit(self)
#         self.textLogin.setGeometry(280, 90, 131, 31)
#         self.textLogin.setPlaceholderText("Введите логин")
#         # Устанавливаем стиль для поля ввода логина (темный фон, белый текст)
#         self.textLogin.setStyleSheet("background-color: #2E2E2E; color: white; font-size: 14px;")
#
#         self.textPassword = QTextEdit(self)
#         self.textPassword.setGeometry(280, 140, 131, 31)
#         self.textPassword.setPlaceholderText("Введите пароль")
#
#         # Устанавливаем стиль для поля ввода пароля (темный фон, белый текст)
#         self.textPassword.setStyleSheet("background-color: #2E2E2E; color: white; font-size: 14px;")
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

# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
# import sys
# from srcDiplom.Controllers.UserController import *
# from srcDiplom.Test.testReg import TestReg
# from PyQt5 import QtWidgets
#
#
# class TaxiApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Устанавливаем цвет фона на черный
#         self.setStyleSheet("background-color: black;")
#
#         self.setWindowTitle("Служба такси")
#         self.setGeometry(100, 100, 1355, 715)
#
#         self.labelMainWindow = QLabel(self)
#         self.labelMainWindow.setGeometry(360, 10, 591, 61)
#         self.labelMainWindow.setText("Добро пожаловать в приложение \"Служба такси\"")
#         self.labelMainWindow.setStyleSheet(
#             "background-color: rgb(255, 172, 0); font-size: 24px;")  # Увеличен размер текста
#         from PyQt5 import QtCore
#         self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.ButtonReg = QPushButton(self)
#         self.ButtonReg.setGeometry(340, 210, 101, 26)
#         self.ButtonReg.setText("Регистрация")
#         self.ButtonReg.clicked.connect(self.registration)
#         # Устанавливаем цвет кнопки на оранжевый и увеличиваем размер текста
#         self.ButtonReg.setStyleSheet("background-color: orange; color: black; font-size: 14px;")
#
#         self.ButtonAuth = QPushButton(self)
#         self.ButtonAuth.setGeometry(450, 210, 101, 26)
#         self.ButtonAuth.setText("Авторизация")
#         self.ButtonAuth.clicked.connect(self.auth)
#         # Устанавливаем цвет кнопки на оранжевый и увеличиваем размер текста
#         self.ButtonAuth.setStyleSheet("background-color: orange; color: black; font-size: 14px;")
#
#         self.textLogin = QLineEdit(self)
#         self.textLogin.setGeometry(280, 90, 131, 31)
#         self.textLogin.setPlaceholderText("Введите логин")
#         # Устанавливаем стиль для поля ввода логина (темный фон, белый текст)
#         self.textLogin.setStyleSheet("background-color: #2E2E2E; color: white; font-size: 14px;")
#
#         self.textPassword = QLineEdit(self)
#         self.textPassword.setGeometry(280, 140, 131, 31)
#         self.textPassword.setPlaceholderText("Введите пароль")
#         self.textPassword.setEchoMode(QLineEdit.Password)  # Устанавливаем режим отображения пароля
#
#         # Устанавливаем стиль для поля ввода пароля (темный фон, белый текст)
#         self.textPassword.setStyleSheet("background-color: #2E2E2E; color: white; font-size: 14px;")
#
#     def registration(self):
#         self.hide()  # Скрываем текущее окно
#         self.registration_window = QtWidgets.QMainWindow()  # Создаем новое окно
#         self.ui = TestReg()  # Создаем экземпляр класса TestReg
#         self.ui.setupUi(self.registration_window)  # Настраиваем интерфейс для нового окна
#         self.registration_window.show()  # Показываем новое окно
#
#     def auth(self):
#         login = self.textLogin.text()  # Используем .text() для QLineEdit
#         password = self.textPassword.text()  # Используем .text() для QLineEdit
#         if UserController.auth(login, password):
#             print("Авторизация успешна")
#         else:
#             print("Ошибка авторизации")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = TaxiApp()
#     window.show()
#     sys.exit(app.exec_())


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys

from srcDiplom.AdminWindow import AdminPanel
from srcDiplom.Controllers.UserController import *
from srcDiplom.Test.testReg import TestReg
from PyQt5 import QtWidgets

from srcDiplom.UsersWindow import UserPanel


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
        self.labelMainWindow.setStyleSheet(
            "background-color: rgb(255, 172, 0); font-size: 24px;")  # Увеличен размер текста
        from PyQt5 import QtCore
        self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)

        self.ButtonReg = QPushButton(self)
        self.ButtonReg.setGeometry(340, 210, 101, 26)
        self.ButtonReg.setText("Регистрация")
        self.ButtonReg.clicked.connect(self.registration)
        # Устанавливаем цвет кнопки на оранжевый и увеличиваем размер текста
        self.ButtonReg.setStyleSheet("background-color: orange; color: black; font-size: 14px;")

        self.ButtonAuth = QPushButton(self)
        self.ButtonAuth.setGeometry(450, 210, 101, 26)
        self.ButtonAuth.setText("Авторизация")
        self.ButtonAuth.clicked.connect(self.auth)
        # Устанавливаем цвет кнопки на оранжевый и увеличиваем размер текста
        self.ButtonAuth.setStyleSheet("background-color: orange; color: black; font-size: 14px;")

        self.textLogin = QLineEdit(self)
        self.textLogin.setGeometry(280, 90, 131, 31)
        self.textLogin.setPlaceholderText("Введите логин")
        # Устанавливаем стиль для поля ввода логина (темный фон, белый текст)
        self.textLogin.setStyleSheet("background-color: #2E2E2E; color: white; font-size: 14px;")

        self.textPassword = QLineEdit(self)
        self.textPassword.setGeometry(280, 140, 131, 31)
        self.textPassword.setPlaceholderText("Введите пароль")
        self.textPassword.setEchoMode(QLineEdit.Password)  # Устанавливаем режим отображения пароля

        # Устанавливаем стиль для поля ввода пароля (темный фон, белый текст)
        self.textPassword.setStyleSheet("background-color: #2E2E2E; color: white; font-size: 14px;")

    def registration(self):
        self.hide()  # Скрываем текущее окно
        self.registration_window = QtWidgets.QMainWindow()  # Создаем новое окно
        self.ui = TestReg()  # Создаем экземпляр класса TestReg
        self.ui.setupUi(self.registration_window)  # Настраиваем интерфейс для нового окна
        self.registration_window.show()  # Показываем новое окно

    def auth(self):
        login = self.textLogin.text()  # Используем .text() для QLineEdit
        password = self.textPassword.text()  # Используем .text() для QLineEdit
        role_id = UserController.auth(login, password)  # Предполагаем, что метод возвращает роль

        if role_id:
            print("Авторизация успешна, роль:", role_id)
            self.open_panel(role_id)  # Открываем соответствующую панель
        else:
            print("Ошибка авторизации")

    def open_panel(self, role_id):
        if role_id == 1:
            self.AdminWindow = AdminPanel()  # Создаем экземпляр класса AdminPanel
            self.AdminWindow.show()  # Показываем панель администратора
        elif role_id == 2:
            self.UserWindow = UserPanel()  # Создаем экземпляр класса UserPanel
            self.UserWindow.show()  # Показываем панель пользователя
        self.close()  # Закрываем главное окно

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaxiApp()
    window.show()
    sys.exit(app.exec_())





