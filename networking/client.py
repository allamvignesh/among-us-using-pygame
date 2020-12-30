import socket
import time
class client():
	def __init__(self):
		self.HEADER = 64
		self.PORT = 5050
		self.FORMAT = 'utf-8'
		self.DISCONNECT_MESSAGE = "DISCONNECT!"
		self.SERVER = "192.168.43.151" #socket.gethostbyname(socket.gethostname())
		self.ADDR = (self.SERVER, self.PORT)    #"192.168.43.245"
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.ADDR)
		self.name = input("Enter Name: ")
		self.client.send(self.name.encode(self.FORMAT))

	def send(self,msg):
		self.client.send(str(msg).encode(self.FORMAT))
		return self.client.recv(2048).decode(self.FORMAT)
if __name__ == "__main__":
	a = client()
	while True:
		mess = input('enter message')
		if mess != '':
			a.send(mess)
		else:
			a.send('disconnect')
			break
