import pygame
from pygame.locals import *
import random
import numpy
import math
from Tasks import Tasks
import threading

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)
s = [0,0]

tasks = Tasks()

while True:
	screen.fill((0, 0, 0))
	print(tasks.tasks)

	if tasks.tasks[0] == 0:
		tasks.tasks[0]=1
		th = threading.Thread(target = tasks.swipeCard())
		th.start()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos())
		'''if event.type == pygame.KEYDOWN:
			#if event.unicode.isalpha():
			print(event.unicode)'''
	pygame.display.update()
	clock.tick(fps)