'''This module runs the chat program through the command line'''

import socket
import threading

class Client(object):
	def __init__(self, address=('217.0.0.1',5000)):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(address)

	def encode(self, data):

	def decode(self, data):

	def _handle_recieving(self):

	def _handle_sending(self):

	def handler(self):
		#this should run the recieving / sending in 2 threads
		#initiallize the threads here

	def run(self):
		self.handler()
		

def main():
	client = Client()
	client.run()

if __name__ == '__main__':
	main()
