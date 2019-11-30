"""Fleet_Maneuver_Game Module"""
import Coordinate
from Fleet import Fleet
from Player import Player
from Playfield import Playfield
import View_Master_UI

#   import numpy


board_size = Coordinate.Coordinate
board_size.x = 10
board_size.y = 10
fleet_class = Fleet()
TestFleet_Test = fleet_class.create_fleet(board_size, 4468415)
print("Test")

TestShip = TestFleet_Test[1]
TestShip_Type = TestShip.get_ship_type()
print(TestShip_Type)

Player_1 = Player(board_size, 1)
Player_2 = Player(board_size, 2)

TestPlayfield = Playfield(board_size)

TestValue = TestPlayfield.get_position_value(board_size)
print("Test 1:" + TestValue)

status = "ship"
board_size.x, board_size.y = 4, 5
TestPlayfield.set_position_value(board_size, status)

status = "water"
board_size.x = 2
board_size.y = 3
TestPlayfield.set_position_value(board_size, status)

board_size.x = 9
TestValue = TestPlayfield.get_position_value(board_size)
print("Test 2:" + TestValue)

TestPlayfield.draw_playfield()
TestPlayfield.draw_playfield_2()

UI_TEST = View_Master_UI.View()

input("Press enter to exit !")


class FleetManeuverGame:

    def __init__(self):
        """"""
        """Test for Home"""
