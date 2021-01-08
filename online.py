import pygame
from pygame.locals import *
import random
from free_play import Free_play

pygame.init()

size =[1000, 550]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 50

class online():
	def __init__(self):
		pass

	def run(self):

		font = pygame.font.Font('freesansbold.ttf', 40)
		text = 'Enter Name'
		text1 = font.render(text, True, (255, 255, 255))
		textRect1 = text1.get_rect()
		editing = False

		colors = [[(random.randint(0, 255)) for i in range(3)] for i in range(1, 7)]

		plys = [self.colorchanger(pygame.image.load(f'images/main_screen/mainscreenCrew{i}.png'), colors[i-1]) for i in range(1, 7)]

		bliting = [[random.choice(plys), random.randint(-500, 1000), random.randint(-100, 560)] for i in range(len(plys))]

		while True:
			screen.fill(0)

			for i in range(len(bliting)):
				bliting[i][1] += 1
				if bliting[i][1] > 1000:
					bliting[i][1] = -100
					colors[i] = (random.randint(0, 255) for i in range(3))
			for i in range(len(bliting)):
				screen.blit(bliting[i][0], (bliting[i][1], bliting[i][2]))

			text1 = font.render(text, True, (255, 255, 255))
			textRect1 = text1.get_rect()
			screen.blit(text1, (350, 49))

			pygame.draw.rect(screen, (255, 255, 255), (345, 32, 300, 80), 1)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 1
				if event.type == pygame.MOUSEBUTTONDOWN:
					print(pygame.mouse.get_pos())
					if 345 < pygame.mouse.get_pos()[0] < 646 and 32 < pygame.mouse.get_pos()[1] < 112:
						editing = True
						if text == 'Enter Name':
							text = ''
					else:
						editing = False
						if text == '':
							text = 'Enter Name'
				if event.type == pygame.KEYDOWN:
					if editing:
						if event.key == pygame.K_RETURN:
							editing = False
						elif event.key == pygame.K_BACKSPACE:
							text = text[:-1]
						elif len(text) < 12:
							text += event.unicode

			pygame.display.update()
			clock.tick(fps)
	def colorchanger(self, surface, color):
		"""Fill all pixels of the surface with color, preserve transparency."""
		surface = surface.convert_alpha()
		w, h = surface.get_size()
		r, g, b = color
		for x in range(w):
			for y in range(h):
				if surface.get_at((x,y)) == (255, 255, 255, 255):
					surface.set_at((x, y), pygame.Color(r, g, b, 255))
		return surface

online()