# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs = ["joueur1", "joueurs2"], nbTresors = 24, nbTresorsMax = 0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    res = {}
    # joueurs entre 1 et 4 donc:
    if len(nomsJoueurs) <= 4:
        liste_joueurs = ListeJoueurs(nomsJoueurs)
        distribuerTresors(liste_joueurs, nbTresors, nbTresorsMax)
        initAleatoireJoueurCourant(liste_joueurs)
        res["Participants"] = liste_joueurs
        res["Plateau"] = Plateau(len(nomsJoueurs), nbTresors)
    else:
        return "nb de joueurs invalide, veuillez avoir entre 1 et 4 joueurs"
    res["Phase"] = 1
    res["directionNonPossible"] = [None, None]
    return res


def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe["Plateau"][0]


def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(labyrinthe['Participants']) 


def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return labyrinthe["Participants"][0]["Nom"]


def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return labyrinthe["Participants"][0]["numJoueur"]


def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """
    return labyrinthe["Phase"]


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    if labyrinthe["Phase"] == 1:
        labyrinthe["Phase"] += 1
    elif labyrinthe["Phase"]== 2:
        labyrinthe["Phase"] -= 1


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    cpt = 0
    for carte in labyrinthe["Plateau"][0][2]:
        if carte["Tresor"] != 0:
            cpt += 1
    return cpt


def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    ListeJoueurs = []
    for joueur in labyrinthe["Participants"]:
        ListeJoueurs.append(joueur)
    return ListeJoueurs


def enleverTresor(labyrinthe, lin, col, numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    prendreTresorPlateau(labyrinthe["Plateau"][0], lin, col, numTresor)


def prendreJoueurCourant(labyrinthe, lin, col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    prendrePionPlateau(labyrinthe["Plateau"][0], lin, col, labyrinthe["Participants"][0]["numJoueur"])



def poserJoueurCourant(labyrinthe, lin, col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    poserPionPlateau(labyrinthe["Plateau"][0], lin, col, labyrinthe["Participants"][0]["numJoueur"])


def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """
    return labyrinthe["Plateau"][1]


def coupInterdit(labyrinthe, direction, rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    rangeeAutorisee = [1,3,5]
    directionAutorisee = ['NSOE']
    if rangee not in rangeeAutorisee or direction not in directionAutorisee:
        return True
    else:
        return False 


def jouerCarte(labyrinthe, direction, rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """

    if direction in 'NSOE':
        # Dommage qu'il n'y ai pas de switch
        if direction == 'N':
            labyrinthe["Plateau"][1] = decalageColonneEnBas(labyrinthe["Plateau"][0], int(rangee), labyrinthe["Plateau"][1])
            labyrinthe["directionNonPossible"][0] = ('S', int(rangee))
        if direction == 'O':
            labyrinthe["Plateau"][1] = decalageLigneADroite(labyrinthe["Plateau"][0], int(rangee), labyrinthe["Plateau"][1])
            labyrinthe["directionNonPossible"][0] = ('E', int(rangee))
        if direction == 'S':
            labyrinthe["Plateau"][1] = decalageColonneEnHaut(labyrinthe["Plateau"][0], int(rangee), labyrinthe["Plateau"][1])
            labyrinthe["directionNonPossible"][0] = ('O', int(rangee))
        if direction == 'E':
            labyrinthe["Plateau"][1] = decalageLigneAGauche(labyrinthe["Plateau"][0], int(rangee), labyrinthe["Plateau"][1])
            labyrinthe["directionNonPossible"][0] = ('O', int(rangee))


def tournerCarte(labyrinthe, sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    if sens == 'H':
        tournerHoraire(labyrinthe["Plateau"][1])
    elif sens == 'A':
        tournerAntiHoraire(labyrinthe["Plateau"][1])


def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    numTresor = labyrinthe["Participants"][0]["Liste de trésor"][0]
    return numTresor


def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(labyrinthe["Plateau"][0], getTresorCourant(labyrinthe))


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(labyrinthe["Plateau"][0], getNumJoueurCourant(labyrinthe))


def executerActionPhase1(labyrinthe, action, rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action == 'T' or action == 't':
        tournerHoraire(labyrinthe["Plateau"][1])
        return 0
    if (action == 'N' or action == 'E' or  action == 'S' or action == 'O') and (rangee == '1' or rangee == '3' or rangee == '5'):
        jouerCarte(labyrinthe, action, rangee)
        changerPhase(labyrinthe)
        return 1
    elif int(action) > 0 and int(rangee) > 0:
        return 3
    else:
        return 4


def accessibleDistJoueurCourant(labyrinthe, ligA, colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    coordJ = getCoordonneesJoueurCourant(labyrinthe)
    if accessible(labyrinthe["Plateau"][0], coordJ[0], coordJ[1], ligA, colA) == True:
        return accessibleDist(labyrinthe["Plateau"][0], coordJ[0], coordJ[1], ligA, colA)
    else:
        return None


def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    joueurCourant = getJoueurCourant(labyrinthe["Participants"])
    coord = getCoordonneesTresorCourant(labyrinthe)
    coordJoueurCourant = getCoordonneesJoueurCourant(labyrinthe)
    if coord == coordJoueurCourant:
        if len(joueurCourant["Liste de trésor"]) == 1:
            return 2
        else:
            joueurCourant["Liste de trésor"].pop(0)
            changerJoueurCourant(labyrinthe["Participants"])
            changerPhase(labyrinthe)
            return 1
    else:
        changerJoueurCourant(labyrinthe["Participants"])
        changerPhase(labyrinthe)
        return 0
