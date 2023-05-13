import pygame
from pygame.locals import *

class Personaggio():
    def __init__(self,screen,pos,size):
        self.screen=screen
        self.pos=pos

        self.rect = pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.imageDestra = pygame.image.load("images/Personaggio_Destra.png")
        self.imageSinistra = pygame.image.load("images/Personaggio_Sinistra.png")
        self.imageDestra = pygame.transform.scale(self.imageDestra,size)
        self.imageSinistra = pygame.transform.scale(self.imageSinistra,size)

        self.image=self.imageDestra

        self.vel=[0,0]
        self.gravita = 0.3
        self.forzaSalto = 10
        self.VelMovimento = 5
        

        self.muoviDestra=False
        self.muoviSinistra=False
        self.inAria=True
        

    def muovi_Destra(self):
        self.muoviDestra=True
        self.image=self.imageDestra
        self.muoviSinistra=False
    
    def muovi_Sinistra(self):
        self.muoviSinistra=True
        self.image=self.imageSinistra
        self.muoviDestra=False
    
    def StopDestra(self):
        self.muoviDestra=False

    def StopSinistra(self):
        self.muoviSinistra=False

    def Salto(self):
        if self.inAria==False:
            self.vel[1] -= self.forzaSalto
            self.inAria = True
    
    def StopSalto(self,blocco):
        self.vel[1]=0
        self.rect.top=blocco
        self.inAria=True
    
    def StopBasso(self,topBlocco):
        self.rect.bottom=topBlocco+1
        self.vel[1]=0
        self.inAria=False


    def muovi(self):
        self.vel[1] += self.gravita
        self.rect.bottom+=self.vel[1]
        # self.inAria=True

        # if self.rect.bottom > self.screen.get_height():
        #     self.rect.bottom=self.screen.get_height()
        #     self.vel[1]=0
        #     self.inAria=False

        
        if self.muoviDestra==True:
            self.rect.right += self.VelMovimento
        
        if self.muoviSinistra==True:
            self.rect.left -= self.VelMovimento
        
    
    def draw(self):
        self.screen.blit(self.image,self.rect)

