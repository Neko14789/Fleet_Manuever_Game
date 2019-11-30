import socket
import errno
import sys
from tkinter import *
from unicodedata import east_asian_width

HEADER_LENGTH = 10
IP = socket.gethostbyname('nico14789.ddns.net')
PORT = 4230

Login = Tk()

Label = Label(Login, text="Set your Username:").grid(row=0, column=0, columnspan=2, sticky=N + S + E + W)

UserNameInput = Entry(Login).grid(row=1, column=0, sticky=E + W)

my_username = "NO_USERNAME"


def send_username_button_press(event=None):
    real_button = Login.children["!button"]
    global my_username
    my_username = Login.children["!entry"].get()

    Login.destroy()


Login.bind("<Return>", send_username_button_press)

send_username_button = Button(Login, text="Send", command=lambda: send_username_button_press()).grid(row=1, column=1,
                                                                                                     sticky=S + E + W)

Grid.rowconfigure(Login, 0, weight=2)
Grid.rowconfigure(Login, 1, weight=0)
Grid.columnconfigure(Login, 0, weight=4)
Grid.columnconfigure(Login, 1, weight=1)

Login.title("Lets Chat: Set User Name")
Login.geometry("300x100")
Login.minsize(150, 50)
Login.eval('tk::PlaceWindow . center')

Login.mainloop()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

my_User_Name = username

master_window = Tk()
master_window.title("Lets Chat")

Frame = LabelFrame(master_window, text=f"Chat: logged in as <{str(my_User_Name, 'utf-8')}>")
Frame.grid(row=0, column=0, columnspan=4, sticky=N + S + E + W)

message_box = Text(Frame, width=146, state=DISABLED)
Scroll_B = Scrollbar(Frame)

message_box.pack(side=LEFT, fill=Y)
Scroll_B.pack(side=RIGHT, fill=Y)

Scroll_B.config(command=message_box.yview)
message_box.config(yscrollcommand=Scroll_B.set)

message_entry = Entry(master_window).grid(row=1, column=0, columnspan=2, sticky=N + S + E + W)


def send_message_button_press(event=None):
    real_button = master_window.children["!button"]
    message = master_window.children['!entry'].get()
    global Multiplayer_Update
    master_window.children['!entry'].delete(0, last=END)
    # master_window.children['!entry'].selection_clear()

    Multiplayer_Update(message)


master_window.bind("<Return>", send_message_button_press)

send_message_button = Button(master_window, text="Send", width=20, height=2,
                             command=lambda button=master_window: send_message_button_press(button)).grid(row=1,
                                                                                                          column=3,
                                                                                                          sticky=N + S + E + W)

Grid.rowconfigure(master_window, 0, weight=4)
Grid.rowconfigure(master_window, 1, weight=1)
Grid.columnconfigure(master_window, 0, weight=1)
Grid.columnconfigure(master_window, 0, weight=1)

master_window.geometry("1200x800")
master_window.minsize(150, 10)
master_window.eval('tk::PlaceWindow . center')


def Multiplayer_Update(message=""):
    def update_message_box(UName, Mg):
        from datetime import datetime
        try:
            Mg = str(Mg, 'utf-8')
        except:
            pass

        try:
            UName = str(UName, 'utf-8')
        except:
            pass
        message_box.configure(state=NORMAL)
        message_box.insert(END, "\n" + "<" + datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S') + ">-<" + UName + ">: " + Mg + "\n")
        message_box.see(END)
        message_box.configure(state=DISABLED)

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)
        global my_User_Name
        # message_box.insert(END, f"<{my_User_Name}>: {message}")
        # b" {message} ".decode("utf-8")

        update_message_box(my_User_Name, message)

    try:
        while True:
            # receive things
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            # print(f"{username} > {message}")

            # message_box.insert(END,f"\n<{username}>: {message}\n")

            update_message_box(username, message)


    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("Reading error", str(e))
            sys.exit()

        master_window.after(10, Multiplayer_Update)



    except Exception as e:
        print("General error", str(e))
        sys.exit()


master_window.after(0, Multiplayer_Update)
master_window.mainloop()
