"""This is the Battleships Game by Nico Hübsch"""



class Coordinate:
    """"Coordinate Object Structure"""

    def __init__(self, x: type(int), y: type(int)):
        """
        Coordinate Object with x and y value, default (0, 0)

        @param x: X position
        @param y: Y position
        """

        self.x = x
        self.y = y


class Ship:
    """
    A Ship for the Battleships Game
    """
    def __init__(self, ship_type: type(str), ship_alignment: type(str), ship_position: type(Coordinate)):
        self.ship_alignment = ship_alignment
        self.ship_position = ship_position
        self.ship_type = ship_type

        self.all_ship_coordinates = []
        self.all_blocking_coordinates = []

        ship_name_dict = self._get_ship_name_dict_local_language()

        self.ship_type_full = ship_name_dict[ship_type][0]
        self.ship_length = ship_name_dict[ship_type][1]
        self.ship_life_amount = self.ship_length

        self.all_ship_coordinates = self.create_ship_part_coordinates(self.ship_alignment, self.ship_position,
                                                                      self.ship_length)
        self.all_blocking_coordinates = self.create_ship_blocking_coordinates(self.ship_alignment, self.ship_position,
                                                                              self.ship_length)

    @staticmethod
    def create_ship_part_coordinates(ship_alignment: type(str), ship_position: type(Coordinate), ship_length: type(int)) -> list:
        """
        creates a list of coordinates of ship
        @param ship_alignment:
        @param ship_position:
        @param ship_length:
        @return: coordinates list
        """
        ship_part_coordinates = []
        for _ in range(ship_length):
            if ship_alignment == "h":

                x = ship_position.x + _
                y = ship_position.y

            elif ship_alignment == "v":
                x = ship_position.x
                y = ship_position.y + _

            else:
                raise ValueError(f"ship_alignment can only be 'h' or 'v', not '{ship_alignment}'")

            coordinate = Coordinate(x, y)

            ship_part_coordinates.append(coordinate)

        return ship_part_coordinates

    @staticmethod
    def create_ship_blocking_coordinates(ship_alignment: type(str), ship_position: type(Coordinate), ship_length: type(int)) -> list:
        """
        creates a list of coordinates that the ship is blocking
        @param ship_alignment:
        @param ship_position:
        @param ship_length:
        @return: coordinates list
        """
        ship_blocking_coordinates = []
        for width in range(-1, 2):
            for _ in range(-1, ship_length + 1):
                if ship_alignment == "h":

                    x = ship_position.x + _
                    y = ship_position.y + width

                elif ship_alignment == "v":
                    x = ship_position.x + width
                    y = ship_position.y + _

                else:
                    raise ValueError(f"ship_alignment can only be 'h' or 'v', not {ship_alignment}")

                coordinate = Coordinate(x, y)

                ship_blocking_coordinates.append(coordinate)

        return ship_blocking_coordinates

    def is_alive(self) -> bool:
        """
        Checks if the Ship is still alive
        @return: True = Ship still alive, False = Ship dead
        """

        if self.ship_life_amount > 0:
            is_alive = True
        else:
            is_alive = False
        return is_alive

    def was_hit(self, hit_position: type(Coordinate), reduce_life: type(bool) = True) -> bool:
        """

        @param hit_position:
        @param reduce_life: choose if running this method should reduce ship life by 1
        """
        for asc in self.all_ship_coordinates:
            if asc.x == hit_position.x and asc.y == hit_position.y:
                if reduce_life:
                    self.ship_life_amount -= 1
                return True
        return False

    @staticmethod
    def _get_ship_name_dict_local_language() -> dict:
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

    def __str__(self):
        return(f"Ship Object:\n"
               f"\t Type: {self.ship_type} ({self.ship_type_full})\n"
               f"\t Position: {self.ship_position.x, self.ship_position.y}\n"
               f"\t Length: {self.ship_length}\n"
               f"\t Alignment: {self.ship_alignment}\n"
               f"\t Is Alive ?: {self.is_alive()}")


class Fleet:
    """
    A Fleet, Collection of Ships
    """
    def __init__(self, board_size: type(Coordinate), fleet_seed: type(int)):
        """
        Creates a Fleet of 10 Ships of varying Type
        :param board_size: Size of the Playfield
        :param fleet_seed: Seed that defines the Fleet placement
        """
        ship_type_length_dict = Ship._get_ship_name_dict_local_language()
        #        (Type, Amount)
        ships = [("c", 1), ("b", 2), ("d", 3), ("s", 4)]
        # s_type, s_alignment, s_position = ships[s_number][0]
        import random
        random.seed(fleet_seed)
        self.ship_list = []
        for ship in ships:
            for _ in range(ship[1]):
                while True:
                    s_type = ship[0]
                    s_alignment = random.choice(["h", "v"])
                    if s_alignment == "h":
                        s_position = Coordinate(random.randint(0, board_size.x-ship_type_length_dict[s_type][1]), random.randint(0,  board_size.y))
                    else:  # if s_alignment == "v":
                        s_position = Coordinate(random.randint(0, board_size.x), random.randint(0, board_size.y - ship_type_length_dict[s_type][1]))
                    current_ship = Ship(s_type, s_alignment, s_position)

                    if not self.check_collision(current_ship):
                        self.ship_list.append(current_ship)
                        break
        pass

    def check_collision(self, current_ship: type(Ship)):
        for test_ship in self.ship_list:
            for cs_abc in current_ship.all_blocking_coordinates:
                for ts_asc in test_ship.all_ship_coordinates:
                    if cs_abc.x == ts_asc.x and cs_abc.y == ts_asc.y:
                        return True
        return False



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
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MasterUi()
    win.show()
    sys.exit(app.exec_())

window()

newShip = Ship("c", "h", Coordinate(2, 4))
print(newShip)
print(f"Hit ? {newShip.was_hit(Coordinate(5, 4), False)}")
Fleet = Fleet(Coordinate(9, 9), 1321)
