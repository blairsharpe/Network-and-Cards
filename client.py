import socket


def client_broadcast_receive():
    """Receives UDP broadcast data from server

    Returns:
        bool: True for success, False otherwise.

    """
    # Socket that it will be listening to for receiving server data
    IP = socket.gethostname()
    PORT = 5005
    BUFFER_SIZE = 1024

    # Setup UDP socket configuration to receive UDP packet broadcast
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP, PORT))

    # Wait to receive data from server
    data = s.recvfrom(BUFFER_SIZE)
    message, socket_info = data
    print(message.decode("utf-8"))

    print("(server -> client) IP: {}, Port: {}".format(socket_info[0],
                                                       socket_info[1]))

    return True


if __name__ == "__main__":

    if client_broadcast_receive() is True:

        # Setup socket that will be used for the rest of the game
        host = socket.gethostbyname(socket.gethostname())
        port = 2005
        BUFFER_SIZE = 2000
        MESSAGE = input("Username: ")

        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientA.connect((host, port))
        tcpClientA.send(MESSAGE.encode("utf-8"))

        tcpClientA.close()
