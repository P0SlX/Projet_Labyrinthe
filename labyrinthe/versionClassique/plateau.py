# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    # C = Coins (spawn des joueurs)
    # F = Cartes fixes

    # C 0 F 0 F 0 C
    # 0 0 0 0 0 0 0
    # F 0 F 0 F 0 F
    # 0 0 0 0 0 0 0
    # F 0 F 0 F 0 F
    # 0 0 0 0 0 0 0
    # C 0 F 0 F 0 C

    MatricePlateau = Matrice(7, 7, 0)
    
    if nbJoueurs == 1: #COINS
        setVal(MatricePlateau, 0, 0, Carte(True, False, False, True, 0, [1]))
        setVal(MatricePlateau, 0, 6, Carte(True, True, False, False, 0, []))
        setVal(MatricePlateau, 6, 0, Carte(False, False, True, True, 0, []))
        setVal(MatricePlateau, 6, 6, Carte(False, True, False, True, 0, []))
    elif nbJoueurs == 2:
        setVal(MatricePlateau, 0, 0, Carte(True, False, False, True, 0, [1]))
        setVal(MatricePlateau, 0, 6, Carte(True, True, False, False, 0, [2]))
        setVal(MatricePlateau, 6, 0, Carte(False, False, True, True, 0, []))
        setVal(MatricePlateau, 6, 6, Carte(False, True, False, True, 0, []))
    elif nbJoueurs == 3:
        setVal(MatricePlateau, 0, 0, Carte(True, False, False, True, 0, [1]))
        setVal(MatricePlateau, 0, 6, Carte(True, True, False, False, 0, [2]))
        setVal(MatricePlateau, 6, 0, Carte(False, False, True, True, 0, [3]))
        setVal(MatricePlateau, 6, 6, Carte(False, True, False, True, 0, []))
    else:
        setVal(MatricePlateau, 0, 0, Carte(True, False, False, True, 0, [1]))
        setVal(MatricePlateau, 0, 6, Carte(True, True, False, False, 0, [2]))
        setVal(MatricePlateau, 6, 0, Carte(False, False, True, True, 0, [3]))
        setVal(MatricePlateau, 6, 6, Carte(False, True, False, True, 0, [4]))

    #FIXES
    setVal(MatricePlateau, 2, 0, Carte(True, False, False, False, 0, []))
    setVal(MatricePlateau, 4, 0, Carte(True, False, False, False, 0, []))
    setVal(MatricePlateau, 0, 2, Carte(False, False, False, True, 0, []))
    setVal(MatricePlateau, 2, 2, Carte(False, False, False, True, 0, []))
    setVal(MatricePlateau, 4, 2, Carte(True, False, False, False, 0, []))
    setVal(MatricePlateau, 6, 2, Carte(False, True, False, False, 0, []))
    setVal(MatricePlateau, 0, 4, Carte(False, False, False, True, 0, []))
    setVal(MatricePlateau, 2, 4, Carte(False, False, True, False, 0, []))
    setVal(MatricePlateau, 4, 4, Carte(False, True, False, False, 0, []))
    setVal(MatricePlateau, 6, 4, Carte(False, True, False, False, 0, []))
    setVal(MatricePlateau, 2, 6, Carte(False, False, True, False, 0, []))
    setVal(MatricePlateau, 4, 6, Carte(False, False, True, False, 0, []))

    #CARTES AMOVIBLES
    PositionRestantes = [
                (1, 0),         (3, 0),         (5, 0), 
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
                (1, 2),         (3, 2),         (5, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
                (1, 4),         (3, 4),         (5, 4),
        (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
                (1, 6),         (3, 6),         (5, 6),
    ]

    RandomInt = random.randint(0, 2)
    x = 16; y = 6; z = 12
    if RandomInt == 0:
        x -= 1
        CarteRestante = Carte(True, False, False, True, 0, [])
    elif RandomInt == 1:
        y -= 1
        CarteRestante = Carte(False, False, False, True, 0, [])
    else:
        z -= 1
        CarteRestante = Carte(False, True, False, True, 0, [])

    for i in range(x): #LES ANGLES DROITS
        position = random.choice(PositionRestantes)
        setVal(MatricePlateau, position[0], position[1], tourneAleatoire(Carte(True, False, False, True, 0, [])))
        PositionRestantes.remove(position)

    for i in range(y): #LES JOINTURES
        position = random.choice(PositionRestantes)
        setVal(MatricePlateau, position[0], position[1], tourneAleatoire(Carte(False, False, False, True, 0, [])))
        PositionRestantes.remove(position)

    for i in range(z): #LES TOUT-DROITS
        position = random.choice(PositionRestantes)
        setVal(MatricePlateau, position[0], position[1], tourneAleatoire(Carte(False, True, False, True, 0, [])))
        PositionRestantes.remove(position)

    return (MatricePlateau, CarteRestante)

print(Plateau(10, 10))


def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    pass

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    pass

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for l in range(getNbLignes(plateau)):
        for c in range(getNbLignes(plateau)):
            if getTresor(getVal(plateau, l, c)) == numTresor:
                return (l, c)
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for l in range(getNbLignes(plateau)):
        for c in range(getNbLignes(plateau)):
            if possedePion(getVal(plateau, l, c), numJoueur):
                return (l, c)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pass


def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pass


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    pass

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass
