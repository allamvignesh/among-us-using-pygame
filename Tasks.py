import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)

def swipeCard():
	spbg = pygame.image.load("models/tasks/Swipe Card/admin_BG.png")
	spbg1 = pygame.image.load("models/tasks/Swipe Card/admin_sliderTop.png")
	spbg2 = pygame.image.load("models/tasks/Swipe Card/admin_sliderBottom.png")
	spbg3 = pygame.image.load("models/tasks/Swipe Card/admin_Wallet.png")
	spbg4 = pygame.image.load("models/tasks/Swipe Card/admin_walletFront.png")
	spbg5 = pygame.image.load("models/tasks/Swipe Card/admin_Card.png")

	doing = 0
	swipeDon = 0

	while swipeDon == 0:
		screen.fill((0, 0, 0, 5))

		screen.blit(spbg, (259, 32))
		screen.blit(spbg2, (259, 169))
		screen.blit(spbg3, (268, 363))
		
		#(201, 150), (633, 150)
		#screen.blit(spbg5, pygame.mouse.get_pos())
		if 286 < pygame.mouse.get_pos()[0] < 507 and pygame.mouse.get_pressed()[0]:
			doing = 1
		
		if doing == 1:
			if pygame.mouse.get_pressed()[0]:
				if 201 < pygame.mouse.get_pos()[0] < 700 and 150 < pygame.mouse.get_pos()[1] < 250:
					screen.blit(spbg5, (pygame.mouse.get_pos()[0], 150))
					if 600 < pygame.mouse.get_pos()[0] < 680:
						swipeDon = 1
			else:
				screen.blit(spbg5, (201, 150))
		else:
			screen.blit(spbg5, (285, 376))

		screen.blit(spbg1, (259, 32))
		screen.blit(spbg4, (279, 446))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()
		clock.tick(fps)

while True:

	swipeCard()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	pygame.display.update()
	clock.tick(fps)
