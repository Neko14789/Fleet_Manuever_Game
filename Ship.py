"""Ship Module"""


class Ship:
    """Class for the Ship of a Fleet in the Fleet Maneuver Game"""

    def __init__(self, ship_type, ship_alignment, ship_position):
        """
        Creates a Ship.

        Parameters:
            ship_type (str): "C": ("Carrier"), "B": ("Battleship"), "D": ("Destroyer"), "S": ("Submarine")
            ship_alignment (str): H = Horizontal, V = Vertical
            ship_position (Coordinate.py.Coordinate) = Position of the Ship
        """
        import Coordinate

        ship_name_dict = self._get_name_dict_local_language()

        ship_type_full = ship_name_dict[ship_type][0]
        ship_life_amount = ship_name_dict[ship_type][1]

        ship_length = ship_life_amount
        #       Update Global Variables
        self._ship_alignment = ship_alignment
        self._ship_position = ship_position
        self._ship_type = ship_type
        self._ship_type_full = ship_type_full
        self._ship_length = ship_length
        self._ship_life_amount = ship_life_amount
        self._all_ship_coordinates = []
        self._all_blocking_coordinates = []
        #       Update Global Variables

        counter_ship_length = ship_length - 1

        times = ship_length
        #       Make List of Ship Coordinates
        while times > 0:
            if ship_alignment == 'H':
                x = ship_position.x + counter_ship_length
                y = ship_position.y

            else:
                x = ship_position.x + counter_ship_length
                y = ship_position.y

            current_coordinate_position = Coordinate.Coordinate(x, y)
            counter_ship_length -= 1
            self._all_ship_coordinates.append(current_coordinate_position)

            times -= 1

        counter_ship_bounds_length = ship_length - 1 + 2

        times = ship_length + 2
        #       Make List of Ship Blocking Coordinates (Ship Coordinates + 1 Border in every direction)
        while times > 0:
            if ship_alignment == 'H':

                for n in range(-1, 2):
                    x = ship_position.x - 1 + counter_ship_bounds_length
                    y = ship_position.y + n
                    current_blocking_coordinate_position = Coordinate.Coordinate(x, y)
                    self._all_blocking_coordinates.append(current_blocking_coordinate_position)

            else:
                for n in range(-1, 2):
                    x = ship_position.y - 1 + counter_ship_bounds_length
                    y = ship_position.x + n
                    current_blocking_coordinate_position = Coordinate.Coordinate(x, y)
                    self._all_blocking_coordinates.append(current_blocking_coordinate_position)

            counter_ship_bounds_length -= 1
            times -= 1

    def is_alive(self):
        """Checks if the Ship is still alive"""
        if self._ship_life_amount > 0:
            is_alive = True
        else:
            is_alive = False
        return is_alive

    def was_hit(self, hit_position):
        """Checks if the Ship was hit"""
        hit = False
        for x in self._all_ship_coordinates:
            if x == hit_position:
                hit = True
                self._ship_life_amount -= 1
        return hit

    def get_all_ship_coordinates(self):
        """Outputs all Coordinates of the Ship"""
        return self._all_ship_coordinates

    def get_all_blocking_coordinates(self):
        """Outputs all blocking Coordinates of the Ship"""
        return self._all_blocking_coordinates

    def get_ship_type(self):
        """Outputs the Type of the Ship"""
        return self._ship_type, self._ship_type_full

    @staticmethod
    def _get_name_dict_local_language():
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
            "C": ("Träger", 5),
            "B": ("Schlachtschiff", 4),
            "D": ("Zerstörer", 3),
            "S": ("U-Boot", 2)
        }
        if system_language == "de_DE":
            ship_name_dict = ship_name_dict_de
        else:
            ship_name_dict = ship_name_dict_en

        return ship_name_dict
