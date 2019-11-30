import socket


HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 4230))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg =f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        msg = input("Send:")
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))
    #clientsocket.send(bytes(input("Message to send"), "utf-8"))
