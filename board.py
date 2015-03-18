import pygame, sys
from pygame.locals import *
from math import *
from random import *


#Initialisation du module pygame
pygame.init()
pygame.display.set_caption("Blackbox | Corentin Duflos && Reda El Ghomari && Camille Osinski && Etienne Mouraille")

#Création de la fenêtre
window = pygame.display.set_mode((1000, 700))
window.fill((31, 31, 31))
pygame.display.flip()

#Chargement des images correspondants aux cases des rayons et des atomes
square_img = pygame.image.load("img/square.jpg")
ray_square_img = pygame.image.load("img/ray_square.jpg")
atom_img = pygame.image.load("img/atom.png")
atoms = pygame.sprite.Group()
atoms_coords = list()

#variables 
nbSphere = 0
nbDifficulte = 2
size = 6


class Atom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = atom_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.display.update()

    def get_position(self):
        return self.rect.x, self.rect.y


#############################
### Fonctions et Méthodes ###
#############################

def init_centers_grid(size):
    #Initialise une liste de tous les centers des cases du jeu
    centers_grid = list()
    for i in range(size):
        for j in range(size):
            #center = position de l'atome
            centers_grid.append((130 + j*61, 137 + i*58))
    return centers_grid


def init_coords_grid(size):
    #Initialise une liste de toutes les positions possibles des atomes dans le jeu
    coords_list = list()
    for i in range(size):
        for j in range(size):
            #center = position de l'atome
            coords_list.append((110 + j*61, 115 + i*58))
    return coords_list


def init_centers_launchzone(size):
    #Initialise une liste de tous les centers de la zone de lancement
    centers_list = list()
    for i in range(size):
        #haut
        centers_list.append((130 + i*61, 79))
    for j in range(size):
        #gauche
        centers_list.append((69, 137 + j*58))
    for k in range(size):
        #bas
        centers_list.append((130 + k*61, 486))
    for l in range(size):
        #droite
        centers_list.append((495, 137+l*58))

    return centers_list


def nearest_center(centers_list, x, y):
    distances_list = list()
    #Calcule la distance euclidienne entre chaque center et la position du clic
    for center in centers_list:
        distances_list.append(sqrt((center[0] - x)**2 + (center[1] - y)**2))

    #Détermine les coordonnées du centre le plus proche et retourne son indice
    return distances_list.index(min(distances_list))


def draw_lines(size):
    for i in range(size):
        window.blit(ray_square_img, (100 + i*61, 50))

    for i in range(size):
        window.blit(ray_square_img, (100 + i*61, 50 + 58*(size+1)))

    for j in range(size):
        for i in range(size + 2):
            if i == 0 or i == size + 1:
                window.blit(ray_square_img, (39 + i*61, 108 + j*58))
            else:
                window.blit(square_img, (39 + i*61, 108 + j*58))


def draw_interface(difficulty_level):
    #Si le mode de diffidulté est facile
    if difficulty_level == "EASY":
        #On dessine les lignes de la grille
        draw_lines(4)
    elif difficulty_level == "NORMAL":
        draw_lines(6)
    elif difficulty_level == "HARD":
        draw_lines(8)  


def place_atom(size, click_x, click_y, nbSphere):
    #Recupère la liste des centers et la liste des coordonnées possibles d'un atome
    coords_list = init_coords_grid(size)
    centers_grid = init_centers_grid(size)

    #Détermine les coordonnées où placer l'atome
    atom_coord = coords_list[nearest_center(centers_grid, click_x, click_y)]
    atom = Atom(atom_coord[0], atom_coord[1])
    #Vérifie si l'atome n'existe pas, si oui le supprimer
    if atom_coord in atoms_coords:
        remove_atom(atom)
        nbSphere -= 1
    elif nbSphere < nbDifficulte:
        atoms.add(atom)
        atoms.draw(window)
        #Ajoute les coordonnées de l'atome à une liste
        atoms_coords.append(atom_coord)
        nbSphere += 1

    return nbSphere


def remove_atom(atom):
    #Calcul de la ligne et de la case correspondant à l'atome en fonction de ses coordonnées
    line = (atom.get_position()[1] - 115)/58
    square = (atom.get_position()[0] - 110)/61+1
    #On supprime l'atome du groupe d'atomes
    for atom_loop in atoms.sprites():
        if atom.get_position() == atom_loop.get_position():
            atoms.remove(atom_loop)
    #On supprime l'atome de la liste des coordonnées d'atome
    atoms_coords.remove(atom.get_position())
    #On met une case vide à la place
    window.blit(square_img, (39 + square*61, 108 + line*58))


def rand_atom(size):
    #On initialise la liste des centers
    centers_grid = init_centers_grid(size)
    #On prend au hasard l'un des centers de la liste précédente
    rand_coord = centers_grid[randint(0, len(centers_grid))]
    #Si l'atome n'est pas déjà placé, on le place, sinon on regénére.
    if rand_coord not in atoms_coords:
        place_atom(size, rand_coord[0], rand_coord[1], nbSphere)
    else:
        rand_atom(size)

def rand_atoms():
    for i in range(0, nbDifficulte):
        rand_atom(size)



#MAIN

draw_interface("NORMAL")
rand_atoms()
            
while True:
    for event in pygame.event.get():
        #Evenement on quitte le jeu
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] in range(100, 467) and event.pos[1] in range(108, 457):
                #Clic sur la grille pour placer ou retirer un atome
                nbSphere = place_atom(6, event.pos[0], event.pos[1], nbSphere)
            elif (event.pos[0] in range(100, 467) and (event.pos[1] in range(50, 109) or event.pos[1] in range(457, 515))) or (event.pos[1] in range(110, 457) and (event.pos[0] in range(39, 101) or event.pos[0] in range(466, 528))):
                centers_list = init_centers_launchzone(6)
                square = nearest_center(centers_list, event.pos[0], event.pos[1])
                side = (trunc(square/24*4)) + 1
                if side == 1:
                    print("Tu as appuyé sur le côté du haut")
                    print("Case : " + str(square % 6 + 1))
                elif side == 2:
                    print("Tu as appuyé sur le côté de gauche")
                    print("Case : " + str(square % 6 + 1))
                elif side == 3:
                    print("Tu as appuyé sur le côté du bas")
                    print("Case : " + str(square % 6 + 2))
                else:
                    print("Tu as appuyé sur le côté de droite")
                    print("Case : " + str(square % 6 + 1))

        #Evenement clic central souris boutons
        elif event.type == MOUSEBUTTONDOWN and event.button == 2:
                if event.pos[0] in range(0, 800) and event.pos[1] in range(0, 800):
                        print(event.pos[0], event.pos[1])


    pygame.display.update()
