import pygame
from pygame.locals import *
from client import client
#from all_colors import colorchanger

pygame.init()

s = client()
print(s.send((0, 0, 1)))
#input()
clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)

def colorchanger(surface, color):
	"""Fill all pixels of the surface with color, preserve transparency."""
	surface = surface.convert_alpha()
	w, h = surface.get_size()
	r, g, b = color
	for x in range(w):
		for y in range(h):
			if surface.get_at((x,y)) == (255, 0, 0, 255):
				surface.set_at((x, y), pygame.Color(r, g, b, 255))
	return surface

class Sprite(pygame.sprite.Sprite):
	def __init__(self, location = "idle.png"):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(location)
		self.location = location
		self.rect = self.image.get_rect()
		print(self.rect)
		self.rect.center = (self.image.get_size()[0] // 2, self.image.get_size()[1] // 2)

		self.speed = 0.5
		self.move = 1
		self.flip = False

	def update(self, color):
		keys = pygame.key.get_pressed()
		if keys[K_w]:
			self.image = pygame.image.load(f"Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.flip = False
		elif keys[K_a]:
			self.image = pygame.transform.flip(pygame.image.load(f"Walk/walkcolor00{int(self.move)}.png"), True, False)
			self.move += self.speed
			self.flip = True
		elif keys[K_s]:
			self.image = pygame.transform.flip(pygame.image.load(f"Walk/walkcolor00{int(self.move)}.png"), True, False)
			self.move += self.speed
			self.flip = True
		elif keys[K_d]:
			self.image = pygame.image.load(f"Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.flip = False
		else:
			self.image = pygame.image.load(self.location)
			self.move = 1
			self.flip = False
		if self.move == 13:
			self.move = 1
		
		self.image = pygame.transform.scale(self.image, (78-25,103-30))
		self.image = colorchanger(self.image, color)


color = eval(input('Enter COLOR: '))
players = pygame.sprite.Group()
player = Sprite()
players.add(player)
a, b = 0, 0
player.rect.x, player.rect.y = 1000//2, 550//2
caf = pygame.image.load("map.png")

while True:
	screen.fill((255, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			s.send('disconnect')
			exit()

	keys = pygame.key.get_pressed()
	if keys[K_w]:
		b -= 10
	if keys[K_a]:
		a -= 10
	if keys[K_s]:
		b += 10
	if keys[K_d]:
		a += 10

	screen.blit(caf, (-a, -b))

	server_info = s.send((a+(1000//2), b+(550//2), player.move, player.flip, color))
	try:
		server_info = eval(server_info)
		for i in server_info:
			if i != s.name:
				server_info[i] = eval(server_info[i])
				player2 = pygame.transform.flip(pygame.image.load(f"Walk/walkcolor00{int(server_info[i][2])}.png"), server_info[i][3], False)
				if int(server_info[i][2]) == 1:
					player2 = pygame.image.load('idle.png')
				player2 = pygame.transform.scale(player2, (78-25,103-30))
				player2 = colorchanger(player2, server_info[i][4])
				screen.blit(player2, (int(server_info[i][0])-a, int(server_info[i][1])-b))

	except Exception as e:
		print(f'{e} Happened')

	players.draw(screen)

	pygame.display.update()
	players.update(color)
	clock.tick(fps)