import pygame
from pygame.locals import *

class Personaggio():
    def __init__(self,screen,pos,size):
        self.screen=screen
        self.pos=pos

        self.rect = pygame.Rect((pos[0],pos[1]),(size[0],size[1]))

        self.persDx1 = pygame.image.load("images/Pers_Dx1.png")
        self.persSx1 = pygame.image.load("images/Pers_Sx1.png")
        self.persDx2 = pygame.image.load("images/Pers_Dx2.png")
        self.persSx2 = pygame.image.load("images/Pers_Sx2.png")
        self.persDx3 = pygame.image.load("images/Pers_Dx3.png")
        self.persSx3 = pygame.image.load("images/Pers_Sx3.png")
        self.persDx4 = pygame.image.load("images/Pers_Dx4.png")
        self.persSx4 = pygame.image.load("images/Pers_Sx4.png")
        self.persDx5 = pygame.image.load("images/Pers_Dx5.png")
        self.persSx5 = pygame.image.load("images/Pers_Sx5.png")
        self.persDx6 = pygame.image.load("images/Pers_Dx6.png")
        self.persSx6 = pygame.image.load("images/Pers_Sx6.png")
        self.persDx7 = pygame.image.load("images/Pers_Dx7.png")
        self.persSx7 = pygame.image.load("images/Pers_Sx7.png")
        self.persDx8 = pygame.image.load("images/Pers_Dx8.png")
        self.persSx8 = pygame.image.load("images/Pers_Sx8.png")
        self.persDx9 = pygame.image.load("images/Pers_Dx9.png")
        self.persSx9 = pygame.image.load("images/Pers_Sx9.png")
        self.persDx10 = pygame.image.load("images/Pers_Dx10.png")
        self.persSx10 = pygame.image.load("images/Pers_Sx10.png")
        self.persDx11 = pygame.image.load("images/Pers_Dx11.png")
        self.persSx11 = pygame.image.load("images/Pers_Sx11.png")
        self.persDx12 = pygame.image.load("images/Pers_Dx12.png")
        self.persSx12 = pygame.image.load("images/Pers_Sx12.png")
        self.persDx13 = pygame.image.load("images/Pers_Dx13.png")
        self.persSx13 = pygame.image.load("images/Pers_Sx13.png")
        self.persDx14 = pygame.image.load("images/Pers_Dx14.png")
        self.persSx14 = pygame.image.load("images/Pers_Sx14.png")
        self.persSaltoDx = pygame.image.load("images/Pers_SaltoDx.png")
        self.persSaltoSx = pygame.image.load("images/Pers_SaltoSx.png")

        self.persDx1 = pygame.transform.scale(self.persDx1,size)
        self.persSx1 = pygame.transform.scale(self.persSx1,size)
        self.persDx2 = pygame.transform.scale(self.persDx2,size)
        self.persSx2 = pygame.transform.scale(self.persSx2,size)
        self.persDx3 = pygame.transform.scale(self.persDx3,size)
        self.persSx3 = pygame.transform.scale(self.persSx3,size)
        self.persDx4 = pygame.transform.scale(self.persDx4,size)
        self.persSx4 = pygame.transform.scale(self.persSx4,size)
        self.persDx5 = pygame.transform.scale(self.persDx5,size)
        self.persSx5 = pygame.transform.scale(self.persSx5,size)
        self.persDx6 = pygame.transform.scale(self.persDx6,size)
        self.persSx6 = pygame.transform.scale(self.persSx6,size)
        self.persDx7 = pygame.transform.scale(self.persDx7,size)
        self.persSx7 = pygame.transform.scale(self.persSx7,size)
        self.persDx8 = pygame.transform.scale(self.persDx8,size)
        self.persSx8 = pygame.transform.scale(self.persSx8,size)
        self.persDx9 = pygame.transform.scale(self.persDx9,size)
        self.persSx9 = pygame.transform.scale(self.persSx9,size)
        self.persDx10 = pygame.transform.scale(self.persDx10,size)
        self.persSx10 = pygame.transform.scale(self.persSx10,size)
        self.persDx11 = pygame.transform.scale(self.persDx11,size)
        self.persSx11 = pygame.transform.scale(self.persSx11,size)
        self.persDx12 = pygame.transform.scale(self.persDx12,size)
        self.persSx12 = pygame.transform.scale(self.persSx12,size)
        self.persDx13 = pygame.transform.scale(self.persDx13,size)
        self.persSx13 = pygame.transform.scale(self.persSx13,size)
        self.persDx14 = pygame.transform.scale(self.persDx14,size)
        self.persSx14 = pygame.transform.scale(self.persSx14,size)
        self.persSaltoDx = pygame.transform.scale(self.persSaltoDx,size)
        self.persSaltoSx = pygame.transform.scale(self.persSaltoSx,size)

        
        self.image=self.persDx6

        self.vel=[0,0]
        self.gravita = 0.3
        self.forzaSalto = 6.5
        self.VelMovimento = 5
        self.velMax=0
        
        self.posAnimazioneDx=0
        self.posAnimazioneSx=0
        self.animazioneDestra=[self.persDx1,self.persDx2,self.persDx3,self.persDx4,self.persDx5,self.persDx6,self.persDx7,self.persDx8,self.persDx9,self.persDx10,self.persDx11,self.persDx12,self.persDx13,self.persDx14]
        self.animazioneSinistra=[self.persSx1,self.persSx2,self.persSx3,self.persSx4,self.persSx5,self.persSx6,self.persSx7,self.persSx8,self.persSx9,self.persSx10,self.persSx11,self.persSx12,self.persSx13,self.persSx14]

        self.muoviDestra=False
        self.muoviSinistra=False
        self.inAria=True

    def nextDestra(self):
        if self.posAnimazioneDx>13:
            self.posAnimazioneDx=0
        self.image=self.animazioneDestra[self.posAnimazioneDx]
        self.posAnimazioneDx+=1
    
    def nextSinistra(self):
        if self.posAnimazioneSx>13:
            self.posAnimazioneSx=0
        self.image=self.animazioneSinistra[self.posAnimazioneSx]
        self.posAnimazioneSx+=1

    def StopSinistra(self):
        self.muoviSinistra=False

    def StopDestra(self):
        self.muoviDestra=False

    def muovi_Destra(self):
        self.muoviDestra=True
        if self.inAria==False:
            self.nextDestra()
        else:
            self.image=self.persSaltoDx
        self.muoviSinistra=False
    
    def muovi_Sinistra(self):
        self.muoviSinistra=True
        if self.inAria==False:
            self.nextSinistra()
        else:
            self.image=self.persSaltoSx
        self.muoviDestra=False
    
    def stopAll(self):
        if self.image in self.animazioneDestra:
            self.image=self.persDx6
        else:
            self.image=self.persSx6

    def Salto(self):
        if self.inAria==False:
            self.vel[1] -= self.forzaSalto
            self.inAria = True
            if self.image in self.animazioneDestra:
                self.image=self.persSaltoDx
            else:
                self.image=self.persSaltoSx
    
    def StopSalto(self,blocco):
        self.vel[1]=0
        self.rect.top=blocco
        self.inAria=True
    
    def StopBasso(self,topBlocco):
        self.rect.bottom=topBlocco+1
        self.vel[1]=0
        self.inAria=False
    
    def SaleScala(self):
        self.vel[1]=-4

    def ScendeScala(self):
        self.vel[1]=+4
    
    def SuScala(self):
        self.vel[1]=0


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

