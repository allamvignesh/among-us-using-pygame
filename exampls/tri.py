import pygame
from pygame.locals import *
import os
import sys
import math
import random
class wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([100,100])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def draw(self,win):
        win.blit(self.image,(self.rect.x,self.rect.y))

class wall2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([100,100])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def draw(self,win):
        win.blit(self.image,(self.rect.x,self.rect.y))

def redrawWin(win):
    win.fill((240,240,240))
    pygame.draw.rect(win,(0,0,0),(0,400,w,10))
    box.draw(win)
    enemy.draw(win)
    enemy2.draw(win)
    pygame.display.update()

w,h=800,500
x1=50
x2=600
a=0
win=pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
run=True
while run:
    box=wall(x1,340,70,80)
    enemy=wall(x2,340,70,80)
    enemy2=wall2(x2+100, 340)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False
            pygame.quit()
            quit()
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            x1-=10
        if keys[K_RIGHT]:
            x1+=10
        if keys[K_d]:
            x2+=10
        if keys[K_a]:
            x2-=10
    sprites = pygame.sprite.Group(enemy,enemy2)
    if pygame.sprite.spritecollide(box,sprites,False):
        print(pygame.sprite.spritecollide(box,sprites,False))
        print(True,a)
        a+=1
    clock.tick(20)
    redrawWin(win)