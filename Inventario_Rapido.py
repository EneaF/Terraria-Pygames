import pygame
from pygame.locals import *

class Inventario():
    def __init__(self,pos,size,screen):
        self.screen=screen
        self.size=size
        self.sizeBlocco=(size[0],size[1])
        self.sizeItem=((size[0]/10*6),(size[1]/10*6))
        self.sizeScritta=((size[0]/10*2),(size[1]/10*2))

        self.rectBox=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.rectItem=pygame.Rect((pos[0]+((size[0]/10*6)/3),pos[1]+((size[1]/10*6)/3)),self.sizeItem)
        self.rectScritta=pygame.Rect((pos[0]+(size[0]/10*5),pos[1]+(size[1]/10*7)),self.sizeScritta)

        self.Boxinventario=pygame.image.load("images/BoxInventario.png")
        self.BoxinventarioSel=pygame.image.load("images/BoxInventarioSelezionato.png")
        self.Boxinventario = pygame.transform.scale(self.Boxinventario,self.sizeBlocco)
        self.BoxinventarioSel = pygame.transform.scale(self.BoxinventarioSel,self.sizeBlocco)

        self.foglia = pygame.image.load("images/FoglieTrsp.png")
        self.legno = pygame.image.load("images/Legno.jpeg")
        self.pietra = pygame.image.load("images/Stone.jpeg")
        self.erba = pygame.image.load("images/Erba.png")
        self.terra = pygame.image.load("images/Terra.jpeg")

        self.foglia = pygame.transform.scale(self.foglia,self.sizeItem)
        self.legno = pygame.transform.scale(self.legno,self.sizeItem)
        self.pietra = pygame.transform.scale(self.pietra,self.sizeItem)
        self.erba = pygame.transform.scale(self.erba,self.sizeItem)
        self.terra = pygame.transform.scale(self.terra,self.sizeItem)

    def draw(self,blocco,qta=0,sel=False):
        qta=str(qta)
        if sel==False:
            selezionato=self.Boxinventario
        else:
            selezionato=self.BoxinventarioSel
        
        if blocco==1:
            bloccoDisplay=self.foglia
        elif blocco==2:
            bloccoDisplay=self.legno
        elif blocco==3:
            bloccoDisplay=self.pietra
        elif blocco==4:
            bloccoDisplay=self.erba
        else:
            bloccoDisplay=self.terra
        
        carattere = pygame.font.Font(None,int(self.size[0]/10*5))
        scritta = carattere.render(qta,True,(50,50,50))

        self.screen.blit(selezionato,self.rectBox)
        self.screen.blit(bloccoDisplay,self.rectItem)
        self.screen.blit(scritta,self.rectScritta)
        
