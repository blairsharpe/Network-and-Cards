import socket


def server_broadcast_send():

    MESSAGE = "Black Jack Server Running"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(MESSAGE.encode('utf-8'), ('10.0.1.255', 5005))

    return True


if __name__ == "__main__":

    server_broadcast_send()
