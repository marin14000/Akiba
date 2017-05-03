## Marin Dorange Launey
## numéro étudiants: 21601861
def test_fin_partie(point,Nom_Joueur):
    """
        test fin partie est la fonction qui test si la partie est finie ou non.
        lorsque la partie est finie la fonction affiche un message via les fonction de messagebox et enléve le gestionnaire d'évènement
        du clic gauche.
        
        :param point: variable globale qui contient le nombre de boules rouges et adverse de chaque joueur.
        
        :type point: dictionnaire .
        
        :param Nom_Joueur: Variables contenant les noms des joueurs.
        
        :type Nom_Joueur: liste.

        :return: une variables contenant deux booléen permetant de dire si le joueur 1 ou 2 à gagné.

        :rtype: tuples.
        
    """
    if point[Nom_Joueur[0]+'R']==7 or point[Nom_Joueur[0]]==8:
        return (True,False)
    elif point[Nom_Joueur[1]+'R']==7 or point[Nom_Joueur[1]]==8:
        return (False,True)
    return (False,False)


def test_Pions_Pousser(liste,x,y,point,coul,fct,Nom_Joueur):
    """
        fonction pour tester est comptabiliser le nombre de pions adverse ou rouge pousser en dehors du plateau de
        jeu.Il modifie aussi l'affichage pour montrer le score au joueur.

        :param liste: contient la les element constituer selon le mouvement réalise (si l'on travaile sur les x ou les y) des element y des sous-liste de plateau ou bien d'une sous-liste de plateau.
        
        :param x: coordonnée x dans la grille.
        
        :param y: coordonnée y dans la grille.
        
        :param point: regroupe les score des joueur.

        :param coul: permet d'indiquer la couleur de la boule qui doit jouer.

        :param fct: permet d'indiquer la direction dans la quelle le joueur veut aller.
        
        :param Nom_Joueur: Variable contenant les noms des joueurs.
        
        :type Nom_Joueur: liste

        :type fct: chaine de caractére.

        :type coul: chaine de caractére.        
        
        :type liste: liste.
        
        :type x: entier compris entre 0 et 6.
        
        :type y: entier compris entre 0 et 6.
        
        :type point: dictionnaire.

        :return: les score des joueur.

        :rtype: dictionnaire
    """
    if fct=='B':
        for i in range(y,7):
            if liste[i]=='V':
                return point
        if liste[6]=='R':
            if coul=='B':
                point[Nom_Joueur[1]+'R']+=1
            else:
                point[Nom_Joueur[0]+'R']+=1
        else:
            if coul=='B':
                point[Nom_Joueur[1]]+=1
            else:
                point[Nom_Joueur[0]]+=1
            
    if fct=='H':
        for i in range(y,-1,-1):
            if liste[i]=='V':
                return point
        if liste[0]=='R':
            if coul=='B':
                point[Nom_Joueur[1]+'R']+=1
            else:
                point[Nom_Joueur[0]+'R']+=1
        else:
            if coul=='B':
                point[Nom_Joueur[1]]+=1
            else:
                point[Nom_Joueur[0]]+=1

    if fct=='D':
        for i in range(x,7):
            if liste[i]=='V':
                return point
        if liste[6]=='R':
            if coul=='B':
                point[Nom_Joueur[1]+'R']+=1
            else:
                point[Nom_Joueur[0]+'R']+=1
        else:
            if coul=='B':
                point[Nom_Joueur[1]]+=1
            else:
                point[Nom_Joueur[0]]+=1

    if fct=='G':
        for i in range(x,-1,-1):
            if liste[i]=='V':
                return point
        if liste[0]=='R':
            if coul=='B':
                point[Nom_Joueur[1]+'R']+=1
            else:
                point[Nom_Joueur[0]+'R']+=1
            
        else:
            if coul=='B':
                point[Nom_Joueur[1]]+=1
            else:
                point[Nom_Joueur[0]]+=1
           

    
    return point
  
if __name__ == '__main__':
	from akiba import *
