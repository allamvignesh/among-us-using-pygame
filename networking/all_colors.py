import pygame
from pygame.locals import *

pygame.init()

size =[500, 200]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 50
bg = [255, 255, 255]

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

players = []
colors = [(0,0,0), (0,0,255), (0,255,0), (255,0,0), (255,255,0),(0,255,255), (255,0,255), (255,255,255), (255,69,0), (165,42,42)]
pos = [(0,0), (100,0), (200,0), (300,0), (400,0), (0,100), (100,100), (200,100), (300,100), (400,100)]
for i in range(10):
	players.append(pygame.image.load("images/Sprites/idle.png"))
	players[-1] = colorchanger(players[-1], colors[i])
while True:
	screen.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		print('hell yay')

	for i in range(10):
		screen.blit(players[i], pos[i])

	pygame.display.update()
	clock.tick(fps)
