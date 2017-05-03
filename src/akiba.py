## Marin Dorange Launey
## numéro étudiants: 21601861
from tkinter import *
from tkinter import messagebox  # normalement importer grace a "from tkinter import *
                                # mais pourtant l'importation ne ce fait pas et on est obligé de
                                 #rajouter cette ligne.
from math import floor
from random import randint
from test import *
from MVT import traitement_coordonne
from score import *
from IA import *
from utilitaire import *
##from utilitaire import copie
def jouerDeux():
    """
		Cette fonction permet de débuter une partie d'akiba à deux joueur.Elle change alors l'affichage sur le coté du plateau de jeu pour permettre d'afficher les scores,les noms des joueur et leur pion.
		De plus elle initialise l'évènement clique gauche.
		
    """
    global Nom_Joueur,point,coul,pion_courant,jL1,jL2,canvas_coul_pion
    Nom_Joueur=j1.get(),j2.get()
    point[Nom_Joueur[0]+'R']=0
    point[Nom_Joueur[1]+'R']=0
    point[Nom_Joueur[0]]=0
    point[Nom_Joueur[1]]=0
    j1.pack_forget()
    j2.pack_forget()
    jL1.pack_forget()
    jL2.pack_forget()
    jouer.entryconfig(1,state="disabled")
    jouer.entryconfig(2,state="disabled")
    jouer.entryconfig(4,state="normal")
    
    frameInfo=Frame(affichage)
    frameJ1=Frame(affichage)
    frameJ2=Frame(affichage)
    frameInfo.pack()
    frameJ1.pack(pady=20)
    frameJ2.pack()
    jL1=Label(frameJ1,text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[0]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[0]])+'\n Votre couleur de pions: ',font=("Comic sans ms",12))
    jL2=Label(frameJ2,text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[1]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[1]])+'\n Votre couleur de pions: ',font=("Comic sans ms",12))
    
    canvas_coul_pion=Canvas(frameInfo,width=50,height=50,bg='#B43104')
    
    if randint(0,1)==1:
        coul='N'
        pion_courant=canvas_coul_pion.create_oval(5,5,45,45,fill='black')
    else:
        pion_courant=canvas_coul_pion.create_oval(5,5,45,45,fill='white')
        coul='B'
        
    Label(frameInfo,text='Couleur du pion\n qui doit jouer: ',font=('Comic sans ms',16,"bold italic underline")).pack()
    canvas_coul_pion.pack()
    Label(frameJ1,text=Nom_Joueur[0],font=('Comic sans ms',16,"bold italic underline")).pack()
    jL1.pack()
    pions_j1=Canvas(frameJ1,width=50,height=50,bg='#B43104')
    pions_j1.create_oval(5,5,45,45,fill='black')
    pions_j1.pack()
    Label(frameJ2,text=Nom_Joueur[1],font=('Comic sans ms',16,"bold italic underline")).pack()
    jL2.pack()
    pions_j2=Canvas(frameJ2,width=50,height=50,bg='#B43104')
    pions_j2.create_oval(5,5,45,45,fill='white')
    pions_j2.pack()
    canvas.bind("<Button-1>",lambda event, ia=False:get_pos(event,ia))   

def get_pos(event,ia):
    """
            fonction appelé lors d'un clique gauche il récupere la position du premier clique gauche puis si les valeurs du premier clic gauches sont définis,définit les valeurs du deuxiéme clic gauche,lorqu'il 
            definit les valeurs get_pos les transforme en coordonnées dans le tableaux(càd il que pos contient des entiers compris entre 0 et 6) ensuite il fait appele à la fonction traitement_coordone().
            
            :param event: class tkinter permettant de recuperer les "event" par exemple les coordonées x,y d'un clic gauche.
            
            :type event: Tkinter Object.

            :param ia: Permet de savoir si il y'a deux joueur ou un joueur et l'ia.

            :type ia: Booléen.
            
            
    """
    global pos,coul,plateau,point,antecedent
    if pos['x1'] is None and pos['y1'] is None:
        pos['x1']=floor((event.x-25)/50)
        pos['y1']=floor((event.y-25)/50)
    else:
        pos['x2']=floor((event.x-25)/50)
        pos['y2']=floor((event.y-25)/50)
        DATA=traitement_coordonne(pos,coul,plateau,point,antecedent,ia,Nom_Joueur)
        
        if DATA==False:messagebox.showwarning('mauvais coup','Désolé ce coup est impossible,\nvous pouvez cliquez dans l'+"'"+'onglet menu sur afficher les regle si vous voulez.')
        else:
            if DATA is not None:
                plateau,coul,antecedent,point=DATA
                
                test=test_fin_partie(point,Nom_Joueur)
                if test[0]:
                    rec=messagebox.askquestion('Vous avez gangné','Bravo '+Nom_Joueur[0]+' tu à surpassé '+Nom_Joueur[1]+'\n Voulez vous enregistrer ce score ?')
                    canvas.unbind("<Button-1>")
                    try:
                        canvas.after_cancel(timer)
                    except:
                        pass
                    if rec:
                        Enregistrer(point,Nom_Joueur)
                elif not(ia)and test[1]:
                    rec=messagebox.askquestion('Vous avez gangné','Bravo '+Nom_Joueur[1]+' tu à surpassé '+Nom_Joueur[0]+'\n Voulez vous enregistrer ce score ?')        
                    canvas.unbind("<Button-1>")
                    if rec:Enregistrer(point,Nom_Joueur)
                if coul=='B':
                    canvas_coul_pion.itemconfigure(pion_courant,fill='white')
                else:
                    canvas_coul_pion.itemconfigure(pion_courant,fill='black')
                pos_pion(plateau,canvas)
                jL1.configure(text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[0]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[0]])+'\n Votre couleur de pions: ')
                jL2.configure(text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[1]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[1]])+'\n Votre couleur de pions: ')

        pos={'x1':None,'y1':None,'x2':None,'y2':None}
        
def Coup_Possible():
    """
        Cette fonction fait est appeler pour que l'IA puisse jouer,elle calcule tout les coups possible puis en tire
        un au hasard.
    """
    global plateau,coul,point,antecedent,timer
    if coul=='B':
        liste_Coup_Possible=[]
        for x in range(len(plateau)):
            for y in range(len(plateau)):
                for mvt in ('H','B','G','D'):
                    if mvt in ('G','D'):
                        liste=copie(y,plateau)
                    else:
                        liste=plateau[x][:]
                    if test_deplacement(x,y,plateau,'B',mvt,False) and anti_deplacement_contraire('t',x,y,liste,antecedent,mvt):
                          liste_Coup_Possible.append([x,y,mvt])
        if liste_Coup_Possible!=[]:
                plateau,coul,antecedent,point=playIa(liste_Coup_Possible,plateau,point,coul,antecedent,Nom_Joueur)        
                test=test_fin_partie(point,Nom_Joueur)
                if test[1]==True:
                    rec=messagebox.askquestion('Vous avez gagné','Bravo '+Nom_Joueur[1]+' tu à surpassé '+Nom_Joueur[0])        
                    canvas.unbind("<Button-1>")
                    canvas.after_cancel(timer)
                    if rec:
                        Enregistrer(point,Nom_Joueur)
                if coul=='B':
                    canvas_coul_pion.itemconfigure(pion_courant,fill='white')
                else:
                    canvas_coul_pion.itemconfigure(pion_courant,fill='black')
                pos_pion(plateau,canvas)
                jL1.configure(text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[0]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[0]])+'\n Votre couleur de pions: ')
                jL2.configure(text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[1]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[1]])+'\n Votre couleur de pions: ')

        pos={'x1':None,'y1':None,'x2':None,'y2':None}


            
    timer=canvas.after(3000,Coup_Possible)




def beginIa():
    """
        Cette fonction permet de débuter une partie en jouant seul avec une "IA".

    """
    global Nom_Joueur,point,coul,pion_courant,jL1,jL2,canvas_coul_pion
    Nom_Joueur=j1.get(),'IA'
    point[Nom_Joueur[0]+'R']=0
    point[Nom_Joueur[1]+'R']=0
    point[Nom_Joueur[0]]=0
    point[Nom_Joueur[1]]=0
    j1.pack_forget()
    j2.pack_forget()
    jL1.pack_forget()
    jL2.pack_forget()
    jouer.entryconfig(1,state="disabled")
    jouer.entryconfig(2,state="disabled")
    jouer.entryconfig(4,state="normal")
    
    frameInfo=Frame(affichage)
    frameJ1=Frame(affichage)
    frameJ2=Frame(affichage)
    frameInfo.pack()
    frameJ1.pack(pady=20)
    frameJ2.pack()
    jL1=Label(frameJ1,text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[0]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[0]])+'\n Votre couleur de pions: ',font=("Comic sans ms",12))
    jL2=Label(frameJ2,text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[1]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[1]])+'\n Votre couleur de pions: ',font=("Comic sans ms",12))
    
    canvas_coul_pion=Canvas(frameInfo,width=50,height=50,bg='#B43104')
    
    if randint(0,1)==1:
        coul='N'
        pion_courant=canvas_coul_pion.create_oval(5,5,45,45,fill='black')
    else:
        pion_courant=canvas_coul_pion.create_oval(5,5,45,45,fill='white')
        coul='B'
        
    Label(frameInfo,text='Couleur du pion\n qui doit jouer: ',font=('Comic sans ms',16,"bold italic underline")).pack()
    canvas_coul_pion.pack()
    Label(frameJ1,text=Nom_Joueur[0],font=('Comic sans ms',16,"bold italic underline")).pack()
    jL1.pack()
    pions_j1=Canvas(frameJ1,width=50,height=50,bg='#B43104')
    pions_j1.create_oval(5,5,45,45,fill='black')
    pions_j1.pack()
    Label(frameJ2,text=Nom_Joueur[1],font=('Comic sans ms',16,"bold italic underline")).pack()
    jL2.pack()
    pions_j2=Canvas(frameJ2,width=50,height=50,bg='#B43104')
    pions_j2.create_oval(5,5,45,45,fill='white')
    pions_j2.pack()
    canvas.bind("<Button-1>",lambda event, ia=True:get_pos(event,ia))
    Coup_Possible()


        

def recommencer():
    """
        fonction permettant de recommencer une partie à 0.
    """
    global plateau
    point[Nom_Joueur[0]+'R']=0
    point[Nom_Joueur[1]+'R']=0
    point[Nom_Joueur[0]]=0
    point[Nom_Joueur[1]]=0
    jL1.configure(text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[0]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[0]])+'\n Votre couleur de pions: ')
    jL2.configure(text='Nombre de boules rouges:\n'+str(point[Nom_Joueur[1]+'R'])+'\n Nombres de boules adverse:\n'+str(point[Nom_Joueur[1]])+'\n Votre couleur de pions: ')
    plateau=Grille_Initialle(CreaPlateau())
    pos_pion(plateau,canvas)

if __name__ == '__main__':
    point={}
    Nom_Joueur=['','']
    pos={'x1':None,'y1':None,'x2':None,'y2':None}
    antecedent=None
    fen= Tk()
    plateau=Grille_Initialle(CreaPlateau())
    mainmenu = Menu(fen)
    jouer = Menu(mainmenu)
    
    jouer.add_command(label="Jouer seul", command=beginIa)
    jouer.add_command(label="Jouer à deux", command=jouerDeux)
    jouer.add_separator()
    jouer.add_command(label="recommencer",command=recommencer)
    jouer.entryconfig(4,state="disabled")
    
    menuHelp = Menu(mainmenu)
    menuHelp.add_command(label="A propos", command=About) 
    menuHelp.add_command(label="Les régles",command=showRugle)

    plus=Menu(mainmenu)
    plus.add_command(label="rechercher un score par nom (partie avec ia)",command=lambda ia=True:recherche_score(ia))
    plus.add_command(label="rechercher un score par nom (partie sans ia)",command=lambda ia=False:recherche_score(ia))
    plus.add_command(label="Réinitialiser les scores (les effacer)",command=reinitialise_fichier_score)
    
    mainmenu.add_cascade(label = "Jouer !", menu=jouer) 
    mainmenu.add_cascade(label = "Aide", menu=menuHelp)
    mainmenu.add_cascade(label="plus",menu=plus)
    mainmenu.add_command(label="Quitter",command=lambda :quitter(fen))
      
    fen.config(menu = mainmenu)
    fen.title("Akiba's Games !!!")
    affichage=Frame(fen)


    jL1=Label(affichage,text='Entrez le nom de joueur 1',font=('Comic sans ms',12,"bold italic"))
    jL1.pack()
    j1=Entry(affichage,text='Joueur1',font=('Comic sans ms',12))
    j1.pack()
    jL2=Label(affichage,text='Entrez le nom de joueur 2\n (si vous jouez à deux)',font=('Comic sans ms',12,"bold italic"))
    jL2.pack()
    j2=Entry(affichage,text='joueur2',font=('Comic sans ms',12))
    j2.pack()
    affichage.pack(side=RIGHT)
    canvas=Canvas(fen,width=400,height=400,bg='#B43104')
    crea_grille_fenetre(canvas)
    pos_pion(plateau,canvas)
    canvas.pack(side=LEFT)
    fen.mainloop()
