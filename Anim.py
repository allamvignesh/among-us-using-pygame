import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)

bg = pygame.image.load("images/death/bg.png")
s = 1
run = True

while run:

	"""s+= 0.2
				if int(s) == 22:
					run = False
					s = 1
				
				screen.fill(0)
			
				screen.blit(bg, (27, 64))
				screen.blit(pygame.image.load(f"images/death/{int(s)}.png"), (334, 242))
				screen.blit(pygame.image.load(f"images/death/de{int(s)}.png"), (512, 218))"""

	screen.fill(0)
	s += 10
	if s > 100:
		run = False
	screen.blit(pygame.image.load("models/shhhhhh.png"), (253, 26))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos())

	pygame.display.update()
	clock.tick(fps)