import pygame, sys
from pygame.locals import *



#initialisation du module pygame et mixer 
pygame.init()


#Création de la fenêtre
fenetre = pygame.display.set_mode((1000, 700))
background_color = (31, 31, 31)
fenetre.fill(background_color)
pygame.display.flip()


square = pygame.image.load("img/square.jpg")

def draw_interface(difficulty_level):
    #Si le mode de diffidulté est facile
    if difficulty_level == "EASY":
        #On dessine les lignes de la grille
        for i in range(4):
            fenetre.blit(square, (200 + i*61,100))

        for i in range(6):
            fenetre.blit(square, (139 + i*61,158))

        for i in range(6):
            fenetre.blit(square, (139 + i*61,216))

        for i in range(6):
            fenetre.blit(square, (139 + i*61,274))

        for i in range(6):
            fenetre.blit(square, (139 + i*61,332))

        for i in range(4):
            fenetre.blit(square, (200 + i*61,390))

    elif difficulty_level == "NORMAL":
        pass
    elif difficulty_level == "HARD":
        pass


#déclaration des couleurs


#variables 
etatPartie = True 
click = 0
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

draw_interface("EASY")

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


