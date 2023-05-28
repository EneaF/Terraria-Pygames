import pygame
from pygame.locals import *

class FantasmaClass():
    def __init__(self,pos,size,screen,Vel=2):
        self.screen=screen
        self.pos=pos
        self.size=size

        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.fantasmaSx=pygame.image.load("images/FantasmaSx.png")
        self.fantasmaSx=pygame.transform.scale(self.fantasmaSx,size)
        self.fantasmaDx=pygame.image.load("images/FantasmaDx.png")
        self.fantasmaDx=pygame.transform.scale(self.fantasmaDx,size)

        self.image=self.fantasmaSx

        self.Vel = Vel

    def muovi(self,velx,vely):
        self.rect.left+=velx
        self.rect.bottom+=vely

        if velx>0:
            self.image=self.fantasmaDx
        else:
            self.image=self.fantasmaSx

    def draw(self):
        self.screen.blit(self.image,self.rect)
    