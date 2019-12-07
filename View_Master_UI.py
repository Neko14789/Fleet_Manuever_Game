from tkinter import *


class View:

    def __init__(self):
        """creates the UI"""
        """Button Frame configuration"""

        def create_button_frame(row, column):
            button_frame = LabelFrame(text="Playfield of Player 2", bg="#99ccff")
            button_frame.grid(row=row, column=column, sticky=N + S + E + W)

            def button_press(y, x, buttons):
                def buttons_state(new_state: str):
                    """State: On, Off, All_On, All_Off"""
                    new_state = new_state.lower()
                    try:
                        states = {
                            "on": ("normal", False),
                            "off": ("disabled", False),
                            "all_on": ("normal", True),
                            "all_off": ("disabled", True),
                        }

                        if states[new_state][1]:
                            for _ in buttons:
                                buttons[_].configure(state=states[new_state][0])
                        else:
                            buttons[(x, y)].configure(state=states[new_state][0])
                        buttons[(x, y)].configure(state="disabled")
                    except KeyError:
                        print("Button State Input Error, check the allowed states")

                #   print("Debug:", x, y)
                buttons[(x, y)].configure(bg="#66e0ff")
                #buttons_state("all_off")
                buttons_state("off")


            height_rows = 10
            width_columns = 10
            button_collection_set = {}
            for i in range(height_rows):  # Rows
                Grid.columnconfigure(button_frame, i, weight=1)
                for j in range(width_columns):  # Columns
                    Grid.rowconfigure(button_frame, j, weight=1)
                    b = Button(button_frame, cursor="crosshair", text="□■~", width=5, height=2, relief="solid",
                               command=lambda y=j, x=i, buttons=button_collection_set: button_press(y, x, buttons))
                    #   Type Coordinate.py for Button Position ?
                    b.grid(row=i, column=j, sticky=N + S + E + W)

                    button_collection_set[(i, j)] = b

        """Button Frame configuration"""

        """Label Frame configuration"""

        def create_label_frame(row, column):
            label_frame = LabelFrame(text="Playfield of Player 1", bg="#21b5ae")
            label_frame.grid(row=row, column=column, sticky=N + S + E + W)

            """def button_press(y,x,buttons):

                def buttons_state(new_state: str):
                    #   State: On, Off, All_On, All_Off
                    new_state = new_state.lower()
                    try:
                        states = {
                            "on": ("normal",False),
                            "off": ("disabled",False),
                            "all_on": ("normal",True),
                            "all_off": ("disabled",True),
                        }

                        if states[new_state][1]:
                            for _ in buttons:
                                buttons[_].configure(state=states[new_state][0])
                        else:
                            buttons[(x,y)].configure(state=states[new_state][0])
                    except KeyError:
                        print("Button State Input Error, check the allowed states")

                #   print("Debug:", x, y)
                buttons[(x,y)].configure(bg="#66e0ff")
                buttons_state("Off")"""

            height_rows = 10
            width_columns = 10
            label_collection_set = {}
            for i in range(height_rows):  # Rows
                Grid.columnconfigure(label_frame, i, weight=1)
                for j in range(width_columns):  # Columns
                    Grid.rowconfigure(label_frame, j, weight=1)
                    label = Label(label_frame, cursor="dot", text="□■~", width=5, height=2, relief="groove")
                    #   Type Coordinate.py for Button Position ?
                    label.grid(row=i, column=j, sticky=N + S + E + W)

                    label_collection_set[(i, j)] = label

        """Button Frame configuration"""

        master = Tk()

        create_button_frame(2, 0)
        create_label_frame(1, 0)
        # create_button_frame(2,2)
        # create_label_frame(1,2)

        """Top Frame configuration"""
        top_frame = Frame(bg="#e6faff")
        top_frame.grid(row=0, column=0, columnspan=3, sticky=E + W)

        msg = Label(top_frame, text="Testing my Fleet Maneuver Game!", bg="#e6faff")
        msg.pack()
        """Top Frame configuration"""
        import tkinter.ttk as ttk

        ttk.Separator(master).grid(column=1, row=1, rowspan=1, sticky=(N, E, S, W), ipadx=10)

        """Master Window configuration"""
        master.title("Schiffe Versenken")
        #   master.resizable(False,False)
        Grid.rowconfigure(master, 1, weight=1)
        Grid.rowconfigure(master, 2, weight=1)
        Grid.columnconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 1, weight=1)

        master.minsize(250, 250)
        master.eval('tk::PlaceWindow . center')
        """Master Window configuration"""

        master.mainloop()
