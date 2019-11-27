from tkinter import *


class View:

    def __init__(self):

        Master = Tk()

        Master.title("Schiffe Versenken")
        #   Master.resizable(False,False)
        Grid.rowconfigure(Master, 1, weight=1)
        Grid.columnconfigure(Master, 0, weight=1)
        Master.minsize(250, 250)

        # Gets the requested values of the height and width.
        window_width = Master.winfo_reqwidth()
        window_height = Master.winfo_reqheight()
        print("Width", window_width, "Height", window_height)

        # Gets both half the screen width/height and window width/height
        position_right = int(Master.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(Master.winfo_screenheight() / 3 - window_height / 2)

        # Positions the window in the center of the page.
        Master.geometry("+{}+{}".format(position_right,position_down))

        root = Canvas()
        root.grid(row=1, column=0, sticky=N + S + E + W)


        def test(y, x, buttons):
            childes = root.children
            print("hi", x, y)
            buttons[(x, y)].configure(bg="#66e0ff", state=DISABLED)


        height = 10
        width = 10
        cells = {}
        timer = ""
        for i in range(height):  # Rows
            Grid.columnconfigure(root, i, weight=1)
            for j in range(width):  # Columns
                Grid.rowconfigure(root, j, weight=1)
                k = (j, i)
                b = Button(root, cursor="crosshair", text="□■~", height=2, width=5, command=lambda y=j, x=i, buttons=cells:
                    test(y, x, buttons))
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
