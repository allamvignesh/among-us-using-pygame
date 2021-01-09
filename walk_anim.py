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
		self.dead_move = 1

	def update(self, secCam=0, color=(255, 0, 0), in_vent = False, Not_Alive = False):
		self.rect.x = 1000//2
		self.rect.y = 550//2
		keys = pygame.key.get_pressed()

		if secCam == 1:
			self.rect.bottomright = (0, 0)
		if keys[K_d]:
			self.flip = 1
			self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.x = 1
		elif keys[K_a]:
			self.flip = 0
			self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.x = 1
		elif keys[K_w]:
			self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.y = 1
		elif keys[K_s]:
			self.image = pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(self.move)}.png")
			self.move += self.speed
			self.y = 1
		else:
			self.image = pygame.image.load(self.location)
			self.move = 1
			self.x, self.y = 0, 0

		if self.move == 13:
			self.move = 1
		if Not_Alive:
			self.dead_move += 0.5
			if int(self.dead_move) == 49:
				self.dead_move = 1
			self.image = pygame.image.load(f'images/Sprites/Ghost/ghostbob{int(self.dead_move)}.png')
		if self.flip == 0:
			self.image = pygame.transform.flip(self.image, True, False)

		if in_vent:
			self.image = pygame.image.load('models/maps/4.png')
		
		self.image = pygame.transform.scale(self.image, (78-25,103-30)) #(78-20,103-26)) 
		self.image = self.colorchanger(self.image, color)

	def colorchanger(self, surface, color):
		"""Fill all pixels of the surface with color, preserve transparency."""
		surface = surface.convert_alpha()
		w, h = surface.get_size()
		r, g, b = color
		print(surface.get_at((20, 50)))
		for x in range(w):
			for y in range(h):
				if surface.get_at((x,y)) == (255, 0, 0, 255):
					surface.set_at((x, y), pygame.Color(r, g, b, 255))
				elif surface.get_at((x,y)) == (254, 0, 0, 127):
					surface.set_at((x, y), pygame.Color(r, g, b, 127))
				elif surface.get_at((x,y)) == (254, 0, 0, 126):
					surface.set_at((x, y), pygame.Color(r, g, b, 126))
		return surface



if __name__ == '__main__':
	pygame.init()

	clock = pygame.time.Clock()
	fps = 50
	size =[1000, 550]
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
		players.update(Not_Alive = True, color = (255,255,255))
		clock.tick(fps)
