import numpy as np
import random

fregate = 2
croiseur = 3
sousMarin = 3
cuirasse = 4
porteAvion = 5


#création de la matrice vide
def structure():
    tab=np.full ((10,10),0)
    return (tab)
    
# Placement aléatoire des bateaux
def aleatoire_user(mat):
    
    taille_navire=[2,3,3,4,5] 
    nombre_bat=len(taille_navire) #Definition de la taille des navires

    for Navire in range(nombre_bat):
        longueur=taille_navire[Navire];

        Verif=1

        while Verif:
           
            I=random.randint(0,9) # coordo. de départ de la matrice
            J=random.randint(0,9)

            if mat [I,J]==0: # si la case est inoccupé 
                orientation=random.randint(0,1) #alors le placement se fait aléatoirement 0=Vert 1=Horiz
                # Place Verticalement 
                if orientation==0:
                    if I+longueur-1<10:
                        if sum(mat[I:I+longueur,J])==0:
                            for n in range(longueur):
                                mat[I+n,J]=Navire+1 
                                Verif=0
                   

                # Place Horizontalement
                else:
                    if J+longueur-1<10:
                        if sum(mat[I,J:J+longueur])==0:
                            for n in range(longueur):
                                mat [I,J+n]=Navire+1 
                                Verif=0
                   
    return(mat)


#Placement manuelle 
def manuelle_user(mat):
    nombre_bat = 5
    while(nombre_bat != 0):
        taille_navire = nombre_bat
        print("Voici votre jeux")
        print(mat)
        print("Placons nos bateaux ")
        print(" ")
        x = int(input("Entrez la ligne : "))
        y = int(input("Entrez la colonne : "))
        orientation = int(input("Choisir orientation(1 pour up et 2 pour droite) : "))
        if taille_navire == 1 :
            taille_navire = 3
        Verif = 0
        if mat[x,y]==0 :
            if orientation == 1:
                if x >= taille_navire - 1 :
                    for i in range (1,taille_navire):
                        if mat[x-i][y] == 0 :
                            Verif = Verif + 1
                    if Verif == taille_navire - 1:
                        for i in range (0,taille_navire):
                            mat[x-i][y] = nombre_bat
                    else:
                        nombre_bat = nombre_bat + 1
                else :
                    nombre_bat = nombre_bat + 1
            else :
                if y < 10 - taille_navire :
                    for i in range (1,taille_navire):
                        if mat[x][y+i] == 0 :
                            Verif = Verif + 1
                    if Verif == taille_navire - 1:
                        for i in range (0,taille_navire):
                            mat[x][y+i] = nombre_bat
                    else:
                        nombre_bat = nombre_bat + 1
                else :
                    nombre_bat = nombre_bat + 1
        else  :
            nombre_bat = nombre_bat - 1
        nombre_bat = nombre_bat - 1
    return(mat)
    
    
# Les navires du BOT
def navire_BOT(mat):
  
    taille_navire=[2,3,3,4,5] 
    nombre_bat=len(taille_navire) #Definition de la taille des navires

    for Navire in range(nombre_bat):
        longueur=taille_navire[Navire];

        Verif=1
    
        while Verif:
           
            I=random.randint(0,9) # coordo. de départ de la matrice
            J=random.randint(0,9)

            if mat [I,J]==0: # si la case est inoccupé 
                orientation=random.randint(0,1) #alors le placement se fait aléatoirement 0=Vert 1=Horiz
                # Place Verticalement 
                if orientation==0:
                    if I+longueur-1<10:
                        if sum(mat[I:I+longueur,J])==0:
                            for n in range(longueur):
                                mat[I+n,J]=Navire+1 
                                Verif=0
                   

                # Place Horizontalement
                else:
                    if J+longueur-1<10:
                        if sum(mat[I,J:J+longueur])==0:
                            for n in range(longueur):
                                mat [I,J+n]=Navire+1 
                                Verif=0
    return (mat)



#Tir, touché ou pas?
def Joueur_touche (jeux_BOT,mat_tiré):
    compt=1
    while compt<4:
        print("Ou tirez ?: ")
        i = int(input("Choisir la ligne : "))
        j = int(input("Choisir la colonne :"))
        if jeux_BOT[i][j] == 0 :
            mat_tiré[i][j]= 8
            print("loupe")
            compt=compt+1 
        else:
            mat_tiré[i][j]= 9
            print("touche")
            compt=compt+1 
    return (mat_tiré)

#envoi de bombes du bot
def bombe(tab_bomb,tab_bat):
    compt=1
    while compt<4:
        L=random.randint(0,9)
        C=random.randint(0,9) 
    #on vérifie si l'envoi n'a pas déjà été fait à cet endroit
        if tab_bomb[L,C]==0:
            compt=compt+1 # une case supplémentaire testée
            if tab_bat[L,C]==0:
                print("loupe")
                tab_bomb[L,C]=8 #8 pour un envoi dans l'eau
            else : # il y a un bateau
                print("touche")
                tab_bomb[L,C]=9 #9 pour une touche
    return tab_bomb

def verif_gagnant(tab_win):
    compt = 0
    rep = True
  
    for I in range(0, 10):
        for J in range (0, 10):
            if tab_win[I, J] == 8:
                compt = compt + 1

    if compt == cuirasse+fregate+sousMarin +croiseur+porteAvion:
        return True
    else:
        return False

#Programme Principal

jeu=True
print("1.Place tout seul?")
print("2.Choisir les places de mes bateaux")
choix = int(input("Quel est votre choix? :"))

if choix == 1:
   jeux_user = aleatoire_user(structure())
elif choix == 2:
    jeux_user= manuelle_user (structure())


jeux_BOT = navire_BOT (structure())
damier_tir = structure()
print("jeux du BOT",'\n',jeux_BOT)
print(" ")
print("Votre jeux: ",'\n',jeux_user)

while jeu == True:
    mat_tiré=structure()
    mat_tiré=Joueur_touche (jeux_BOT,mat_tiré)
    print("Vos touches sont \n",mat_tiré)
    
    tab_bat=structure()
    tab_bomb=structure()
    tab_bomb= bombe (tab_bomb,tab_bat)
    print ("le bot a tiré ici \n" , tab_bomb)

    if verif_gagnant(tab_bomb) == True:

        print ("\n La machine vous a vaincu")
        jeu = False
    elif verif_gagnant(mat_tiré) == True :
        print ("\n Vous l'emportez' !")
        jeu = False
    else:
        print("\n Nouveau tour ")
