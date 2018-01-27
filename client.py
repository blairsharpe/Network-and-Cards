import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 4
BUFFER_SIZE = 1024

# Chosen SOCK_STREAM which is used by TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((TCP_IP, TCP_PORT))
client_socket.send("Establishing connection".encode('utf-8'))
client_socket.close()
