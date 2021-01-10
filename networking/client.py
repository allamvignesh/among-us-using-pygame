import socket
import time
from tkinter import *
import random

root = Tk()
e = Entry(root, width=50)
e.pack()
IP = 0
NAME = '0'
def getIp():
	global IP
	IP = e.get()
	root.destroy()
	print(IP)

def getName():
	global NAME
	NAME = e.get()
	root.destroy()

def create():
	global root, e
	root = Tk()
	e = Entry(root, width=50)
	e.pack()

class client():
	def __init__(self):
		self.HEADER = 64
		self.PORT = 5050
		self.FORMAT = 'utf-8'
		self.DISCONNECT_MESSAGE = "DISCONNECT!"
		
		while IP==0:
			myButton = Button(root, text="Enter Server IP", command=getIp)
			myButton.pack()
			root.mainloop()

		self.SERVER = IP #"192.168.43.151"
		create()
		
		self.ADDR = (self.SERVER, self.PORT)    #"192.168.43.245"
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.ADDR)
		
		while NAME == '0':
			myButton = Button(root, text="Enter Name", command=getName)
			myButton.pack()
			root.mainloop()

		self.name = NAME
		
		while 'change it' in self.send(self.name.encode(self.FORMAT)):
			create()
			myButton = Button(root, text="Name Already taken\nEnter another", command=getName)
			myButton.pack()
			self.name = NAME
			root.mainloop()

		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))



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