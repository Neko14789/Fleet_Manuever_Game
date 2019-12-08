"""UI Module for the Fleet Maneuver Game"""
from tkinter import *


# from Coordinate import Coordinate


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
    btn_frame = LabelFrame(master, text=frame_text, bg=frame_background_color)

    button_collection_set = {}
    for y in range(height_rows):  # Rows
        Grid.columnconfigure(btn_frame, y)
        for x in range(width_columns):  # Columns
            Grid.rowconfigure(btn_frame, x)
            btn = Button(btn_frame, cursor="crosshair", text="□■~", width=5, height=2, relief="solid")
            btn.configure(command=lambda x_pos=x, y_pos=y, b=btn: button_press(x_pos, y_pos, b))
            #   Type Coordinate.py for Button Position ?
            btn.grid(row=y, column=x)

            button_collection_set[(x, y)] = btn

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

    label_collection_set = {}
    for y in range(height_rows):  # Rows
        Grid.columnconfigure(lbl_frame, y)
        for x in range(width_columns):  # Columns
            Grid.rowconfigure(lbl_frame, x)
            lbl = Label(lbl_frame, cursor="dot", text="□■~", width=5, height=2, relief="solid")
            #   Type Coordinate.py for Button Position ?
            lbl.grid(row=y, column=x)

            label_collection_set[(x, y)] = lbl

    return lbl_frame


def button_press(x, y, button):
    print("test {} {}".format(x, y))
    button.configure(bg="green")


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

    sub_menu_settings = Menu(main_menu)
    sub_menu_settings.add_command(label="Setting 1", underline=0,
                                  command=change_board_size)
    main_menu.add_cascade(label="Settings", menu=sub_menu_settings, underline=0)

    sub_menu_help = Menu(main_menu)
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


"""Start of UI Creation"""
root = Tk()
root.title('Game "Testing"')
root.configure(bg="light blue")


try:
    root.iconbitmap('Fleet_Maneuver_Game.ico')
except TclError:
    print("Icon ('Fleet_Maneuver_Game.ico') was not found")


"""ADD Widgets"""
root.configure(menu=main_menu())
# root.eval('tk::PlaceWindow . center')
# TestLabel = Label(root)
# TestLabel.grid(row=1, column=3)

Grid.rowconfigure(root, 0, weight=4)
# Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
# Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=4)

Grid.columnconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 3, weight=10)


label_frame = label_frame(root, 10, 10, "Player 2", "Light grey")
# label_frame.grid(ipadx=0.2, ipady=0.2, padx=0.6, pady=0.6)
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
root.deiconify() # Window in foreground


"""Start App"""
root.mainloop()
