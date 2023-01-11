
import socket, threading
from colorama import Fore, Back, Style
nickname = input("Choose your nickname: ")
print("\n"+"Choose your Color:"+"\n")
print(" - Red")
print(" - Green")
print(" - Blue")
print(" - Magenta" + "\n")


color_input = input("Color you want: ")

if color_input == "Red":
    color = "\033[38;5;1m"
elif color_input == "Green":
    color = "\033[38;5;200m"
elif color_input == "Blue":
    color = "\033[38;5;4m"
elif color_input == "\033[38;5;5mMagenta":
    color = "\033[38;5;5m"
else:
    color = "\033[38;5;7m"

print("\n")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect(('127.0.0.1', 7979))                             #connecting client to server

def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('UTF-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('UTF-8'))
            elif nickname not in message:
                print("                     " + message)
        except:                                                 #case on wrong ip/port details
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                              #message layout
        message = '\033{}{}: \033[48;5;236m\033[38;5;231m{}\033[0;0m'.format(color,nickname, input(''))
        client.send(message.encode('UTF-8'))

receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()