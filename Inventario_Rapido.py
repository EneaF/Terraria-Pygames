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

        self.BoxinventarioSelC1=pygame.image.load("images/BoxInventarioSelezionatoC1.png")
        self.BoxinventarioSelC2=pygame.image.load("images/BoxInventarioSelezionatoC2.png")
        self.BoxinventarioSelC3=pygame.image.load("images/BoxInventarioSelezionatoC3.png")
        self.BoxinventarioSelC4=pygame.image.load("images/BoxInventarioSelezionatoC4.png")
        self.BoxinventarioSelC5=pygame.image.load("images/BoxInventarioSelezionatoC5.png")
        self.BoxinventarioSelC6=pygame.image.load("images/BoxInventarioSelezionatoC6.png")
        self.BoxinventarioSelC7=pygame.image.load("images/BoxInventarioSelezionatoC7.png")

        self.BoxinventarioSelC1 = pygame.transform.scale(self.BoxinventarioSelC1,self.sizeBlocco)
        self.BoxinventarioSelC2 = pygame.transform.scale(self.BoxinventarioSelC2,self.sizeBlocco)
        self.BoxinventarioSelC3 = pygame.transform.scale(self.BoxinventarioSelC3,self.sizeBlocco)
        self.BoxinventarioSelC4 = pygame.transform.scale(self.BoxinventarioSelC4,self.sizeBlocco)
        self.BoxinventarioSelC5 = pygame.transform.scale(self.BoxinventarioSelC5,self.sizeBlocco)
        self.BoxinventarioSelC6 = pygame.transform.scale(self.BoxinventarioSelC6,self.sizeBlocco)
        self.BoxinventarioSelC7 = pygame.transform.scale(self.BoxinventarioSelC7,self.sizeBlocco)



        self.foglia = pygame.image.load("images/FoglieTrsp.png")
        self.legno = pygame.image.load("images/Legno.jpeg")
        self.pietra = pygame.image.load("images/Stone.jpeg")
        self.erba = pygame.image.load("images/Erba.png")
        self.terra = pygame.image.load("images/Terra.jpeg")
        self.oakPlanks = pygame.image.load("images/oakPlanks.png")
        self.scala = pygame.image.load("images/Ladder.png")
        self.sapling = pygame.image.load("images/sapling.png")
        self.pistola = pygame.image.load("images/pistola.png")

        self.foglia = pygame.transform.scale(self.foglia,self.sizeItem)
        self.legno = pygame.transform.scale(self.legno,self.sizeItem)
        self.pietra = pygame.transform.scale(self.pietra,self.sizeItem)
        self.erba = pygame.transform.scale(self.erba,self.sizeItem)
        self.terra = pygame.transform.scale(self.terra,self.sizeItem)
        self.oakPlanks = pygame.transform.scale(self.oakPlanks,self.sizeItem)
        self.scala = pygame.transform.scale(self.scala,self.sizeItem)
        self.sapling = pygame.transform.scale(self.sapling,self.sizeItem)
        self.pistola = pygame.transform.scale(self.pistola,self.sizeItem)

    def draw(self,blocco,qta=0,sel=False,cooldown=None):
        qta=str(qta)
        if sel==False:
            selezionato=self.Boxinventario
        else:
            selezionato=self.BoxinventarioSel
        
        if cooldown==7:
            selezionato=self.BoxinventarioSelC7
        elif cooldown==1:
            selezionato=self.BoxinventarioSelC6
        elif cooldown==2:
            selezionato=self.BoxinventarioSelC5
        elif cooldown==3:
            selezionato=self.BoxinventarioSelC4
        elif cooldown==4:
            selezionato=self.BoxinventarioSelC3
        elif cooldown==5:
            selezionato=self.BoxinventarioSelC2
        elif cooldown==6:
            selezionato=self.BoxinventarioSelC1
        
        if blocco==1:
            bloccoDisplay=self.foglia
        elif blocco==2:
            bloccoDisplay=self.legno
        elif blocco==3:
            bloccoDisplay=self.pietra
        elif blocco==4:
            bloccoDisplay=self.erba
        elif blocco==5:
            bloccoDisplay=self.terra
        elif blocco==6:
            bloccoDisplay=self.oakPlanks
        elif blocco==7:
            bloccoDisplay=self.scala
        elif blocco==8:
            bloccoDisplay=self.sapling
        elif blocco==9:
            bloccoDisplay=self.pistola
        
        carattere = pygame.font.Font(None,int(self.size[0]/10*5))
        scritta = carattere.render(qta,True,(50,50,50))

        self.screen.blit(selezionato,self.rectBox)
        self.screen.blit(bloccoDisplay,self.rectItem)
        self.screen.blit(scritta,self.rectScritta)
        
