# from PyQt5 import QtCore, QtGui, QtWidgets
# from srcDiplom.Controllers.UserController import UserController
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1355, 715)
#         MainWindow.setToolTip("")
#         MainWindow.setStatusTip("")
#         MainWindow.setWhatsThis("")
#         MainWindow.setAccessibleName("")
#         MainWindow.setAccessibleDescription("")
#         MainWindow.setAutoFillBackground(False)
#         MainWindow.setStyleSheet("")
#         MainWindow.setWindowFilePath("")
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.labelEditUserWindow = QtWidgets.QLabel(self.centralwidget)
#         self.labelEditUserWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.labelEditUserWindow.setFont(font)
#         self.labelEditUserWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelEditUserWindow.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelEditUserWindow.setObjectName("labelEditUserWindow")
#         self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
#         self.ExitButton.setGeometry(QtCore.QRect(460, 460, 71, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.ExitButton.setFont(font)
#         self.ExitButton.setObjectName("ExitButton")
#         self.AddButton = QtWidgets.QPushButton(self.centralwidget)
#         self.AddButton.setGeometry(QtCore.QRect(70, 440, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.AddButton.setFont(font)
#         self.AddButton.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.AddButton.setObjectName("AddButton")
#         self.EditButton = QtWidgets.QPushButton(self.centralwidget)
#         self.EditButton.setGeometry(QtCore.QRect(420, 290, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.EditButton.setFont(font)
#         self.EditButton.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.EditButton.setObjectName("EditButton")
#         self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
#         self.DeleteButton.setGeometry(QtCore.QRect(760, 240, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.DeleteButton.setFont(font)
#         self.DeleteButton.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.DeleteButton.setObjectName("DeleteButton")
#         self.textAddFullname = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddFullname.setGeometry(QtCore.QRect(70, 190, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddFullname.setFont(font)
#         self.textAddFullname.setObjectName("textAddFullname")
#         self.textAddPassword = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddPassword.setGeometry(QtCore.QRect(70, 390, 141, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddPassword.setFont(font)
#         self.textAddPassword.setObjectName("textAddPassword")
#         self.textAddLogin = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddLogin.setGeometry(QtCore.QRect(70, 340, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddLogin.setFont(font)
#         self.textAddLogin.setObjectName("textAddLogin")
#         self.textAddGender = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddGender.setGeometry(QtCore.QRect(70, 240, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddGender.setFont(font)
#         self.textAddGender.setObjectName("textAddGender")
#         self.textAddNumber = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddNumber.setGeometry(QtCore.QRect(70, 290, 201, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddNumber.setFont(font)
#         self.textAddNumber.setObjectName("textAddNumber")
#         self.textDeleteUserId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textDeleteUserId.setGeometry(QtCore.QRect(760, 190, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textDeleteUserId.setFont(font)
#         self.textDeleteUserId.setObjectName("textDeleteUserId")
#         self.textEditUserId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditUserId.setGeometry(QtCore.QRect(420, 190, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditUserId.setFont(font)
#         self.textEditUserId.setObjectName("textEditUserId")
#         self.textEditFullname = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditFullname.setGeometry(QtCore.QRect(420, 240, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditFullname.setFont(font)
#         self.textEditFullname.setObjectName("textEditFullname")
#         self.labelUserAdd = QtWidgets.QLabel(self.centralwidget)
#         self.labelUserAdd.setGeometry(QtCore.QRect(30, 100, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelUserAdd.setFont(font)
#         self.labelUserAdd.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelUserAdd.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelUserAdd.setObjectName("labelUserAdd")
#         self.labelUserEdit = QtWidgets.QLabel(self.centralwidget)
#         self.labelUserEdit.setGeometry(QtCore.QRect(360, 100, 251, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelUserEdit.setFont(font)
#         self.labelUserEdit.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelUserEdit.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelUserEdit.setObjectName("labelUserEdit")
#         self.labelUserDelete = QtWidgets.QLabel(self.centralwidget)
#         self.labelUserDelete.setGeometry(QtCore.QRect(700, 100, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelUserDelete.setFont(font)
#         self.labelUserDelete.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelUserDelete.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelUserDelete.setObjectName("labelUserDelete")
#         self.textAddRole = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddRole.setGeometry(QtCore.QRect(190, 240, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddRole.setFont(font)
#         self.textAddRole.setObjectName("textAddRole")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.AddButton.clicked.connect(self.add_user)
#         self.EditButton.clicked.connect(self.edit_user)
#         self.DeleteButton.clicked.connect(self.delete_user)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения пользователя"))
#         self.labelEditUserWindow.setText(_translate("MainWindow", "Окно изменения пользователя"))
#         self.ExitButton.setText(_translate("MainWindow", "Выйти"))
#         self.AddButton.setText(_translate("MainWindow", "Добавить"))
#         self.EditButton.setText(_translate("MainWindow", "Изменить"))
#         self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
#         self.textAddFullname.setPlaceholderText(_translate("MainWindow", "Введите ФИО"))
#         self.textAddPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
#         self.textAddLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
#         self.textAddGender.setPlaceholderText(_translate("MainWindow", "Введите пол"))
#         self.textAddNumber.setPlaceholderText(_translate("MainWindow", "Введите номер телефона"))
#         self.textDeleteUserId.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.textEditUserId.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.textEditFullname.setPlaceholderText(_translate("MainWindow", "Введите ФИО"))
#         self.labelUserAdd.setText(_translate("MainWindow", "Добавить Пользователя"))
#         self.labelUserEdit.setText(_translate("MainWindow", "Изменить пользователя"))
#         self.labelUserDelete.setText(_translate("MainWindow", "Удалить пользователя"))
#         self.textAddRole.setPlaceholderText(_translate("MainWindow", "Введите роль"))
#
#
#     def add_user(self):
#         fullname = self.textAddFullname.toPlainText()
#         login = self.textAddLogin.toPlainText()
#         password = self.textAddPassword.toPlainText()
#         gender = self.textAddGender.toPlainText()
#         phone = self.textAddNumber.toPlainText()
#         role = self.textAddRole.toPlainText()
#
#         response = UserController.registration(fullname, login, password, gender, phone, role)
#         self.clear_add_fields()
#         QtWidgets.QMessageBox.information(None, "Информация", response)
#
#     def edit_user(self):
#         user_id = self.textEditUserId.toPlainText()
#         new_fullname = self.textEditFullname.toPlainText()
#
#         if user_id:
#             UserController.update(user_id, new_fullname)
#             self.clear_edit_fields()
#             QtWidgets.QMessageBox.information(None, "Информация", f"Пользователь с ID {user_id} изменён.")
#         else:
#             QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите ID пользователя для изменения.")
#
#     def delete_user(self):
#         user_id = self.textDeleteUserId.toPlainText()
#
#         if user_id:
#             UserController.delete(user_id)
#             self.textDeleteUserId.clear()
#             QtWidgets.QMessageBox.information(None, "Информация", f"Пользователь с ID {user_id} удалён.")
#         else:
#             QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите ID пользователя для удаления.")
#
#     def clear_add_fields(self):
#         self.textAddFullname.clear()
#         self.textAddLogin.clear()
#         self.textAddPassword.clear()
#         self.textAddGender.clear()
#         self.textAddNumber.clear()
#         self.textAddRole.clear()
#
#
#     def clear_edit_fields(self):
#         self.textEditUserId.clear()
#         self.textEditFullname.clear()
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from srcDiplom.Controllers.UserController import UserController


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 715)
        MainWindow.setStyleSheet("background-color: black;")  # Фон программы черный

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelEditUserWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelEditUserWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelEditUserWindow.setFont(font)
        self.labelEditUserWindow.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.labelEditUserWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEditUserWindow.setObjectName("labelEditUserWindow")

        # Кнопка "Выйти"
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(460, 460, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.ExitButton.setObjectName("ExitButton")

        # Кнопка "Добавить"
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(70, 440, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.AddButton.setObjectName("AddButton")

        # Кнопка "Изменить"
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(420, 290, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditButton.setFont(font)
        self.EditButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.EditButton.setObjectName("EditButton")

        # Кнопка "Удалить"
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(760, 240, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.DeleteButton.setObjectName("DeleteButton")

        # Окна ввода с видимым фоном
        text_edit_style = "background-color: rgb(50, 50, 50); color: white;"  # Темный фон для текста, белый текст

        self.textAddFullname = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddFullname.setGeometry(QtCore.QRect(70, 190, 121, 31))
        self.textAddFullname.setStyleSheet(text_edit_style)
        self.textAddFullname.setFont(font)
        self.textAddFullname.setObjectName("textAddFullname")

        self.textAddPassword = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddPassword.setGeometry(QtCore.QRect(70, 390, 141, 31))
        self.textAddPassword.setStyleSheet(text_edit_style)
        self.textAddPassword.setFont(font)
        self.textAddPassword.setObjectName("textAddPassword")

        self.textAddLogin = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddLogin.setGeometry(QtCore.QRect(70, 340, 121, 31))
        self.textAddLogin.setStyleSheet(text_edit_style)
        self.textAddLogin.setFont(font)
        self.textAddLogin.setObjectName("textAddLogin")

        self.textAddGender = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddGender.setGeometry(QtCore.QRect(70, 240, 101, 31))
        self.textAddGender.setStyleSheet(text_edit_style)
        self.textAddGender.setFont(font)
        self.textAddGender.setObjectName("textAddGender")

        self.textAddRole = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddRole.setGeometry(QtCore.QRect(200, 240, 120, 31))
        self.textAddRole.setStyleSheet(text_edit_style)
        self.textAddRole.setFont(font)
        self.textAddRole.setObjectName("textAddRole")

        self.textAddNumber = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddNumber.setGeometry(QtCore.QRect(70, 290, 201, 31))
        self.textAddNumber.setStyleSheet(text_edit_style)
        self.textAddNumber.setFont(font)
        self.textAddNumber.setObjectName("textAddNumber")

        self.textDeleteUserId = QtWidgets.QTextEdit(self.centralwidget)
        self.textDeleteUserId.setGeometry(QtCore.QRect(760, 190, 101, 31))
        self.textDeleteUserId.setStyleSheet(text_edit_style)
        self.textDeleteUserId.setFont(font)
        self.textDeleteUserId.setObjectName("textDeleteUserId")

        self.textEditUserId = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditUserId.setGeometry(QtCore.QRect(420, 190, 101, 31))
        self.textEditUserId.setStyleSheet(text_edit_style)
        self.textEditUserId.setFont(font)
        self.textEditUserId.setObjectName("textEditUserId")

        self.textEditFullname = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditFullname.setGeometry(QtCore.QRect(420, 240, 121, 31))
        self.textEditFullname.setStyleSheet(text_edit_style)
        self.textEditFullname.setFont(font)
        self.textEditFullname.setObjectName("textEditFullname")

        self.labelUserAdd = QtWidgets.QLabel(self.centralwidget)
        self.labelUserAdd.setGeometry(QtCore.QRect(30, 100, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelUserAdd.setFont(font)
        self.labelUserAdd.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.labelUserAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUserAdd.setObjectName("labelUserAdd")

        self.labelUserEdit = QtWidgets.QLabel(self.centralwidget)
        self.labelUserEdit.setGeometry(QtCore.QRect(360, 100, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelUserEdit.setFont(font)
        self.labelUserEdit.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.labelUserEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUserEdit.setObjectName("labelUserEdit")

        self.labelUserDelete = QtWidgets.QLabel(self.centralwidget)
        self.labelUserDelete.setGeometry(QtCore.QRect(700, 100, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelUserDelete.setFont(font)
        self.labelUserDelete.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон, черный текст
        self.labelUserDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUserDelete.setObjectName("labelUserDelete")

        # self.textAddRole = QtWidgets.QTextEdit(self.centralwidget)
        # self.textAddRole.setGeometry(QtCore.QRect(190, 240, 101, 31))
        # self.textAddRole.setStyleSheet(text_edit_style)
        # self.textAddRole.setFont(font)
        # self.textAddRole.setObjectName("textAddRole")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.AddButton.clicked.connect(self.add_user)
        self.EditButton.clicked.connect(self.edit_user)
        self.DeleteButton.clicked.connect(self.delete_user)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения пользователя"))
        self.labelEditUserWindow.setText(_translate("MainWindow", "Окно изменения пользователя"))
        self.ExitButton.setText(_translate("MainWindow", "Выйти"))
        self.AddButton.setText(_translate("MainWindow", "Добавить"))
        self.EditButton.setText(_translate("MainWindow", "Изменить"))
        self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
        self.textAddFullname.setPlaceholderText(_translate("MainWindow", "Введите ФИО"))
        self.textAddPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.textAddLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.textAddGender.setPlaceholderText(_translate("MainWindow", "Введите пол"))
        self.textAddNumber.setPlaceholderText(_translate("MainWindow", "Введите номер телефона"))
        self.textDeleteUserId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditUserId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditFullname.setPlaceholderText(_translate("MainWindow", "Введите ФИО"))
        self.labelUserAdd.setText(_translate("MainWindow", "Добавить Пользователя"))
        self.labelUserEdit.setText(_translate("MainWindow", "Изменить пользователя"))
        self.labelUserDelete.setText(_translate("MainWindow", "Удалить пользователя"))
        self.textAddRole.setPlaceholderText(_translate("MainWindow", "Введите роль"))

    def add_user(self):
        fullname = self.textAddFullname.toPlainText()
        login = self.textAddLogin.toPlainText()
        password = self.textAddPassword.toPlainText()
        gender = self.textAddGender.toPlainText()
        phone = self.textAddNumber.toPlainText()
        role = self.textAddRole.toPlainText()

        response = UserController.registration(fullname, login, password, gender, phone, role)
        self.clear_add_fields()
        QtWidgets.QMessageBox.information(None, "Информация", response)

    def edit_user(self):
        user_id = self.textEditUserId.toPlainText()
        new_fullname = self.textEditFullname.toPlainText()

        if user_id:
            UserController.update(user_id, new_fullname)
            self.clear_edit_fields()
            QtWidgets.QMessageBox.information(None, "Информация", f"Пользователь с ID {user_id} изменён.")
        else:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите ID пользователя для изменения.")

    def delete_user(self):
        user_id = self.textDeleteUserId.toPlainText()

        if user_id:
            UserController.delete(user_id)
            self.textDeleteUserId.clear()
            QtWidgets.QMessageBox.information(None, "Информация", f"Пользователь с ID {user_id} удалён.")
        else:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите ID пользователя для удаления.")

    def clear_add_fields(self):
        self.textAddFullname.clear()
        self.textAddLogin.clear()
        self.textAddPassword.clear()
        self.textAddGender.clear()
        self.textAddNumber.clear()
        self.textAddRole.clear()

    def clear_edit_fields(self):
        self.textEditUserId.clear()
        self.textEditFullname.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

