import pygame
from random import *
import math
import numpy as np
from pygame.draw import *
def trian(x,y,size,color,screen,sd):
    lin=int(size/2/np.cos(math.radians(30)))
    polygon(screen,color,[(x+sd,y-9*int(lin)),(x+int(size/2),y+int(lin/2)),(x-int(size/2),y+int(lin/2))])
pygame.init()
def mushroom(x,y,size,screen):
    ellipse(screen,(255,255,255),((x,y),(size*20,size*70)))
    ellipse(screen,(255,0,0),((x-size*25,y-size*5),(size*70,size*20)))
    ellipse(screen,(255,255,255),((x+size*1,y+size*2),(size*7,size*4)))
    ellipse(screen,(255,255,255),((x+size*24,y+size*6),(size*4,size*2)))
    ellipse(screen,(255,255,255),((x+size*10,y+size*6),(size*4,size*2)))
    ellipse(screen,(255,255,255),((x+size*15,y+size*1),(size*4,size*2)))
    ellipse(screen,(255,255,255),((x-size*10,y+size*6),(size*6,size*2)))
def hedg(x,y,size,screen):
    ellipse(screen,(149,123,141),((x,y),(size*200,size*110)))
    ellipse(screen,(149,123,141),((x+size*10,y+size*80),(size*40,size*29)))
    ellipse(screen,(149,123,141),((x+size*150,y+size*80),(size*40,size*29)))
    ellipse(screen,(149,123,141),((x+size*170,y+size*40),(size*60,size*39)))
    
    ellipse(screen,(0,0,0),((x+size*205,y+size*50),(size*7,size*7)))
    ellipse(screen,(0,0,0),((x+size*215,y+size*45),(size*7,size*7)))
    ellipse(screen,(0,0,0),((x+size*227,y+size*55),(size*5,size*5)))
    for i in range(60):
        x1=x+randint(size*10,size*180)
        y1=y+randint(size*20,size*90)
        trian(x1,y1,size*15,(0,0,0),screen,randint(-size*65,size*65))
    ellipse(screen,(255,0,0),((x+size*20,y+size*5),(size*40,size*50)))
    ellipse(screen,(255,255,0),((x+size*120,y+size*15),(size*40,size*50)))
    ellipse(screen,(255,0,0),((x+size*60,y+size*15),(size*40,size*50)))
    mushroom(x+40,y-10,1,screen)
    for i in range(20):
        x1=x+randint(10,180)
        y1=y+randint(20,90)
        trian(x1,y1,size*15,(0,0,0),screen,randint(-size*65,size*65))
FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((120,110,128))
rect(screen,(0,80,0),((0,0),(800,500)))
#filling trees
rect(screen,(80,180,0),((40,0),(50,670)))
rect(screen,(80,180,0),((240,0),(60,690)))
rect(screen,(80,180,0),((600,0),(40,670)))
rect(screen,(80,180,0),((700,0),(60,640)))
rect(screen,(80,180,0),((140,0),(20,670)))
hedg(400,700,1,screen)
hedg(300,500,1,screen)
hedg(200,650,1,screen)
hedg(50,500,1,screen)
mushroom(700,730,1,screen)
mushroom(600,760,1,screen)
mushroom(740,765,1,screen)
mushroom(670,775,1,screen)
mushroom(630,750,1,screen)
#screen.blit(surf,(0,0))
#mushroom(60,40,screen,-15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
