import pygame
from pygame.locals import *
from client import client

pygame.init()

s = client()
print(s.send((0, 0, 1)))
#input()
clock = pygame.time.Clock()
fps = 50
size =[800, 550]
screen = pygame.display.set_mode(size)

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

	def update(self):
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



players = pygame.sprite.Group()
player = Sprite()
players.add(player)
a, b = 0, 0
while True:
	screen.fill((255, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			s.send('disconnect')
			exit()

	keys = pygame.key.get_pressed()
	if keys[K_w] and player.rect.y > 0:
		b -= 10
	if keys[K_a] and player.rect.x > 0:
		a -= 10
	if keys[K_s] and player.rect.y < 500:
		b += 10
	if keys[K_d] and player.rect.x < 750:
		a += 10

	players.draw(screen)

	pos = s.send((a, b, player.move, player.flip))
	try:
		pos = eval(pos)
		for i in pos:
			if i != s.name:
				pos[i] = eval(pos[i])
				player2 = pygame.transform.flip(pygame.image.load(f"Walk/walkcolor00{int(pos[i][2])}.png"), pos[i][3], False)
				player2 = pygame.transform.scale(player2, (78-25,103-30))
				screen.blit(player2, (int(pos[i][0]), int(pos[i][1])))

	except Exception as e:
		print(f'{e} Happened')

	pygame.display.update()
	players.update()
	clock.tick(fps)