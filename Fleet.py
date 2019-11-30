"""Fleet Module"""
import Ship


class Fleet:
    """Class for the Fleet in the Fleet Maneuver Game"""

    def create_fleet(self, board_size, fleet_seed=type(int)):
        """
        Creates a Fleet of 10 Ships of varying Type and returns the Fleet

        Parameters:
            board_size (Coordinate.py.Coordinate): Size of the Playfield
            fleet_seed (int): Seed that defines the Fleet placement

        Returns:
            list: List of Ship.py.Ship Objects
        """
        import random
        import Coordinate

        random.seed(fleet_seed)

        ship_type_length_dict = {
            1: ("C", 5),
            2: ("B", 4),
            4: ("D", 3),
            7: ("S", 2),
        }

        ship_amount_in_fleet = 0
        while not ship_amount_in_fleet == 10:
            ship_amount_in_fleet = 0
            counter = 1
            fleet = []
            impossible_counter = 0
            while counter <= 10:
                create_current_ship = False

                while not create_current_ship:
                    try:
                        current_ship_type = ship_type_length_dict[counter][0]
                        current_ship_length = ship_type_length_dict[counter][1]
                    except KeyError:
                        ""
                    current_ship_alignment_number = random.randrange(0, 2)

                    if current_ship_alignment_number == 0:
                        current_ship_alignment = "H"
                    else:
                        current_ship_alignment = "V"
                    "Decides if the ship is horizontal or vertical"

                    if current_ship_alignment == "H":
                        x = random.randrange(0, board_size.x - current_ship_length + 1)  # BS10 - CSL2 + 1 + 1
                        y = random.randrange(0, 10)
                    else:
                        x = random.randrange(0, 10)
                        y = random.randrange(0, board_size.y - current_ship_length + 1)

                    tmp_pos = Coordinate.Coordinate(x, y)
                    current_ship = Ship.Ship(current_ship_type, current_ship_alignment, tmp_pos)

                    create_current_ship = True
                    for test_ship in fleet:
                        create_current_ship = self.rules_placement_ok(current_ship, test_ship)
                        if not create_current_ship:
                            break

                    if create_current_ship:
                        fleet.append(current_ship)
                        ship_amount_in_fleet += 1

                    impossible_counter += 1
                    if impossible_counter == 100:
                        break

                if impossible_counter == 100:
                    break

                counter += 1

            if ship_amount_in_fleet == 10:
                break

        # noinspection PyUnboundLocalVariable
        return fleet

    @staticmethod
    def rules_placement_ok(current_ship=type(Ship), test_ship=type(Ship)):
        """
        Checks if the two given ships positions don't touch each other in 1 unit radius

        Parameters:
            current_ship (Ship.py.Ship): 1st Ship
            test_ship (Ship.py.Ship): 2nd Ship

        Returns:
            boolean: True = No Overlap etc. False = Overlap etc.
        """
        placement_ok = True
        for current_ship_position in current_ship.get_all_blocking_coordinates():
            for test_ship_position in test_ship.get_all_ship_coordinates():
                if current_ship_position.x == test_ship_position.x and current_ship_position.y == test_ship_position.y:
                    placement_ok = False
                    break
            if not placement_ok:
                break
        return placement_ok
