## Marin Dorange Launey
## numéro étudiants: 21601861
from utilitaire import *
from test import *
from Point import *
def H(x,y,plateau,liste):
    """
        fonction permetant de déplacer les pions dans la grille vers le haut.
        
        :param x: coordonnée x dans la grille.
        
        :param y: coordonnée y dans la grille.
        
        :param plateau:  La liste 2D representant la grille / le plateau du jeu d’akiba.

        :param liste: Une liste 1D representant l'axe des y.

        :type liste: liste.

        :type x: entier compris entre 0 et 6.
        
        :type y: entier compris entre 0 et 6.
        
        :type plateau: liste.

        :return: La liste 2D representant la grille / le plateau du jeu d’akiba.
        
        :rtype: liste.
    """
    #attend position dans la liste et non dans tkinter
    for i in range(y,0,-1):
        if liste[i]=='V':
            break
        else:
            plateau[x][i-1]=liste[i]
    plateau[x][y]='V'

    return plateau
def B(x,y,plateau,liste):
    """
        fonction permetant de déplacer les pions dans la grille vers le bas.
        
        :param x: coordonnée x dans la grille.
        
        :param y: coordonnée y dans la grille.
        
        :param plateau:  La liste 2D representant la grille / le plateau du jeu d’akiba.

        :param liste: Une liste 1D representant l'axe des y.

        :type liste: liste.

        :type x: entier compris entre 0 et 6.
        
        :type y: entier compris entre 0 et 6.
        
        :type plateau: liste.

        :return: La liste 2D representant la grille / le plateau du jeu d’akiba.
        
        :rtype: liste.
        
    """
    for i in range(y,len(plateau[x])-1):
        if liste[i]=='V':
            break
        else:
            plateau[x][i+1]=liste[i]
    plateau[x][y]='V'
    return plateau
def G(x,y,plateau,liste):
    """
        fonction permetant de déplacer les pions dans la grille vers la gauche.
        
        :param x: coordonnée x dans la grille.
        
        :param y: coordonnée y dans la grille.
        
        :param plateau:  La liste 2D representant la grille / le plateau du jeu d’akiba.

        :param liste: Une liste 1D representant l'axe des x.

        :type liste: liste.

        :type x: entier compris entre 0 et 6.
        
        :type y: entier compris entre 0 et 6.
        
        :type plateau: liste.

        :return: La liste 2D representant la grille / le plateau du jeu d’akiba.
        
        :rtype: liste.
        
    """
    for i in range(x,0,-1):
        if liste[i]=='V':
            break
        else:
            plateau[i-1][y]=liste[i]
    plateau[x][y]='V'
    return plateau
def D(x,y,plateau,liste):
    """
        fonction permetant de déplacer les pions dans la grille vers la droite.
        
        :param x: coordonnée x dans la grille.
        
        :param y: coordonnée y dans la grille.
        
        :param plateau:  La liste 2D representant la grille / le plateau du jeu d’akiba.

        :param liste: Une liste 1D representant l'axe des x.

        :type liste: liste.

        :type x: entier compris entre 0 et 6.
        
        :type y: entier compris entre 0 et 6.
        
        :type plateau: liste.

        :return: La liste 2D representant la grille / le plateau du jeu d’akiba.
        
        :rtype: liste.
    """

    for i in range(x,len(plateau[x])-1):
        if liste[i]=='V':
            break
        else:
            plateau[i+1][y]=liste[i]
    plateau[x][y]='V'
    return plateau

def traitement_coordonne(pos,coul,plateau,point,antecedent,ia,Nom_Joueur):
    """
            Fonction qui traite les coordonnées et donc définie si le joueur a voulue faire un mouvement vers le bas,le haut,la droite ou la gauche.Il fait dans le même temps appele 
            à la fonction coresspondant au mouvement.Enfin il re-initialise le dictionnaire pos.

            :param coul: contient la couleur du pion qui doit jouer.

            :param plateau: La liste 2D representant la grille / le plateau du jeu d’akiba.

            :param point: regroupe les score des joueur.

            :param antecedent: contient la position, le mouvement ainsi que la liste du joueur qui à jouer juste avant.

            :type coul: chaine de caractére

            :type plateau: liste

            :type point: dictionnaire

            :type antecedent: dictionnaire
            
            :param pos: Variable globale qui contient les position de deux clic gauche.
            
            :type pos: dictionnaire.

            :param ia: Permet de savoir si il y'a deux joueur ou un joueur et l'ia.

            :type ia: Booléen.
            
            :param Nom_Joueur: Variables contenant le nom du ou des joueur(s).
            
            :type Nom_Joueur: liste.

            :return: un tuples contenant les variables plateau,coul,antecedent,point pour les "remmetre" dans les variables globales.

            :rtype: tuples
    """

    if pos['x1']<pos['x2']:
        liste=copie(pos['y1'],plateau)
        if test_deplacement(pos['x1'],pos['y1'],plateau,coul,'D',ia) and anti_deplacement_contraire('t',pos['x1'],pos['y1'],liste,antecedent,'D'):
            point=test_Pions_Pousser(liste,pos['x1'],pos['y1'],point,coul,'D',Nom_Joueur)	
            plateau=D(pos['x1'],pos['y1'],plateau,liste)
            antecedent=anti_deplacement_contraire('w',pos['x1'],pos['y1'],liste,antecedent,'D')
            coul=contraire_Couleur(coul)
            return (plateau,coul,antecedent,point)
        else:return False       
    elif pos['x1']>pos['x2']:
        liste=copie(pos['y1'],plateau)
        if test_deplacement(pos['x1'],pos['y1'],plateau,coul,'G',ia) and anti_deplacement_contraire('t',pos['x1'],pos['y1'],liste,antecedent,'G'):
            point=test_Pions_Pousser(liste,pos['x1'],pos['y1'],point,coul,'G',Nom_Joueur)	
            plateau=G(pos['x1'],pos['y1'],plateau,liste)
            antecedent=anti_deplacement_contraire('w',pos['x1'],pos['y1'],liste,antecedent,'G')
            coul=contraire_Couleur(coul)
            return (plateau,coul,antecedent,point)
        else:return False
    elif pos['y1']<pos['y2']:
        liste=plateau[pos['x1']][:]
        if test_deplacement(pos['x1'],pos['y1'],plateau,coul,'B',ia) and anti_deplacement_contraire('t',pos['x1'],pos['y1'],liste,antecedent,'B'):
            point=test_Pions_Pousser(liste,pos['x1'],pos['y1'],point,coul,'B',Nom_Joueur)		
            plateau=B(pos['x1'],pos['y1'],plateau,liste)
            antecedent=anti_deplacement_contraire('w',pos['x1'],pos['y1'],liste,antecedent,'B')
            coul=contraire_Couleur(coul)
            return (plateau,coul,antecedent,point)
        else:return False
    elif pos['y1']>pos['y2']:
        liste=plateau[pos['x1']][:]
        if test_deplacement(pos['x1'],pos['y1'],plateau,coul,'H',ia) and anti_deplacement_contraire('t',pos['x1'],pos['y1'],liste,antecedent,'H'):
            point=test_Pions_Pousser(liste,pos['x1'],pos['y1'],point,coul,'H',Nom_Joueur)
            plateau=H(pos['x1'],pos['y1'],plateau,liste)
            antecedent=anti_deplacement_contraire('w',pos['x1'],pos['y1'],liste,antecedent,'H')
            coul=contraire_Couleur(coul)
            return (plateau,coul,antecedent,point)
        else:return False

if __name__ == '__main__':
	from akiba import *
