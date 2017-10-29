'''This will be the server that recieves all data from clients and servs is'''

import socket
import threading


class Server(object):
    def __init__(self, address=('127.0.0.1',5000)):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(address)
        self.s.listen(1)
        self.connections = []

    def encode(self, data):
        return bytes(data, 'utf-8')

    def _handle_connections(self):
        '''
        This method will create a chat thread for all socket-client connections
        '''
        print('Waiting for connections...')
        while True:
            conn, addr = self.s.accept()
            self.connections.append(conn)
            print('{} has connected'.format(str(addr)))

            chatThread = threading.Thread(target=self._handle_chat, args=(conn,addr))
            chatThread.daemon = True
            chatThread.start()

    def _handle_chat(self, conn, addr, buff=1024):
        '''
        This method recieves data from a connection and sends it to all others
        in self.connections. 
        '''
        while True:
            try:
                data = conn.recv(buff)
                for connection in self.connections:
                    if connection != conn:
                        conn.send(data)
            except:
                self.disconnect(conn, addr)

    def disconnect(self, conn, addr):
        '''This method removes closed sockets from the chat server list'''
        self.connections.remove(conn)
        msg = '{} has disconnected.'.format(str(addr))
        msg = self.encode(msg)
        for connection in self.connections:
            connection.send(msg)

    def run(self):
        self._handle_connections()


def main():
    server = Server()
    server.run()

if __name__ == '__main__':
    main()