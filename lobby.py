import pygame
from pygame.locals import *
import random

pygame.init()

size =[1000, 550]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 50

a, b = 0, 0

lob1 = pygame.image.load("models/map parts/lobby/1.png")
lob2 = pygame.image.load("models/map parts/lobby/2.png")
lob3 = pygame.image.load("models/map parts/lobby/3.png")
lob4 = pygame.image.load("models/map parts/lobby/4.png")

while True:

	screen.fill(0)

	keys = pygame.key.get_pressed()
	if keys[K_w]:
		b += 3
	if keys[K_a]:
		a += 5
	if keys[K_s]:
		b -= 3
	if keys[K_d]:
		a -= 5

	screen.blit(lob1, (-125+a, 0+b))
	screen.blit(lob2, (153+a, 617+b))
	screen.blit(lob3, (311+a, 279+b))
	screen.blit(lob4, (880+a+random.random()*10, 728+b+random.random()))
	screen.blit(pygame.transform.rotate(lob4, 25), (-104+a+random.random()*10, 702+b+random.random()))

	coll_pos = [(202, 294, 10, 341), (204, 289, 10, 10), (223, 281, 10, 10), (241, 272, 10, 10), (255, 262, 10, 10), (276, 256, 10, 10), (290, 249, 10, 10), (306, 245, 10, 10), (322, 240, 10, 10), (332, 235, 10, 10), (350, 228, 10, 10), (368, 223, 10, 10),
				(376, 223, 214, 10), (589, 224, 10, 10), (606, 230, 10, 10), (629, 236, 10, 10), (643, 245, 10, 10), (661, 254, 10, 10), (676, 259, 10, 10), (692, 264, 10, 10), (708, 271, 10, 10), (726, 278, 10, 10), (740, 287, 10, 10), (752, 294, 10, 10), (765, 299, 10, 10),
				(765, 303, 10, 290), (213, 613, 10, 10), (223, 628, 10, 10), (231, 642, 10, 10), (243, 652, 477, 10), (728, 645, 10, 10), (742, 631, 10, 10), (753, 616, 10, 10), (765, 601, 10, 10)]
	for i in coll_pos:
		clo = pygame.surface.Surface([i[2], i[3]])
		clo.fill((255,0,0))
		screen.blit(clo, (i[0]+a, i[1]+b))

	clo = pygame.surface.Surface([100, 60])
	clo.fill((255,0,0))
	screen.blit(clo, pygame.mouse.get_pos())

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos()[0]-a, pygame.mouse.get_pos()[1]-b)

	pygame.display.update()
	clock.tick(fps)