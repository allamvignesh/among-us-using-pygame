import pygame
from pygame.locals import *
import random
import numpy
import math

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)

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
cllevDon = 1
tot = 0
cllev1 = pygame.image.load("models/tasks/Clean O2 Filter/o2_bgBase.png")
cllev2 = pygame.image.load("models/tasks/Clean O2 Filter/o2_bgTop.png")

levPos = [(random.randint(390, 649), random.randint(109, 400)) for i in range(7)]
leaves = [pygame.image.load(f"models/tasks/Clean O2 Filter/o2_leafs/o2_leaf{i}.png") for i in range(1,8)]

#align engine
enDon = 1
enp = [132, 205]
count = 1
en1 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_base.png")
en2 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_slider.png")
en3 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_engine.png")
en4 = pygame.image.load("models/tasks/Align Engine Output/engineAlign_engine_green.png")
en5 = pygame.image.load("models/tasks/Align Engine Output/green.png")

#calibrate
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

#chart Course
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

def blitRotate(surf, image, pos, originPos, angle):

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

def draw_dashed_line(surf, color, start_pos, end_pos, width=5, dash_length=10):
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

while True:
	screen.fill((0, 0, 0))

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

	if enDon == 0:
		screen.blit(en5, (286, 54))
		screen.blit(en1, (253, 22))
		screen.blit(en4, (220, 170))
		if pygame.mouse.get_pressed()[0] and 126 < pygame.mouse.get_pos()[1] < 379 and 614 < pygame.mouse.get_pos()[0] < 687:
			if enp[1]-20 < pygame.mouse.get_pos()[1] < enp[1]+20:
				enp[1] = pygame.mouse.get_pos()[1]
			if 240 < pygame.mouse.get_pos()[1] < 260:
				count += 1
				if count == 100:
					enDon = 1
			else:
				count = 0
		screen.blit(en2, (611, enp[1]))
		screen.blit(en3, (220, enp[1]-73))

	if calDon == 0:
		screen.blit(cal1, (258, 24))
		screen.blit(cal2, (609, 124))
		screen.blit(cal2, (609, 271))
		screen.blit(cal2, (609, 421))
		screen.blit(cal3, (597, 385))
		screen.blit(cal3, (597, 231))
		screen.blit(cal3, (597, 82))

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
			blitRotate(screen, cal4, (369, 123), (w/2, h/2), angles[0])
		else:
			blitRotate(screen, cal4, (369, 123), (w/2, h/2), 0)
		if calDoing[1] == 0:
			blitRotate(screen, cal5, (369, 276), (w/2, h/2), angles[1])
		else:
			blitRotate(screen, cal5, (369, 276), (w/2, h/2), 0)
		if calDoing[2] == 0:
			blitRotate(screen, cal6, (369, 422), (w/2, h/2), angles[2])
		else:
			blitRotate(screen, cal6, (369, 422), (w/2, h/2), 0)

		if 612 < pygame.mouse.get_pos()[0] < 716 and 128 < pygame.mouse.get_pos()[1] < 152 and calDoing[0] == 0:
			if pygame.mouse.get_pressed()[0]:
				screen.blit(cal2, (609, 130))
				#print(angles[0]/360)
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
			calDon = 1

	if ccDon == 0:
		angle += 1
		screen.blit(cc1, (253, 118))
		for i in ccPos[1:]:
			screen.blit(cc2, (i[0]-cc2.get_size()[0]//2, i[1]-cc2.get_size()[1]//2))
			screen.blit(cc8, (i[0]-cc7.get_size()[0]//2, i[1]-cc7.get_size()[1]//2))
		screen.blit(cc7, (ccPos[0][0]-cc7.get_size()[0]//2, ccPos[0][1]-cc7.get_size()[1]//2))
		blitRotate(screen , cc4, ccPos[-1], (cc4.get_size()[0]//2, cc4.get_size()[1]//2), angle)
		for i in range(len(ccPos)-1):
			draw_dashed_line(screen, (0, 0, 0), ccPos[i], ccPos[i+1])

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
			ccDon = 1




	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos())
			pass
	pygame.display.update()
	clock.tick(fps)