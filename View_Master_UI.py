from tkinter import *


class View:

    def __init__(self):

        master = Tk()

        """Master Window configuration"""
        master.title("Schiffe Versenken")
        #   master.resizable(False,False)
        Grid.rowconfigure(master,1,weight=1)
        Grid.columnconfigure(master,0,weight=1)

        master.minsize(250,250)
        master.eval('tk::PlaceWindow . center')
        """Master Window configuration"""

        """Button_Panel configuration"""
        button_frame = LabelFrame(text="Playfield of Player 1",bg="#99ccff")
        button_frame.grid(row=1, column=0, sticky=N + S + E + W)


        def button_press(y, x, button_collection_set):
            childes = button_frame.children
            print("hi", x, y)
            button_collection_set[(x, y)].configure(bg="#66e0ff", state=DISABLED)

        height_rows = 10
        width_columns = 10
        button_collection_set = {}
        for i in range(height_rows):  # Rows
            Grid.columnconfigure(button_frame, i, weight=1)
            for j in range(width_columns):  # Columns
                Grid.rowconfigure(button_frame, j, weight=1)
                b = Button(button_frame, cursor="crosshair", text="□■~", width=5, height=2,
                           command=lambda y=j, x=i, buttons=button_collection_set: button_press(y, x, buttons))
                #   Type Coordinate.py for Button Position ?
                b.grid(row=i, column=j, sticky=N + S + E + W)

                button_collection_set[(i, j)] = b

        top_frame = Frame(bg="#e6faff")
        top_frame.grid(row=0, column=0, sticky=E + W)

        msg = Label(top_frame, text="Testing my Fleet Maneuver Game!", bg="#e6faff")
        msg.pack()

        master.mainloop()