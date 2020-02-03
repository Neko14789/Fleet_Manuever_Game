"""This is the Battleships Game by Nico Hübsch"""


class Ship:

    def __init__(self, ship_type: type(str), ship_alignment: type(str), ship_position: type(tuple)):
        self._ship_alignment = ship_alignment
        self._ship_position = ship_position
        self._ship_type = ship_type

        self._all_ship_coordinates = []
        self._all_blocking_coordinates = []

        ship_name_dict = self._get_name_dict_local_language()

        self._ship_type_full = ship_name_dict[ship_type][0]
        self._ship_length = ship_name_dict[ship_type][1]
        self._ship_life_amount = self._ship_length

        self._create_ship_part_coordinates(self._ship_alignment, self._ship_position)

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
            "c": ("Carrier", 5),
            "b": ("Battleship", 4),
            "d": ("Destroyer", 3),
            "s": ("Submarine", 2)
        }

        # noinspection SpellCheckingInspection
        ship_name_dict_de = {
            "c": "Träger",
            "b": "Schlachtschiff",
            "d": "Zerstörer",
            "s": "U-Boot"
        }
        # noinspectionend SpellCheckingInspection

        ship_length_dict = {
            "c": 5,  # Carrier
            "b": 4,  # Battleship
            "d": 3,  # Destroyer
            "s": 2  # Submarine
        }

        if system_language == "de_DE":
            ship_name_dict = ship_name_dict_de
        else:
            ship_name_dict = ship_name_dict_en

        ship_name_dict = {"c": (ship_name_dict["c"], ship_length_dict["c"]),
                          "b": (ship_name_dict["b"], ship_length_dict["b"]),
                          "d": (ship_name_dict["d"], ship_length_dict["d"]),
                          "s": (ship_name_dict["s"], ship_length_dict["s"])}

        return ship_name_dict

    @staticmethod
    def _create_ship_part_coordinates(ship_alignment: type(str), ship_position: type(tuple)):

        ship_part_coordinates = []
        status = "alive"
        coordinate = (ship_position, status)
        ship_part_coordinates.append(coordinate)
        print("test")

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


# def window():
#     app = QApplication(sys.argv)
#     win = MasterUi()
#     win.show()
#     sys.exit(app.exec_())
#
# window()

newShip = Ship("c", "h", (2, 6))
print("test")
