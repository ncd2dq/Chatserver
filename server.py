'''This will be the server that recieves all data from clients and servs is'''

import socket
import threading


class Server(object):
	def __init__(self,address=('127.0.0.1',5000)):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind(address)
		self.s.listen(1)
		self.connections = []

	def _handle_connections(self):
		'''
		This method will create a chat thread for all socket-client connections
		'''
		while True:
			conn, addr = self.s.accept()
			self.connections.append(conn)
			print('{} has connected'.format(str(addr)))

			chatThread = threading.Thread(target=self._handle_chat, args=(conn,))
			chatThread.daemon = True
			chatThread.start()

	def _handle_chat(self, conn):
		'''
		This method recieves data from a connection and sends it to all others
		in self.connections. 
		'''

	def disconnect(self, conn):
		'''This method removes closed sockets from the chat server list'''

