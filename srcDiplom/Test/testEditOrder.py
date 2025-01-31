# -*- coding: utf-8 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets
# from srcDiplom.Controllers.OrderController import OrderController
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1355, 715)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.centralwidget.setObjectName("centralwidget")
#         self.labelEditOrderWindow = QtWidgets.QLabel(self.centralwidget)
#         self.labelEditOrderWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.labelEditOrderWindow.setFont(font)
#         self.labelEditOrderWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelEditOrderWindow.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelEditOrderWindow.setObjectName("labelEditOrderWindow")
#         self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
#         self.ExitButton.setGeometry(QtCore.QRect(590, 550, 71, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.ExitButton.setFont(font)
#         self.ExitButton.setObjectName("ExitButton")
#         self.AddButton = QtWidgets.QPushButton(self.centralwidget)
#         self.AddButton.setGeometry(QtCore.QRect(70, 490, 80, 31))
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
#         self.textAddDriverId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddDriverId.setGeometry(QtCore.QRect(70, 190, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddDriverId.setFont(font)
#         self.textAddDriverId.setObjectName("textAddDriverId")
#         self.textAddPrice = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddPrice.setGeometry(QtCore.QRect(70, 390, 141, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddPrice.setFont(font)
#         self.textAddPrice.setObjectName("textAddPrice")
#         self.textAddDataId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddDataId.setGeometry(QtCore.QRect(70, 340, 121, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddDataId.setFont(font)
#         self.textAddDataId.setObjectName("textAddDataId")
#         self.textAddUserId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddUserId.setGeometry(QtCore.QRect(70, 240, 141, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddUserId.setFont(font)
#         self.textAddUserId.setObjectName("textAddUserId")
#         self.textAddCarId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddCarId.setGeometry(QtCore.QRect(70, 290, 141, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddCarId.setFont(font)
#         self.textAddCarId.setObjectName("textAddCarId")
#         self.textDeleteId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textDeleteId.setGeometry(QtCore.QRect(760, 190, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textDeleteId.setFont(font)
#         self.textDeleteId.setObjectName("textDeleteId")
#         self.textEditOrderId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditOrderId.setGeometry(QtCore.QRect(420, 190, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditOrderId.setFont(font)
#         self.textEditOrderId.setObjectName("textEditOrderId")
#         self.textEditStatusId = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEditStatusId.setGeometry(QtCore.QRect(420, 240, 171, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textEditStatusId.setFont(font)
#         self.textEditStatusId.setObjectName("textEditStatusId")
#         self.labelOrderAdd = QtWidgets.QLabel(self.centralwidget)
#         self.labelOrderAdd.setGeometry(QtCore.QRect(30, 130, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelOrderAdd.setFont(font)
#         self.labelOrderAdd.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelOrderAdd.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelOrderAdd.setObjectName("labelOrderAdd")
#         self.labelOrderEdit = QtWidgets.QLabel(self.centralwidget)
#         self.labelOrderEdit.setGeometry(QtCore.QRect(360, 130, 251, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelOrderEdit.setFont(font)
#         self.labelOrderEdit.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelOrderEdit.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelOrderEdit.setObjectName("labelOrderEdit")
#         self.labelOrderDelete = QtWidgets.QLabel(self.centralwidget)
#         self.labelOrderDelete.setGeometry(QtCore.QRect(700, 130, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.labelOrderDelete.setFont(font)
#         self.labelOrderDelete.setStyleSheet("background-color: rgb(161, 161, 161);")
#         self.labelOrderDelete.setAlignment(QtCore.Qt.AlignCenter)
#         self.labelOrderDelete.setObjectName("labelOrderDelete")
#         self.textAddStartPlace = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddStartPlace.setGeometry(QtCore.QRect(70, 440, 201, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddStartPlace.setFont(font)
#         self.textAddStartPlace.setObjectName("textAddStartPlace")
#         self.textAddEndPLace = QtWidgets.QTextEdit(self.centralwidget)
#         self.textAddEndPLace.setGeometry(QtCore.QRect(290, 440, 201, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textAddEndPLace.setFont(font)
#         self.textAddEndPLace.setObjectName("textAddEndPLace")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.AddButton.clicked.connect(self.add_order)
#         self.EditButton.clicked.connect(self.edit_order)
#         self.DeleteButton.clicked.connect(self.delete_order)
#         self.ExitButton.clicked.connect(MainWindow.close)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения заказов"))
#         self.labelEditOrderWindow.setText(_translate("MainWindow", "Окно изменения заказов"))
#         self.ExitButton.setText(_translate("MainWindow", "Выйти"))
#         self.AddButton.setText(_translate("MainWindow", "Добавить"))
#         self.EditButton.setText(_translate("MainWindow", "Изменить"))
#         self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
#         self.textAddDriverId.setPlaceholderText(_translate("MainWindow", "Введите driver_id"))
#         self.textAddPrice.setPlaceholderText(_translate("MainWindow", "Введите цену"))
#         self.textAddDataId.setPlaceholderText(_translate("MainWindow", "Введите дату"))
#         self.textAddUserId.setPlaceholderText(_translate("MainWindow", "Введите user_id"))
#         self.textAddCarId.setPlaceholderText(_translate("MainWindow", "Введите car_id"))
#         self.textDeleteId.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.textEditOrderId.setPlaceholderText(_translate("MainWindow", "Введите id"))
#         self.textEditStatusId.setPlaceholderText(_translate("MainWindow", "Введите id статуса"))
#         self.labelOrderAdd.setText(_translate("MainWindow", "Добавить Заказ"))
#         self.labelOrderEdit.setText(_translate("MainWindow", "Изменить статус заказа"))
#         self.labelOrderDelete.setText(_translate("MainWindow", "Удалить заказ"))
#         self.textAddStartPlace.setPlaceholderText(_translate("MainWindow", "Введите starting_place"))
#         self.textAddEndPLace.setPlaceholderText(_translate("MainWindow", "Введите end_place"))
#
#
#     # ... other UI methods (e.g., retranslateUi, etc.)
#
#     def add_order(self):
#         try:
#             user_id = self.textAddUserId.toPlainText()
#             driver_id = self.textAddDriverId.toPlainText()
#             car_id = self.textAddCarId.toPlainText()
#             date_id = self.textAddDataId.toPlainText()
#             price = self.textAddPrice.toPlainText()
#             start_place = self.textAddStartPlace.toPlainText()
#             end_place = self.textAddEndPLace.toPlainText()
#
#             # Вызов метода add с необходимыми параметрами
#             OrderController.add(user_id=user_id,
#                                 driver_id=driver_id,
#                                 car_id=car_id,
#                                 data=date_id,
#                                 price=price,
#                                 starting_place=start_place,
#                                 end_place=end_place)
#             self.clear_add_fields()
#             QtWidgets.QMessageBox.information(None, "Успех", "Заказ добавлен успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#     def edit_order(self):
#         try:
#             order_id = self.textEditOrderId.toPlainText()
#             status_id = self.textEditStatusId.toPlainText()
#             OrderController.update(status_id, order_id)
#             self.clear_edit_fields()
#             QtWidgets.QMessageBox.information(None, "Успех", "Статус заказа изменен успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#     def delete_order(self):
#         try:
#             order_id = self.textDeleteId.toPlainText()
#             OrderController.delete(order_id)
#             self.textDeleteId.clear()
#             QtWidgets.QMessageBox.information(None, "Успех", "Заказ удален успешно.")
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))
#
#
#     def clear_add_fields(self):
#         self.textAddUserId.clear()
#         self.textAddCarId.clear()
#         self.textAddDriverId.clear()
#         self.textAddDataId.clear()
#         self.textAddPrice.clear()
#         self.textAddStartPlace.clear()
#         self.textAddEndPLace.clear()
#
#
#     def clear_edit_fields(self):
#         self.textEditOrderId.clear()
#         self.textEditStatusId.clear()
#
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
#     self.retranslateUi(MainWindow)
#     QtCore.QMetaObject.connectSlotsByName(MainWindow)


from PyQt5 import QtCore, QtGui, QtWidgets
from srcDiplom.Controllers.OrderController import OrderController


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Установка черного фона для центрального виджета
        self.centralwidget.setStyleSheet("background-color: black;")


        # Кнопка "Выйти"
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(590, 550, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон с черным текстом
        self.ExitButton.setObjectName("ExitButton")

        # Кнопка "Добавить"
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(70, 490, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон с черным текстом
        self.AddButton.setObjectName("AddButton")

        # Кнопка "Изменить"
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(420, 290, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditButton.setFont(font)
        self.EditButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон с черным текстом
        self.EditButton.setObjectName("EditButton")

        # Кнопка "Удалить"
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(760, 240, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet(
            "background-color: rgb(255, 172, 0); color: black;")  # Оранжевый фон с черным текстом
        self.DeleteButton.setObjectName("DeleteButton")

        # Поля для ввода текста
        self.textAddDriverId = self.create_text_edit(70, 190)
        self.textAddPrice = self.create_text_edit(70, 390)
        self.textAddDataId = self.create_text_edit(70, 340)
        self.textAddUserId = self.create_text_edit(70, 240)
        self.textAddCarId = self.create_text_edit(70, 290)
        self.textDeleteId = self.create_text_edit(760, 190)
        self.textEditOrderId = self.create_text_edit(420, 190)
        self.textEditStatusId = self.create_text_edit(420, 240)
        self.textAddStartPlace = self.create_text_edit(70, 440)
        self.textAddEndPLace = self.create_text_edit(250, 440)

        # Создание меток с оранжевым фоном
        self.labelEditOrderWindow = self.create_label(350, 13, "Окно заказа")
        self.labelOrderAdd = self.create_label(30, 130, "Добавить Заказ")
        self.labelOrderEdit = self.create_label(360, 130, "Изменить статус заказа")
        self.labelOrderDelete = self.create_label(700, 130, "Удалить заказ")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.AddButton.clicked.connect(self.add_order)
        self.EditButton.clicked.connect(self.edit_order)
        self.DeleteButton.clicked.connect(self.delete_order)
        self.ExitButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_text_edit(self, x, y):
        text_edit = QtWidgets.QTextEdit(self.centralwidget)
        text_edit.setGeometry(QtCore.QRect(x, y, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        text_edit.setFont(font)
        text_edit.setStyleSheet("background-color: rgb(50, 50, 50); color: black;")  # Белый фон и черный текст
        return text_edit

    def create_label(self, x, y, text):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(x, y, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        label.setFont(font)
        label.setStyleSheet("color: black; background-color: rgb(255, 172, 0);")  # Оранжевый фон с черным текстом
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(text)
        return label

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения заказов"))
        self.ExitButton.setText(_translate("MainWindow", "Выйти"))
        self.AddButton.setText(_translate("MainWindow", "Добавить"))
        self.EditButton.setText(_translate("MainWindow", "Изменить"))
        self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
        self.textAddDriverId.setPlaceholderText(_translate("MainWindow", "Введите driver_id"))
        self.textAddPrice.setPlaceholderText(_translate("MainWindow", "Введите цену"))
        self.textAddDataId.setPlaceholderText(_translate("MainWindow", "Введите дату"))
        self.textAddUserId.setPlaceholderText(_translate("MainWindow", "Введите user_id"))
        self.textAddCarId.setPlaceholderText(_translate("MainWindow", "Введите car_id"))
        self.textDeleteId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditOrderId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditStatusId.setPlaceholderText(_translate("MainWindow", "Введите id статуса"))
        self.textAddStartPlace.setPlaceholderText(_translate("MainWindow", "Введите starting_place"))
        self.textAddEndPLace.setPlaceholderText(_translate("MainWindow", "Введите end_place"))

    def add_order(self):
        try:
            user_id = self.textAddUserId.toPlainText()
            driver_id = self.textAddDriverId.toPlainText()
            car_id = self.textAddCarId.toPlainText()
            date_id = self.textAddDataId.toPlainText()
            price = self.textAddPrice.toPlainText()
            start_place = self.textAddStartPlace.toPlainText()
            end_place = self.textAddEndPLace.toPlainText()

            # Вызов метода add с необходимыми параметрами
            OrderController.add(user_id=user_id,
                                driver_id=driver_id,
                                car_id=car_id,
                                data=date_id,
                                price=price,
                                starting_place=start_place,
                                end_place=end_place)
            self.clear_add_fields()
            QtWidgets.QMessageBox.information(None, "Успех", "Заказ добавлен успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def edit_order(self):
        try:
            order_id = self.textEditOrderId.toPlainText()
            status_id = self.textEditStatusId.toPlainText()
            OrderController.update(status_id, order_id)
            self.clear_edit_fields()
            QtWidgets.QMessageBox.information(None, "Успех", "Статус заказа изменен успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def delete_order(self):
        try:
            order_id = self.textDeleteId.toPlainText()
            OrderController.delete(order_id)
            self.textDeleteId.clear()
            QtWidgets.QMessageBox.information(None, "Успех", "Заказ удален успешно.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))

    def clear_add_fields(self):
        self.textAddUserId.clear()
        self.textAddCarId.clear()
        self.textAddDriverId.clear()
        self.textAddDataId.clear()
        self.textAddPrice.clear()
        self.textAddStartPlace.clear()
        self.textAddEndPLace.clear()

    def clear_edit_fields(self):
        self.textEditOrderId.clear()
        self.textEditStatusId.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

