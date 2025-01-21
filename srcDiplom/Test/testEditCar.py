# from PyQt5 import QtCore, QtGui, QtWidgets
# from srcDiplom.Controllers.CarController import CarController
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
#         self.labelEditCarsWindow = QtWidgets.QLabel(self.centralwidget)
#         self.labelEditCarsWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.labelEditCarsWindow.setFont(font)
#         self.labelEditCarsWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelEditCarsWindow.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelEditCarsWindow.setObjectName("labelEditCarsWindow")
#         self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
#         self.ExitButton.setGeometry(QtCore.QRect(460, 460, 71, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.ExitButton.setFont(font)
#         self.ExitButton.setObjectName("ExitButton")
#         self.AddButton = QtWidgets.QPushButton(self.centralwidget)
#         self.AddButton.setGeometry(QtCore.QRect(70, 390, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.AddButton.setFont(font)
#         self.AddButton.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.AddButton.setObjectName("AddButton")
#         self.EditButtonNumberCar = QtWidgets.QPushButton(self.centralwidget)
#         self.EditButtonNumberCar.setGeometry(QtCore.QRect(380, 290, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.EditButtonNumberCar.setFont(font)
#         self.EditButtonNumberCar.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.EditButtonNumberCar.setObjectName("EditButtonNumberCar")
#         self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
#         self.DeleteButton.setGeometry(QtCore.QRect(1070, 240, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.DeleteButton.setFont(font)
#         self.DeleteButton.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.DeleteButton.setObjectName("DeleteButton")
#         self.textAddFullname = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddFullname.setGeometry(QtCore.QRect(70, 190, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddFullname.setFont(font)
#         self.textAddFullname.setObjectName("textAddFullname")
#         self.textAddLogin = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddLogin.setGeometry(QtCore.QRect(70, 340, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddLogin.setFont(font)
#         self.textAddLogin.setObjectName("textAddLogin")
#         self.textAddGender = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddGender.setGeometry(QtCore.QRect(70, 240, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddGender.setFont(font)
#         self.textAddGender.setObjectName("textAddGender")
#         self.textAddNumber = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddNumber.setGeometry(QtCore.QRect(70, 290, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddNumber.setFont(font)
#         self.textAddNumber.setObjectName("textAddNumber")
#         self.textDeleteCarId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textDeleteCarId.setGeometry(QtCore.QRect(1070, 190, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textDeleteCarId.setFont(font)
#         self.textDeleteCarId.setObjectName("textDeleteCarId")
#         self.labelCarAdd = QtWidgets.QLabel(self.centralwidget)
#         self.labelCarAdd.setGeometry(QtCore.QRect(30, 130, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelCarAdd.setFont(font)
#         self.labelCarAdd.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelCarAdd.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelCarAdd.setObjectName("labelCarAdd")
#         self.labelCarNumberEdit = QtWidgets.QLabel(self.centralwidget)
#         self.labelCarNumberEdit.setGeometry(QtCore.QRect(360, 130, 291, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelCarNumberEdit.setFont(font)
#         self.labelCarNumberEdit.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelCarNumberEdit.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelCarNumberEdit.setObjectName("labelCarNumberEdit")
#         self.labelCarDelete = QtWidgets.QLabel(self.centralwidget)
#         self.labelCarDelete.setGeometry(QtCore.QRect(1060, 130, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelCarDelete.setFont(font)
#         self.labelCarDelete.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelCarDelete.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelCarDelete.setObjectName("labelCarDelete")
#         self.labelCarColorEdit = QtWidgets.QLabel(self.centralwidget)
#         self.labelCarColorEdit.setGeometry(QtCore.QRect(730, 130, 241, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelCarColorEdit.setFont(font)
#         self.labelCarColorEdit.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelCarColorEdit.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelCarColorEdit.setObjectName("labelCarColorEdit")
#         self.EditButtonColorCar = QtWidgets.QPushButton(self.centralwidget)
#         self.EditButtonColorCar.setGeometry(QtCore.QRect(750, 290, 80, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.EditButtonColorCar.setFont(font)
#         self.EditButtonColorCar.setStyleSheet("background-color: rgb(255, 172, 0);")
#         self.EditButtonColorCar.setObjectName("EditButtonColorCar")
#         self.textEditNumberCarID = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditNumberCarID.setGeometry(QtCore.QRect(380, 240, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditNumberCarID.setFont(font)
#         self.textEditNumberCarID.setObjectName("textEditNumberCarID")
#         self.textEditColorCarId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditColorCarId.setGeometry(QtCore.QRect(750, 240, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditColorCarId.setFont(font)
#         self.textEditColorCarId.setObjectName("textEditColorCarId")
#         self.textEditNumberCar = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditNumberCar.setGeometry(QtCore.QRect(380, 190, 171, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditNumberCar.setFont(font)
#         self.textEditNumberCar.setObjectName("textEditNumberCar")
#         self.textEditColorCar = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditColorCar.setGeometry(QtCore.QRect(750, 190, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditColorCar.setFont(font)
#         self.textEditColorCar.setObjectName("textEditColorCar")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.AddButton.clicked.connect(self.add_car)
#         self.EditButtonNumberCar.clicked.connect(self.edit_car_number)
#         self.EditButtonColorCar.clicked.connect(self.edit_car_color)
#         self.DeleteButton.clicked.connect(self.delete_car)
#         self.ExitButton.clicked.connect(MainWindow.close)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения машин"))
#         self.labelEditCarsWindow.setText(_translate("MainWindow", "Окно изменения машин"))
#         self.ExitButton.setText(_translate("MainWindow", "Выйти"))
#         self.AddButton.setText(_translate("MainWindow", "Добавить"))
#         self.EditButtonNumberCar.setText(_translate("MainWindow", "Изменить"))
#         self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
#         self.textAddFullname.setPlaceholderText(_translate("MainWindow", "Введите бренд"))
#         self.textAddLogin.setPlaceholderText(_translate("MainWindow", "Введите гос.номер"))
#         self.textAddGender.setPlaceholderText(_translate("MainWindow", "Введите модель"))
#         self.textAddNumber.setPlaceholderText(_translate("MainWindow", "Введите цвет"))
#         self.textDeleteCarId.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.labelCarAdd.setText(_translate("MainWindow", "Добавить Машину"))
#         self.labelCarNumberEdit.setText(_translate("MainWindow", "Изменить гос. номер Машины"))
#         self.labelCarDelete.setText(_translate("MainWindow", "Удалить Машину"))
#         self.labelCarColorEdit.setText(_translate("MainWindow", "Изменить цвет Машины"))
#         self.EditButtonColorCar.setText(_translate("MainWindow", "Изменить"))
#         self.textEditNumberCarID.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.textEditColorCarId.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.textEditNumberCar.setPlaceholderText(_translate("MainWindow", "Введите гос. номер"))
#         self.textEditColorCar.setPlaceholderText(_translate("MainWindow", "Введите цвет"))
#
#     def add_car(self):
#         try:
#             brand = self.textAddFullname.toPlainText()
#             model = self.textAddGender.toPlainText()
#             color = self.textAddNumber.toPlainText()
#             state_number = self.textAddLogin.toPlainText()
#             CarController.add(brand, model, color, state_number)
#             self.clear_add_fields()
#             QtWidgets.QMessageBox.information(None, "Успех", "Машина добавлена успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#
#
#
#     def edit_car_number(self):
#         try:
#             new_number = self.textEditNumberCar.toPlainText()
#             car_id = self.textEditNumberCarID.toPlainText()
#             CarController.update_number(new_number, int(car_id))
#             self.clear_edit_fields()
#             QtWidgets.QMessageBox.information(None, "Успех", "Номер машины изменен успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#
#     def edit_car_color(self):
#         try:
#             new_color = self.textEditColorCar.toPlainText()
#             car_id = self.textEditColorCarId.toPlainText()
#             CarController.update_color(new_color, int(car_id))
#             self.clear_edit_fields()
#             QtWidgets.QMessageBox.information(None, "Успех", "Цвет машины изменен успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#     def delete_car(self):
#         try:
#             car_id = self.textDeleteCarId.toPlainText()
#             CarController.delete(int(car_id))
#             self.textDeleteCarId.clear()
#             QtWidgets.QMessageBox.information(None, "Успех", "Машина удалена успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#
#
#     def clear_add_fields(self):
#         self.textAddFullname.clear()
#         self.textAddGender.clear()
#         self.textAddNumber.clear()
#         self.textAddLogin.clear()
#
#     def clear_edit_fields(self):
#         self.textEditNumberCar.clear()
#         self.textEditNumberCarID.clear()
#         self.textEditColorCar.clear()
#         self.textEditColorCarId.clear()
#
#
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
from srcDiplom.Controllers.CarController import CarController

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 715)
        MainWindow.setStyleSheet("background-color: black; color: black")  # Установка черного фона и белого текста
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Заголовок окна
        self.labelEditCarsWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelEditCarsWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelEditCarsWindow.setFont(font)
        self.labelEditCarsWindow.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон
        self.labelEditCarsWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEditCarsWindow.setObjectName("labelEditCarsWindow")

        # Кнопки
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(460, 460, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон для кнопки
        self.ExitButton.setObjectName("ExitButton")

        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(70, 390, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон для кнопки
        self.AddButton.setObjectName("AddButton")

        # Остальные кнопки...
        self.EditButtonNumberCar = QtWidgets.QPushButton(self.centralwidget)
        self.EditButtonNumberCar.setGeometry(QtCore.QRect(380, 290, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditButtonNumberCar.setFont(font)
        self.EditButtonNumberCar.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон для кнопки
        self.EditButtonNumberCar.setObjectName("EditButtonNumberCar")

        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(1070, 240, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон для кнопки
        self.DeleteButton.setObjectName("DeleteButton")

        # Окна ввода
        self.textAddFullname = self.createTextEdit(70, 190)
        self.textAddLogin = self.createTextEdit(70, 340)
        self.textAddGender = self.createTextEdit(70, 240)
        self.textAddNumber = self.createTextEdit(70, 290)
        self.textDeleteCarId = self.createTextEdit(1070, 190)
        self.textEditNumberCarID = self.createTextEdit(380, 240)
        self.textEditColorCarId = self.createTextEdit(750, 240)
        self.textEditNumberCar = self.createTextEdit(380, 190)
        self.textEditColorCar = self.createTextEdit(750, 190)

        # Метки
        self.labelCarAdd = self.createLabel("Добавить Машину", 30, 130)
        self.labelCarNumberEdit = self.createLabel("Изменить гос. номер", 360, 130)
        self.labelCarDelete = self.createLabel("Удалить Машину", 1060, 130)
        self.labelCarColorEdit = self.createLabel("Изменить цвет Машины", 730, 130)

        # Кнопка для изменения цвета
        self.EditButtonColorCar = QtWidgets.QPushButton(self.centralwidget)
        self.EditButtonColorCar.setGeometry(QtCore.QRect(750, 290, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditButtonColorCar.setFont(font)
        self.EditButtonColorCar.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон для кнопки
        self.EditButtonColorCar.setObjectName("EditButtonColorCar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Связывание кнопок с методами
        self.AddButton.clicked.connect(self.add_car)
        self.EditButtonNumberCar.clicked.connect(self.edit_car_number)
        self.EditButtonColorCar.clicked.connect(self.edit_car_color)
        self.DeleteButton.clicked.connect(self.delete_car)
        self.ExitButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def createTextEdit(self, x, y):
        text_edit = QtWidgets.QTextEdit(self.centralwidget)
        text_edit.setGeometry(QtCore.QRect(x, y, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        text_edit.setFont(font)
        text_edit.setStyleSheet("background-color: rgb(50, 50, 50); color: black;")  # Темный фон для текстовых полей
        return text_edit

    def createLabel(self, text, x, y):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(x, y, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        label.setFont(font)
        label.setStyleSheet("background-color: rgb(255, 172, 0);")  # Оранжевый фон для меток
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(text)
        return label

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения машин"))
        self.labelEditCarsWindow.setText(_translate("MainWindow", "Окно изменения машин"))
        self.ExitButton.setText(_translate("MainWindow", "Выйти"))
        self.AddButton.setText(_translate("MainWindow", "Добавить"))
        self.EditButtonNumberCar.setText(_translate("MainWindow", "Изменить"))
        self.EditButtonColorCar.setText(_translate("MainWindow", "Изменить"))
        self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
        self.textAddFullname.setPlaceholderText(_translate("MainWindow", "Введите бренд"))
        self.textAddLogin.setPlaceholderText(_translate("MainWindow", "Введите гос.номер"))
        self.textAddGender.setPlaceholderText(_translate("MainWindow", "Введите модель"))
        self.textAddNumber.setPlaceholderText(_translate("MainWindow", "Введите цвет"))
        self.textDeleteCarId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditNumberCarID.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditColorCarId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditNumberCar.setPlaceholderText(_translate("MainWindow", "Введите гос. номер"))
        self.textEditColorCar.setPlaceholderText(_translate("MainWindow", "Введите цвет"))

    def add_car(self):
        try:
            brand = self.textAddFullname.toPlainText()
            model = self.textAddGender.toPlainText()
            color = self.textAddNumber.toPlainText()
            state_number = self.textAddLogin.toPlainText()
            CarController.add(brand, model, color, state_number)
            self.clear_add_fields()
            QtWidgets.QMessageBox.information(None, "Успех", "Машина добавлена успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def edit_car_number(self):
        try:
            new_number = self.textEditNumberCar.toPlainText()
            car_id = self.textEditNumberCarID.toPlainText()
            CarController.update_number(new_number, int(car_id))
            self.clear_edit_fields()
            QtWidgets.QMessageBox.information(None, "Успех", "Номер машины изменен успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def edit_car_color(self):
        try:
            new_color = self.textEditColorCar.toPlainText()
            car_id = self.textEditColorCarId.toPlainText()
            CarController.update_color(new_color, int(car_id))
            self.clear_edit_fields()
            QtWidgets.QMessageBox.information(None, "Успех", "Цвет машины изменен успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def delete_car(self):
        try:
            car_id = self.textDeleteCarId.toPlainText()
            CarController.delete(int(car_id))
            self.textDeleteCarId.clear()
            QtWidgets.QMessageBox.information(None, "Успех", "Машина удалена успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def clear_add_fields(self):
        self.textAddFullname.clear()
        self.textAddGender.clear()
        self.textAddNumber.clear()
        self.textAddLogin.clear()

    def clear_edit_fields(self):
        self.textEditNumberCar.clear()
        self.textEditNumberCarID.clear()
        self.textEditColorCar.clear()
        self.textEditColorCarId.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


