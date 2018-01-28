import socket


def server_broadcast_send():
    MESSAGE = "This is a test"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(MESSAGE.encode('utf-8'), ('10.0.1.255', 5005))


if __name__ == "__main__":

    server_broadcast_send()
