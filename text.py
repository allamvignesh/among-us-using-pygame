import pygame
from randomizer import getAllTasks

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 1000
Y = 550
f = 18

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')

AllTasks = getAllTasks()
Text1 = f'fixWiring {len(AllTasks[0])}'
Text2 = f'divert and accept power {len(AllTasks[1])}'
Text3 = f'Download and Upload {len(AllTasks[2])}'
Text4 = f'{AllTasks[3][0]} {len(AllTasks[3][1:])}'
if str(AllTasks[4][0]).isalpha():
	Text5 = f'{AllTasks[4][0]} {len(AllTasks[4][1:])}'
else:
	Text5 = f'Usual Tasks {len(AllTasks[4][1:])}'
Text6 = f'Main Tasks {len(AllTasks[5])}'

font = pygame.font.Font('freesansbold.ttf', f)

while True:

	# completely fill the surface object
	# with white color
	screen.fill(0)

	Text1 = f'fixWiring {len(AllTasks[0])}'
	Text2 = f'divert and accept power {len(AllTasks[1])}'
	Text3 = f'Download and Upload {len(AllTasks[2])}'
	Text4 = f'{AllTasks[3][0]} {len(AllTasks[3][1:])}'
	if str(AllTasks[4][0]).isalpha():
		Text5 = f'{AllTasks[4][0]} {len(AllTasks[4][1:])}'
	else:
		Text5 = f'Usual Tasks {len(AllTasks[4][1:])}'
	Text6 = f'Main Tasks {len(AllTasks[5])}'

	text1 = font.render(Text1, True, green)
	text2 = font.render(Text2, True, green)
	text3 = font.render(Text3, True, green)
	text4 = font.render(Text4, True, green)
	text5 = font.render(Text5, True, green)
	text6 = font.render(Text6, True, green)

	textRect1 = text1.get_rect()
	textRect2 = text2.get_rect()
	textRect3 = text3.get_rect()
	textRect4 = text4.get_rect()
	textRect5 = text5.get_rect()
	textRect6 = text6.get_rect()

	screen.blit(text1, (0, 70))
	screen.blit(text2, (0, 70+f))
	screen.blit(text3, (0, 70+f*2))
	screen.blit(text4, (0, 70+f*3))
	screen.blit(text5, (0, 70+f*4))
	screen.blit(text6, (0, 70+f*5))

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:

			# deactivates the pygame library
			pygame.quit()

			# quit the program.
			quit()

		# Draws the surface object to the screen.
		pygame.display.update()
