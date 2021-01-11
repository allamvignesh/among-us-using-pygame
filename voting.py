import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)

vs1 = pygame.image.load('models/voting/1.png')
vs2 = pygame.image.load('models/voting/2.png')
vs3 = pygame.image.load('models/voting/3.png')
vs4 = pygame.image.load('models/voting/4.png')

qwe = -10
voted = -10

Names = []
for i in range(10):
	name = ''
	for i in [random.randint(65,122) for i in range(5)]:
		name += chr(i)
	Names.append(name)

print(Names)
while True:
	screen.fill(0)

	screen.blit(vs1, (77, -10))

	z = -1
	for i in Names:

		z += 1

		if z < 5:
			screen.blit(vs2, (121, 100+74*z))
			screen.blit(vs4, (128, 106+74*z))
			if 121 < pygame.mouse.get_pos()[0] < 467 and 100+74*z < pygame.mouse.get_pos()[1] < 160+74*z:
				if pygame.mouse.get_pressed()[0]:
					qwe = z+1
		if z >= 5:
			screen.blit(vs2, (491, 100+74*(z-5)))
			screen.blit(vs4, (491, 106+74*(z-5)))
			if 491 < pygame.mouse.get_pos()[0] < 838 and 100+74*(z-5) < pygame.mouse.get_pos()[1] < 160+74*(z-5):
				if pygame.mouse.get_pressed()[0]:
					qwe = 6+z-5

		if qwe <= 5:
			screen.blit(vs3, (354, 105+74*(qwe-1)))
			if 355 < pygame.mouse.get_pos()[0] < 403 and 105+74*(qwe-1) < pygame.mouse.get_pos()[1] < 105+74*(qwe-1)+50:
				if pygame.mouse.get_pressed()[0]:
					voted = qwe
			if 410 < pygame.mouse.get_pos()[0] < 460 and 105+74*(qwe-1) < pygame.mouse.get_pos()[1] < 105+74*(qwe-1)+50:
				if pygame.mouse.get_pressed()[0]:
					qwe = -10
		if qwe > 5:
			screen.blit(vs3, (728, 105+74*(qwe-1-5)))
			if 728 < pygame.mouse.get_pos()[0] < 778 and 105+74*(qwe-6) < pygame.mouse.get_pos()[1] < 105+74*(qwe-6)+50:
				if pygame.mouse.get_pressed()[0]:
					voted = qwe
			if 781 < pygame.mouse.get_pos()[0] < 829 and 105+74*(qwe-6) < pygame.mouse.get_pos()[1] < 105+74*(qwe-6)+50:
				if pygame.mouse.get_pressed()[0]:
					qwe = -10

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos())

	pygame.display.update()
	clock.tick(fps)