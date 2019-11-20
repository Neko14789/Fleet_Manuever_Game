class Playfield:
    playfield_symbols = {"unknown": "□",
                         "ship": "■",
                         "water": "~"
                         }

    def __init__(self, board_size):

        self.playfield = [[Playfield.playfield_symbols["unknown"] for _ in range(board_size.x)]
                          for _ in range(board_size.x)]
        self.board_size = board_size
#       Without this for _ in range ... every entry would not be unique and so not able to be changed individual

    def get_position_value(self, coordinate):
        return self.playfield[coordinate.y - 1][coordinate.x - 1]

    def set_position_value(self, coordinate, status):
        self.playfield[coordinate.y - 1][coordinate.x - 1] = Playfield.playfield_symbols[status]

    def draw_playfield(self):
        for x in self.playfield:
            timer = 0
            row = ""
            for y in x:
                row += y + "  "
                timer += 1
                if timer == self.board_size.x + 1:
                    print(format(row))

    def draw_playfield_2(self):
        for x in self.playfield:
            print(x)
