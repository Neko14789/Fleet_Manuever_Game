"""Ship Module"""
from Coordinate import Coordinate


class Ship:
    """Class for the Ship of a Fleet in the Fleet Maneuver Game"""

    def __init__(self, ship_type: type(str), ship_alignment: type(str), ship_position: type(Coordinate)):
        """
        Creates a Ship.
        @param ship_type: "C": ("Carrier"), "B": ("Battleship"), "D": ("Destroyer"), "S": ("Submarine")
        @param ship_alignment: H = Horizontal, V = Vertical
        """

        from Coordinate import Coordinate

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
                x = ship_position.x
                y = ship_position.y + counter_ship_length

            current_coordinate_position = Coordinate(x, y)
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
                    current_blocking_coordinate_position = Coordinate(x, y)
                    self._all_blocking_coordinates.append(current_blocking_coordinate_position)

            else:
                for n in range(-1, 2):
                    x = ship_position.y - 1 + counter_ship_bounds_length
                    y = ship_position.x + n
                    current_blocking_coordinate_position = Coordinate(x, y)
                    self._all_blocking_coordinates.append(current_blocking_coordinate_position)


            counter_ship_bounds_length -= 1
            times -= 1

    def is_alive(self) -> bool:
        """
        Checks if the Ship is still alive
        @return: True = Ship still alive, False = Ship dead
        """

        if self._ship_life_amount > 0:
            is_alive = True
        else:
            is_alive = False
        return is_alive

    def was_hit(self, hit_position: type(Coordinate)) -> bool:
        """
        Checks if the Ship was hit
        @param hit_position: Hit Coordinate
        @return: True = Ship got hit, False = Ship was not hit
        """

        hit = False
        for x in self._all_ship_coordinates:
            if x.x == hit_position.x and x.y == hit_position.y:
                hit = True
                self._ship_life_amount -= 1
        return hit

    def get_all_ship_coordinates(self) -> list:
        """
        Outputs all Coordinates of the Ship
        @return: All Ship Coordinates
        """
        return self._all_ship_coordinates

    def get_all_blocking_coordinates(self) -> list:
        """
        Outputs all blocking Coordinates of the Ship
        @return: All blocking Ship Coordinates
        """
        return self._all_blocking_coordinates

    def get_ship_type(self) -> tuple:
        """
        Outputs the Type of the Ship
        @return: Ship Type, Ship Type Full
        """

        return self._ship_type, self._ship_type_full

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
            "C": 5,
            "B": 4,
            "D": 3,
            "S": 2
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
