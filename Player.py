"""Player Module"""
from Coordinate import Coordinate


class Player:
    """
    Player Class
    """
    Player_Count = 0

    def __init__(self, board_size: type(Coordinate), fleet_seed: type(int), player_name: type(str) = "Undefined"):

        from Fleet import Fleet

        Player.Player_Count += 1
        fleet_class = Fleet()
        if not player_name == "Undefined":
            self.__player_name = player_name
        else:
            self.__player_name = player_name + " " + format(self.Player_Count)
        self.__Fleet = fleet_class.create_fleet(board_size, fleet_seed)
