# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres:
    résultat:
    '''
    matrice = []
    for i in range(nbLignes):
        matrice.append([valeurParDefaut]*nbColonnes)
    return {'lig':nbLignes, 'col':nbColonnes, 'val':matrice}

assert Matrice(3,3,0) == {'lig':3 ,'col':3 ,'val':[[0,0,0],[0,0,0],[0,0,0]]}

def getNbLignes(matrice): 
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre:
    resultat:
    '''
    return matrice['lig']

assert getNbLignes({'lig':3 ,'col':3 ,'val':[[0,0,0],[0,0,0],[0,0,0]]}) == 3

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre:
    resultat:    
    '''
    return matrice['col']

assert getNbColonnes({'lig':3 ,'col':3 ,'val':[[0,0,0],[0,0,0],[0,0,0]]}) == 3

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres:
    resultat:        
    '''
    return matrice['val'][lig][col]

assert getVal({'lig':3 ,'col':3 ,'val':[[0,1,2],[3,4,5],[6,7,8]]}, 1, 0) == 3
assert getVal({'lig':3 ,'col':3 ,'val':[[0,1,2],[3,4,5],[6,7,8]]}, 2, 2) == 8

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres:
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice['val'][lig][col] = val
    return matrice

assert setVal({'lig':3 ,'col':3 ,'val':[[0,1,2],[3,4,5],[6,7,8]]}, 1, 0, 5) == {'lig':3 ,'col':3 ,'val':[[0,1,2],[5,4,5],[6,7,8]]}
assert setVal({'lig':3 ,'col':3 ,'val':[[0,1,2],[3,4,5],[6,7,8]]}, 2, 2, 5) == {'lig':3 ,'col':3 ,'val':[[0,1,2],[3,4,5],[6,7,5]]}


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    pass

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    pass
def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    pass

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    pass

