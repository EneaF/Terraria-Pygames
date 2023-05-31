import pygame
from pygame.locals import *

class TormenelliClass():
    def __init__(self,pos,size,screen,dir):
        self.screen=screen
        self.pos=pos
        self.size=size
        self.vel=20
        
        if dir==0:
            self.velX=16
            self.velY=0
        elif dir==1:
            self.velX=8
            self.velY=8
        elif dir==2:
            self.velX=0
            self.velY=16
        elif dir==3:
            self.velX=-8
            self.velY=8
        elif dir==4:
            self.velX=-16
            self.velY=0
        elif dir==5:
            self.velX=-8
            self.velY=-8
        elif dir==6:
            self.velX=0
            self.velY=-16
        elif dir==7:
            self.velX=8
            self.velY=-8
        

        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.fase1img=pygame.image.load("images/BossFinale1.png")
        self.Tormenello=pygame.transform.scale(self.fase1img,(30,30))


    def muovi(self):
        self.rect.bottom+=self.velX
        self.rect.left+=self.velY
    
    def draw(self):
        self.screen.blit(self.Tormenello,self.rect)