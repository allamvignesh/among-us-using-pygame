import pygame
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
	def __init__(self, location = "images/Sprites/idle.png"):

		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(location)
		self.image = pygame.transform.scale(self.image, (78-20,103-26))
		self.location = location
		self.rect = self.image.get_rect()

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

		if keys[K_w] or keys[K_a] or keys[K_s] or keys[K_d]:
			if pygame.mixer.Channel(3).get_busy() == 0:
				pygame.mixer.Channel(3).set_volume(0.2)
				pygame.mixer.Channel(3).play(pygame.mixer.Sound(f'bgs/Player/Footsteps/Metal/FootstepMetal0{random.randint(1,8)}.wav'))
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
		for x in range(w):
			for y in range(h):
				if surface.get_at((x,y)) == (255, 0, 0, 255):
					surface.set_at((x, y), pygame.Color(r, g, b, 255))
				elif surface.get_at((x,y)) == (254, 0, 0, 127):
					surface.set_at((x, y), pygame.Color(r, g, b, 127))
				elif surface.get_at((x,y)) == (254, 0, 0, 126):
					surface.set_at((x, y), pygame.Color(r, g, b, 126))
		return surface