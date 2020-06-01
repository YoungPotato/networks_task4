from socket import *
import time
from config_parser import Parser


class TimeServer:
    def __init__(self, deception):
        self.addr = ('localhost', 123)
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.deception = deception

    def run(self):
        self.socket.bind(self.addr)

        while True:
            print('wait data...')

            conn, addr = self.socket.recvfrom(1024)
            print(bytes.decode(conn))
            print('client addr: ', addr)
            self.socket.sendto(str.encode(time.ctime(time.time() +
                                                     self.deception)), addr)


if __name__ == '__main__':
    conf_parser = Parser()
    deception = conf_parser.get_deception("settings.ini")
    time_server = TimeServer(deception)
    time_server.run()
