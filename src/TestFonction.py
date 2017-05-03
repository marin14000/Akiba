## Marin Dorange Launey
## numéro étudiants: 21601861
from IA import *
from MVT import *
from Point import *
from score import *
from test import *
from utilitaire import *

plateau=[["N" ,"N", "V", "V" ,"V", "B", "B"],
         ["N", "N", "V" ,"R" ,"V" ,"B" ,"B"],
         ["V", "V" ,"R" ,"R", "R", "V" ,"V"],
         ["V","R","R","R","R","R","V"],
         ["V","V","R","R","R","V","V"],
         ["B","B","V","R","V","N","N"],
         ["B","B","V","V","V","N","N"]]

##
##
##
## /!\ Les explications des erreurs se trouvent dans le rapport /!\
## /!\ à la section "Erreur et test de fonction représentative du programme" /!\
##
## 
##

def test_anti_deplacement_contraire():
    antecedent=None
    mode=''

    antecedent=anti_deplacement_contraire('w', 0, 0, ["N","N","V","V","V","B","B"], antecedent, 'B')
    #utilisation normale renvoie un dictionnaire
    #on obtien le bon dictionnaire
    print(antecedent)
    
    antecedent=anti_deplacement_contraire(mode, 0, 0, ["N","N","V","V","V","B","B"], antecedent, 'B')
    #rien ne doit se passer
    #rien ne se passe
    print(antecedent)

    antecedent=anti_deplacement_contraire('w', 0, 2, ["V","V","N","N"], antecedent, 'B')
    #Ne doit pas affiche d'erreur même si plus tard le script rique de beuger
    #N'affiche aucune erreur 
    print(antecedent)

    antecedent=anti_deplacement_contraire('t', 0, 6, ["V","V","N","N","B","B"], antecedent, 'H')
    # un booléen permettant de jouer ou non
    # une erreur IndexError

    
def test_B():

    print(B(2, 6,plateau, ["B","B","V","V","V","N","N"]))
    #le plateau avec les pions decaler de un rang en partant des coordonné (2,6)
    #le plateau avec les pions decaler de un rang en partant des coordonné (2,6)
    
    print(B(2, 5,plateau, ["B","B","V","V","V","N","N"]))
    #le plateau avec les pions decaler de un rang en partant des coordonné (2,6)
    #le plateau à completement changé et est incohérent
def test_test_fin_partie():
    print(test_fin_partie({'':7,'R':0},['','']))
    #une erreur car les deux joueur on le même nom
    #un tuple (False,False)
    
    #print(test_fin_partie({'az':8,'R':0},['','az']))
    # une erreur car il manque deux valeurs dans le dico
    # erreur KeyError
    
    print(test_fin_partie({'a':8,'aR':0},['a','a']))
    #une erreur car les deux joueur on le même nom
    # un tuple (False,False)

def test_test_pions_pousser():
    print(test_Pions_Pousser(['V','V','V','V','N','N','B'], 4, 0, {'':7,'R':0}, 'N','D',['','']))
    print("var point= ",{'':7,'R':0})
    #une erreur car les deux joueur ont le même nom
    #le dictionnaire point {'':7,'R':0}
    
    print(test_Pions_Pousser(['V','V','V','V','n','n','b'], 4, 0, {'':7,'R':0}, 'N','D',['','']))
    print("var point= ",{'':7,'R':0})
    #un dictionnaire point {'':7,'R':0}
    #la valeur attendu est retourné
    
    print(test_Pions_Pousser(['V','V','V','V','N','N','B'], 4, 0, {'a':7,'aR':0}, 'N','D',['a','a']))
    print("var point= ",{'a':7,'aR':0})
    #une erreur car les deux joueur ont le même nom
    #le dictionnaire point {'':7,'R':0}
    
    print(test_Pions_Pousser(['V','V','V','V','N','N','v'], 4, 0, {'a':7,'aR':0}, 'N','D',['a','a']))
    print("var point= ",{'a':7,'aR':0})
    #un dictionnaire point {'a':7,'aR':0}
    #Une erreur se produit car le dernier symbole 'v' aurait du être codé 'V'




def test_traitement_coordone():
    antecedent=anti_deplacement_contraire('w', 0, 0, ["N","N","V","V","V","B","B"], None, 'B')#utilisation normale pour les besoins des test
    point={'a':7,'aR':0,'b':6,'bR':5}
    Nom_Joueur=['a','b']

    pos={'x1':0,'y1':0,'x2':0,'y2':0}
    print(traitement_coordonne(pos,'N',plateau,point,antecedent,False,Nom_Joueur))
    #Rien ne doit se passer car on clique sur le même pions
    #la valeur attendu est obtenu
    
##  pos={'x1':7,'y1':0,'x2':0,'y2':0}
##  print(traitement_coordonne(pos,'N',plateau,point,antecedent,False,Nom_Joueur))
    ##le plateau avec les pions decaler de un rang vers la gauche en partant des coordonné (7,0)
    #on obtient une erreur IndexError

def test_test_deplacement():
    plateau=[["N","N","V","V","V","B"],
             ["N","N","V","R","V","B"],
             ["V","R","R","R","V","V"],
             ["R","R","R","R","R","V"],
             ["V","R","R","R","V","V"],
             ["B","B","V","R","V","N"],]
    
    print(test_deplacement(0, 0, plateau,"N", "B",False))
    #Un booléen autorisant ou non le déplacement
    #la valeur attendu est obtenu
    print(test_deplacement(0, 5, plateau,"B", "B",False))
    #Un booléen autorisant ou non le déplacement
    #IndexError car plateau de 6*6 et non 7*7 et que l'on est à la fin du plateau
    
def test_compte_pions_coul():
    plateau=[["N","N","V","V","V","B"],
             ["N","N","V","R","V","B"],
             ["V","R","R","R","V","V"],
             ["R","R","R","R","R","V"],
             ["V","R","R","R","V","V"],
             ["B","B","V","R","V","N"],]
##  print(compte_pions_coul(0, 5, "B", plateau, "B"))
    #un booléen permetant de savoir si la derniere boule pousser est blanche ou non
    #On obtient l'erreur IndexError car plateau de 6*6 et non 7*7

    print(compte_pions_coul(0, 0, "B", plateau, "B"))
    #un booléen permetant de savoir si la derniere boule pousser est blanche ou non
    #Ici pas d'erreur car le rang 0 est defini
    




def test_search_by_name():
    print(search_by_name("marin", "True"))
    #Rien ne doit se passer car le deuxieme parametre n'est pas explicitement un bolléen
    #Une top level s'affiche avec les resultat de la recherche avec IA
    print(search_by_name("marin", ""))
    #Rien ne doit se passer car le deuxieme parametre n'est pas explicitement un bolléen
    #Une top level s'affiche avec les resultat de la recherche sans IA
    print(search_by_name('', True))
    #Une top level s'affiche avec les resultat de la recherche avec IA
    #les résultat attenduse produisent
    print(search_by_name("marin", True))
    #Une top level s'affiche avec les resultat de la recherche avec IA
    #Les resultat attendu se produisent

def test_Grille_Initialle():
    plateau=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#   print(Grille_Initialle(plateau))
    #le plateau initiale avec les "boules" codé "V" pour les espaces vide,"R" pour les boules rouge,"B" pour les boules blanche et "N" pour les boules noir
    #on obtient une erreur IndexError
    plateau=[[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

    print(Grille_Initialle(plateau))
    #le plateau initiale avec les "boules" codé normalement
    ##les valeurs souhaité sont obtenu
    plateau.append([0,0,0,0,0,0,0])
    print(Grille_Initialle(plateau))
    #le plateau initiale avec les "boules" codé normalement
    ##la dérniere ligne reste inchangé.
