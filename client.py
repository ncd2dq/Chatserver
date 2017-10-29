'''This module runs the chat program through the command line'''

import socket
import threading

class Client(object):
	def __init__(self, address=('217.0.0.1',5000)):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(address)
		self.name = input('Please select a username: ')

	def encode(self, data):
		return bytes(data, 'utf-8')

	def decode(self, data):
		return str(data, 'utf-8')

	def _handle_recieving(self, buff=1024):
		while True
			try:
				data = self.s.recv(buff)
				data = self.decode(data)
				print(data)

			except Exception as e:
				print(e)

	def _handle_sending(self):
		while True:
			try:
				data = input('--> ')
				data = self.name + ' ' + data
				data = self.encode(data)
				self.s.send(data)

			except Exception as e:
				print(e)

	def handler(self):
		recieveThread = threading.Thread(target=self._handle_recieving)
		recieveThread.daemon = True
		recieveThread.start()

		sendThread = threading.Thread(target=self._handle_sending)
		sendingThread.daemon = True
		sendingThread.start()

	def run(self):
		self.handler()


def main():
	client = Client()
	client.run()

if __name__ == '__main__':
	main()
