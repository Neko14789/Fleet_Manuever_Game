class Player:
    Player_Count = 0

    def __init__(self, board_size, fleet_seed, player_name="Undefined"):
        import Fleet
#       import Coordinate

        Player.Player_Count += 1
        fleet_class = Fleet.Fleet()
        if not player_name == "Undefined":
            self.__player_name = player_name
        else:
            self.__player_name = player_name + " " + format(self.Player_Count)
        self.__Fleet = fleet_class.create_fleet(board_size, fleet_seed)
