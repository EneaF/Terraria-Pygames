import pygame
from pygame.locals import*

class SfondoClass():
    def __init__(self,pos,size,screen,sizeWindow):
        self.screen=screen
        self.sizeWindow=sizeWindow
        self.size=size
        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))

        self.sfondo=pygame.image.load("images/Sfondo.png")
        self.sfondo=pygame.transform.scale(self.sfondo,self.sizeWindow)
        self.sfondo1=pygame.image.load("images/Sfondo1.png")
        self.sfondo1=pygame.transform.scale(self.sfondo1,self.sizeWindow)
        self.sfondo2=pygame.image.load("images/Sfondo2.png")
        self.sfondo2=pygame.transform.scale(self.sfondo2,self.sizeWindow)
        self.sfondo3=pygame.image.load("images/Sfondo3.png")
        self.sfondo3=pygame.transform.scale(self.sfondo3,self.sizeWindow)
        self.sfondo4=pygame.image.load("images/Sfondo4.png")
        self.sfondo4=pygame.transform.scale(self.sfondo4,self.sizeWindow)
        self.sfondoSottoterra=pygame.image.load("images/SfondoSottoterra.jpeg")
        self.sfondoSottoterra=pygame.transform.scale(self.sfondoSottoterra,self.sizeWindow)
        self.sfondoBoss=pygame.image.load("images/SfondoBoss.jpg")
        self.sfondoBoss=pygame.transform.scale(self.sfondoBoss,self.sizeWindow)

        self.sole=pygame.image.load("images/Sole.png")
        self.luna=pygame.image.load("images/Luna.png")

        self.notte=False
        self.image=self.sole
        self.sfondoAct=self.sfondo

    def drawBoss(self):
        self.screen.blit(self.sfondoBoss,self.rect)
    
    def draw(self,time,posMondoy):
        if posMondoy>=-800 and posMondoy<=-100:
            diffY=-100
            diffY-=posMondoy
        elif posMondoy<-800:
            diffY=700
        else :
            diffY=0
        self.screen.blit(self.sfondoAct,((0,0-diffY),(self.sizeWindow)))
        self.screen.blit(self.sfondoSottoterra,((0,700-diffY),(self.sizeWindow)))
        PosCielo=(time-90)/3
        ritorna=1
        if PosCielo>=1000 and self.notte==False:
            self.notte=True
            ritorna=0
        elif PosCielo>=1000 and self.notte==True:
            self.notte=False
            ritorna=0
        if self.notte==False:
            if PosCielo<50:
                self.sfondoAct=self.sfondo2
            elif PosCielo<150:
                self.sfondoAct=self.sfondo1
            elif PosCielo<850:
                self.sfondoAct=self.sfondo
            elif PosCielo<950:
                self.sfondoAct=self.sfondo1
            else:
                self.sfondoAct=self.sfondo2
            self.screen.blit(self.sole,((PosCielo,130-diffY),(self.size)))
        else:
            if PosCielo<50:
                self.sfondoAct=self.sfondo2
            elif PosCielo<150:
                self.sfondoAct=self.sfondo3
            elif PosCielo<850:
                self.sfondoAct=self.sfondo4
            elif PosCielo<950:
                self.sfondoAct=self.sfondo3
            else:
                self.sfondoAct=self.sfondo2
            self.screen.blit(self.luna,((PosCielo,130-diffY),(self.size)))
        return ritorna
