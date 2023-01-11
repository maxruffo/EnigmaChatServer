import time, socket, sys
from datetime import datetime
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
new_socket.bind(('', 0))

print("Binding successful!")

print("This is your IP: ", s_ip)
print("This is your Port: ", new_socket.getsockname()[1])

now = datetime.now()
time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")
welcome = "Chatroom started at : " + time_stamp + "/n"
 
new_socket.listen(1) 
 

while True: 
    conn, add = new_socket.accept()
 
    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')
 
    conn.send(welcome.encode())
"""
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
"""
