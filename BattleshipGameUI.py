# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Neko\PycharmProjects\Fleet_Manuever_Game\BattleshipGameUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainUIWindow(object):
    def setupUi(self, MainUIWindow):
        MainUIWindow.setObjectName("MainUIWindow")
        MainUIWindow.setWindowModality(QtCore.Qt.NonModal)
        MainUIWindow.setEnabled(True)
        MainUIWindow.resize(1201, 1000)
        self.widget = QtWidgets.QWidget(MainUIWindow)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 2, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.treeWidgetFleetP2 = QtWidgets.QTreeWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidgetFleetP2.sizePolicy().hasHeightForWidth())
        self.treeWidgetFleetP2.setSizePolicy(sizePolicy)
        self.treeWidgetFleetP2.setObjectName("treeWidgetFleetP2")
        self.gridLayout.addWidget(self.treeWidgetFleetP2, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem9, 4, 3, 1, 1)
        self.treeWidgetFleetP1 = QtWidgets.QTreeWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidgetFleetP1.sizePolicy().hasHeightForWidth())
        self.treeWidgetFleetP1.setSizePolicy(sizePolicy)
        self.treeWidgetFleetP1.setObjectName("treeWidgetFleetP1")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetFleetP1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetFleetP1)
        self.gridLayout.addWidget(self.treeWidgetFleetP1, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem10, 4, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem11, 0, 1, 1, 1)
        self.groupBoxPlayfieldP2 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPlayfieldP2.sizePolicy().hasHeightForWidth())
        self.groupBoxPlayfieldP2.setSizePolicy(sizePolicy)
        self.groupBoxPlayfieldP2.setObjectName("groupBoxPlayfieldP2")
        self.gridLayout.addWidget(self.groupBoxPlayfieldP2, 3, 1, 1, 1)


        # class toolButton(QtWidgets.QGroupBox):
        #     def __init__(self,parent=None):
        #         QtWidgets.QToolButton.__init__(self,parent)
        #         policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Preferred)
        #         policy.setHeightForWidth(True)
        #         self.setSizePolicy(policy)
        #
        #     def heightForWidth(self,width):
        #         return width


        self.groupBoxPlayfieldP1 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPlayfieldP1.sizePolicy().hasHeightForWidth())
        self.groupBoxPlayfieldP1.setSizePolicy(sizePolicy)
        self.groupBoxPlayfieldP1.setObjectName("groupBoxPlayfieldP1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxPlayfieldP1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridLayout_2.setSpacing(1)

        class PushButton(QtWidgets.QPushButton):
            def __init__(self,parent=None):
                QtWidgets.QToolButton.__init__(self,parent)
                policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Preferred)
                policy.setHeightForWidth(True)
                self.setSizePolicy(policy)

            def heightForWidth(self,width):
                return width


        self.buttons = {}
        for x in range(10):
            for y in range(10):


                self.PushButton = PushButton(self.groupBoxPlayfieldP1)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.PushButton.sizePolicy().hasHeightForWidth())
                self.PushButton.setSizePolicy(sizePolicy)
                self.PushButton.setObjectName(f"PushButton_{x}_{y}")
                self.PushButton.setText(f"PushButton_{x}_{y}")
                self.PushButton.setMinimumSize(10, 10)

                self.PushButton.clicked.connect(self.make_ButtonClicked(x, y))

                self.buttons[(x, y)] = self.PushButton

                self.gridLayout_2.addWidget(self.buttons[(x, y)], y, x, 1, 1)


        self.gridLayout.addWidget(self.groupBoxPlayfieldP1, 1, 1, 1, 1)
        MainUIWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainUIWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 21))
        self.menubar.setObjectName("menubar")
        self.menuJoin_Game = QtWidgets.QMenu(self.menubar)
        self.menuJoin_Game.setObjectName("menuJoin_Game")
        self.menuHost_Game = QtWidgets.QMenu(self.menubar)
        self.menuHost_Game.setObjectName("menuHost_Game")
        self.menuQuit_Game = QtWidgets.QMenu(self.menubar)
        self.menuQuit_Game.setObjectName("menuQuit_Game")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainUIWindow.setMenuBar(self.menubar)
        self.actionChange_Playfield_Size = QtWidgets.QAction(MainUIWindow)
        self.actionChange_Playfield_Size.setObjectName("actionChange_Playfield_Size")
        self.actionInfo = QtWidgets.QAction(MainUIWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuSettings.addAction(self.actionChange_Playfield_Size)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuJoin_Game.menuAction())
        self.menubar.addAction(self.menuHost_Game.menuAction())
        self.menubar.addAction(self.menuQuit_Game.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainUIWindow)
        QtCore.QMetaObject.connectSlotsByName(MainUIWindow)

    def make_ButtonClicked(self,x,y):
        def ButtonClicked():
            print(f"debug_{x},{y}")
            self.buttons[(x, y)].setDisabled(True)

        return ButtonClicked

    def retranslateUi(self, MainUIWindow):
        _translate = QtCore.QCoreApplication.translate
        MainUIWindow.setWindowTitle(_translate("MainUIWindow", "Nico\'s Fleet Manuever Game!"))
        self.treeWidgetFleetP2.headerItem().setText(0, _translate("MainUIWindow", "Ship"))
        self.treeWidgetFleetP2.headerItem().setText(1, _translate("MainUIWindow", "Status"))
        self.treeWidgetFleetP1.headerItem().setText(0, _translate("MainUIWindow", "Ship"))
        self.treeWidgetFleetP1.headerItem().setText(1, _translate("MainUIWindow", "Status"))
        __sortingEnabled = self.treeWidgetFleetP1.isSortingEnabled()
        self.treeWidgetFleetP1.setSortingEnabled(False)
        self.treeWidgetFleetP1.topLevelItem(0).setText(0, _translate("MainUIWindow", "Destroyer_1"))
        self.treeWidgetFleetP1.topLevelItem(0).setText(1, _translate("MainUIWindow", "Alive"))
        self.treeWidgetFleetP1.topLevelItem(1).setText(0, _translate("MainUIWindow", "Destroyer_2"))
        self.treeWidgetFleetP1.topLevelItem(1).setText(1, _translate("MainUIWindow", "Alive"))
        self.treeWidgetFleetP1.setSortingEnabled(__sortingEnabled)
        self.groupBoxPlayfieldP2.setTitle(_translate("MainUIWindow", "GroupBox"))
        self.groupBoxPlayfieldP1.setTitle(_translate("MainUIWindow", "GroupBox"))

        #self.toolButton.setText(_translate("MainUIWindow", "..."))
        self.menuJoin_Game.setTitle(_translate("MainUIWindow", "Join Game"))
        self.menuHost_Game.setTitle(_translate("MainUIWindow", "Host Game"))
        self.menuQuit_Game.setTitle(_translate("MainUIWindow", "Quit Game"))
        self.menuSettings.setTitle(_translate("MainUIWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainUIWindow", "Help"))
        self.actionChange_Playfield_Size.setText(_translate("MainUIWindow", "Change Playfield Size"))
        self.actionInfo.setText(_translate("MainUIWindow", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainUIWindow = QtWidgets.QMainWindow()
    ui = Ui_MainUIWindow()
    ui.setupUi(MainUIWindow)
    MainUIWindow.show()
    sys.exit(app.exec_())
