## Marin Dorange Launey
## numéro étudiants: 21601861
from tkinter import Label,Toplevel,Button,Entry
def Enregistrer(point,Nom_Joueur):
    """
        Fonction qui enregistre si l'on à voulu a la fin de la partie le score des joueur.

        :param point: Variable contenant le nombre de boules rouges ou adverse de chacun des joueur.

        :param Nom_Joueur: Variables contenant le nom du ou des joueur.

        :type point: dictionnaire.

        :type Nom_Joueur: liste.
    """
    Fichier=open("Score.txt","a")
    Fichier.write(Nom_Joueur[0]+"/"+str(point[Nom_Joueur[0]+'R'])+"/"+str(point[Nom_Joueur[0]])+'/')
    Fichier.write(Nom_Joueur[1]+"/"+str(point[Nom_Joueur[1]+'R'])+"/"+str(point[Nom_Joueur[1]])+'/')
    Fichier.write('\n')
    Fichier.close()
    
def LitFichier():
    """
        Fonction qui lit le fichier Score.txt ou est enregitsrer tout les scores que l'on à voulu enregistrer.

        :return: Une variable contenant les ligne du fichier.

        :rtype: Liste
    """
    try:
        Fichier=open("Score.txt","r")
        Ligne=[]
        for i in Fichier:
            Ligne.append(i.split('/'))
        Fichier.close()
        return Ligne
    except:return []
def search_by_name(NomJoueur,ia):
    """
        Fonction recherchant dans une liste le nom d'un joueur.

        :param NomJoueur: Variable contenant le nom du joueur à rechercher.

        :param ia: Variable définissant si le deuxiéme joueur peut être l'ia ou non.

        :type NomJoueur: chaine de caractére.

        :type ia: Booléen.

        :return: Variable contenant les scores des joueur ou figurer le joueur rechercher.

        :rtype: liste.

    """
    if ia:                                          ##variable clé qui permet de définir si l'on veut que le joueur 2 ouisse être l'ia
        ListeLigne=LitFichier()
        ListePointJoueur=[]
        for i in ListeLigne:
            if i[0]==NomJoueur or i[3]==NomJoueur:  ## les indice 0 et 3 corresponde au nom des joueur telles que l'on a enregistrer ceux ci
                ListePointJoueur.append(i)
    else:
        ListeLigne=LitFichier()
        ListePointJoueur=[]
        for i in ListeLigne:
            if (i[0]==NomJoueur and i[3]!='IA') or i[3]==NomJoueur:
                ListePointJoueur.append(i)
    return ListePointJoueur
def recherche_score(ia):
    """
        Fonction permettant d'afficher une fenetre pour demander le nom du joueur pour recercher ses score dans le fichier Scores.txt

        :param ia: Variable définissant si le deuxiéme joueur peut être l'ia ou non.

        :type ia: Booléen.

    """
    fen2=Toplevel()
    Label(fen2,text='Entrez le nom du joueur à rechercher',font=('Comic sans ms',12,"bold italic")).pack()
    Nom=Entry(fen2,font=('Comic sans ms',12,"bold italic"))
    Nom.pack()
    Boutton=Button(fen2,text='validez',command=lambda :affiche_resultat(search_by_name(Nom.get(),ia),fen2),font=('Comic sans ms',8,"bold italic"))
    Boutton.pack()
def affiche_resultat(Liste_Score,fen2):
    """
        Fonction permetant d'afficher les scores d'un joueur d'aprés le fichier Score.txt

        :param Liste_Score: Variable contenant les scores des parties auquel le joueur recherché à participé.

        :param fen: Variables contenant l'addresse de la fenetre tkinter ouverte pour demander le nom du joueur.

        :type Liste_Score: liste

        :type fen: Tkinter Object.
    """
    fen2.quit()
    fen2.destroy()
    fen2=Toplevel()
    Label(fen2,text='Nom J1',font=('Comic sans ms',12,"bold italic underline")).grid(row=0,column=0,padx=10)
    Label(fen2,text='Nombre de boules rouges',font=('Comic sans ms',12,"bold italic underline")).grid(row=0,column=1,padx=10)
    Label(fen2,text='Nombre de boules adverse',font=('Comic sans ms',12,"bold italic underline")).grid(row=0,column=2,padx=10)
    Label(fen2,text='Nom J2',font=('Comic sans ms',12,"bold italic underline")).grid(row=0,column=3,padx=10)
    Label(fen2,text='Nombre de boules rouges',font=('Comic sans ms',12,"bold italic underline")).grid(row=0,column=4,padx=10)
    Label(fen2,text='Nombre de boules adverse',font=('Comic sans ms',12,"bold italic underline")).grid(row=0,column=5,padx=10)
    row=1
    column=0
    for i in Liste_Score:
        for j in i:
            Label(fen2,text=j,font=('Comic sans ms',12)).grid(row=row,column=column)
            column+=1 
        column=0
        row+=1
        
def reinitialise_fichier_score():
    """
        Fonction permettant d'effacer tout le contenu du fichier Score.txt, la ou se trouve les scores enregistrer.
    """
    Fichier=open('score.txt','w')
    Fichier.close()
