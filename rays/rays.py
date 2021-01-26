import pygame
from pygame.locals import *
import threading
import pickle

pygame.init()

screen = pygame.display.set_mode([1000, 550])
clock = pygame.time.Clock()
fps = 50

class Sprite(pygame.sprite.Sprite):
	def __init__(self, sizex = 10, sizey = 10, surface = 'default'):
		pygame.sprite.Sprite.__init__(self)
		if surface == 'default':
			self.image = pygame.Surface((sizex, sizey))
			self.image.fill((255, 0, 0))
		else:
			self.image = surface
		self.rect = self.image.get_rect()

obj = Sprite()
coll_group = pygame.sprite.Group()
coll_group.add(obj)

ray_points = []

q = open('collision_points.dat', 'rb')
coll_loc = pickle.load(q)
collision = [Sprite(k, l) for i,j,k,l in coll_loc]
wall_group = pygame.sprite.Group()

for i in range(len(collision)):
	wall_group.add(collision[i])

mouse = pygame.Surface([1, 1])
mouse_rect = mouse.get_rect()

def rays():
	pass

thread = threading.Thread(target=rays)
#thread.start()
a, b = 0, 0
print('Equation: (275-i)(500-x) = (500-j)(275-y)', )

while True:
	screen.fill(0)

	mouse_rect.x, mouse_rect.y = pygame.mouse.get_pos()
	ray_points = []

	#if mouse_rect.colliderect(obj.rect) == 1:
	for i in range(1000):
		ray_points.extend([(i, 0), (i, 550)])
		pygame.draw.line(screen, (255, 255, 255), (500, 275), (i, 0))
		pygame.draw.line(screen, (255, 255, 255), (500, 275), (i, 550))
	for i in range(550):
		ray_points.extend([(0, i), (1000, i)])
		pygame.draw.line(screen, (255, 255, 0), (500, 275), (0, i))
		pygame.draw.line(screen, (255, 255, 0), (500, 275), (1000, i))

	keys = pygame.key.get_pressed()
	if keys[K_w]:
		b += 3
	if keys[K_a]:
		a += 5
	if keys[K_s]:
		b -= 3
	if keys[K_d]:
		a -= 5

	#collision
	for i in range(len(collision)):
		collision[i].rect.x, collision[i].rect.y = coll_loc[i][0]+a, coll_loc[i][1]+b
	wall_group.draw(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	pygame.display.update()
	clock.tick(fps)
