import pygame
from pygame.locals import *
import random

if __name__ == '__main__':
	pygame.init()

	clock = pygame.time.Clock()
	fps = 50
	size =[1000, 550]
	screen = pygame.display.set_mode(size)

	#swipe card
	spbg = pygame.image.load("models/tasks/Swipe Card/admin_BG.png")
	spbg1 = pygame.image.load("models/tasks/Swipe Card/admin_sliderTop.png")
	spbg2 = pygame.image.load("models/tasks/Swipe Card/admin_sliderBottom.png")
	spbg3 = pygame.image.load("models/tasks/Swipe Card/admin_Wallet.png")
	spbg4 = pygame.image.load("models/tasks/Swipe Card/admin_walletFront.png")
	spbg5 = pygame.image.load("models/tasks/Swipe Card/admin_Card.png")

	doing = 0
	swipeDon = 1

	#fixwiring
	fixWirDon = 1
	fw1 = pygame.image.load("models/tasks/Fix Wiring/electricity_wiresBaseBack.png")
	fw2 = pygame.image.load("models/tasks/Fix Wiring/electricity_wires1.png")
	fw3 = pygame.image.load("models/tasks/Fix Wiring/electricity_wires1.png")

	red, green, blue, yellow = 0, 0, 0, 0

	#empty garbage
	EGDon = 1
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

	#upload
	uplDon = 301
	down = 1
	man = 1
	speed = 0
	Download = 1
	up1 = pygame.image.load("models/tasks/Upload Data/dataTransfer_Base.png")
	up2 = pygame.image.load("models/tasks/Upload Data/dataTransfer_progressBar.png")
	up3 = pygame.image.load("models/tasks/Upload Data/dataTransfer_downloadButton.png")
	up4 = pygame.image.load("models/tasks/Upload Data/dataTransfer_folderOpen0001.png")
	up4 = pygame.transform.scale(up4, (10, 10))
	up5 = pygame.image.load("models/tasks/Upload Data/dataTransfer_uploadButton.png")

	#leaves
	cllevDon = 0
	tot = 0
	cllev1 = pygame.image.load("models/tasks/Clean O2 Filter/o2_bgBase.png")
	cllev2 = pygame.image.load("models/tasks/Clean O2 Filter/o2_bgTop.png")

	levPos = [(random.randint(390, 649), random.randint(109, 400)) for i in range(7)]
	leaves = [pygame.image.load(f"models/tasks/Clean O2 Filter/o2_leafs/o2_leaf{i}.png") for i in range(1,8)]


	while True:
		screen.fill((255, 255, 255))

		#swipecard
		if swipeDon == 0:
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

		if fixWirDon == 0:
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
				fixWirDon = 1

		if EGDon == 0:
			screen.blit(eg1, (256, 28))
			screen.blit(eg2, (259, 32))
			if 652 < pygame.mouse.get_pos()[0] < 717 and 63 < pygame.mouse.get_pos()[1] < 168 and pygame.mouse.get_pressed()[0]:
				screen.blit(eg3, (651, 68))
				tot = 0
				for i in range(len(garPos)):
					garPos[i][1][1] += 5
					tot += garPos[i][1][1]
				if tot > 550 * len(garPos):
					EGDon = 1

			else:
				screen.blit(eg3, (651, 60))

			for i in garPos:
				screen.blit(i[0], i[1])

		if uplDon <= 300:
			screen.blit(up1, (256, 90))
			screen.blit(up2, (316, 288))
			screen.blit(up3, (462, 316))
			if 465 < pygame.mouse.get_pos()[0] < 553 and 321 < pygame.mouse.get_pos()[1] < 340 and pygame.mouse.get_pressed()[0]:
				down = 0
			if down == 0:
				uplDon += 1 #360, 636
				if Download != 1:
					screen.blit(pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(man)}.png"), (360+speed,191))
				else:
					screen.blit(pygame.transform.flip(pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(man)}.png"), True, False), (636-speed,191))
				man += 0.5
				speed += 5
				if speed > 250:
					speed = 0
				print(speed)
				if man == 13:
					man = 1
				screen.blit(pygame.transform.scale(up4, (10*(uplDon//8), 10)), (319, 291))
			if down != 0:
				if Download != 1:
					screen.blit(up4, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
				else:
					screen.blit(up5, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

		if cllevDon == 0:
			screen.blit(cllev1, (263, 29))
			for i in range(len(leaves)):
				if levPos[i][0] < pygame.mouse.get_pos()[0] < levPos[i][0]+100:
					if levPos[i][1] < pygame.mouse.get_pos()[1] < levPos[i][1]+100:
						if pygame.mouse.get_pressed()[0]:
							levPos[i] = pygame.mouse.get_pos()[0]-50, pygame.mouse.get_pos()[1]-50
				if levPos[i][0] < 309 and 157 < levPos[i][1] < 340:
					levPos[i] = (0, -200)
					tot += 1

				screen.blit(leaves[i], levPos[i])
				screen.blit(cllev2, (263, 29))
			if tot == 7:
				cllevDon = 1


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(pygame.mouse.get_pos())
				pass
		pygame.display.update()
		clock.tick(fps)