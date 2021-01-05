import pygame
from pygame.locals import *
import random, math, numpy

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)
close = pygame.image.load("models/buttons/close.png")

class Tasks():
	def __init__(self):
		self.tasks = [0 for i in range(20)]
		self.tasks = [1 for i in range(20)]
		#print(self.tasks)
	
	def blitRotate(self, surf, image, pos, originPos, angle):

	    # calcaulate the axis aligned bounding box of the rotated image
	    w, h       = image.get_size()
	    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
	    box_rotate = [p.rotate(angle) for p in box]
	    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
	    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

	    # calculate the translation of the pivot 
	    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
	    pivot_rotate = pivot.rotate(angle)
	    pivot_move   = pivot_rotate - pivot

	    # calculate the upper left origin of the rotated image
	    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

	    # get a rotated image
	    rotated_image = pygame.transform.rotate(image, angle)

	    # rotate and blit the image
	    surf.blit(rotated_image, origin)
	  
	    # draw rectangle around the image
	    #pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)

	def draw_dashed_line(self, surf, color, start_pos, end_pos, width=5, dash_length=10):
		x1, y1 = start_pos
		x2, y2 = end_pos
		dl = dash_length

		if (x1 == x2):
			ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
			xcoords = [x1] * len(ycoords)
		elif (y1 == y2):
			xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
			ycoords = [y1] * len(xcoords)
		else:
			a = abs(x2 - x1)
			b = abs(y2 - y1)
			c = round(math.sqrt(a**2 + b**2))
			dx = dl * a / c
			dy = dl * b / c

			xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
			ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

		next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
		last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
		for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
			start = (round(x1), round(y1))
			end = (round(x2), round(y2))
			pygame.draw.line(surf, color, start, end, width)

	def swipeCard(self):

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
							self.tasks[0] = 1
							return 1
				else:
					screen.blit(spbg5, (201, 150))
			else:
				screen.blit(spbg5, (285, 376))

			screen.blit(spbg1, (259, 32))
			screen.blit(spbg4, (279, 446))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[0] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def fixWiring(self):

		fw1 = pygame.image.load("models/tasks/Fix Wiring/electricity_wiresBaseBack.png")
		fw2 = pygame.image.load("models/tasks/Fix Wiring/electricity_wires1.png")
		fw3 = pygame.image.load("models/tasks/Fix Wiring/electricity_wires1.png")

		red, green, blue, yellow = 0, 0, 0, 0

		while True:

			screen.fill((0, 0, 0))

			screen.blit(fw1, (264, 28))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
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
				self.tasks[1] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[1] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def emptyGarbage(self):
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
			screen.fill((0, 0, 0, 5))
			screen.blit(eg1, (256, 28))
			screen.blit(eg2, (259, 32))

			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				self.tasks[2] = 0
				return 0

			if 652 < pygame.mouse.get_pos()[0] < 717 and 63 < pygame.mouse.get_pos()[1] < 168 and pygame.mouse.get_pressed()[0]:
				screen.blit(eg3, (651, 68))
				tot = 0
				for i in range(len(garPos)):
					garPos[i][1][1] += 5
					tot += garPos[i][1][1]
				if tot > 550 * len(garPos):
					self.tasks[2] = 1
					return 1

			else:
				screen.blit(eg3, (651, 60))

			for i in garPos:
				screen.blit(i[0], i[1])

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[2] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def upload(self, Download = 0):
		#upload
		uplDon = 0
		down = 1
		man = 1
		speed = 0
		up1 = pygame.image.load("models/tasks/Upload Data/dataTransfer_Base.png")
		up2 = pygame.image.load("models/tasks/Upload Data/dataTransfer_progressBar.png")
		up3 = pygame.image.load("models/tasks/Upload Data/dataTransfer_downloadButton.png")
		up4 = pygame.image.load("models/tasks/Upload Data/dataTransfer_folderOpen0001.png")
		up4 = pygame.transform.scale(up4, (10, 10))
		up5 = pygame.image.load("models/tasks/Upload Data/dataTransfer_uploadButton.png")

		while uplDon <= 300:
			screen.fill((0, 0, 0))
			screen.blit(up1, (256, 90))
			screen.blit(up2, (316, 288))
			screen.blit(up3, (462, 316))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				self.tasks[3] = 1
				return 0

			if Download == 1:
				screen.blit(up5, (462, 316))
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
				if man == 13:
					man = 1
				screen.blit(pygame.transform.scale(up4, (10*(uplDon//8), 10)), (319, 291))
			'''if down != 0:
				if Download != 1:
					screen.blit(up4, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
				else:
					screen.blit(up5, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))'''

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[3] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)
		self.tasks[3] = 1
		return 1
	def Download(self, Download):
		#upload
		uplDon = 0
		down = 1
		man = 1
		speed = 0
		up1 = pygame.image.load("models/tasks/Upload Data/dataTransfer_Base.png")
		up2 = pygame.image.load("models/tasks/Upload Data/dataTransfer_progressBar.png")
		up3 = pygame.image.load("models/tasks/Upload Data/dataTransfer_downloadButton.png")
		up4 = pygame.image.load("models/tasks/Upload Data/dataTransfer_folderOpen0001.png")
		up4 = pygame.transform.scale(up4, (10, 10))
		up5 = pygame.image.load("models/tasks/Upload Data/dataTransfer_uploadButton.png")

		while uplDon <= 300:
			screen.fill((0, 0, 0))
			screen.blit(up1, (256, 90))
			screen.blit(up2, (316, 288))
			screen.blit(up3, (462, 316))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				self.tasks[4] = 1
				return 0

			if Download == 1:
				screen.blit(up5, (462, 316))
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
				if man == 13:
					man = 1
				screen.blit(pygame.transform.scale(up4, (10*(uplDon//8), 10)), (319, 291))
			'''if down != 0:
				if Download != 1:
					screen.blit(up4, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
				else:
					screen.blit(up5, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))'''

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[4] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)
		self.tasks[4] = 1
		return 1

	def clearLeaves(self):
		tot = 0
		cllev1 = pygame.image.load("models/tasks/Clean O2 Filter/o2_bgBase.png")
		cllev2 = pygame.image.load("models/tasks/Clean O2 Filter/o2_bgTop.png")

		levPos = [(random.randint(390, 649), random.randint(109, 400)) for i in range(7)]
		leaves = [pygame.image.load(f"models/tasks/Clean O2 Filter/o2_leafs/o2_leaf{i}.png") for i in range(1,8)]

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(cllev1, (263, 29))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
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
				self.tasks[5] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[5] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def alignEngine(self):
		enDon = 1
		enp = [132, 205]
		count = 1
		en1 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_base.png")
		en2 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_slider.png")
		en3 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_engine.png")
		en4 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_engine_green.png")
		en5 = pygame.image.load("models/tasks/Align Engine Output/green.png")

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(en5, (286, 54))
			screen.blit(en1, (253, 22))
			screen.blit(en4, (220, 170))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			if pygame.mouse.get_pressed()[0] and 126 < pygame.mouse.get_pos()[1] < 379 and 614 < pygame.mouse.get_pos()[0] < 687:
				if enp[1]-20 < pygame.mouse.get_pos()[1] < enp[1]+20:
					enp[1] = pygame.mouse.get_pos()[1]
				if 240 < pygame.mouse.get_pos()[1] < 260:
					count += 1
					if count == 100:
						self.tasks[6] = 1
						return 1
				else:
					count = 0
			screen.blit(en2, (611, enp[1]))
			screen.blit(en3, (220, enp[1]-73))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[6] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def calibrate(self):
		calDon = 1
		cal1 = pygame.image.load("models/tasks/Calibrate Distributor/CalibratorBaseWWires.png")
		cal2 = pygame.image.load("models/tasks/Calibrate Distributor/calibratorButton.png")
		cal3 = pygame.image.load("models/tasks/Calibrate Distributor/calibratorGauge.png")
		cal4 = pygame.image.load("models/tasks/Calibrate Distributor/calibratorSpin1.png")
		w, h = cal4.get_size()
		angles = [random.randint(0, 360) for i in range(3)]
		angle1, angle2, angle3 = [random.randint(0, 132) for i in range(3)]
		calDoing = [0, 0, 0]
		cal5 = pygame.image.load("models/tasks/Calibrate Distributor/calibratorSpin2.png")
		cal6 = pygame.image.load("models/tasks/Calibrate Distributor/calibratorSpin3.png")

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(cal1, (258, 24))
			screen.blit(cal2, (609, 124))
			screen.blit(cal2, (609, 271))
			screen.blit(cal2, (609, 421))
			screen.blit(cal3, (597, 385))
			screen.blit(cal3, (597, 231))
			screen.blit(cal3, (597, 82))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0

			if calDoing[0] == 0:
				angle1 += 1
				if angle1 > 132:
					angle1 = 0
			yellow = pygame.surface.Surface([angle1, 32])
			yellow.fill((255, 255, 0))
			screen.blit(yellow, (597, 82))
			if calDoing[1] == 0:
				angle2 += 1
				if angle2 > 132:
					angle2 = 0
			blue = pygame.surface.Surface([angle2, 32])
			blue.fill((0, 102, 204))
			screen.blit(blue, (597, 231))
			if calDoing[2] == 0:
				angle3 += 1
				if angle3 > 132:
					angle3 = 0
			cyan = pygame.surface.Surface([angle3, 32])
			cyan.fill((102, 255, 255))
			screen.blit(cyan, (597, 385))
			angles = [i+1 if i !=360 else 0 for i in angles]
			if calDoing[0] == 0:
				self.blitRotate(screen, cal4, (369, 123), (w/2, h/2), angles[0])
			else:
				self.blitRotate(screen, cal4, (369, 123), (w/2, h/2), 0)
			if calDoing[1] == 0:
				self.blitRotate(screen, cal5, (369, 276), (w/2, h/2), angles[1])
			else:
				self.blitRotate(screen, cal5, (369, 276), (w/2, h/2), 0)
			if calDoing[2] == 0:
				self.blitRotate(screen, cal6, (369, 422), (w/2, h/2), angles[2])
			else:
				self.blitRotate(screen, cal6, (369, 422), (w/2, h/2), 0)

			if 612 < pygame.mouse.get_pos()[0] < 716 and 128 < pygame.mouse.get_pos()[1] < 152 and calDoing[0] == 0:
				if pygame.mouse.get_pressed()[0]:
					screen.blit(cal2, (609, 130))
					##print(angles[0]/360)
					if 0.1 < angles[0]/360 < 0.9:
						angles = [random.randint(0, 360) for i in range(3)]
						calDoing = [0 for i in range(3)]
					else:
						if calDoing[1] == calDoing[2] == 0:
							calDoing[0] = 1
				else:
					screen.blit(cal2, (609, 124))

			elif 612 < pygame.mouse.get_pos()[0] < 716 and 276 < pygame.mouse.get_pos()[1] < 300 and calDoing[1] == 0:
				if pygame.mouse.get_pressed()[0]:
					screen.blit(cal2, (609, 278))
					if 0.1 < angles[1]/360 < 0.9:
						angles = [random.randint(0, 360) for i in range(3)]
						calDoing = [0 for i in range(3)]
					else:
						if calDoing[0] == 1 and calDoing[2] == 0:
							calDoing[1] = 1
				else:
					screen.blit(cal2, (609, 271))

			elif 612 < pygame.mouse.get_pos()[0] < 716 and 427 < pygame.mouse.get_pos()[1] < 450 and calDoing[2] == 0:
				if pygame.mouse.get_pressed()[0]:
					screen.blit(cal2, (609, 427))
					if 0.1 < angles[2]/360 < 0.9:
						angles = [random.randint(0, 360) for i in range(3)]
						calDoing = [0 for i in range(3)]
					else:
						if calDoing[0] == calDoing[1] == 1:
							calDoing[2] = 1
				else:
					screen.blit(cal2, (609, 421))
			if calDoing[0] == calDoing[1] == calDoing[2] == 1:
				self.tasks[7] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[7] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def chartCourse(self):
		ccDon = 1
		cc1 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_base.png")
		cc2 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_checkPt.png")
		cc3 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_checkPtShadow.png")
		cc4 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_end.png")
		cc5 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_endShadow.png")
		cc6 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_ship.png")
		cc7 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_start.png")
		cc8 = pygame.image.load("models/tasks/Chart Course/nav_chartCourse_startShadow.png")
		angle = 0
		ccpos = [344, 430, 507, 597, 673]
		ccPos = [(i, random.randint(178, 353)) for i in ccpos]
		ship = [0, 0, 0, 0, 0]

		while True:
			screen.fill((0, 0, 0, 5))
			angle += 1
			screen.blit(cc1, (253, 118))

			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0

			for i in ccPos[1:]:
				screen.blit(cc2, (i[0]-cc2.get_size()[0]//2, i[1]-cc2.get_size()[1]//2))
				screen.blit(cc8, (i[0]-cc7.get_size()[0]//2, i[1]-cc7.get_size()[1]//2))
			screen.blit(cc7, (ccPos[0][0]-cc7.get_size()[0]//2, ccPos[0][1]-cc7.get_size()[1]//2))
			self.blitRotate(screen , cc4, ccPos[-1], (cc4.get_size()[0]//2, cc4.get_size()[1]//2), angle)
			for i in range(len(ccPos)-1):
				self.draw_dashed_line(screen, (0, 0, 0), ccPos[i], ccPos[i+1])

			if ship[0] == 0:
				screen.blit(cc6, (ccPos[0][0]-17, ccPos[0][1]-22))
				if ccPos[0][0]-20 < pygame.mouse.get_pos()[0] < ccPos[0][0]+20 and ccPos[0][1]-20 < pygame.mouse.get_pos()[1] < ccPos[0][1]+20:
					if pygame.mouse.get_pressed()[0]:
						ship[0] = 1
			elif ship[1] == 0:
				screen.blit(cc6, (ccPos[1][0]-17, ccPos[1][1]-22))
				if ccPos[1][0]-20 < pygame.mouse.get_pos()[0] < ccPos[1][0]+20 and ccPos[1][1]-20 < pygame.mouse.get_pos()[1] < ccPos[1][1]+20:
					if pygame.mouse.get_pressed()[0]:
						ship[1] = 1
			elif ship[2] == 0:
				screen.blit(cc6, (ccPos[2][0]-17, ccPos[2][1]-22))
				if ccPos[2][0]-20 < pygame.mouse.get_pos()[0] < ccPos[2][0]+20 and ccPos[2][1]-20 < pygame.mouse.get_pos()[1] < ccPos[2][1]+20:
					if pygame.mouse.get_pressed()[0]:
						ship[2] = 1
			elif ship[3] == 0:
				screen.blit(cc6, (ccPos[3][0]-17, ccPos[3][1]-22))
				if ccPos[3][0]-20 < pygame.mouse.get_pos()[0] < ccPos[3][0]+20 and ccPos[3][1]-20 < pygame.mouse.get_pos()[1] < ccPos[3][1]+20:
					if pygame.mouse.get_pressed()[0]:
						ship[3] = 1
			else:
				self.tasks[8] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[8] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def weapons(self):
		waDon = 1
		wa1 = pygame.image.load("models/tasks/Clear Asteroids/weapons_base.png")
		wa2 = pygame.image.load("models/tasks/Clear Asteroids/weapons_target.png")
		ast1 = pygame.image.load("models/tasks/Clear Asteroids/weapons_asteroid1.png")
		ast2 = pygame.image.load("models/tasks/Clear Asteroids/weapons_asteroid2.png")
		ast3 = pygame.image.load("models/tasks/Clear Asteroids/weapons_asteroid3.png")
		ast4 = pygame.image.load("models/tasks/Clear Asteroids/weapons_asteroid4.png")
		ast5 = pygame.image.load("models/tasks/Clear Asteroids/weapons_asteroid5.png")
		((322,92), (674, 453))
		astPos = [[(i*322)+322*2, random.randint(92, 400)] for i in range(10)]
		tarPos = [wa1.get_size()[0]//2 + 247, wa1.get_size()[1]//2 + 23]
		asDes = 0

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(wa1, (247, 23))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0

			for i in range(len(astPos)):
				astPos[i][0] -= 5
			
			if  277 < astPos[0][0] < 660:
				screen.blit(ast1, astPos[0])
			if  277 < astPos[5][0] < 660:
				screen.blit(ast1, astPos[5])
			if  277 < astPos[1][0] < 660:
				screen.blit(ast2, astPos[1])
			if  277 < astPos[6][0] < 660:
				screen.blit(ast2, astPos[6])
			if  277 < astPos[2][0] < 660:
				screen.blit(ast3, astPos[2])
			if  277 < astPos[7][0] < 660:
				screen.blit(ast3, astPos[7])
			if  277 < astPos[3][0] < 660:
				screen.blit(ast4, astPos[3])
			if  277 < astPos[8][0] < 660:
				screen.blit(ast4, astPos[8])
			if  277 < astPos[4][0] < 660:
				screen.blit(ast5, astPos[4])
			if  277 < astPos[9][0] < 660:
				screen.blit(ast5, astPos[9])
			if 322 < pygame.mouse.get_pos()[0] < 674 and 92 < pygame.mouse.get_pos()[1] < 453: 
				if pygame.mouse.get_pressed()[0]:
					tarPos = pygame.mouse.get_pos()
					for i in range(len(astPos)):
						if astPos[i][0] < tarPos[0] < astPos[i][0]+100 and astPos[i][1] < tarPos[1] < astPos[i][1]+100:
							astPos[i] = [0, -200]
							asDes += 1
			screen.blit(wa2, (tarPos[0] - wa2.get_size()[0]//2, tarPos[1] - wa2.get_size()[1]//2))

			if asDes > 9:
				self.tasks[9] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[9] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def divertPower(self, station):
		dpDon = 1
		dp1 = pygame.image.load("models/tasks/Divert Power/electricity_Divert_Base.png")
		dp2 = pygame.image.load("models/tasks/Divert Power/electricity_Divert_switch.png")
		dpBut = [[288+54*i, 387] for i in range(8)]
		dpto = [0, 0, 0, 0, 0, 0, 0, 0]
		dpto[station] = 1
		to = 0

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(dp1, (249, 26))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			for i in dpBut:
				ind = dpBut.index(i)
				if dpto[ind] == 1:
					if i[0] < pygame.mouse.get_pos()[0] < i[0]+45 and i[1] < pygame.mouse.get_pos()[1] < i[1]+30:
						if pygame.mouse.get_pressed()[0]:
							dpBut[ind][1] = pygame.mouse.get_pos()[1]-15
							if dpBut[ind][1] < 350:
								dpto[ind] = 0
							if dpBut[ind][1] > 450:
								dpBut[ind][1] = 445
				screen.blit(dp2, i)
			for i in range(len(dpto)):
				if dpto[i] == 1:
					to = i
				sur = pygame.surface.Surface([15, 50])
				sur.fill((255, 255, 0)) #301, 227, 354, 228
				screen.blit(sur, (305 + i*54, 227))
			if dpto[to] == 0:
				screen.blit(sur, (305 + to*54, 200))
				self.tasks[10] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[10] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def fualEngine(self):
		feDon = 1
		fe1 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_fillBase.png")
		fe2 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_wires.png")
		fe3 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_buttonBase.png")
		fe4 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_Button.png")
		fe5 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_Light.png")
		fe6 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_LightRed.png")
		en = 0

		while True:
			screen.fill((0, 0, 0))
			sur = pygame.surface.Surface([90, 65])
			sur.fill((255, 255, 0))
			screen.blit(sur, (498+en, 45))
			#444, 118, 527, 432
			sur = pygame.surface.Surface([83, 314])
			sur.fill((255, 255, 0))
			screen.blit(sur, (444, 432-int(en)*5))
			screen.blit(fe1, (324, 23))
			if 432-int(en)*5 < 118:
				self.tasks[11] = 1
				return 1
			screen.blit(fe2, (661, 397))
			screen.blit(fe3, (711, 356))
			screen.blit(fe4, (735, 379))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			if 735 < pygame.mouse.get_pos()[0] < 811 and 379 < pygame.mouse.get_pos()[1] < 456:
				if pygame.mouse.get_pressed()[0]:
					screen.blit(fe4, (735, 382))
					en += 0.5
			screen.blit(fe5, (777, 335))
			screen.blit(fe6, (741, 335))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[11] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def fillCan(self):
		en = 0
		fe1 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_fillBase.png")
		fe2 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_wires.png")
		fe3 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_buttonBase.png")
		fe4 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_Button.png")
		fe5 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_Light.png")
		fe6 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_LightRed.png")
		fc1 = pygame.image.load("models/tasks/Fuel Engines/engineFuel_gasCanBase.png")

		while True:
			screen.fill((0, 0, 0, 5))
			sur = pygame.surface.Surface([300, 320]) #344, 80
			sur.fill((255, 255, 0))
			screen.blit(sur, (344, 413-int(en)*5))
			screen.blit(fc1, (324, 23))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			
			if 413-int(en)*5 < 105:
				self.tasks[12] = 1
				return 1

			screen.blit(fe2, (661, 397))
			screen.blit(fe3, (711, 356))
			screen.blit(fe4, (735, 379))
			if 735 < pygame.mouse.get_pos()[0] < 811 and 379 < pygame.mouse.get_pos()[1] < 456:
				if pygame.mouse.get_pressed()[0]:
					screen.blit(fe4, (735, 382))
					en += 0.5
			screen.blit(fe5, (777, 335))
			screen.blit(fe6, (741, 335))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[12] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def inspectSample(self):
		isDon = 1
		is1 = pygame.image.load("models/tasks/Inspect Sample/medBay_back.png")
		is2 = pygame.image.load("models/tasks/Inspect Sample/medBay_panelCenter.png")
		is3 = pygame.image.load("models/tasks/Inspect Sample/medBay_glassBack.png")
		is4 = pygame.image.load("models/tasks/Inspect Sample/medBay_glassFrontTestTubes.png")
		is5 = pygame.image.load("models/tasks/Inspect Sample/medBay_dispenser.png")
		is6 = pygame.image.load("models/tasks/Inspect Sample/medBay_liquid_filled.png")
		is7 = pygame.image.load("models/tasks/Inspect Sample/medBay_panelBottom.png")
		is8 = pygame.image.load("models/tasks/Inspect Sample/medBay_buttonConfirm.png")
		is9 = pygame.image.load("models/tasks/Inspect Sample/medBay_liquid_anom.png")
		is10 = pygame.image.load("models/tasks/Inspect Sample/medBay_sampleButton_green.png")
		is11 = pygame.image.load("models/tasks/Inspect Sample/medBay_sampleButton_red.png")
		is12 = pygame.image.load("models/tasks/Inspect Sample/medBay_liquid_filled.png")
		anom = random.randint(0,4)
		before = 0
		fills = [0, 0, 0, 0, 0]
		statfilling = 0
		fillingDon = 0

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(is1, (250, 22))
			screen.blit(is2, (257, 274))
			screen.blit(is3, (285, 221))
			screen.blit(is4, (285, 184))
			screen.blit(is7, (248, 406))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			
			if statfilling == 1:
				for i in range(len(fills)):
					if fills[i] == 100:
						screen.blit(is6, (360+63*i, 233))
						if fillingDon == 1:
							before += 1
							if anom == i and before > 1000:
								screen.blit(is9, (360+63*i, 233))
								screen.blit(is11, (360+63*i, 419))
								if (360+63*i) < pygame.mouse.get_pos()[0] < (40+360+63*i) and (419) < pygame.mouse.get_pos()[1] < (40+419):
									if pygame.mouse.get_pressed()[0]:
										self.tasks[13] = 1
										return 1
							elif before > 1000:
								screen.blit(is10, (360+63*i, 419))
								if (360+63*i) < pygame.mouse.get_pos()[0] < (40+360+63*i) and (419) < pygame.mouse.get_pos()[1] < (40+419):
									if pygame.mouse.get_pressed()[0]:
										anom = random.randint(0,4)
										before = 0
										fills = [0, 0, 0, 0, 0]
										statfilling = 0
										fillingDon = 0

					if fills[i] < 100:
						screen.blit(is5, (355+60*i, 25))
						fills[i] += 2
						break

			if 652 < pygame.mouse.get_pos()[0] < 684 and 468 < pygame.mouse.get_pos()[1] < 498 and pygame.mouse.get_pressed()[0]:
				statfilling = 1
			tot = 0
			for i in fills:
				tot += i
			if tot == 500:
				fillingDon = 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[13] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def primeShield(self):
		psDon = 1
		ps1 = pygame.image.load("models/tasks/Prime Shields/shield_screen.png")
		ps2 = pygame.image.load("models/tasks/Prime Shields/shield_Panel.png")
		ps3 = pygame.image.load("models/tasks/Prime Shields/shield_Panel_red.png")
		ps4 = pygame.image.load("models/tasks/Prime Shields/shield_Gauge100.png")
		psPos = [(417, 203), (538, 131), (541, 273), (419, 346), (295, 276), (295, 132), (416, 60)]
		psred = [random.randint(0, 1) for i in range(7)]
		angle = 0

		while True:
			screen.fill((0, 0, 0, 5))
			angle += 1
			screen.blit(ps1, (238, 25))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			for i in range(len(psPos)):
				screen.blit(ps2, psPos[i])
				if psred[i] == 1:
					screen.blit(ps3, psPos[i])
					if psPos[i][0] < pygame.mouse.get_pos()[0] < psPos[i][0]+152 and psPos[i][1] < pygame.mouse.get_pos()[1] < psPos[i][1]+152:
						if pygame.mouse.get_pressed()[0]:
							psred[i] = 0
			self.blitRotate(screen , ps4, (493, 268), (ps4.get_size()[0]//2, ps4.get_size()[1]//2), angle)
			#screen.blit(ps4, pygame.mouse.get_pos())
			tot = 0
			for i in psred:
				tot += i
			if tot == 0:
				self.tasks[14] = 1
				return 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[14] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def stabSteering(self):
		ssDon = 1
		ss1 = pygame.image.load("models/tasks/Stabilize Steering/nav_stabilize_base.png")
		ss2 = pygame.image.load("models/tasks/Stabilize Steering/nav_stabilize_graph.png")
		ss3 = pygame.image.load("models/tasks/Stabilize Steering/nav_stabilize_target.png")

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(ss2, (261, 42))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			if 251 < pygame.mouse.get_pos()[0] < 730 and 34 < pygame.mouse.get_pos()[1] < 511:
				pygame.draw.line(screen, (255, 255, 255), (pygame.mouse.get_pos()[0],34), (pygame.mouse.get_pos()[0],511), 5)
				pygame.draw.line(screen, (255, 255, 255), (251, pygame.mouse.get_pos()[1]), (730, pygame.mouse.get_pos()[1]), 5)
				screen.blit(ss3, (pygame.mouse.get_pos()[0]-ss3.get_size()[0]//2, pygame.mouse.get_pos()[1]-ss3.get_size()[1]//2))

				if 487 < pygame.mouse.get_pos()[0] < 500 and 269 < pygame.mouse.get_pos()[1] < 281:
					if pygame.mouse.get_pressed()[0]:
						self.tasks[15] = 1
						return 1
			screen.blit(ss1, (241, 23))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[15] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def unlockManifolds(self):
		umDon = 1
		um1 = pygame.image.load("models/tasks/Unlock Manifolds/reactorPanel.png")
		um2 = pygame.image.load("models/tasks/Unlock Manifolds/reactorPanelGlass.png")
		um3 = pygame.image.load("models/tasks/Unlock Manifolds/reactorWire.png")
		um4 = pygame.image.load("models/tasks/Unlock Manifolds/red.png")
		nums = {i:pygame.image.load(f"models/tasks/Unlock Manifolds/reactorButton{i}.png") for i in range(1, 11)}
		numPos = []
		numDid = 1
		while len(numPos) != 10:
			i = random.randint(1, 10)
			if i not in numPos:
				numPos.append(i)

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(um1, (255, 151))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			for i in range(1, 11):
				if i > 5:
					screen.blit(nums[numPos[i-1]], (292+(i-6)*85, 278))
					if numPos[i-1] < numDid:
						screen.blit(um4, (292+(i-6)*85, 278))
					if 292+(i-6)*85 < pygame.mouse.get_pos()[0] < 83+292+(i-6)*85 and 278 < pygame.mouse.get_pos()[1] < 278+82:
						if pygame.mouse.get_pressed()[0]:
							if numDid == numPos[i-1]:
								numDid += 1
				else:
					screen.blit(nums[numPos[i-1]], (292+(i-1)*85, 192))
					if numPos[i-1] < numDid:
						screen.blit(um4, (292+(i-1)*85, 192))
					if 292+(i-1)*85 < pygame.mouse.get_pos()[0] < 82+292+(i-1)*85 and 192 < pygame.mouse.get_pos()[1] < 192+82:
						if pygame.mouse.get_pressed()[0]:
							if numDid == numPos[i-1]:
								numDid += 1
			if numDid == 11:
				self.tasks[16] = 1
				return 1

			screen.blit(um2, (288, 187))
			screen.blit(um3, (208, 89))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[16] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def starReactor(self):
		srDon = 1
		sr1 = pygame.image.load("models/tasks/Start Reactor/simonSaysBase.png")
		sr2 = pygame.image.load("models/tasks/Start Reactor/simonSaysButtonsShadow.png")
		sr3 = pygame.image.load("models/tasks/Start Reactor/simonSaysLightsIndicationWShadows.png")
		sr4 = pygame.image.load("models/tasks/Start Reactor/simonSaysScreen.png")
		sr5 = pygame.image.load("models/tasks/Start Reactor/ssbutton.png")
		sr6 = pygame.image.load("models/tasks/Start Reactor/ssbuttonblue.png")
		sr7 = pygame.image.load("models/tasks/Start Reactor/ssbuttonred.png")
		srDoing = 1
		sr = [random.randint(0,8) for i in range(srDoing)]
		l = 0

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(sr1, (243, 118))
			screen.blit(sr1, (520, 118))
			screen.blit(sr2, (572, 195))
			screen.blit(pygame.image.load(f"models/tasks/Start Reactor/{srDoing}.png"), (290, 163))
			screen.blit(pygame.image.load(f"models/tasks/Start Reactor/{len(sr)}.png"), (564, 163))
			screen.blit(sr4, (290, 199))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			
			for i in range(9):
				#screen.blit(sr5, (575+i*50, 200))
				if i >= 6:
					screen.blit(sr5, (575+(i-6)*50, 300))
					if i == sr[0]:
						screen.blit(sr6, (295+(i-6)*50, 300))
				elif i >= 3:
					screen.blit(sr5, (575+(i-3)*50, 250))
					if i == sr[0]:
						screen.blit(sr6, (295+(i-3)*50, 250))
				else:
					screen.blit(sr5, (575+i*50, 200))
					if i == sr[0]:
						screen.blit(sr6, (295+i*50, 200))
			butPress = None
			for i in range(9):
				if i>=6:
					if 575+(i-6)*50 < pygame.mouse.get_pos()[0] < 40+575+(i-6)*50 and 300 < pygame.mouse.get_pos()[1] < 300+40:
						if pygame.mouse.get_pressed()[0]:
							butPress = i
				elif i>=3:
					if 575+(i-3)*50 < pygame.mouse.get_pos()[0] < 40+575+(i-3)*50 and 250 < pygame.mouse.get_pos()[1] < 250+40:
						if pygame.mouse.get_pressed()[0]:
							butPress = i
				else:
					if 575+i*50 < pygame.mouse.get_pos()[0] < 40+575+i*50 and 200 < pygame.mouse.get_pos()[1] < 200+40:
						if pygame.mouse.get_pressed()[0]:
							butPress = i
			if butPress != None:
				if butPress == sr[0]:
					#print(butPress)
					del sr[0]
					if len(sr) == 0:
						srDoing += 1
						sr = [random.randint(0,8) for i in range(srDoing)]
						#print(sr)
						l = 0
					if srDoing == 6:
						self.tasks[17] = 1
						return 1
				else:
					l += 1
					if l > 10:
						srDoing = 1
						sr = [random.randint(0,8) for i in range(srDoing)]
						l = 0
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[17] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def acceptPower(self):
		apDon = 1
		ap1 = pygame.image.load("models/tasks/Accept Power/1.png")
		ap2 = pygame.image.load("models/tasks/Accept Power/2.png")
		ap3 = pygame.image.load("models/tasks/Accept Power/3.png")

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(ap2, (160, 58))
			screen.blit(ap1, (482, 198))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			if 458 < pygame.mouse.get_pos()[0] < 552 and 238 < pygame.mouse.get_pos()[1] < 311 and pygame.mouse.get_pressed()[0]:
				self.tasks[18] = 1
				return 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[18] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)

	def medbayScan(self):
		msDon = 1
		ms1 = pygame.image.load("models/tasks/Submite Scan/medbayScan_panelBottom.png")
		ms2 = pygame.image.load("models/tasks/Submite Scan/medbayScan_panelTop.png")
		ms3 = pygame.image.load("models/tasks/Submite Scan/medbayScan_wires.png")
		num = 1
		n = 0

		while True:
			screen.fill((0, 0, 0, 5))
			screen.blit(ms2, (250, 7))
			screen.blit(ms3, (719, 72))
			screen.blit(ms1, (250, 372))
			screen.blit(close, (100, 25))

			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				return 0
			num += 0.1
			if num >= 9:
				num = 1
				#print(n)
				n += 1
			if n > 2:
				self.tasks[19] = 1
				return 1
			screen.blit(pygame.image.load(f"models/scan/{int(num)}.png"), (488, 256))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.tasks[19] = 0
					return 0

			pygame.display.update()
			clock.tick(fps)


if __name__ == '__main__':
	Task = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	#Task = [0 for i in range(20)]
	ta = Tasks()

	while True:

		screen.fill((255, 0, 0))

		#print(ta.tasks)

		if Task[0] == 0:
			Task[0] = ta.swipeCard()
		elif Task[1] == 0:
			Task[1] = ta.fixWiring()
		elif Task[2] == 0:
			Task[2] = ta.emptyGarbage()
		elif Task[3] == 0:
			Task[3] = ta.upload()
		elif Task[4] == 0:
			Task[4] = ta.Download(1)
		elif Task[5] == 0:
			Task[5] = ta.clearLeaves()
		elif Task[6] == 0:
			Task[6] = ta.alignEngine()
		elif Task[7] == 0:
			Task[7] = ta.calibrate()
		elif Task[8] == 0:
			Task[8] = ta.chartCourse()
		elif Task[9] == 0:
			Task[9] = ta.weapons()
		elif Task[10] == 0:
			Task[10] = ta.divertPower(2)
		elif Task[11] == 0:
			Task[11] = ta.fualEngine()
		elif Task[12] == 0:
			Task[12] = ta.fillCan()
		elif Task[13] == 0:
			Task[13] = ta.inspectSample()
		elif Task[14] == 0:
			Task[14] = ta.primeShield()
		elif Task[15] == 0:
			Task[15] = ta.stabSteering()
		elif Task[16] == 0:
			Task[16] = ta.unlockManifolds()
		elif Task[17] == 0:
			Task[17] = ta.starReactor()
		elif Task[18] == 0:
			Task[18] = ta.acceptPower()
		elif Task[19] == 0:
			Task[19] = ta.medbayScan()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		pygame.display.update()
		clock.tick(fps)
