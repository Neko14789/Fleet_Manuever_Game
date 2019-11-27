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
print("Test 2:"+TestValue)

TestPlayfield.draw_playfield()
TestPlayfield.draw_playfield_2()

from tkinter import *

Master = Tk()

Master.title("Schiffe Versenken")
#   Master.resizable(False,False)
Grid.rowconfigure(Master, 1, weight=1)
Grid.columnconfigure(Master, 0, weight=1)
Master.minsize(250, 250)

# Gets the requested values of the height and width.
windowWidth = Master.winfo_reqwidth()
windowHeight = Master.winfo_reqheight()
print("Width",windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(Master.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(Master.winfo_screenheight() / 3 - windowHeight / 2)

# Positions the window in the center of the page.
Master.geometry("+{}+{}".format(positionRight, positionDown))


root = Canvas()
root.grid(row=1, column=0, sticky=N + S + E + W)


def test(y, x, buttons):
    childes=root.children
    print("hi", x, y)
    buttons[(x, y)].configure(bg="#66e0ff", state=DISABLED)


height = 10
width = 10
cells = {}
timer = ""
for i in range(height): #Rows
    Grid.columnconfigure(root, i, weight=1)
    for j in range(width): #Columns
        Grid.rowconfigure(root,j,weight=1)
        k = (j, i)
        b = Button(root, cursor="tcross", text="□■~", command=lambda y=j, x=i, buttons=cells: test(y, x, buttons))
        if timer == "":
            timer = 1
        timer += 1
#   Type Coordinate übergeben ?

        b.grid(row=i, column=j, sticky=N + S + E + W)

        cells[(i, j)] = b


root2 = Canvas(bg="#e6faff")
root2.grid(row=0, column=0, sticky=E + W)


msg = Label(root2, text="Testing my Fleet Maneuver Game!", bg="#e6faff")
msg.pack()

Master.mainloop()


input("Press enter to exit !")


class FleetManeuverGame:

    def __init__(self):
        """"""
        """Test for Home"""
