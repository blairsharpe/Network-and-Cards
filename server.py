import socket
import time
from threading import Thread


class ClientThread(Thread):

    """Creates a client thread with information about the user

    Attributes:
        ip (str): The ip address of the client
        port (str): port that the client will be using
    """

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.username = ""

        print("(client - > server) + New thread for: IP {}, Port: {}".
              format(ip, port))

    def run(self):
        """Setups basic information with client with initial connection"""

        self.username = conn.recv(2048).decode("utf-8")
        print("(client -> server) Server received username: {}"
              .format(self.username))


def server_broadcast_send():
    """Broadcasts to all clients on the network that the server is up

    Returns:
        bool: True for sucess
    """

    MESSAGE = "(server - > client) Black Jack server up"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(MESSAGE.encode('utf-8'), ('10.0.1.255', 5005))

    return True


if __name__ == "__main__":

    # Setup sockets to listen for any clients
    TCP_IP = socket.gethostbyname(socket.gethostname())
    TCP_PORT = 2005
    BUFFER_SIZE = 20
    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, TCP_PORT))

    # Add all of our clients to a list of threds
    threads = []

    # Allow clients to sign up in 10 seconds

    # Broadcast to clients that we are live
    server_broadcast_send()

    # Wait for any clients to respond to the broadcast
    tcpServer.listen(4)
    print("Waiting for clients...")

    # Connect to any clients reponding to our message
    (conn, (ip, port)) = tcpServer.accept()

    # Create our client thread instance
    newthread = ClientThread(ip, port)

    # Starts the threads activity. Calls run() method
    newthread.start()

    # Add to our list of client threads
    threads.append(newthread)

    # Black Magic
    for t in threads:
        t.join()
