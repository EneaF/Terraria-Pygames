import pygame,random
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
        self.bedrock = pygame.image.load("images/bedrock.png")
        self.oakPlanks = pygame.image.load("images/oakPlanks.png")
        self.ferro = pygame.image.load("images/ferro.png")
        self.diamante = pygame.image.load("images/diamante.png")
        

        self.fogliaDietro = pygame.image.load("images/FoglieTrspDietro.png")
        self.legnoDietro = pygame.image.load("images/LegnoDietro.jpg")
        self.pietraDietro = pygame.image.load("images/StoneDietro.jpg")
        self.erbaDietro = pygame.image.load("images/ErbaDietro.png")
        self.terraDietro = pygame.image.load("images/TerraDietro.jpg")
        self.oakPlanksDietro = pygame.image.load("images/oakPlanksDietro.png")
        self.scala = pygame.image.load("images/Ladder.png")
        self.sapling = pygame.image.load("images/sapling.png")

        self.foglia = pygame.transform.scale(self.foglia,self.sizeBlocco)
        self.legno = pygame.transform.scale(self.legno,self.sizeBlocco)
        self.pietra = pygame.transform.scale(self.pietra,self.sizeBlocco)
        self.erba = pygame.transform.scale(self.erba,self.sizeBlocco)
        self.terra = pygame.transform.scale(self.terra,self.sizeBlocco)
        self.bedrock = pygame.transform.scale(self.bedrock,self.sizeBlocco)
        self.oakPlanks = pygame.transform.scale(self.oakPlanks,self.sizeBlocco)
        self.ferro = pygame.transform.scale(self.ferro,self.sizeBlocco)
        self.diamante = pygame.transform.scale(self.diamante,self.sizeBlocco)

        self.fogliaDietro = pygame.transform.scale(self.fogliaDietro,self.sizeBlocco)
        self.legnoDietro = pygame.transform.scale(self.legnoDietro,self.sizeBlocco)
        self.pietraDietro = pygame.transform.scale(self.pietraDietro,self.sizeBlocco)
        self.erbaDietro = pygame.transform.scale(self.erbaDietro,self.sizeBlocco)
        self.terraDietro = pygame.transform.scale(self.terraDietro,self.sizeBlocco)
        self.oakPlanksDietro = pygame.transform.scale(self.oakPlanksDietro,self.sizeBlocco)
        self.scala = pygame.transform.scale(self.scala,self.sizeBlocco)
        self.sapling = pygame.transform.scale(self.sapling,self.sizeBlocco)

        self.blocchi=[]
        self.blocchiAria=[]
        self.blocchiDietro=[]
        self.scale=[]
        self.saplings=[]

    def ScorrimentoDestra(self,scorrix,scorriy):
        self.posMondox=-45
        self.posMondoy=-50
        self.blocchi=[]
        self.blocchiAria=[]
        self.scale=[]

    def RimuoviBlocco(self,posMondox,posMondoy,Blocco):
        posizy=posMondoy
        with open("FileTXT/Mondo.txt","r+",encoding="utf-8") as f:
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
                        riga[i]="A"
                riga=str(riga)
                tmp.append(riga)

        f.close()

        with open("FileTXT/Mondo.txt","r+",encoding="utf-8") as f:
            f.truncate()
        

        f1 = open("FileTXT/Mondo.txt","a",encoding="utf-8")
        
        for riga in tmp:
            riga=riga.strip('[]",')
            riga=riga.strip("'")
            riga=riga.replace("', '"," ")
            
            f1.write(riga)
            f1.write("\n")
        f1.close()
        self.blocchi=[]
        self.blocchiAria=[]
        self.blocchiDietro=[]
        self.scale=[]

    def AggiungiBlocco(self,posMondox,posMondoy,BloccoAria,lum):
        posizy=posMondoy
        with open("FileTXT/Mondo.txt","r+",encoding="utf-8") as f:
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
                            riga[i]="F"
                        elif lum==2:
                            riga[i]="L"
                        elif lum==3:
                            riga[i]="P"
                        elif lum==4:
                            riga[i]="E"
                        elif lum==5:
                            riga[i]="T"
                        elif lum==6:
                            riga[i]="O"
                        elif lum==7:
                            pass   
                        
                riga=str(riga)
                tmp.append(riga)

        f.close()

        with open("FileTXT/Mondo.txt","r+",encoding="utf-8") as f:
            f.truncate()
        

        f1 = open("FileTXT/Mondo.txt","a",encoding="utf-8")
        
        for riga in tmp:
            riga=riga.strip('[]",')
            riga=riga.strip("'")
            riga=riga.replace("', '"," ")
            
            f1.write(riga)
            f1.write("\n")
        f1.close()
        self.blocchi=[]
        self.blocchiAria=[]
        self.blocchiDietro=[]
        self.scale=[]
        
    def AggiungiBloccoDietro(self,posMondox,posMondoy,BloccoAria,lum):
        posizy=posMondoy
        with open("FileTXT/Mondo.txt","r+",encoding="utf-8") as f:
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
                            riga[i]="f"
                        elif lum==2:
                            riga[i]="l"
                        elif lum==3:
                            riga[i]="p"
                        elif lum==4:
                            riga[i]="e"
                        elif lum==5:
                            riga[i]="t"
                        elif lum==6:
                            riga[i]="o"
                        elif lum==7:
                            riga[i]="s"
                        elif lum==8:
                            riga[i]="S"
                        
                riga=str(riga)
                tmp.append(riga)

        f.close()

        with open("FileTXT/Mondo.txt","r+",encoding="utf-8") as f:
            f.truncate()
        

        f1 = open("FileTXT/Mondo.txt","a",encoding="utf-8")
        
        for riga in tmp:
            riga=riga.strip('[]",')
            riga=riga.strip("'")
            riga=riga.replace("', '"," ")
            
            f1.write(riga)
            f1.write("\n")
        f1.close()
        self.blocchi=[]
        self.blocchiAria=[]
        self.blocchiDietro=[]
        self.scale=[]
        
    def draw(self,posMondox,posMondoy):
        posizy=posMondoy
        nY=0
        with open("FileTXT/Mondo.txt","r",encoding="utf-8") as f:
            for riga in f:
                nY+=1
                posizy=posizy+50
                posizx=posMondox
                nX=0
                riga=riga.split()
                for el in riga:
                    posizx=posizx+50
                    nX+=1
                    if el=="A":
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy) not in self.blocchiAria:
                                self.blocchiAria.append((posizx,posizy))
                    elif el=="E":
                        self.screen.blit(self.erba,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="T":
                        self.screen.blit(self.terra,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="P":
                        self.screen.blit(self.pietra,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="F":
                        self.screen.blit(self.foglia,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="L":
                        self.screen.blit(self.legno,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="B":
                        self.screen.blit(self.bedrock,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="O":
                        self.screen.blit(self.oakPlanks,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="e":
                        self.screen.blit(self.erbaDietro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="t":
                        self.screen.blit(self.terraDietro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="p":
                        self.screen.blit(self.pietraDietro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="f":
                        self.screen.blit(self.fogliaDietro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="l":
                        self.screen.blit(self.legnoDietro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="o":
                        self.screen.blit(self.oakPlanksDietro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="s":
                        self.screen.blit(self.scala,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.scale:
                                self.scale.append((posizx,posizy))
                            if (posizx,posizy,el) not in self.blocchiDietro:
                                self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="S":
                        self.screen.blit(self.sapling,((posizx,posizy),(self.sizeBlocco)))
                        if (posizx,posizy,el) not in self.blocchiDietro:
                            self.blocchiDietro.append((posizx,posizy,el))
                    elif el=="I":
                        self.screen.blit(self.ferro,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
                    elif el=="D":
                        self.screen.blit(self.diamante,((posizx,posizy),(self.sizeBlocco)))
                        if posizx>=0 and posizy>=0 and posizx<=1000 and posizy<=700:
                            if (posizx,posizy,el) not in self.blocchi:
                                self.blocchi.append((posizx,posizy,el))
         