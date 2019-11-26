import Coordinate
import Fleet
import Player
import Playfield

#   import numpy

board_size = Coordinate.Coordinate
board_size.x = 10
board_size.y = 10
fleet_class = Fleet.Fleet()
TestFleet_Test = fleet_class.create_fleet(board_size, 4468415)
print("Test")

TestShip = TestFleet_Test[1]
TestShip_Type = TestShip.get_ship_type()
print(TestShip_Type)


Player_1 = Player.Player(board_size, 1)
Player_2 = Player.Player(board_size, 2)


TestPlayfield = Playfield.Playfield(board_size)

TestValue = TestPlayfield.get_position_value(board_size)
print(TestValue)

status = "ship"
TestPlayfield.set_position_value(board_size, status)

status = "water"
board_size.x = 2
TestPlayfield.set_position_value(board_size, status)

board_size.x = 9
TestValue = TestPlayfield.get_position_value(board_size)
print(TestValue)

TestPlayfield.draw_playfield()
TestPlayfield.draw_playfield_2()

from tkinter import *

root = Tk()
root.title("Schiffe Versenken")
root.resizable(False,False)

root.update()


def test(x, y, b, buttonID):
    childes=root.children
    print("hi", x, y, b)
    x = "!button" + format(buttonID)
    root.children[x].configure(bg="blue")
    print(x in childes)


height = 20
width = 20
cells = {}
timer = ""
for i in range(height): #Rows
    for j in range(width): #Columns
        k = (j, i)
        b = Button(root, text="□■~", width=3, height=1, command=lambda y=j, x=i, xy=k, timer_=timer: test(y, x, xy, timer_))
        if timer == "":
            timer = 1
        timer += 1
#   Type Coordinate übergeben ?

        b.grid(row=i, column=j)
        cells[(i, j)] = b

root.mainloop()





input("Press enter to exit !")


class FleetManeuverGame:

    def __init__(self):
        """"""
        """Test for Home"""
