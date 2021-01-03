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

while True:
	screen.fill((0, 0, 0))

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