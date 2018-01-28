import socket


def client_broadcast_receive():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('10.0.1.173', 5005))
    m = s.recvfrom(1024)
    print(print(m))


if __name__ == "__main__":

    client_broadcast_receive()
