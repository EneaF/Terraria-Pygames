import pygame
from pygame.locals import*

class ProiettileClass():
    def __init__(self,pos,size,screen):
        self.screen=screen
        self.pos=pos
        self.size=size
        self.vel=20
        
        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.image=pygame.surface.Surface((10,10))
    
    def muovi(self,velX,velY):
        self.rect.bottom+=velX
        self.rect.left+=velY
    
    def draw(self):
        self.screen.blit(self.image,self.rect)