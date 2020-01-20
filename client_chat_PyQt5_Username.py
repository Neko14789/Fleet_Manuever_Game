# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Neko\PycharmProjects\Fleet_Manuever_Game\client - chat PyQt5 - Username.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from client_chat_PyQt5_Chat import Ui_ChatWindow

class Ui_LoginWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self.window)
        self.ui.setup()
        LoginWindow.hide()
        self.window.show()

        my_username = self.lineEdit.text()
        # print(my_username)
        self.ui.setUsername(my_username)



    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(373, 113)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")


        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def setup(self):
        self.pushButton.clicked.connect(self.openWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Nicochat - Set User Name"))
        self.label.setText(_translate("LoginWindow", "Set your Username"))
        self.lineEdit.setPlaceholderText(_translate("LoginWindow", "Put your Username here"))
        self.pushButton.setToolTip(_translate("LoginWindow", "You can also just press the ENTER key on your Keyboard"))
        self.pushButton.setText(_translate("LoginWindow", "Send"))
        self.pushButton.setShortcut(_translate("LoginWindow", "Return"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    ui.setup()
    LoginWindow.show()

    #import multiprocessing

    # from PyQt5.QtCore import QThread, pyqtSignal
    # class Network_Server(QThread):
    #     count_value = pyqtSignal(int)
    #     def run(self, connected=False):
    #         import time
    #         count = 1
    #         while True:
    #             print("alive " + str(count))
    #             count += 1
    #             time.sleep(1)
    #             #self.count_value.emit(int)


        #thread = Network_Server()
    #thread.finished.connect(app.exit)
        #thread.start()
    #CTS = Network_Server()
    #CTS.ConnectToServer()
    #CTS = multiprocessing.Process(target=ConnectToServer)
    #CTS.start()

    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook

    sys.exit(app.exec_())
