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
nbDifficulte = 0


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

def init_centres_list(size):
    #Initialise une liste de tous les centres des cases du jeu
    centres_list = list()
    for i in range(size):
        for j in range(size):
            #centre = position de l'atome
            centres_list.append((130 + j*61, 137 + i*58))
    return centres_list


def init_coords_list(size):
    #Initialise une liste de toutes les positions possibles des atomes dans le jeu
    coords_list = list()
    for i in range(size):
        for j in range(size):
            #centre = position de l'atome
            coords_list.append((110 + j*61, 115 + i*58))
    return coords_list


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


def draw_interface(difficulty_level, nbDifficulte):
    #Si le mode de diffidulté est facile
    if difficulty_level == "EASY":
        #On dessine les lignes de la grille
        draw_lines(4)
        nbDifficulte = 1

    elif difficulty_level == "NORMAL":
        draw_lines(6)
        nbDifficulte = 2

    elif difficulty_level == "HARD":
        draw_lines(8)
        nbDifficulte = 3

    return nbDifficulte 


def place_atom(size, click_x, click_y, nbSphere):
    #Recupère la liste des centres et la liste des coordonnées possibles d'un atome
    coords_list = init_coords_list(size)
    centres_list = init_centres_list(size)

    distances_list = list()
    #Calcule la distance euclidienne entre chaque centre et la position du clic
    for centre in centres_list:
        distances_list.append(sqrt((centre[0] - click_x)**2 + (centre[1] - click_y)**2))

    #Détermine les coordonnées où placer l'atome grâce à la distance minimale
    atom_coord = coords_list[distances_list.index(min(distances_list))]
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


def rand_atom(size, nbDifficulte):
    #On initialise la liste des centres
    centres_list = init_centres_list(size)
    for i in range(0, nbDifficulte):
        #On prend au hasard l'un des centres de la liste précédente
        rand_coord = centres_list[randint(0, len(centres_list))]
        #Si l'atome n'est pas déjà placé, on le place, sinon on regénére.
        if rand_coord not in atoms_coords:
            place_atom(size, rand_coord[0], rand_coord[1], nbSphere)
        else:
            rand_atom(size, nbDifficulte)


#variables 
nbSphere = 0

nbDifficulte = draw_interface("NORMAL", nbDifficulte)
rand_atom(6, nbDifficulte)

#MAIN 
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

        
        #Evenement clic central souris boutons
        elif event.type == MOUSEBUTTONDOWN and event.button == 2:
                if event.pos[0] in range(0, 800) and event.pos[1] in range(0,800):
                        print(event.pos[0], event.pos[1])

    pygame.display.update()


