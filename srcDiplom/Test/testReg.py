
# from PyQt5 import QtCore, QtGui, QtWidgets
# from srcDiplom.Controllers.UserController import UserController
#
# class TestReg(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1355, 715)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.labelRegistrationWindow = QtWidgets.QLabel(self.centralwidget)
#         self.labelRegistrationWindow.setGeometry(QtCore.QRect(490, 10, 231, 51))
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.labelRegistrationWindow.setFont(font)
#         self.labelRegistrationWindow.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.labelRegistrationWindow.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelRegistrationWindow.setObjectName("labelRegistrationWindow")
#         self.registrationButton = QtWidgets.QPushButton(self.centralwidget)
#         self.registrationButton.setGeometry(QtCore.QRect(430, 360, 101, 26))
#         self.registrationButton.setObjectName("registrationButton")
#         self.registrationButton.clicked.connect(self.register_user)  # Подключаем обработчик
#         self.textLogin = QtWidgets.QTextEdit(self.centralwidget)
#         self.textLogin.setGeometry(QtCore.QRect(290, 260, 131, 31))
#         self.textLogin.setObjectName("textLogin")
#         self.textPassword = QtWidgets.QTextEdit(self.centralwidget)
#         self.textPassword.setGeometry(QtCore.QRect(290, 300, 131, 31))
#         self.textPassword.setObjectName("textPassword")
#         self.textName = QtWidgets.QTextEdit(self.centralwidget)
#         self.textName.setGeometry(QtCore.QRect(290, 90, 131, 31))
#         self.textName.setObjectName("textName")
#         self.textAddres = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddres.setGeometry(QtCore.QRect(290, 180, 131, 31))
#         self.textAddres.setObjectName("textAddres")
#         self.startNumber = QtWidgets.QLabel(self.centralwidget)
#         self.startNumber.setGeometry(QtCore.QRect(290, 230, 58, 18))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.startNumber.setFont(font)
#         self.startNumber.setObjectName("startNumber")
#         self.ManButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.ManButton.setGeometry(QtCore.QRect(290, 140, 101, 24))
#         self.ManButton.setObjectName("ManButton")
#         self.WomanButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.WomanButton.setGeometry(QtCore.QRect(410, 140, 101, 24))
#         self.WomanButton.setObjectName("WomanButton")
#         self.line_1 = QtWidgets.QFrame(self.centralwidget)
#         self.line_1.setGeometry(QtCore.QRect(370, 230, 20, 21))
#         self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_1.setObjectName("line_1")
#         self.line_2 = QtWidgets.QFrame(self.centralwidget)
#         self.line_2.setGeometry(QtCore.QRect(450, 230, 20, 21))
#         self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_2.setObjectName("line_2")
#         self.textNumbers_1 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_1.setGeometry(QtCore.QRect(320, 230, 41, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textNumbers_1.setFont(font)
#         self.textNumbers_1.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_1.setObjectName("textNumbers_1")
#         self.textNumbers_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_2.setGeometry(QtCore.QRect(400, 230, 41, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textNumbers_2.setFont(font)
#         self.textNumbers_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_2.setObjectName("textNumbers_2")
#         self.textNumbers_3 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_3.setGeometry(QtCore.QRect(480, 230, 41, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textNumbers_3.setFont(font)
#         self.textNumbers_3.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_3.setObjectName("textNumbers_3")
#         self.authButton = QtWidgets.QPushButton(self.centralwidget)
#         self.authButton.setGeometry(QtCore.QRect(550, 360, 101, 26))
#         self.authButton.setObjectName("authButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Окно регистрации"))
#         self.labelRegistrationWindow.setText(_translate("MainWindow", "Окно регистрации"))
#         self.registrationButton.setText(_translate("MainWindow", "Регистрация"))
#         self.textLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
#         self.textPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
#         self.textName.setPlaceholderText(_translate("MainWindow", "Введите имя"))
#         self.textAddres.setPlaceholderText(_translate("MainWindow", "Введите адрес"))
#         self.startNumber.setText(_translate("MainWindow", "+7"))
#         self.ManButton.setText(_translate("MainWindow", "Мужской"))
#         self.WomanButton.setText(_translate("MainWindow", "Женский"))
#         self.authButton.setText(_translate("MainWindow", "Авторизация"))
#
#     def register_user(self):
#         fullname = self.textName.toPlainText()
#         login = self.textLogin.toPlainText()
#         password = self.textPassword.toPlainText()
#         address = self.textAddres.toPlainText()
#         phone = f"+7{self.textNumbers_1.text()}{self.textNumbers_2.text()}{self.textNumbers_3.text()}"
#         gender = 1 if self.ManButton.isChecked() else 2  # Предположим, что 1 - мужской, 2 - женский
#         role_id = 1  # Здесь можете указать ID роли, если это необходимо
#
#         message = UserController.registration(fullname, login, password, gender, phone, role_id)
#         QtWidgets.QMessageBox.information(None, "Результат регистрации", message)
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = TestReg()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


# from PyQt5 import QtCore, QtGui, QtWidgets
# from srcDiplom.Controllers.UserController import UserController
#
# class TestReg(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1355, 715)
#
#         # Задаем черный фон для основного виджета
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")  # Черный фон
#
#         self.labelRegistrationWindow = QtWidgets.QLabel(self.centralwidget)
#         self.labelRegistrationWindow.setGeometry(QtCore.QRect(490, 10, 231, 51))
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.labelRegistrationWindow.setFont(font)
#         self.labelRegistrationWindow.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, белый текст
#         self.labelRegistrationWindow.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelRegistrationWindow.setObjectName("labelRegistrationWindow")
#
#         self.registrationButton = QtWidgets.QPushButton(self.centralwidget)
#         self.registrationButton.setGeometry(QtCore.QRect(430, 360, 101, 26))
#         self.registrationButton.setObjectName("registrationButton")
#         self.registrationButton.clicked.connect(self.register_user)  # Подключаем обработчик
#         self.registrationButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Белый текст
#
#         # Настраиваем окна ввода
#         self.textLogin = QtWidgets.QTextEdit(self.centralwidget)
#         self.textLogin.setGeometry(QtCore.QRect(290, 260, 131, 31))
#         self.textLogin.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         self.textPassword = QtWidgets.QTextEdit(self.centralwidget)
#         self.textPassword.setGeometry(QtCore.QRect(290, 300, 131, 31))
#
#
#         self.textPassword.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         self.textName = QtWidgets.QTextEdit(self.centralwidget)
#         self.textName.setGeometry(QtCore.QRect(290, 90, 131, 31))
#         self.textName.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         self.textAddres = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddres.setGeometry(QtCore.QRect(290, 180, 131, 31))
#         self.textAddres.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         self.startNumber = QtWidgets.QLabel(self.centralwidget)
#         self.startNumber.setGeometry(QtCore.QRect(290, 230, 58, 18))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.startNumber.setFont(font)
#         self.startNumber.setStyleSheet("color: white;")  # Белый текст
#         self.startNumber.setObjectName("startNumber")
#
#         self.ManButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.ManButton.setGeometry(QtCore.QRect(290, 140, 101, 24))
#         self.ManButton.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Белый текст
#         self.ManButton.setObjectName("ManButton")
#
#         self.WomanButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.WomanButton.setGeometry(QtCore.QRect(410, 140, 101, 24))
#         self.WomanButton.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Белый текст
#         self.WomanButton.setObjectName("WomanButton")
#
#         self.textNumbers_1 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_1.setGeometry(QtCore.QRect(320, 230, 41, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textNumbers_1.setFont(font)
#         self.textNumbers_1.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_1.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textNumbers_1.setObjectName("textNumbers_1")
#         self.textNumbers_1.setMaxLength(3)
#
#
#         self.textNumbers_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_2.setGeometry(QtCore.QRect(400, 230, 41, 21))
#         self.textNumbers_2.setFont(font)
#         self.textNumbers_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_2.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textNumbers_2.setObjectName("textNumbers_2")
#         self.textNumbers_2.setMaxLength(3)
#
#         self.textNumbers_3 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_3.setGeometry(QtCore.QRect(480, 230, 41, 21))
#         self.textNumbers_3.setFont(font)
#         self.textNumbers_3.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_3.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textNumbers_3.setObjectName("textNumbers_3")
#         self.textNumbers_3.setMaxLength(3)
#
#         self.authButton = QtWidgets.QPushButton(self.centralwidget)
#         self.authButton.setGeometry(QtCore.QRect(550, 360, 101, 26))
#         self.authButton.setObjectName("authButton")
#         self.authButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Белый текст
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Окно регистрации"))
#         self.labelRegistrationWindow.setText(_translate("MainWindow", "Окно регистрации"))
#         self.registrationButton.setText(_translate("MainWindow", "Регистрация"))
#         self.textLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
#         self.textPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
#         self.textName.setPlaceholderText(_translate("MainWindow", "Введите имя"))
#         self.textAddres.setPlaceholderText(_translate("MainWindow", "Введите адрес"))
#         self.startNumber.setText(_translate("MainWindow", "+7"))
#         self.ManButton.setText(_translate("MainWindow", "Мужской"))
#         self.WomanButton.setText(_translate("MainWindow", "Женский"))
#         self.authButton.setText(_translate("MainWindow", "Авторизация"))
#
#     def register_user(self):
#         fullname = self.textName.toPlainText()
#         login = self.textLogin.toPlainText()
#         password = self.textPassword.toPlainText()
#         address = self.textAddres.toPlainText()
#         phone = f"+7{self.textNumbers_1.text()}{self.textNumbers_2.text()}{self.textNumbers_3.text()}"
#         gender = 1 if self.ManButton.isChecked() else 2  # Предположим, что 1 - мужской, 2 - женский
#         role_id = 1  # Здесь можете указать ID роли, если это необходимо
#
#         message = UserController.registration(fullname, login, password, gender, phone, role_id)
#         QtWidgets.QMessageBox.information(None, "Результат регистрации", message)
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = TestReg()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# from PyQt5 import QtCore, QtGui, QtWidgets
# from srcDiplom.Controllers.UserController import UserController
#
# class TestReg(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1355, 715)
#
#         # Задаем черный фон для основного виджета
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")  # Черный фон
#
#         self.labelRegistrationWindow = QtWidgets.QLabel(self.centralwidget)
#         self.labelRegistrationWindow.setGeometry(QtCore.QRect(490, 10, 231, 51))
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.labelRegistrationWindow.setFont(font)
#         self.labelRegistrationWindow.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, белый текст
#         self.labelRegistrationWindow.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelRegistrationWindow.setObjectName("labelRegistrationWindow")
#
#         self.registrationButton = QtWidgets.QPushButton(self.centralwidget)
#         self.registrationButton.setGeometry(QtCore.QRect(430, 360, 101, 26))
#         self.registrationButton.setObjectName("registrationButton")
#         self.registrationButton.clicked.connect(self.register_user)  # Подключаем обработчик
#         self.registrationButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Белый текст
#
#         # Настраиваем окна ввода
#         self.textLogin = QtWidgets.QTextEdit(self.centralwidget)
#         self.textLogin.setGeometry(QtCore.QRect(290, 260, 131, 31))
#         self.textLogin.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         # Изменяем на QLineEdit для маскирования пароля
#         self.textPassword = QtWidgets.QLineEdit(self.centralwidget)
#         self.textPassword.setGeometry(QtCore.QRect(290, 300, 131, 31))
#         self.textPassword.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textPassword.setEchoMode(QtWidgets.QLineEdit.Password)  # Устанавливаем режим ввода пароля
#
#         self.textName = QtWidgets.QTextEdit(self.centralwidget)
#         self.textName.setGeometry(QtCore.QRect(290, 90, 131, 31))
#         self.textName.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         self.textAddres = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddres.setGeometry(QtCore.QRect(290, 180, 131, 31))
#         self.textAddres.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#
#         self.startNumber = QtWidgets.QLabel(self.centralwidget)
#         self.startNumber.setGeometry(QtCore.QRect(290, 230, 58, 18))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.startNumber.setFont(font)
#         self.startNumber.setStyleSheet("color: white;")  # Белый текст
#         self.startNumber.setObjectName("startNumber")
#
#         self.ManButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.ManButton.setGeometry(QtCore.QRect(290, 140, 101, 24))
#         self.ManButton.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Белый текст
#         self.ManButton.setObjectName("ManButton")
#
#         self.WomanButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.WomanButton.setGeometry(QtCore.QRect(410, 140, 101, 24))
#         self.WomanButton.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Белый текст
#         self.WomanButton.setObjectName("WomanButton")
#
#         self.textNumbers_1 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_1.setGeometry(QtCore.QRect(320, 230, 41, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textNumbers_1.setFont(font)
#         self.textNumbers_1.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_1.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textNumbers_1.setObjectName("textNumbers_1")
#         self.textNumbers_1.setMaxLength(3)
#         self.textNumbers_1.setValidator(QtGui.QIntValidator(0, 999, self.textNumbers_1))
#
#         self.textNumbers_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_2.setGeometry(QtCore.QRect(400, 230, 41, 21))
#         self.textNumbers_2.setFont(font)
#         self.textNumbers_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_2.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textNumbers_2.setObjectName("textNumbers_2")
#         self.textNumbers_2.setMaxLength(3)
#         self.textNumbers_2.setValidator(QtGui.QIntValidator(0, 999, self.textNumbers_2))
#
#         self.textNumbers_3 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textNumbers_3.setGeometry(QtCore.QRect(480, 230, 41, 21))
#         self.textNumbers_3.setFont(font)
#         self.textNumbers_3.setAlignment(QtCore.Qt.AlignCenter)
#         self.textNumbers_3.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
#         self.textNumbers_3.setObjectName("textNumbers_3")
#         self.textNumbers_3.setMaxLength(4)
#         self.textNumbers_3.setValidator(QtGui.QIntValidator(0, 999, self.textNumbers_3))
#
#         self.authButton = QtWidgets.QPushButton(self.centralwidget)
#         self.authButton.setGeometry(QtCore.QRect(550, 360, 101, 26))
#         self.authButton.setObjectName("authButton")
#         self.authButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Белый текст
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Окно регистрации"))
#         self.labelRegistrationWindow.setText(_translate("MainWindow", "Окно регистрации"))
#         self.registrationButton.setText(_translate("MainWindow", "Регистрация"))
#         self.textLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
#         self.textPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
#         self.textName.setPlaceholderText(_translate("MainWindow", "Введите имя"))
#         self.textAddres.setPlaceholderText(_translate("MainWindow", "Введите адрес"))
#         self.startNumber.setText(_translate("MainWindow", "+7"))
#         self.ManButton.setText(_translate("MainWindow", "Мужской"))
#         self.WomanButton.setText(_translate("MainWindow", "Женский"))
#         self.authButton.setText(_translate("MainWindow", "Авторизация"))
#
#     def register_user(self):
#         fullname = self.textName.toPlainText()
#         login = self.textLogin.toPlainText()
#         password = self.textPassword.text()  # Изменено на text() для QLineEdit
#         address = self.textAddres.toPlainText()
#         phone = f"+7{self.textNumbers_1.text()}{self.textNumbers_2.text()}{self.textNumbers_3.text()}"
#         gender = 1 if self.ManButton.isChecked() else 2  # Предположим, что 1 - мужской, 2 - женский
#         role_id = 1  # Здесь можете указать ID роли, если это необходимо
#
#         message = UserController.registration(fullname, login, password, gender, phone, role_id)
#         QtWidgets.QMessageBox.information(None, "Результат регистрации", message)
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = TestReg()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets
from srcDiplom.Controllers.UserController import UserController

class TestReg(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 715)

        # Задаем черный фон для основного виджета
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")  # Черный фон

        self.labelRegistrationWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelRegistrationWindow.setGeometry(QtCore.QRect(490, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelRegistrationWindow.setFont(font)
        self.labelRegistrationWindow.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, белый текст
        self.labelRegistrationWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRegistrationWindow.setObjectName("labelRegistrationWindow")

        self.registrationButton = QtWidgets.QPushButton(self.centralwidget)
        self.registrationButton.setGeometry(QtCore.QRect(430, 360, 101, 26))
        self.registrationButton.setObjectName("registrationButton")
        self.registrationButton.clicked.connect(self.register_user)  # Подключаем обработчик
        self.registrationButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Белый текст

        # Настраиваем окна ввода
        self.textLogin = QtWidgets.QTextEdit(self.centralwidget)
        self.textLogin.setGeometry(QtCore.QRect(290, 260, 131, 31))
        self.textLogin.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст

        # Изменяем на QLineEdit для маскирования пароля
        self.textPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.textPassword.setGeometry(QtCore.QRect(290, 300, 131, 31))
        self.textPassword.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
        self.textPassword.setEchoMode(QtWidgets.QLineEdit.Password)  # Устанавливаем режим ввода пароля

        self.textName = QtWidgets.QTextEdit(self.centralwidget)
        self.textName.setGeometry(QtCore.QRect(290, 90, 131, 31))
        self.textName.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст

        self.textAddres = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddres.setGeometry(QtCore.QRect(290, 180, 131, 31))
        self.textAddres.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст

        self.startNumber = QtWidgets.QLabel(self.centralwidget)
        self.startNumber.setGeometry(QtCore.QRect(290, 230, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startNumber.setFont(font)
        self.startNumber.setStyleSheet("color: white;")  # Белый текст
        self.startNumber.setObjectName("startNumber")

        self.ManButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ManButton.setGeometry(QtCore.QRect(290, 140, 101, 24))
        self.ManButton.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Белый текст
        self.ManButton.setObjectName("ManButton")

        self.WomanButton = QtWidgets.QRadioButton(self.centralwidget)
        self.WomanButton.setGeometry(QtCore.QRect(410, 140, 101, 24))
        self.WomanButton.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Белый текст
        self.WomanButton.setObjectName("WomanButton")

        self.textNumbers_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textNumbers_1.setGeometry(QtCore.QRect(320, 230, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textNumbers_1.setFont(font)
        self.textNumbers_1.setAlignment(QtCore.Qt.AlignCenter)
        self.textNumbers_1.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
        self.textNumbers_1.setObjectName("textNumbers_1")
        self.textNumbers_1.setMaxLength(3)
        self.textNumbers_1.setValidator(QtGui.QIntValidator(0, 999, self.textNumbers_1))

        self.textNumbers_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textNumbers_2.setGeometry(QtCore.QRect(400, 230, 41, 21))
        self.textNumbers_2.setFont(font)
        self.textNumbers_2.setAlignment(QtCore.Qt.AlignCenter)
        self.textNumbers_2.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
        self.textNumbers_2.setObjectName("textNumbers_2")
        self.textNumbers_2.setMaxLength(3)
        self.textNumbers_2.setValidator(QtGui.QIntValidator(0, 999, self.textNumbers_2))

        self.textNumbers_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textNumbers_3.setGeometry(QtCore.QRect(480, 230, 41, 21))
        self.textNumbers_3.setFont(font)
        self.textNumbers_3.setAlignment(QtCore.Qt.AlignCenter)
        self.textNumbers_3.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")  # Темный фон, белый текст
        self.textNumbers_3.setObjectName("textNumbers_3")
        self.textNumbers_3.setMaxLength(4)
        self.textNumbers_3.setValidator(QtGui.QIntValidator(0, 999, self.textNumbers_3))

        self.authButton = QtWidgets.QPushButton(self.centralwidget)
        self.authButton.setGeometry(QtCore.QRect(550, 360, 101, 26))
        self.authButton.setObjectName("authButton")
        self.authButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Белый текст
        self.authButton.clicked.connect(self.go_to_auth)  # Подключаем обработчик

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно регистрации"))
        self.labelRegistrationWindow.setText(_translate("MainWindow", "Окно регистрации"))
        self.registrationButton.setText(_translate("MainWindow", "Регистрация"))
        self.textLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.textPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.textName.setPlaceholderText(_translate("MainWindow", "Введите имя"))
        self.textAddres.setPlaceholderText(_translate("MainWindow", "Введите адрес"))
        self.startNumber.setText(_translate("MainWindow", "+7"))
        self.ManButton.setText(_translate("MainWindow", "Мужской"))
        self.WomanButton.setText(_translate("MainWindow", "Женский"))
        self.authButton.setText(_translate("MainWindow", "Авторизация"))

    def register_user(self):
        fullname = self.textName.toPlainText()
        login = self.textLogin.toPlainText()
        password = self.textPassword.text()  # Изменено на text() для QLineEdit
        address = self.textAddres.toPlainText()
        phone = f"+7{self.textNumbers_1.text()}{self.textNumbers_2.text()}{self.textNumbers_3.text()}"
        gender = 1 if self.ManButton.isChecked() else 2  # Предположим, что 1 - мужской, 2 - женский
        role_id = 1  # Здесь можете указать ID роли, если это необходимо

        message = UserController.registration(fullname, login, password, gender, phone, role_id)
        QtWidgets.QMessageBox.information(None, "Результат регистрации", message)

    def go_to_auth(self):
        self.centralwidget.setVisible(False)  # Скрываем текущее окно регистрации
        # Переместим импорт TaxiApp внутрь функции
        from srcDiplom.Test.testMain import TaxiApp  # Импортируем здесь, чтобы избежать циклического импорта
        self.auth_window = TaxiApp()  # Создаем экземпляр окна авторизации
        self.auth_window.show()  # Показываем окно авторизации

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TestReg()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



