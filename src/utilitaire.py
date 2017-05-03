## Marin Dorange Launey
## numéro étudiants: 21601861
def copie(y,plateau):
    """
		fonction qui copie le terme en position y de chaque liste contenue 
		dans la variable plateau.
		
		:param y: position du terme que l'on veut récuperer.
		
		:param plateau: La liste representant la grille / le plateau du jeu d’akiba.
		
		:type y: entier compris entre 0 et 6.
		
		:type plateau: liste.
		
		:return: la liste des termes en position y des sous-liste de la liste plateau.
		
		:rtype: liste.
    """
    liste=[]
    for i in plateau:
        liste.append(i[y])
    return liste
def contraire_Couleur(coul):
	"""
		fonction qui permet de passer la couleur du pion qui joue à la couleur du pion 
		adverse. Par exemple si coul=='N' coul vaudra aprés la fonction 'B'.De plus elle 
		change la couleur du pion qui indique qui doit jouer.
		
		:param coul: contient la couleur du pion qui doit jouer.
		
		:type coul: chaine de caractére.
		
        :return: La couleur contraire à celle donnée en paramétre

        :rtype: chaine de caractére
		
	"""
	if coul=='B':return 'N'
	else:return 'B'

def CreaPlateau():
    """
            Fonction créant une grille de 7 liste de 7 éléments.
           
            :return: la grille contenant 7 liste qui contiennent des 0.
            
            :rtype: liste.
    """
    plateau=[0]*7
    for i in range(7):
        plateau[i]= [0]*7
    return plateau

def pos_pion(plateau,canvas):
    """
        fonction qui créer les pions (objets oval tkinter) qui grace au plateau indique la couleur et la position
        du pions à tracer.De plus via la fonction crea_grille_fenetre() on affiche la grille dans la fenetre.
        
        :param plateau: Représente la grille via une liste de liste.
        
        :type plateau: liste.
        
        :param canvas: Variable contenant l'addresse de l'objet canvas.

		:type canvas: Tkinter Object.
    """
    canvas.delete('all')
    crea_grille_fenetre(canvas)
    x,y=25,25
    for i in plateau:
        for j in i:
            if j=='R':
                canvas.create_oval(x+5,y+5,x+45,y+45,fill='red')
            elif j=='B':
                canvas.create_oval(x+5,y+5,x+45,y+45,fill='white')

            elif j=='N':
                canvas.create_oval(x+5,y+5,x+45,y+45,fill='black')
            y+=50
        x+=50
        y=25

def crea_grille_fenetre(canvas):
    """
            crea_grille_fenetre créé grace au canvas de tkinter une grille permetant
            d'afficher à l'ecran les pions.

            :param canvas: Variable contenant l'addresse de l'objet canvas.

            :type canvas: Tkinter Object.
    """
    for i in range(25,376,50):
        canvas.create_line(i,25,i,375,fill='black')
        canvas.create_line(25,i,375,i,fill='black')

def Grille_Initialle(plateau):
    """
            Fonction initialisant la grille (qui represente le plateau) de départ 
            avec 'N' pour figurer les boules noir, 'B' pour figurer les boules blanche,
            'R' pour figurer les boules rouges et 'V' pour figurer les emplacements vides.
            
            :param plateau: liste de 7 liste qui contienent 7 element.
            
            :type plateau: liste.
            
            :return: La liste 2D representant la  grille / le plateau de départ du jeu d'akiba.
            
            :rtype: liste.
    """
    for i in range(7):
        for j in range(7):
            if (i<2 and j<2) or (i>4 and j>4):
                plateau[i][j]='N'
            elif (i>4 and j<2) or (i<2 and j>4):
                plateau[i][j]='B'
            elif ((i==1 or i==5) and j==3) or ((i==2 or i==4) and (j>1 and j<5)) or (i==3 and (j>0 and j<6)):
                plateau[i][j]='R'
            else:
                plateau[i][j]='V'
    return plateau

def About():
    """
        fonction affichant des information sur le programme.
    """
    from tkinter import Toplevel,Label
    fenAbout=Toplevel
    Label(fenAbout,text="Ce jeu à était réalisé par Mr Dorange Launey Marin dans le cadre du projet de methodolgie année 2016/2017").pack()
def showRugle():
    """
        Affiche le manuel d'utilisation du jeu.
    """
    import os
    try:
        os.startfile("..\manuel\manuel_utilisation_akiba.pdf")  # tentative d'ouvrir le fichier pdf marche pour windows
    except:
        try:
            os.system('evince ..\manuel\manuel_utilisation_akiba.pdf') # tentative d'ouvrir le fichier pdf marche pour linux
        except:
            try:
                os.startfile('..\manuel\manuel_utilisation_akiba.pdf')  # tentative d'ouvrir le fichier pdf normalement marche pour mac mais pas testé
            except:
                from tkinter import messagebox
                messagebox.showerror("imppossible d'ouvrir le manuel.\n le manuel se trouve dans le dossier manuel sous le nom 'manuel_utilisation_akiba.pdf'")
            
    
def quitter(fen):
    """
        fonction permettant de quitter complétemment les jeu.
        
        :param fen: Fenetre principale tkinter.
        
        :type fen: Tkinter Object.
    """
    fen.quit()
    fen.destroy()

if __name__ == '__main__':
	from akiba import *
