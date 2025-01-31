# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOrdersWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 715)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEditOrderWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelEditOrderWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelEditOrderWindow.setFont(font)
        self.labelEditOrderWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.labelEditOrderWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEditOrderWindow.setObjectName("labelEditOrderWindow")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(590, 550, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(50, 340, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("background-color: rgb(255, 172, 0);")
        self.AddButton.setObjectName("AddButton")
        self.textAddPrice = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddPrice.setGeometry(QtCore.QRect(50, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddPrice.setFont(font)
        self.textAddPrice.setObjectName("textAddPrice")
        self.labelOrderAdd = QtWidgets.QLabel(self.centralwidget)
        self.labelOrderAdd.setGeometry(QtCore.QRect(40, 130, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelOrderAdd.setFont(font)
        self.labelOrderAdd.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.labelOrderAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOrderAdd.setObjectName("labelOrderAdd")
        self.textAddStartPlace = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddStartPlace.setGeometry(QtCore.QRect(50, 190, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddStartPlace.setFont(font)
        self.textAddStartPlace.setObjectName("textAddStartPlace")
        self.textAddEndPLace = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddEndPLace.setGeometry(QtCore.QRect(50, 240, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddEndPLace.setFont(font)
        self.textAddEndPLace.setObjectName("textAddEndPLace")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно создания заказа"))
        self.labelEditOrderWindow.setText(_translate("MainWindow", "Окно создания заказа"))
        self.ExitButton.setText(_translate("MainWindow", "Выйти"))
        self.AddButton.setText(_translate("MainWindow", "Создать"))
        self.textAddPrice.setPlaceholderText(_translate("MainWindow", "Введите цену"))
        self.labelOrderAdd.setText(_translate("MainWindow", "Добавить Заказ"))
        self.textAddStartPlace.setPlaceholderText(_translate("MainWindow", "Начальное место"))
        self.textAddEndPLace.setPlaceholderText(_translate("MainWindow", "Конечное место"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
