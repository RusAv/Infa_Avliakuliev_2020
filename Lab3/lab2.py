import pygame
from random import *
import math
import numpy as np
from pygame.draw import *
def trian(x,y,size,color,screen,sd):
    lin=int(size/2/np.cos(math.radians(30)))
    polygon(screen,color,[(x+sd,y-9*int(lin)),(x+int(size/2),y+int(lin/2)),(x-int(size/2),y+int(lin/2))])
pygame.init()
def mushroom(x,y,screen):
    surf.fill((130,255,90))
    ellipse(screen,(255,255,255),((x,y),(20,70)))
    ellipse(screen,(255,0,0),((x-25,y-5),(70,20)))
    ellipse(screen,(255,255,255),((x+1,y+2),(7,4)))
    ellipse(screen,(255,255,255),((x+24,y+6),(4,2)))
    ellipse(screen,(255,255,255),((x+10,y+6),(4,2)))
    ellipse(screen,(255,255,255),((x+15,y+1),(4,2)))
    ellipse(screen,(255,255,255),((x-10,y+6),(6,2)))
def hedg(x,y,screen):
    ellipse(screen,(149,123,141),((x,y),(200,110)))
    ellipse(screen,(149,123,141),((x+10,y+80),(40,29)))
    ellipse(screen,(149,123,141),((x+150,y+80),(40,29)))
    ellipse(screen,(149,123,141),((x+170,y+40),(60,39)))
    
    ellipse(screen,(0,0,0),((x+205,y+50),(7,7)))
    ellipse(screen,(0,0,0),((x+215,y+45),(7,7)))
    ellipse(screen,(0,0,0),((x+227,y+55),(5,5)))
    for i in range(60):
        x1=x+randint(10,180)
        y1=y+randint(20,90)
        trian(x1,y1,15,(0,0,0),screen,randint(-65,65))
    ellipse(screen,(255,0,0),((x+20,y+5),(40,50)))
    ellipse(screen,(255,255,0),((x+120,y+15),(40,50)))
    ellipse(screen,(255,0,0),((x+60,y+15),(40,50)))
    mushroom(x+40,y-10,screen)
    for i in range(20):
        x1=x+randint(10,180)
        y1=y+randint(20,90)
        trian(x1,y1,15,(0,0,0),screen,randint(-65,65))
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
surf = pygame.Surface((400, 400))
surf.fill((120,128,110))
hedg(500,600,screen)
surf=pygame.transform.rotate(surf,50)
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
