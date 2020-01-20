"""This is the Battleships Game by Nico Hübsch"""


class Ship:

    def _init_(self, ship_type: type(str), ship_alignment: type(str), ship_position: type(tuple)):
        self._ship_alignment = ship_alignment
        self._ship_position = ship_position
        self._ship_type = ship_type

        self._all_ship_coordinates = []
        self._all_blocking_coordinates = []

        ship_name_dict = self._get_name_dict_local_language()

        self._ship_type_full = ship_name_dict[ship_type][0]
        self._ship_life_amount, self._ship_length = ship_name_dict[ship_type][1]

    @staticmethod
    def _get_name_dict_local_language() -> dict:
        """
        Gets a Name dict for translation purpose...
        @return: Ship Name, Length Dict
        """
        import locale
        locale.setlocale(locale.LC_ALL, "")
        system_language = locale.getlocale()[0]

        ship_name_dict_en = {
            "C": ("Carrier", 5),
            "B": ("Battleship", 4),
            "D": ("Destroyer", 3),
            "S": ("Submarine", 2)
        }

        # noinspection SpellCheckingInspection
        ship_name_dict_de = {
            "C": "Träger",
            "B": "Schlachtschiff",
            "D": "Zerstörer",
            "S": "U-Boot"
        }
        # noinspectionend SpellCheckingInspection

        ship_length_dict = {
            "C": 5,  # Carrier
            "B": 4,  # Battleship
            "D": 3,  # Destroyer
            "S": 2  # Submarine
        }

        if system_language == "de_DE":
            ship_name_dict = ship_name_dict_de
        else:
            ship_name_dict = ship_name_dict_en

        ship_name_dict = {"C": (ship_name_dict["C"], ship_length_dict["C"]),
                          "B": (ship_name_dict["B"], ship_length_dict["B"]),
                          "D": (ship_name_dict["D"], ship_length_dict["D"]),
                          "S": (ship_name_dict["S"], ship_length_dict["S"])}

        return ship_name_dict


class Fleet:
    pass


class Playfield:
    pass


class Player:
    pass


class _Testing:
    pass


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MasterUi(QMainWindow):
    def __init__(self):
        super(MasterUi, self).__init__()
        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle("Battleship Game")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(60, 60)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click mich!")
        self.b1.move(60, 30)
        self.b1.clicked.connect(self.clicked)


    def clicked(self):
        self.label.setText("du hast den Knopf gedrückt")
        self.update()


    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MasterUi()
    win.show()
    sys.exit(app.exec_())

window()
