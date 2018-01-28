import socket


def client_broadcast_receive(IP, PORT, BUFFER_SIZE):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP, PORT))
    data = s.recvfrom(BUFFER_SIZE)
    message, socket_info = data
    print(message.decode("utf-8"))
    print("IP: {}, PORT: {}".format(socket_info[0], socket_info[1]))

    return True


if __name__ == "__main__":

    TCP_IP = '10.0.1.173'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024

    client_broadcast_receive(TCP_IP, TCP_PORT, BUFFER_SIZE)
