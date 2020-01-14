# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes = ['╬', '╦', '╣', '╗', '╩', '═', '╝',
               'Ø', '╠', '╔', '║', 'Ø', '╚', 'Ø', 'Ø', 'Ø']


def Carte(nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    return {"Nord": nord, "Est": est, "Sud": sud, "Ouest": ouest, "Tresor": tresor, "Pions": pions}


assert Carte(False, False, True, False, 20, [1, 2, 3, 4]) == {"Nord": False, "Est": False, "Sud": True, "Ouest": False, "Tresor": 20, "Pions": [1, 2, 3, 4]}


def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    test = [c['Nord'], c['Est'], c['Sud'], c['Ouest']]
    compteur = 0
    for position in test:
        if position:
            compteur += 1
    if compteur >= 0 and 2 >= compteur:
        return True
    else:
        return False


assert estValide(Carte(True, False, False, False, 20, [1, 2, 3, 4])) == True
assert estValide(Carte(False, False, False, False, 20, [1, 2, 3, 4])) == True
assert estValide(Carte(True, False, False, True, 20, [1, 2, 3, 4])) == True
assert estValide(Carte(True, True, False, True, 20, [1, 2, 3, 4])) == False


def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['Nord']


assert murNord(Carte(True, False, False, False, 20, [1, 2, 3, 4])) == True


def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c['Sud']


assert murSud(Carte(False, False, True, False, 20, [1, 2, 3, 4])) == True


def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['Est']


assert murEst(Carte(False, True, False, False, 20, [1, 2, 3, 4])) == True


def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c['Ouest']


assert murOuest(Carte(False, False, False, True, 20, [1, 2, 3, 4])) == True


def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['Pions']


def setListePions(c, listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['Pions'] = listePions


def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return (len(c['Pions']))


assert getNbPions(Carte(False, False, False, True, 20, [1, 2, 3, 4])) == 4


def possedePion(c, pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c['Pions']


assert possedePion(Carte(False, False, False, True,
                         20, [1, 2, 3, 4]), 4) == True
assert possedePion(Carte(False, False, False, True, 20, [1, 2, 3]), 4) == False
assert possedePion(Carte(False, False, False, True, 20, []), 1) == False


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['Tresor'] if c['Tresor'] >= 0 else 0


assert getTresor(Carte(False, False, False, True, 20, [1, 2, 3, 4])) == 20
assert getTresor(Carte(False, False, False, True, -2, [1, 2, 3, 4])) == 0


def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res = c['Tresor']
    c['Tresor'] = 0
    return res


assert prendreTresor(Carte(False, False, False, True, 20, [1, 2, 3, 4])) == 20
assert prendreTresor(Carte(False, False, False, True, 15, [1, 2, 3, 4])) == 15


def mettreTresor(c, tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res = c['Tresor']
    c['Tresor'] = tresor
    return res


assert mettreTresor(Carte(False, False, False, True,
                          20, [1, 2, 3, 4]), 15) == 20


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    listePions = c['Pions']
    if pion in listePions:
        listePions.remove(pion)
    # print(c['Pions'])

#print(prendrePion(Carte(False, False, False, True, 20, [1, 2, 3, 4]), 4))


def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    listePions = c['Pions']
    if pion not in listePions:
        listePions.append(pion)
    # print(c['Pions'])

#print(poserPion(Carte(False, False, False, True, 20, [1, 2, 3]), 4))


def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    save = c['Nord']
    c['Nord'] = c['Est']
    c['Est'] = c['Sud']
    c['Sud'] = c['Ouest']
    c['Ouest'] = save
    #print(c)

#print(tournerAntiHoraire(Carte(False, False, False, True, 20, [1, 2, 3, 4])))


def tournerHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    save = c['Nord']
    c['Nord'] = c['Ouest']
    c['Ouest'] = c['Sud']
    c['Sud'] = c['Est']
    c['Est'] = save
    #print(c)

#print(tournerHoraire(Carte(False, False, False, True, 20, [1, 2, 3, 4])))


def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    for i in range(0, random.randint(0, 16), 1):
        save = c['Nord']
        c['Nord'] = c['Est']
        c['Est'] = c['Sud']
        c['Sud'] = c['Ouest']
        c['Ouest'] = save
    # print(c)

#print(tourneAleatoire(Carte(False, False, False, True, 20, [1, 2, 3, 4])))


def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res = ""
    for direction in [c['Ouest'], c['Sud'], c['Est'], c['Nord']]:
        if direction:
            res += '1'
        else:
            res += '0'
    binaire = res
    res = 0
    for chiffre in binaire:
        res = res*2 + int(chiffre)
    return res


assert coderMurs(Carte(False, False, False, False, 20, [1, 2, 3, 4])) == 0
assert coderMurs(Carte(False, False, False, True, 20, [1, 2, 3, 4])) == 8
assert coderMurs(Carte(True, False, False, False, 20, [1, 2, 3, 4])) == 1
assert coderMurs(Carte(True, False, False, True, 20, [1, 2, 3, 4])) == 9
assert coderMurs(Carte(True, True, False, False, 20, [1, 2, 3, 4])) == 3


def decoderMurs(c, code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    if code == 0:
        c['Nord'] = False
        c['Est'] = False
        c['Sud'] = False
        c['Ouest'] = False
    else:
        binaire = ""
        while code > 0:
            binaire = str(code % 2) + binaire  
            code = code//2
        i = 0
        while len(binaire) < 4:
            binaire = '0' + binaire
        for direction in ['Ouest', 'Sud', 'Est', 'Nord']:
            if binaire[i] == '1':
                c[direction] = True
            else:
                c[direction] = False
            i += 1
        #print(c)


#print(decoderMurs(Carte(True, False, False, True, 20, [1, 2, 3, 4]), 0))


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    res = coderMurs(c)
    return listeCartes[res]


assert toChar(Carte(True, True, False, False, 20, [1, 2, 3, 4])) == "╗"
assert toChar(Carte(True, False, True, False, 20, [1, 2, 3, 4])) == "═"


def passageNord(carte1, carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return (carte1['Nord'] == False and carte2['Sud'] == False)


assert passageNord(Carte(False, True, False, False, 20, [1, 2, 3, 4]), Carte(True, True, False, False, 20, [1, 2, 3, 4])) == True
assert passageNord(Carte(True, True, False, False, 20, [1, 2, 3, 4]), Carte(True, True, False, False, 20, [1, 2, 3, 4])) == False


def passageSud(carte1, carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return (carte1['Sud'] == False and carte2['Nord'] == False)


assert passageNord(Carte(False, True, False, False, 20, [1, 2, 3, 4]), Carte(True, True, False, False, 20, [1, 2, 3, 4])) == True
assert passageNord(Carte(True, False, True, False, 20, [1, 2, 3, 4]), Carte(True, True, False, False, 20, [1, 2, 3, 4])) == False


def passageOuest(carte1, carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return (carte1['Ouest'] == False and carte2['Est'] == False)


assert passageNord(Carte(False, True, False, False, 20, [1, 2, 3, 4]), Carte(True, False, False, False, 20, [1, 2, 3, 4])) == True
assert passageNord(Carte(True, True, False, True, 20, [1, 2, 3, 4]), Carte(True, True, False, False, 20, [1, 2, 3, 4])) == False


def passageEst(carte1, carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    return (carte1['Est'] == False and carte2['Ouest'] == False)


assert passageNord(Carte(False, False, True, False, 20, [1, 2, 3, 4]), Carte(True, True, False, False, 20, [1, 2, 3, 4])) == True
assert passageNord(Carte(True, True, False, False, 20, [1, 2, 3, 4]), Carte(True, True, False, True, 20, [1, 2, 3, 4])) == False
