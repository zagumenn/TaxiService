

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
        self.labelMainWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelMainWindow.setGeometry(QtCore.QRect(360, 10, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelMainWindow.setFont(font)
        self.labelMainWindow.setStyleSheet("background-color: rgb(255, 172, 0);")
        self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMainWindow.setObjectName("labelMainWindow")
        self.ButtonReg = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonReg.setGeometry(QtCore.QRect(340, 210, 101, 26))
        self.ButtonReg.setObjectName("ButtonReg")
        self.ButtonAuth = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAuth.setGeometry(QtCore.QRect(450, 210, 101, 26))
        self.ButtonAuth.setObjectName("ButtonAuth")
        self.textLogin = QtWidgets.QTextEdit(self.centralwidget)
        self.textLogin.setGeometry(QtCore.QRect(280, 90, 131, 31))
        self.textLogin.setObjectName("textLogin")
        self.textPassword = QtWidgets.QTextEdit(self.centralwidget)
        self.textPassword.setGeometry(QtCore.QRect(280, 140, 131, 31))
        self.textPassword.setObjectName("textPassword")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))
        self.labelMainWindow.setText(_translate("MainWindow", "Добро пожаловать в приложение \"Служба такси\""))
        self.ButtonReg.setText(_translate("MainWindow", "Регистрация"))
        self.ButtonAuth.setText(_translate("MainWindow", "Авторизация"))
        self.textLogin.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.textPassword.setPlaceholderText(_translate("MainWindow", "Введите пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




