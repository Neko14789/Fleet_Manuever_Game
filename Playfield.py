"""Playfield Module."""
from Coordinate import Coordinate


class Playfield:
    """This is a class for a variable Playfield for the Fleet_Maneuver_Game."""

    playfield_symbols = {"unknown": "□",
                         "ship": "■",
                         "water": "~"
                         }

    def __init__(self, board_size: type(Coordinate)):

        self.playfield = [[Playfield.playfield_symbols["unknown"] for _ in range(board_size.x)]
                          for _ in range(board_size.y)]
        self.board_size = board_size

    #       Without this for _ in range ..., every entry would not be unique and so not able to be changed individual

    def get_position_value(self, coordinate: type(Coordinate)) -> str:
        """
        Gets the Value(Status) of one coordinate.
        :param coordinate: The position as coordinate object
        :return: Value(Status) of the coordinate
        """
        return self.playfield[coordinate.x - 1][coordinate.y - 1]

    def set_position_value(self, coordinate:type(Coordinate), value:type(str)):
        """
        Changes a Value(Status) of one coordinate.
        :param coordinate: The position as coordinate object
        :param value: The value/status of the field ("unknown": "□", "ship": "■", "water": "~")
        """
        self.playfield[coordinate.x - 1][coordinate.y - 1] = Playfield.playfield_symbols[value]

    def draw_playfield(self):
        """
        Draws the Playfield.
        """
        for x in self.playfield:
            timer = 0
            row = " "
            for y in x:
                row += y + "  "
                timer += 1
                if timer == self.board_size.x:
                    print(format(row))

    def draw_playfield_2(self):
        """
        Different Approach to draw the Playfield.
        """
        for x in self.playfield:
            print(x)
