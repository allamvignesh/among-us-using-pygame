import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self, location = "images/Sprites/idle.png"):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(location)
		self.image = pygame.transform.scale(self.image, (78-20,103-26))
		self.location = location
		self.rect = self.image.get_rect()
		print(self.rect)

		self.speed = 0.5
		self.move = 1
		self.flip = 0
		self.x = 0
		self.y = 0

	def update(self):
		self.rect.x = 1000//2
		self.rect.y = 550//2
		keys = pygame.key.get_pressed()
		if keys[K_d]:
			self.flip = 1
			self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.x = 1
		elif keys[K_a]:
			self.flip = 0
			self.image = pygame.transform.flip(pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png"), True, False)
			self.move += self.speed
			self.x = 1
		elif keys[K_w]:
			if self.flip == 0:
				self.image = pygame.transform.flip(pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png"), True, False)
			else:
				self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.y = 1
		elif keys[K_s]:
			if self.flip == 0:
				self.image = pygame.transform.flip(pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png"), True, False)
			else:
				self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.y = 1
		else:
			self.image = pygame.image.load(self.location)
			self.move = 1
			self.x, self.y = 0, 0
		if self.move == 13:
			self.move = 1
		
		self.image = pygame.transform.scale(self.image, (78-20,103-26))



if __name__ == '__main__':
	pygame.init()

	clock = pygame.time.Clock()
	fps = 50
	size =[800, 550]
	screen = pygame.display.set_mode(size)

	players = pygame.sprite.Group()
	player = Player()
	players.add(player)
	bg = pygame.image.load('models/map parts/PC Computer - Among Us - Skeld Cafeteria.png')
	bg_pos = [0,0]
	while True:
		screen.fill((255, 255, 255))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.blit(bg, bg_pos)

		keys = pygame.key.get_pressed()
		if keys[K_w]:
			bg_pos[1] += 10
		if keys[K_a]:
			bg_pos[0] += 10
		if keys[K_s]:
			bg_pos[1] -= 10
		if keys[K_d]:
			bg_pos[0] -= 10

		players.draw(screen)

		pygame.display.update()
		players.update()
		clock.tick(fps)