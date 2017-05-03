## Marin Dorange Launey
## numéro étudiants: 21601861
from random import choice
from MVT import *
def playIa(liste_coup_possible,plateau,point,coul,antecedent,Nom_Joueur):
    """
        cette Fonction fait jouer l'IA,c'est à dire qu'il choisi au hasard un coup à jouée parmi tout les coups possible, et, grace à la fonction traitement_coordonne joue ce coup.

        :param liste_coup_possible: Liste des coup possible de jouer pour l'IA.

        :param plateau: Liste 2D représentant la grill/plateau du jeu d'akiba

        :param point: Variable contenant les points/les boule de chaque joueur.

        :param coul: Variable représentant la couleur du/de la pion/boules qui doit jouer.
        
        :param antecedent: contient la position, le mouvement ainsi que la liste du joueur qui à jouer juste avant.
        
        :param Nom_Joueur: Variable contenant le nom des joueur.
        
        :type antecedent: dictionnaire.
        
        :type Nom_Joueur: liste.

        :type liste_coup_possible: liste.

        :type plateau: liste.

        :type point: dictionnaire.

        :type coul: chaine de caractére.

        :return: Variables contenant les variables citer plus haut changer.

        :rtype: tuples.

    """
    x=choice(liste_coup_possible)                       ##choix au hasard 
    if x[2]=='G':
        pos={'x1':x[0],'y1':x[1],'x2':x[0]-1,'y2':x[1]}
    elif x[2]=='D':
        pos={'x1':x[0],'y1':x[1],'x2':x[0]+1,'y2':x[1]}
    elif x[2]=='B':
        pos={'x1':x[0],'y1':x[1],'x2':x[0],'y2':x[1]+1}
    elif x[2]=='H':
        pos={'x1':x[0],'y1':x[1],'x2':x[0],'y2':x[1]-1}
    DATA=traitement_coordonne(pos,coul,plateau,point,antecedent,False,Nom_Joueur)
    return DATA

if __name__ == '__main__':
	from akiba import *
