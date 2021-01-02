import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)
close = pygame.image.load("models/buttons/close.png")

def swipeCard():

	spbg = pygame.image.load("models/tasks/Swipe Card/admin_BG.png")
	spbg1 = pygame.image.load("models/tasks/Swipe Card/admin_sliderTop.png")
	spbg2 = pygame.image.load("models/tasks/Swipe Card/admin_sliderBottom.png")
	spbg3 = pygame.image.load("models/tasks/Swipe Card/admin_Wallet.png")
	spbg4 = pygame.image.load("models/tasks/Swipe Card/admin_walletFront.png")
	spbg5 = pygame.image.load("models/tasks/Swipe Card/admin_Card.png")

	doing = 0
	swipeDon = 0

	while True:
		screen.fill((0, 0, 0, 5))

		screen.blit(spbg, (259, 32))
		screen.blit(spbg2, (259, 169))
		screen.blit(spbg3, (268, 363))

		screen.blit(close, (100, 25))

		if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
			return 0

		if 286 < pygame.mouse.get_pos()[0] < 507 and pygame.mouse.get_pressed()[0]:
			doing = 1
		
		if doing == 1:
			if pygame.mouse.get_pressed()[0]:
				if 201 < pygame.mouse.get_pos()[0] < 700 and 150 < pygame.mouse.get_pos()[1] < 250:
					screen.blit(spbg5, (pygame.mouse.get_pos()[0], 150))
					if 600 < pygame.mouse.get_pos()[0] < 680:
						return 1
			else:
				screen.blit(spbg5, (201, 150))
		else:
			screen.blit(spbg5, (285, 376))

		screen.blit(spbg1, (259, 32))
		screen.blit(spbg4, (279, 446))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0

		pygame.display.update()
		clock.tick(fps)

def fixWiring():

	fw1 = pygame.image.load("models/tasks/Fix Wiring/electricity_wiresBaseBack.png")
	fw2 = pygame.image.load("models/tasks/Fix Wiring/electricity_wires1.png")
	fw3 = pygame.image.load("models/tasks/Fix Wiring/electricity_wires1.png")

	red, green, blue, yellow = 0, 0, 0, 0

	while True:

		screen.fill((0, 0, 0))

		screen.blit(fw1, (264, 28))
		if 269 < pygame.mouse.get_pos()[0] < 300 and 130 < pygame.mouse.get_pos()[1] < 200 and pygame.mouse.get_pressed()[0] and red != 2:
			red = 1
		elif 269 < pygame.mouse.get_pos()[0] < 300 and 230 < pygame.mouse.get_pos()[1] < 300 and pygame.mouse.get_pressed()[0] and green != 2:
			green = 1
		elif 269 < pygame.mouse.get_pos()[0] < 300 and 335 < pygame.mouse.get_pos()[1] < 400 and pygame.mouse.get_pressed()[0] and blue != 2:
			blue = 1
		elif 269 < pygame.mouse.get_pos()[0] < 300 and 440 < pygame.mouse.get_pos()[1] < 500 and pygame.mouse.get_pressed()[0] and yellow != 2:
			yellow = 1

		if red == 1:
			pygame.draw.line(screen, (255, 0, 0), (269, 130), pygame.mouse.get_pos(), 20)
			#(735, 129)
			if 735 < pygame.mouse.get_pos()[0] < 800 and 130 < pygame.mouse.get_pos()[1] < 200 and pygame.mouse.get_pressed()[0]:
				red = 2
				redpos = pygame.mouse.get_pos()
			screen.blit(fw2, (pygame.mouse.get_pos()[0]-5, pygame.mouse.get_pos()[1]-10))
		elif green == 1:
			pygame.draw.line(screen, (0, 255, 0), (269, 230), pygame.mouse.get_pos(), 20)
			if 735 < pygame.mouse.get_pos()[0] < 800 and 230 < pygame.mouse.get_pos()[1] < 300 and pygame.mouse.get_pressed()[0]:
				green = 2
				greenpos = pygame.mouse.get_pos()
			screen.blit(fw2, (pygame.mouse.get_pos()[0]-5, pygame.mouse.get_pos()[1]-10))
		elif blue == 1:
			pygame.draw.line(screen, (0, 0, 255), (269, 335), pygame.mouse.get_pos(), 20)
			if 735 < pygame.mouse.get_pos()[0] < 800 and 335 < pygame.mouse.get_pos()[1] < 400 and pygame.mouse.get_pressed()[0]:
				blue = 2
				bluepos = pygame.mouse.get_pos()
			screen.blit(fw2, (pygame.mouse.get_pos()[0]-5, pygame.mouse.get_pos()[1]-10))
		elif yellow == 1:
			pygame.draw.line(screen, (255, 255, 0), (269, 440), pygame.mouse.get_pos(), 20)
			if 735 < pygame.mouse.get_pos()[0] < 800 and 440 < pygame.mouse.get_pos()[1] < 500 and pygame.mouse.get_pressed()[0]:
				yellow = 2
				yellowpos = pygame.mouse.get_pos()
			screen.blit(fw2, (pygame.mouse.get_pos()[0]-5, pygame.mouse.get_pos()[1]-10))

		if red == 2:
			pygame.draw.line(screen, (255, 0, 0), (269, 130), redpos, 20)
			screen.blit(fw2, (redpos[0]-10, redpos[1]-10))
		if green == 2:
			pygame.draw.line(screen, (0, 255, 0), (269, 230), greenpos, 20)
			screen.blit(fw2, (greenpos[0]-10, greenpos[1]-10))
		if blue == 2:
			pygame.draw.line(screen, (0, 0, 255), (269, 335), bluepos, 20)
			screen.blit(fw2, (bluepos[0]-10, bluepos[1]-10))
		if yellow == 2:
			pygame.draw.line(screen, (255, 255, 0), (269, 440), yellowpos, 20)
			screen.blit(fw2, (yellowpos[0]-10, yellowpos[1]-10))

		if red == green == blue == yellow == 2:
			return 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0

		pygame.display.update()
		clock.tick(fps)

def emptyGarbage():
	eg1 = pygame.image.load("models/tasks/Empty Garbage/garbage_Base.png")
	eg2 = pygame.image.load("models/tasks/Empty Garbage/garbage_lightShadow.png")
	eg3 = pygame.image.load("models/tasks/Empty Garbage/button.png")
	eg4 = pygame.image.load("models/tasks/Empty Garbage/garbage_leverBars.png")
	eg5 = pygame.image.load("models/tasks/Empty Garbage/garbage_leverHandle.png")

	gar1 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/diamond.png")
	gar2 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/garbage_1.png")
	gar3 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/garbage_2.png")
	gar4 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/garbage_3.png")
	gar5 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/garbage_4.png")
	gar6 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/garbage_5.png")
	gar7 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/garbage_6.png")
	gar8 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/teleporter.png")
	gar9 = pygame.image.load("models/tasks/Empty Garbage/Nova pasta/totem.png")

	garPos = []
	garba = [gar1, gar2, gar3, gar4, gar5, gar6, gar7, gar8, gar9]

	for i in range(1,20):
			garPos.append([garba[random.randint(0,8)], [random.randint(261, 539), random.randint(270, 469)]])
	while True:
		screen.blit(eg1, (256, 28))
		screen.blit(eg2, (259, 32))
		if 652 < pygame.mouse.get_pos()[0] < 717 and 63 < pygame.mouse.get_pos()[1] < 168 and pygame.mouse.get_pressed()[0]:
			screen.blit(eg3, (651, 68))
			tot = 0
			for i in range(len(garPos)):
				garPos[i][1][1] += 5
				tot += garPos[i][1][1]
			if tot > 550 * len(garPos):
				return 1

		else:
			screen.blit(eg3, (651, 60))

		for i in garPos:
			screen.blit(i[0], i[1])

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0

		pygame.display.update()
		clock.tick(fps)

Tasks = [1, 1, 0]
while True:

	screen.fill((255, 0, 0))

	if Tasks[0] == 0:
		Tasks[0] = swipeCard()
	elif Tasks[1] == 0:
		Tasks[1] = fixWiring()
	elif Tasks[2] == 0:
		Tasks[2] = emptyGarbage()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	pygame.display.update()
	clock.tick(fps)
