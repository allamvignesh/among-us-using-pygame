import socket
import time
from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()

class client():
	def __init__(self):

		self.PORT = 5050

		self.FORMAT = 'utf-8'
		self.myButton = Button(root, text="Enter Server IP", command=self.__click)
		self.myButton.pack()
		self.SERVER = "192.168.43.151"
		self.ADDR = (self.SERVER, self.PORT)    #"192.168.43.245"
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.ADDR)
		self.name = input("Enter Name: ")
		print(self.send(self.name.encode(self.FORMAT)))

	def send(self,msg):
		self.client.send(str(msg).encode(self.FORMAT))
		return self.client.recv(2048).decode(self.FORMAT)

	def __click(self):
		return e.get()

if __name__ == "__main__":
	a = client()
	while True:
		mess = input('enter message')
		if mess != '':
			a.send(mess)
		else:
			a.send('disconnect')
			break
