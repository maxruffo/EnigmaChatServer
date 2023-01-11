import time, socket, sys
 
socket_server = socket.socket()
server_host = socket.gethostname()
c_ip = socket.gethostbyname(server_host)
c_port = socket_server.getsockname()[1]
print(c_port)


print('This is your IP address: ',c_ip)
server_ip = input('Enter friend\'s IP address:')
print(c_port)
server_port = int(input('Enter friend\'s Port address:'))
name = input('Enter Your Username: ')
 
 
socket_server.connect((server_ip, server_port))
 
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' has joined...')

"""
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())  

    192.168.178.160
"""
