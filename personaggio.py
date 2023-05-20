import pygame
from pygame.locals import *

class Personaggio():
    def __init__(self,screen,pos,size):
        self.screen=screen
        self.pos=pos

        self.rect = pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.imageDestra1 = pygame.image.load("images/Personaggio_Destra1.png")
        self.imageSinistra1 = pygame.image.load("images/Personaggio_Sinistra1.png")
        self.imageDestra1 = pygame.transform.scale(self.imageDestra1,size)
        self.imageSinistra1 = pygame.transform.scale(self.imageSinistra1,size)
        self.imageDestra2 = pygame.image.load("images/Personaggio_Destra2.png")
        self.imageSinistra2 = pygame.image.load("images/Personaggio_Sinistra2.png")
        self.imageDestra2 = pygame.transform.scale(self.imageDestra2,size)
        self.imageSinistra2 = pygame.transform.scale(self.imageSinistra2,size)
        self.imageDestra3 = pygame.image.load("images/Personaggio_Destra3.png")
        self.imageSinistra3 = pygame.image.load("images/Personaggio_Sinistra3.png")
        self.imageDestra3 = pygame.transform.scale(self.imageDestra3,size)
        self.imageSinistra3 = pygame.transform.scale(self.imageSinistra3,size)
        
        self.image=self.imageDestra1

        self.vel=[0,0]
        self.gravita = 0.3
        self.forzaSalto = 6.5
        self.VelMovimento = 5
        self.velMax=0
        
        self.posAnimazione=0
        self.animazioneDestra=[self.imageDestra2,self.imageDestra2,self.imageDestra2,self.imageDestra2,self.imageDestra2,self.imageDestra3,self.imageDestra3,self.imageDestra3,self.imageDestra3,self.imageDestra3]
        self.animazioneSinistra=[self.imageSinistra2,self.imageSinistra2,self.imageSinistra2,self.imageSinistra2,self.imageSinistra2,self.imageSinistra3,self.imageSinistra3,self.imageSinistra3,self.imageSinistra3,self.imageSinistra3]

        self.muoviDestra=False
        self.muoviSinistra=False
        self.inAria=True

    def nextDestra(self):
        if self.posAnimazione>9:
            self.posAnimazione=0
        imageDestra=self.animazioneDestra[self.posAnimazione]
        self.posAnimazione+=1
        return imageDestra
    
    def nextSinistra(self):
        if self.posAnimazione>9:
            self.posAnimazione=0
        imageSinistra=self.animazioneSinistra[self.posAnimazione]
        self.posAnimazione+=1
        return imageSinistra

    def muovi_Destra(self):
        self.muoviDestra=True
        self.image=self.nextDestra()
        self.muoviSinistra=False
    
    def muovi_Sinistra(self):
        self.muoviSinistra=True
        self.image=self.nextSinistra()
        self.muoviDestra=False
    
    def StopDestra(self):
        self.muoviDestra=False
        self.image=self.imageDestra1

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


    def calcolaVelMax(self):
        if self.vel[1]<=3 and self.vel[0]!=0:
            self.velMax=3
        if self.velMax<self.vel[1]:
            self.velMax=self.vel[1]
    
    def draw(self):
        self.screen.blit(self.image,self.rect)

