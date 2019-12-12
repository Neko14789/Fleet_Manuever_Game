"""UI Module for the Fleet Maneuver Game"""
from tkinter import *
from tkinter import ttk


# from Coordinate import Coordinate
from Playfield import Playfield
from Coordinate import Coordinate
from Fleet import Fleet
button_collection_set = {}
board_size = Coordinate(9,9)
TestPlayfield = Playfield(board_size)
p1_fleet = Fleet().create_fleet(board_size, 11)
print("a")



def button_frame(master, height_rows: int = 10, width_columns: int = 10, frame_text: str = "Frame",
                 frame_background_color: str = "Grey"):
    """
    Creates a Frame filled with Buttons
    @param master: Widget in that this Widget gets put
    @param height_rows: Buttons per Row
    @param width_columns: Buttons per Column
    @param frame_text: Text of the Frame
    @param frame_background_color: Background color of the Frame
    @return: Frame filled with Buttons
    """
    btn_frame = LabelFrame(master, text=frame_text, bg=frame_background_color, width=width_columns*50, height=height_rows*50)



    index = 0
    global button_collection_set
    # button_collection_set = {}
    frames_list = []


    for y in range(height_rows):  # Rows
        Grid.columnconfigure(btn_frame, y, weight=1)
        for x in range(width_columns):  # Columns
            Grid.rowconfigure(btn_frame, x,  weight=1)

            frames_list.append(Frame(btn_frame, width=40, height=40))
            frames_list[index].propagate(False)
            frames_list[index].grid(row=y, column=x, sticky=NSEW, padx=1, pady=1)

            # btn = Button(btn_frame, cursor="crosshair", text="□■~", relief="solid")
            # btn.configure(command=lambda x_pos=x, y_pos=y, b=btn: button_press(x_pos, y_pos, b))
            #   Type Coordinate.py for Button Position ?
            # btn.grid(row=y, column=x, sticky=NSEW, padx=0.5, pady=0.5)

            button_collection_set[(x, y)] = Button(frames_list[index], cursor="crosshair", text="□■~", relief="solid")
            button_collection_set[(x, y)].configure(command=lambda x_pos=x, y_pos=y, b=button_collection_set[(x, y)]: button_press(x_pos, y_pos, b))
            button_collection_set[(x, y)].pack(expand=True, fill=BOTH)
            index += 1

    return btn_frame


def label_frame(master, height_rows: int = 10, width_columns: int = 10, frame_text: str = "Frame",
                frame_background_color: str = "Grey"):
    """
    Creates a Frame filled with Labels
    @param master: Widget in that this Widget gets put
    @param height_rows: Labels per Row
    @param width_columns: Labels per Column
    @param frame_text: Text of the Frame
    @param frame_background_color: Background color of the Frame
    @return: Frame filled with Labels
    """
    lbl_frame = LabelFrame(master, text=frame_text, bg=frame_background_color)

    index = 0
    frames_list = []
    label_collection_set = {}

    for y in range(height_rows):  # Rows
        Grid.columnconfigure(lbl_frame, y, weight=1)
        for x in range(width_columns):  # Columns
            Grid.rowconfigure(lbl_frame, x, weight=1)

            frames_list.append(Frame(lbl_frame, width=40, height=40))
            frames_list[index].propagate(False)
            frames_list[index].grid(row=y, column=x, sticky=NSEW, padx=1, pady=1)

            label_collection_set[(x, y)] = Label(frames_list[index], cursor="dot", text="□■~", width=5, height=2, relief="groove")
            label_collection_set[(x, y)].pack(expand=True, fill=BOTH)
            index += 1


    return lbl_frame


def button_press(x, y, button):


    print("test {} {}".format(x, y))
    button.configure(bg="green")

    current_cord = Coordinate(x,y)
    #TestPlayfield.set_position_value(current_cord, "ship")

    state = "water"
    for ship in p1_fleet:
        if ship.was_hit(current_cord):
           state = "■"
           break
           #TestPlayfield.set_position_value(current_cord,"ship")


    #TestPlayfield.set_position_value(current_cord, state)
    #status = TestPlayfield.get_position_value(current_cord)
    button_collection_set[(x,y)].configure(text=state)

def main_menu():
    """
    Creates the Main Menu for your Window
    @return: Main Menu Object
    """
    main_menu = Menu(root)

    main_menu.add_command(label="Join Game", underline=5, command=lambda master=main_menu: join_game(master))
    # main_menu.bind_all("<Control-g>", self.__join_game)

    main_menu.add_command(label="Quit Game", underline=0, command=lambda master=main_menu: quit_game(master),
                          state=DISABLED)
    # main_menu.bind_all("<Control-q>", self.__quit_game)

    main_menu.add_command(label="Host Game", underline=0, command=lambda master=main_menu: host_game(master))
    # main_menu.bind_all("<Control-h>", self.__quit_game)

    main_menu.add_command(label="Play AI Game", underline=5, command=lambda master=main_menu: ai_game(master))
    # main_menu.bind_all("<Control-h>", self.__quit_game)

    sub_menu_settings = Menu(main_menu, tearoff=False)
    sub_menu_settings.add_command(label="Setting 1", underline=0,
                                  command=change_board_size)
    main_menu.add_cascade(label="Settings", menu=sub_menu_settings, underline=0)

    sub_menu_help = Menu(main_menu, tearoff=False)
    sub_menu_help.add_command(label="Show Info", underline=7,
                              command=show_info)
    main_menu.add_cascade(label="Help", menu=sub_menu_help, underline=1)

    return main_menu


def quit_game(master, event=None):
    print("Not jet implemented q")
    master.entryconfig('Quit Game', state=DISABLED)
    master.entryconfig('Join Game', state=NORMAL)
    master.entryconfig('Host Game', state=NORMAL)
    master.entryconfig('Play AI Game', state=NORMAL)


def join_game(master, event=None):
    print("Not jet implemented g")
    master.entryconfig('Quit Game', state=NORMAL)
    master.entryconfig('Join Game', state=DISABLED)
    master.entryconfig('Host Game', state=DISABLED)
    master.entryconfig('Play AI Game', state=DISABLED)



def host_game(master, event=None):
    print("Not jet implemented h")
    master.entryconfig('Quit Game', state=NORMAL)
    master.entryconfig('Join Game', state=DISABLED)
    master.entryconfig('Host Game', state=DISABLED)
    master.entryconfig('Play AI Game', state=DISABLED)


def ai_game(master, event=None):
    print("Not jet implemented a")
    master.entryconfig('Quit Game', state=NORMAL)
    master.entryconfig('Join Game', state=DISABLED)
    master.entryconfig('Host Game', state=DISABLED)
    master.entryconfig('Play AI Game', state=DISABLED)


def change_board_size(event=None):
    # print("pass c")
    from tkinter import messagebox
    messagebox.showinfo("Setting 1", "Not yet implemented")


def show_info(event=None):
    # print("pass f")
    from tkinter import messagebox
    messagebox.showinfo("Info", "This Game was created by Nico Hübsch with Python")


def ship_tree_view(master):

    tree = ttk.Treeview(master)

    tree["columns"] = ("ships", "state")
    tree.column("#0", width=30, minwidth=30, stretch=False)
    tree.column("ships", width=100, minwidth=100, stretch=False)
    tree.column("state", width=100, minwidth=100, stretch=False)

    tree.heading("#0", text="ID", anchor=W)
    tree.heading("ships", text="Ship", anchor=W)
    tree.heading("state", text="State", anchor=W)

    tree.insert("", 1, text="0", values=("Test Ship", "Alive"))

    """Stops User from changing column width"""
    def handle_click(event):
        if tree.identify_region(event.x, event.y) == "separator":
            return "break"

    tree.bind('<Button-1>', handle_click)

    return tree


def random_fleet_button(master, height, width, frame_background_color: str = "Grey", btn_text: str = "□■~"):

    btn_frame = Frame(master, bg=frame_background_color, width=width, height=height)
    btn_frame.propagate(False)

    btn = Button(btn_frame,text=btn_text,relief="solid")
    btn.configure(command=lambda b=btn: random_fleet_button_press(b))

    btn.pack(expand=True,fill=BOTH)

    return btn_frame


def random_fleet_button_press(button):
    print("Creating Fleet (hopefully)")



    for x in range(10):
        for y in range(10):
            current_cord = Coordinate(x,y)
            status = TestPlayfield.get_position_value(current_cord)
            button_collection_set[(x, y)].configure(text=status)
    #
    pass


"""Start of UI Creation"""
root = Tk()
root.title('Game "Testing"')
root.configure(bg="light blue")
#  root.geometry("1440x960")


try:
    root.iconbitmap('Fleet_Maneuver_Game.ico')
except TclError:
    print("Icon ('Fleet_Maneuver_Game.ico') was not found")


"""ADD Widgets"""
root.configure(menu=main_menu())


"""TESTING"""
separator = Frame(height=2, bd=1, relief=RAISED, bg="blue")
separator.grid(row=2, column=1, columnspan=3, padx=5, pady=20, sticky=EW)

ShipList = ship_tree_view(root)
ShipList.grid(row=2, column=3)

random_fleet_button = random_fleet_button(root,200,80,btn_text="New Fleet")
random_fleet_button.grid(row=1, column=3)
"""TESTING"""

Grid.rowconfigure(root, 0, weight=5)
# Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=3)
# Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=5)

Grid.columnconfigure(root, 0, weight=3)
# Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 3, weight=7)


label_frame = label_frame(root, 10, 10, "Player 2", "Light grey")
label_frame.grid(row=1, column=1)

button_frame = button_frame(root, 10, 10, "You", "Light Green")
button_frame.grid(row=3, column=1)


"""Center Window"""
# Apparently a common hack to get the window size. Temporarily hide the
# window to avoid update_idletasks() drawing the window in the wrong
# position.
root.withdraw()
root.update_idletasks()  # Update "requested size" from geometry manager

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position
root.deiconify()  # Window in foreground


"""Start App"""
root.mainloop()
