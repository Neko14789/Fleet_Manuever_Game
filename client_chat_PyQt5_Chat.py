# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Neko\PycharmProjects\Fleet_Manuever_Game\client - chat PyQt5.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import socket, errno


class Ui_ChatWindow(object):

    def setUsername(self, my_username):
        self.username = my_username
        self.groupBox.setTitle(f"Chat: logged in as <{my_username}>")
        self.setupConnection(my_username)


    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(920, 725)
        self.centralwidget = QtWidgets.QWidget(ChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        ChatWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def setup(self):
        self.pushButton.clicked.connect(self.sendMessage)

    def setupConnection(self, my_User_Name="NO_USERNAME"):

        class Network_Server(QThread):
            changeMessage = pyqtSignal(str)

            HEADER_LENGTH = 10
            IP = socket.gethostbyname('nico14789.ddns.net')
            PORT = 4230


            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((IP, PORT))
            client_socket.setblocking(False)

            username = my_User_Name.encode("utf-8")
            username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
            client_socket.send(username_header + username)

            def run(self):
                while True:
                    self.Multiplayer_Update()

            def Multiplayer_Update(self, message=""):

                def update_message_box(UName, Mg):
                    from datetime import datetime
                    try:
                        Mg = str(Mg, 'utf-8')
                    except:
                        pass

                    try:
                        UName = str(UName, 'utf-8')
                    except:
                        pass


                    # message_box.configure(state=NORMAL)
                    # message_box.insert(END, "\n" + "<" + datetime.now().strftime(
                    #     '%Y-%m-%d %H:%M:%S') + ">-<" + UName + ">: " + Mg + "\n")
                    # message_box.see(END)
                    # message_box.configure(state=DISABLED)
                    #global changeMessage
                    new_message = ("<" + datetime.now().strftime(
                         '%Y-%m-%d %H:%M:%S') + ">-<" + UName + ">: " + Mg)
                    self.changeMessage.emit(new_message)


                if message:
                    message = message.encode("utf-8")
                    message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode("utf-8")
                    self.client_socket.send(message_header + message)

                    # message_box.insert(END, f"<{my_User_Name}>: {message}")
                    # b" {message} ".decode("utf-8")

                    update_message_box(my_User_Name, message)

                try:
                    while True:
                        # receive things
                        username_header = self.client_socket.recv(self.HEADER_LENGTH)
                        if not len(username_header):
                            print("connection closed by the server")
                            sys.exit()
                        username_length = int(username_header.decode("utf-8").strip())
                        username = self.client_socket.recv(username_length).decode("utf-8")

                        message_header = self.client_socket.recv(self.HEADER_LENGTH)
                        message_length = int(message_header.decode("utf-8").strip())
                        message = self.client_socket.recv(message_length).decode("utf-8")

                        # print(f"{username} > {message}")

                        # message_box.insert(END,f"\n<{username}>: {message}\n")

                        update_message_box(username, message)


                except IOError as e:
                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                        print("Reading error", str(e))
                        sys.exit()

                    import time
                    #time.sleep(1)


                except Exception as e:
                    print("General error", str(e))
                    sys.exit()
                    #self.count_value.emit(int)

        self.Network_Server_Thread = Network_Server()
        self.Network_Server_Thread.changeMessage.connect(self.newMessageChange)
        self.Network_Server_Thread.start()



    def sendMessage(self):

        message = self.textEdit.toPlainText()

        self.Network_Server_Thread.Multiplayer_Update(message)

    def newMessageChange(self, newMessage):
        self.textBrowser.append(newMessage)





    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "Nicochat - Lets Chat"))
        self.groupBox.setTitle(_translate("ChatWindow", "Chat: logged in as <PLACEHOLDER>"))
        self.textEdit.setPlaceholderText(_translate("ChatWindow", "Here goes your Message that you want to Send"))
        self.pushButton.setToolTip(_translate("ChatWindow", "You can also just press the ENTER key on your Keyboard"))
        self.pushButton.setText(_translate("ChatWindow", "Send"))
        self.pushButton.setShortcut(_translate("ChatWindow", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatWindow = QtWidgets.QMainWindow()
    ui = Ui_ChatWindow()
    ui.setupUi(ChatWindow)
    ui.setup()
    ChatWindow.show()



    sys.exit(app.exec_())

