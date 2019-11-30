"""Player Module"""


class Player:
    """
    Player Class
    """
    Player_Count = 0

    def __init__(self, board_size, fleet_seed, player_name="Undefined"):
        """
        Creates a Player with a Fleet of 10 Ships of varying Type

        Parameters:
            board_size (Coordinate.py.Coordinate): Size of the Playfield
            fleet_seed (int): Seed that defines the Fleet placement
            player_name (str): Name of the Player
        """
        from Fleet import Fleet
#       from Coordinate import Coordinate

        Player.Player_Count += 1
        fleet_class = Fleet()
        if not player_name == "Undefined":
            self.__player_name = player_name
        else:
            self.__player_name = player_name + " " + format(self.Player_Count)
        self.__Fleet = fleet_class.create_fleet(board_size, fleet_seed)
