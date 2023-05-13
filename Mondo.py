import pygame
from pygame.locals import *

class MondoClass():
    def __init__(self,pos,size,screen,posMondo):
        self.screen=screen

        self.mondoRect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))


        self.posMondox=posMondo[0]
        self.posMondoy=posMondo[1]

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
        self.blocchiAria=[]

    def ScorrimentoDestra(self,scorrix,scorriy):
        self.posMondox=-45
        self.posMondoy=-50
        self.blocchi=[]
        self.blocchiAria=[]

    def RimuoviBlocco(self,posMondox,posMondoy,Blocco):
        posizy=posMondoy
        with open("Mondo.txt","r+",encoding="utf-8") as f:
            tutto=[]
            for riga in f:
                tutto.append(riga)

            tmp=[]
            for riga in tutto:
                riga=riga.strip().split()
                posizy=posizy+50
                posizx=posMondox
                for i in range(len(riga)):
                    posizx=posizx+50
                    if (posizx,posizy)==Blocco:
                        riga[i]="0"
                riga=str(riga)
                tmp.append(riga)

        f.close()

        with open("Mondo.txt","r+",encoding="utf-8") as f:
            f.truncate()
        

        f1 = open("Mondo.txt","a",encoding="utf-8")
        
        for riga in tmp:
            riga=riga.strip('[]",')
            riga=riga.strip("'")
            riga=riga.replace("', '"," ")
            
            f1.write(riga)
            f1.write("\n")
        f1.close()
        self.blocchi=[]
        self.blocchiAria=[]

    def AggiungiBlocco(self,posMondox,posMondoy,BloccoAria,lum):
        posizy=posMondoy
        with open("Mondo.txt","r+",encoding="utf-8") as f:
            tutto=[]
            for riga in f:
                tutto.append(riga)

            tmp=[]
            for riga in tutto:
                riga=riga.strip().split()
                posizy=posizy+50
                posizx=posMondox
                for i in range(len(riga)):
                    posizx=posizx+50
                    if (posizx,posizy)==BloccoAria:
                        if lum==1:
                            riga[i]="4"
                        elif lum==2:
                            riga[i]="5"
                        elif lum==3:
                            riga[i]="3"
                        elif lum==4:
                            riga[i]="1"
                        elif lum==5:
                            riga[i]="2"
                        
                riga=str(riga)
                tmp.append(riga)

        f.close()

        with open("Mondo.txt","r+",encoding="utf-8") as f:
            f.truncate()
        

        f1 = open("Mondo.txt","a",encoding="utf-8")
        
        for riga in tmp:
            riga=riga.strip('[]",')
            riga=riga.strip("'")
            riga=riga.replace("', '"," ")
            
            f1.write(riga)
            f1.write("\n")
        f1.close()
        self.blocchi=[]
        self.blocchiAria=[]

    def draw(self,posMondox,posMondoy):
        posizy=posMondoy
        with open("Mondo.txt","r",encoding="utf-8") as f:
            for riga in f:
                posizy=posizy+50
                posizx=posMondox
                riga=riga.split()
                for el in riga:
                    el = int(el)
                    posizx=posizx+50
                    if el==0:
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy) not in self.blocchiAria:
                                self.blocchiAria.append((posizx,posizy))
                    elif el==1:
                        self.screen.blit(self.erba,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el==2:
                        self.screen.blit(self.terra,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el==3:
                        self.screen.blit(self.pietra,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el==4:
                        self.screen.blit(self.foglia,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el==5:
                        self.screen.blit(self.legno,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el==9:
                        # self.screen.blit(self.legno,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
            

                