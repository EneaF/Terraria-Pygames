import pygame,random
from pygame.locals import *

class Bossfinale():
    def __init__(self,pos,size,screen):
        self.screen=screen

        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))

        self.fase1img=pygame.image.load("images/BossFinale1.png")
        self.fase2=pygame.image.load("images/BossFinale3.png")
        self.upgradeBoss=pygame.image.load("images/BossFinale2.png")

        self.fase1=pygame.transform.scale(self.fase1img,(size[0],size[1]))
        self.fase2=pygame.transform.scale(self.fase2,(size[0],size[1]))
        self.upgradeBoss=pygame.transform.scale(self.upgradeBoss,(size[0],size[1]))

        self.image=self.fase1
        self.velocita=7
        self.velY=0
        self.gravitàGiu=20
        self.gravitàSu=0.5
        self.inAria=True
        self.HP=200
        self.destra=True
        self.sinistra=False

        self.RectBase=pygame.Rect((298,660),(404,30))
        self.SurfBase=pygame.Surface((404,30))
        


    def CheckMuovi(self):
        if self.rect.right>=950:
            self.destra=False
            self.sinistra=True
        elif self.rect.left<=50:
            self.destra=True
            self.sinistra=False
    
    def Jump(self):
        if self.inAria==False:
            self.velY-=20
        
    def muovi(self):
        self.rect.bottom+=self.velY
        if self.velY>0:
            self.velY+=self.gravitàGiu
        else:
            self.velY+=self.gravitàSu
        self.inAria=True
        if self.rect.bottom>=650:
            self.velY=0
            self.rect.bottom=650
            self.inAria=False
        
        if self.destra:
            self.rect.left+=self.velocita
        if self.sinistra:
            self.rect.left-=self.velocita
    
    def drawHP(self):
        self.screen.blit(self.SurfBase,self.RectBase)
        dimHP=2*self.HP
        RectHP=pygame.Rect((300,662),(dimHP,26))
        SurfHP=pygame.Surface((dimHP,26))
        SurfHP.fill((255,0,0))
        self.screen.blit(SurfHP,RectHP)
        
    def draw(self):
        self.screen.blit(self.image,self.rect)