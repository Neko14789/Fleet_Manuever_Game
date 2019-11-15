class Player:
    Player_Count = 0
    def __init__(self, board_size, fleet_seed, player_name="Undifined"):
        import Fleet
        import Coordinate

        Player.Player_Count += 1
        fleetclass = Fleet.Fleet()
        if not player_name == "Undifined":
            self.__player_name = player_name
        else:
            self.__player_name = player_name + " " + format(self.Player_Count)
        self.__Fleet = fleetclass.create_fleet(board_size, fleet_seed)
