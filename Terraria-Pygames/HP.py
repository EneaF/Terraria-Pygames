from typing import Any
import pygame
from pygame.locals import *

class VitaClass():
    def __init__(self,pos,size,screen) -> None:
        self.screen=screen

        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.cuore=pygame.image.load("images/cuore.png")
        self.mezzoCuore=pygame.image.load("images/Mezzo_cuore.png")
        self.CuorePerso=pygame.image.load("images/Perso_cuore.png")
        self.cuore=pygame.transform.scale(self.cuore,size)
        self.mezzoCuore=pygame.transform.scale(self.mezzoCuore,size)
        self.CuorePerso=pygame.transform.scale(self.CuorePerso,size)
    

    def draw(self,tipo=0):
        if tipo==0:
            immagine=self.cuore
        elif tipo==1:
            immagine=self.mezzoCuore
        elif tipo==2:
            immagine=self.CuorePerso
        
        self.screen.blit(immagine,self.rect)