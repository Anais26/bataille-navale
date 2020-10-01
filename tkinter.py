from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk

# CREATION FENETRE
fenetre = Tk()

# FENETRE ET SES PROPRIETES
fenetre.title("Bataille navale")
fenetre.geometry("1080x720")
fenetre.minsize(480, 400)
fenetre.config(background ='salmon')


# CORPS DE LA FENETRE
#barre de menu
def alert():
    showinfo("alerte", "Bravo!")
menubar = Menu(fenetre)
#onglet1
menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menu1.add_command(label="Nouveau jeu", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
#onglet2
menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Clean", menu=menu2)
menu2.add_command(label="Config", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
#onglet3
menu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide", menu=menu3)
menu3.add_command(label="A propos", command=alert)

fenetre.config(menu=menubar)
#TITRE
label_title = Label(fenetre, text="LA BATAILLE NAVALE", font=("Arial, 32"), bg='salmon', fg='white')
label_title.grid(row=1,column=3)

#text definissant la grille du joueur
label1 = Label( text =" Joueur", font=("Arial, 15") , fg='black')
#grille du joueur
label1.grid(row=2,column=2,padx=50,pady=100)
terrain = Canvas(fenetre, height=200, width=200)
terrain.grid(row=3,column=2,padx=50)
carreau=[[terrain.create_rectangle(i*20,j*20,(i+1)*20, (j+1)*20, fill="#FFFFFF")for i in range(10)]for j in range(10)]

#text definissant la grille du BOT
label2 = Label( text ="Ordinateur", font=("Arial, 15") , fg='black')
#grille du BOT
label2.grid(row=2,column=4,pady=100)
terrain1 = Canvas(fenetre, height=200, width=200)
terrain1.grid(row=3,column=4)
carreau1=[[terrain1.create_rectangle(i*20,j*20,(i+1)*20, (j+1)*20, fill="#FFFFFF")for i in range(10)]for j in range(10)]

#BOUTON POUR QUITTER
bouton=Button( text="Fermer", command=fenetre.quit)
bouton.grid(row=4,column=3)


# AFFICHAGE
fenetre.mainloop() #pour executer la fenetre dans son ensemble
