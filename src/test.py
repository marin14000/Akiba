## Marin Dorange Launey
## numéro étudiants: 21601861
def anti_deplacement_contraire(mode,x,y,liste,antecedent,fct):
    """
            fonction qui empeche un mouvement contraire au deplacement précedent.
            En effet grace à cette fonction si joueur 1 joue un coups en haut et deplace
            les pions de joueur 2,joueur 2 n'a pas le droit d'effectuer aussitot un mouvement
            contraire à celui de joueur 1 (ici un coup en bas dans les même case verticales).
            cette fonction possedent deux "modes", w pour write ou on inscrits les mouvement
            ainsi que les position effectuer par le joueur, t pour test pour verifier si le
            joueur peut jouer le coup qu'il demande.
            
            :param mode: permet deux differencier le mode t du mode w.
            
            :param x: donne la position x du pions selon la grille.
            
            :param y: donne la position y du pions selon la grille.
            
            :param liste: contient la les element constituer selon le mouvement réalise (si l'on travaile sur les x ou les y) des element y des sous-liste de plateau ou bien d'une sous-liste de plateau.
            
            :param antecedent: contient la position, le mouvement ainsi que la liste du joueur qui à jouer juste avant.

            :param fct: parametre d'identifier la direction dans laquele on veut deplacer ses boules

            :type fct: chaine de caractére
            
            :type mode: chaine de caractére.
            
            :type x: entier entre 0 et 6.
            
            :type y: entier entre 0 et 6.
            
            :type liste: liste.
            
            :type antecedent: dictionnaire.

            :return: Un booléen permetant de dire si oui ou non le mouvement est autorisée.

            :rtype: Booléen.
            

    """
    if mode=='w':
        antecedent={'x':x,'y':y,'fct':fct,'newliste':liste}
        return antecedent  
    elif mode=='t':
        if antecedent is not None:
            if fct=='G':
                if antecedent['fct']=='D':
                    if y==antecedent['y']:
                        for i in range(antecedent['x']+1,x):
                            if antecedent['newliste'][i]=='V':
                                return True
                        return False
            if fct=='D':
                if antecedent['fct']=='G':
                    if y==antecedent['y']:
                        for i in range(x+1,antecedent['x']):                  
                            if antecedent['newliste'][i]=='V':
                                return True
                        return False

            if fct=='H':
                if antecedent['fct']=='B':
                    if x==antecedent['x']:
                        for i in range(antecedent['y']+1,y):
                            if antecedent['newliste'][i]=='V':
                                return True
                        return False           
            if fct=='B':
                if antecedent['fct']=='H':
                    if x==antecedent['x']:
                        for i in range(y+1,antecedent['y']):
                            if antecedent['newliste'][i]=='V':
                                return True
                        return False      
        return True

def compte_pions_coul(x,y,fct,plateau,coul):
    """
        Cette fonction regarde si le deplacement d'un pions n'entrenerait pas un de ses pions en dehors du plateau.
        Pour cela il parcours la grille est renvoie True si il trouve une case vide ou que la derniere boules n'est
        pas de sa couleurs sinon il renvoie False.

        :param x: Position x du pion selon la grille.
        
        :param y: Position y du pion selon la grille.
        
        :param fct: Donne la fonction ou autrement dit le mouvement que l'on veut réaliser.
        
        :param plateau: La liste representant la grille / le plateau du jeu d’akiba.
        
        :param coul: permet d'indiquer la couleur de la boule qui doit jouer.
        
        :type coul: chaine de carctére.
        
        :type x: Entier compris entre 0 et 6.
        
        :type y: Entier compris entre 0 et 6.
        
        :type fct: chaine de caractére.
        
        :type plateau: liste.

        :return: Un booléen permetant de dire si oui ou non le mouvement est autorisée

        :rtype: booléen
        

    """
    if fct=='B':
        for i in range(y,len(plateau[x])):
            try:
                if plateau[x][i+1]=='V':
                    return True
            except IndexError:
                if plateau[x][6]==coul:
                    return False
        return True

    if fct=='H':
        for i in range(y,-1,-1):
            if plateau[x][i]=='V':
                return True
            if plateau[x][0]==coul and i==0:
                return False

        return True
    if fct=='D':
        for i in range(x,len(plateau[x])):
            try:
                if plateau[i+1][y]=='V':
                    return True
            except IndexError:
                
                if plateau[6][y]==coul:return False
        return True

    if fct=='G':
        for i in range(x,-1,-1):
            if plateau[i][y]=='V':
                return True
            if plateau[0][y]==coul and i==0:
                return False
        return True             
def test_deplacement(x,y,plateau,coul,fct,ia):
    """
        fonction qui regroupe les test fait par la fonction "compte_pions_coul" et qui rajoute d'autre régles pour
        verifier que le pions que l'on joue soit celui du joueur, ainsi qu'il puisse mettre son doit derriére sa pierre
        sans toucher d'autre pierre.
        
        :param x: Position x du pion selon la grille.
        
        :param y: Position y du pion selon la grille.
        
        :param plateau: La liste representant la grille  le plateau du jeu d’akiba.

        :param coul: permet d'indiquer la couleur de la boule qui doit jouer.

        :param fct: permet d'indiquer la direction dans la quelle le joueur veut aller.

        :param ia: Permet de savoir si il y'a deux joueur ou un joueur et l'ia.

        :type ia: Booléen.

        :type fct: chaine de caractére.

        :type coul: chaine de caractére.
        
        :type x: Entier compris entre 0 et 6.
        
        :type y: Entier compris entre 0 et 6.
        
        :type plateau: liste.

        :return: Un booléen permetant de dire si oui ou non le mouvement est autorisée

        :rtype: Booléen

    """
    if ia==True and plateau[x][y]=='B' :
        return False
    else:
        if fct=='B':
            if (plateau[x][y-1] =='V' or y==0) and compte_pions_coul(x,y,fct,plateau,coul) and plateau[x][y]==coul:return True
            else:return False

        if fct=='H':
            if compte_pions_coul(x,y,fct,plateau,coul) and plateau[x][y]==coul:
                if y==6:return True
                elif plateau[x][y+1]=='V':return True
                else:return False
            else:return False
        if fct=='G':
            if compte_pions_coul(x,y,fct,plateau,coul) and plateau[x][y]==coul:
                try:
                    if plateau[x+1][y] =='V':
                        return True
                    else:
                        return False
                except IndexError:
                    if x==6:
                        return True
                    else:
                        return False
                return True
            else:
                return False
        if fct=='D':
            if compte_pions_coul(x,y,fct,plateau,coul) and plateau[x][y]==coul and (plateau[x-1][y] =='V' or x==0):
                return True
            else:        
                return False

if __name__ == '__main__':
	from akiba import *
