import pygame
from pygame.locals import *

class MondoClass():
    def __init__(self,pos,size,screen):
        self.screen=screen

        self.mondoRect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))

        self.sizeBlocco=(50,50)

        self.foglia = pygame.image.load("images/FoglieTrsp.png")
        self.legno = pygame.image.load("images/Legno.jpeg")
        self.pietra = pygame.image.load("images/Stone.jpeg")
        self.erba = pygame.image.load("images/Erba.png")
        self.terra = pygame.image.load("images/Terra.jpeg")

        self.foglia = pygame.transform.scale(self.foglia,self.sizeBlocco)
        self.legno = pygame.transform.scale(self.legno,self.sizeBlocco)
        self.pietra = pygame.transform.scale(self.pietra,self.sizeBlocco)
        self.erba = pygame.transform.scale(self.erba,self.sizeBlocco)
        self.terra = pygame.transform.scale(self.terra,self.sizeBlocco)
        self.blocchi=[]
    
    def draw(self):
        posizy=-50
        with open("Mondo.txt","r",encoding="utf-8") as f:
            for riga in f:
                posizy=posizy+50
                posizx=-50
                riga=riga.split()
                for el in riga:
                    el = int(el)
                    posizx=posizx+50
                    if el==0:
                        pass
                    elif el==1:
                        self.screen.blit(self.erba,((posizx,posizy),(self.sizeBlocco)))
                        if (posizx,posizy) not in self.blocchi:
                            self.blocchi.append((posizx,posizy))
                    elif el==2:
                        self.screen.blit(self.terra,((posizx,posizy),(self.sizeBlocco)))
                        if (posizx,posizy) not in self.blocchi:
                            self.blocchi.append((posizx,posizy))
                    elif el==3:
                        self.screen.blit(self.pietra,((posizx,posizy),(self.sizeBlocco)))
                        if (posizx,posizy) not in self.blocchi:
                            self.blocchi.append((posizx,posizy))
                    elif el==4:
                        self.screen.blit(self.foglia,((posizx,posizy),(self.sizeBlocco)))
                        if (posizx,posizy) not in self.blocchi:
                            self.blocchi.append((posizx,posizy))
                    elif el==5:
                        self.screen.blit(self.legno,((posizx,posizy),(self.sizeBlocco)))
                        if (posizx,posizy) not in self.blocchi:
                            self.blocchi.append((posizx,posizy))
            

                