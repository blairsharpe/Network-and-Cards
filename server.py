import socket

TCP_IP = "10.0.1.173"
TCP_PORT = 4
BUFFER_SIZE = 1024


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

print("Connection request: {}".format(addr))
