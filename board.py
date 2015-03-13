import pygame, sys
from pygame.locals import *
from random import *


#initialisation du module pygame et mixer 
pygame.init()
pygame.mixer.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((800, 800))
fond = pygame.image.load("bg.png")
fenetre.blit(fond, (0,0))
pygame.display.flip()

#déclaration des couleurs 
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,127,0)
PURPLE = (255,0,127)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
COULEUR = (205,201,201)

#variables 
etatPartie = True 
click = 0
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

#MAIN 
while True:
    for event in pygame.event.get(): #Evenement on quitte le jeu
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        #Evenement clic gauche souris choix position sphère  
        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and click < 3 and etatPartie == True:#condition d'entrée
                x = event.pos[0]
                y = event.pos[1]
                pygame.draw.circle(fenetre,YELLOW, (x,y),12)

                click += 1
                
                if click == 1:
                    a = x
                    b = y
                elif click == 2:
                    c = x
                    d = y
                else: 
                    e = x
                    f = y

        #Evenement clic central souris boutons
        elif event.type == MOUSEBUTTONDOWN and event.button == 2:
                if event.pos[0] in range(0,800) and event.pos[1] in range(0,800):
                        print(event.pos[0], event.pos[1])

        #Evenement clic droit souris boutons
        elif event.type == MOUSEBUTTONDOWN and event.button == 3 and click > 0:
                if event.pos[0] in range(526,663) and event.pos[1] in range(40,92):
                    print("lol")

                    if click == 1:
                        pygame.draw.circle(fenetre,BLACK, (a,b),12)
                    elif click == 2: 
                        pygame.draw.circle(fenetre,BLACK, (c,d),12)
                    else:
                        pygame.draw.circle(fenetre,BLACK, (e,f),12)

                    click -= 1

    pygame.display.update()
