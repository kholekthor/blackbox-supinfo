import pygame, sys
from pygame.locals import *

#initialisation du module pygame
pygame.init()
#Création de la fenêtre
window = pygame.display.set_mode((1000, 700))
background_color = (31, 31, 31)
window.fill(background_color)
pygame.display.flip()
#Chargement des images correspondants aux cases des rayons et des atomes
square = pygame.image.load("img/square.jpg")
ray_square = pygame.image.load("img/ray_square.jpg")
atom_img = pygame.image.load("img/atom.png")


class Atom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = atom_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.display.update()


def init_centers_list(size):
    #Initialise un tableau des centres qui contient les centres de toutes les cases du jeu
    centers_list = list()
    for i in range(size):
        for j in range(size):
            centers_list.append((110 + j*61, 115 + i*58))
    return centers_list


init_centers_list(6)


def draw_lines(size):
    for i in range(size):
        window.blit(ray_square, (100 + i*61,50))

    for i in range(size):
        window.blit(ray_square, (100 + i*61, 50 + 58*(size+1)))

    for j in range(size):
        for i in range(size + 2):
            if i == 0 or i == size + 1:
                window.blit(ray_square, (39 + i*61,108 + j*58))
            else:
                window.blit(square, (39 + i*61,108 + j*58))


def draw_interface(difficulty_level):
    #Si le mode de diffidulté est facile
    if difficulty_level == "EASY":
        #On dessine les lignes de la grille
        draw_lines(4)

    elif difficulty_level == "NORMAL":
        draw_lines(6)

    elif difficulty_level == "HARD":
        draw_lines(8)

#variables 
etatPartie = True 
click = 0
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

draw_interface("NORMAL")

#MAIN 
while True:
    for event in pygame.event.get():
        #Evenement on quitte le jeu
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        #Evenement clic gauche souris choix position sphère  
        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and click < 3 and etatPartie:#condition d'entrée
                x = event.pos[0]
                y = event.pos[1]

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
                        pygame.draw.circle(window,BLACK, (a,b),12)
                    elif click == 2: 
                        pygame.draw.circle(window,BLACK, (c,d),12)
                    else:
                        pygame.draw.circle(window,BLACK, (e,f),12)

                    click -= 1

    pygame.display.update()


