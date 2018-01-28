import socket
from threading import Thread


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("(client - > server) + New thread for: IP {}, Port: {}".format(ip, port))

    def run(self):
        data = conn.recv(2048)
        print("(client -> server) Server received data: {}".format(data.decode("utf-8")))


def server_broadcast_send():

    MESSAGE = "(server - > client) Black Jack server up"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(MESSAGE.encode('utf-8'), ('10.0.1.255', 5005))

    return True


if __name__ == "__main__":

    TCP_IP = '10.0.1.173'
    TCP_PORT = 2005
    BUFFER_SIZE = 20  # Usually 1024, but we need quick response

    server_broadcast_send()

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, TCP_PORT))

    threads = []

    server_broadcast_send()

    tcpServer.listen(4)
    print("Waiting for clients...")
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

    for t in threads:
        t.join()
