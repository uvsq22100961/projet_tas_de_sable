# Projet tas de sable
# Groupe TD02
# Thibault ROYERE
# Camille ROESSLER
# Manira MAHAMAT HAGGAR
# url du dépôt github https://github.com/uvsq22100961/projet_tas_de_sable

#######################################################################

#bibliothèques
import tkinter as tk
import random

##VARIABLES
#dimensions du canvas
HEIGHT = 500
WIDTH = 500
#liste à deux dimensions
L = [[0]*100 for i in range(100)]
#Bonton et text pour créer une configuration
bouton_fin = 0
Text = 0
#témoin de la création ou non de la grille
grille_créée = False
#Listes (avec leur bouton) associées aux configurations à charger
lconfig_Random = [[0]*100 for i in range(100)]
bouton_Random = 0
lconfig_Pile = [[0]*100 for i in range(100)] #On la définira quand l'utilisateur voudra charger une configuration, pour lui
#demander le nombre central N
bouton_Pile = 0
lconfig_Max_stable = [[3]*100 for i in range(100)]
bouton_Max_stable = 0
lconfig_identity = [[0]*100 for i in range(100)] #On la définira quand on pourra stailiser une configuration
bouton_Identity = 0
#témoin de la fin ou non de la création d'une configuration:
fin_creation_config = True
#témoin d'utilisation ou non de liste_config
a = 0
#témoin d'utilisation ou non de additionner_configs
b = 0
#text lors de l'addition de configurations
Text2 = 0
#témoin d'utilisation ou non de soustraire_configs
c = 0
#text lors de la soustraction d'une configuration à une autre
Text3 = 0


#fenêtre 
racine = tk.Tk()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)

##FONCTIONS
def init_config_courante():
    """fonction qui crée la grille"""
    global grille_créée
    #Si la grille n'est pas créée, on le fait(cela évite de créer plusieurs fois la grille):
    if grille_créée == False:
        #Pour chaque pixel...
        for i in range(500):
            #...on n'en choisis qu'un sur 5...
            if i%5 == 0:
                #...et on crée une ligne verticale.
                canvas.create_line((i,0), (i,500), width=1, fill="black")
        for i in range(500):
            if i%5 == 0:
                #/...et on crée une ligne horizontale.
                canvas.create_line((0,i), (500,i), width=1, fill="black")
        grille_créée = True

def couleurs():
    """Affecte une couleur à chaque valeur de la matrice"""
    #On parcours la liste...
    for ligne in range(len(L)):
        for element in range(len(L[ligne])):
            #...et pour chaque case, on crée un rectangle d'une certaine couleur.
            if L[ligne][element] == 1:
                canvas.create_rectangle((5*element, 5*ligne),(5*(element + 1),5*(ligne + 1)), fill="grey70")
            elif L[ligne][element] == 2:
                canvas.create_rectangle((5*element, 5*ligne),(5*(element + 1),5*(ligne + 1)), fill="yellow")
            elif L[ligne][element] >= 3:
                canvas.create_rectangle((5*element, 5*ligne),(5*(element + 1),5*(ligne + 1)), fill="orange")

def config_aleatoire():
    global L
    #On vérifie d'abord s'il y a des rectangles pour les supprimer et éviter les bugs.
    ##On parcours tous le canevas avec les deux "for":
    for ligne in range(len(L)):
        for colonne in range(len(L[ligne])):
            #S'il y a au moins un grain de sable dans la case...
            if L[ligne][colonne] != 0:
                objet = canvas.find_closest(1 + 5*colonne, 1 + 5*ligne)
                #(la fonction find_closest retourne une liste contenant l'identifiant des objets les plus proches du point (x, y)).
                #...on supprime le rectangle de la case...
                if len(objet) != 0:
                    canvas.delete(objet[0])
                #...et on initialise L aux coordonnées:
                L[ligne][colonne] = 0
    #On parcours la liste...
    for ligne in range(len(L)):
        for element in range(len(L[ligne])):
            #...et on affecte à chaque élément une valeur aléatoire entre 0 et 3.
            L[ligne][element] = random.randint(0,3)
    #On appelle la fonction "couleurs" pour afficher les changements dans le canevas.
    couleurs()

def creer_config():
    """fonction qui permet à l'utilisateur de créer une configuration"""
    global L
    global bouton_fin
    global Text
    global fin_creation_config
    #On désactive le témoin de fin de la création de la configuration s'il est activé
    fin_creation_config = False
    #On vérifie d'abord s'il y a des rectangles pour les supprimer et éviter les bugs.
    #On parcours tous le canevas avec les deux "for":
    for ligne in range(len(L)):
        for colonne in range(len(L[ligne])):
            #S'il y a au moins un grain de sable dans la case...
            if L[ligne][colonne] != 0:
                objet = canvas.find_closest(1 + 5*colonne, 1 + 5*ligne)
                #la fonction find_closest retourne une liste contenant l'identifiant des objets les plus proches du point (x, y).
                #...on supprime le rectangle de la case...
                if len(objet) != 0:
                    canvas.delete(objet[0])
                #...et on initialise L aux coordonnées:
                L[ligne][colonne] = 0
    #text d'explications:
    Text = tk.Label(racine, text="Cliquer sur une case pour augmenter le nombre de grains")
    Text.grid(row=6, column=2)
    #bouton pour arrêter la création de la configuration
    bouton_fin = tk.Button(racine, text="J'ai fini", command=creation_config_finie)
    bouton_fin.grid(row=6, column=3)
    #Enfin, on lie le clic gauche de la souris avec une fonction:
    racine.bind("<Button-1>", coordonnees)

def coordonnees(event):
    global L
    global fin_creation_config
    #On vérifie d'abord que le témoin est désactivé pour continuer
    if fin_creation_config == False:
        #On récupère les coordonnées du clic:
        x = event.x
        y = event.y
        #On transforme les coordonnées en valeurs qui seront adaptées à la liste:
        x1 = x//5
        y1 = y//5
        #Si on clic plus d'une fois sur la même case, il faut supprimer les anciens rectangles:
        if L[y1][x1] >= 1:
            objet = canvas.find_closest(x, y)
            if len(objet) != 0:
                canvas.delete(objet[0])
        if (0 <= x and x <= 500) and (0 <= y and y <= 500):
            #On ajoute un grain de sable aux coordonnées:
            L[y1][x1] += 1
            #Enfin, on l'affiche avec des rectangles:
            if L[y1][x1] == 1:
                canvas.create_rectangle((5*x1, 5*y1),(5*(x1 + 1),5*(y1 + 1)), fill="grey70")
            elif L[y1][x1] == 2:
                canvas.create_rectangle((5*x1, 5*y1),(5*(x1 + 1),5*(y1 + 1)), fill="yellow")
            elif L[y1][x1] >= 3:
                canvas.create_rectangle((5*x1, 5*y1),(5*(x1 + 1),5*(y1 + 1)), fill="orange")
        #Et on recommence pour chaque clics tant que le bouton fin n'est pas utilisé.
        racine.bind("<Button-1>", coordonnees)

def creation_config_finie():
    """Arrête la création d'une configuration"""
    global bouton_fin
    global Text
    global fin_creation_config
    #On supprime le text et le bouton:
    bouton_fin.destroy()
    Text.destroy()
    #On actionne le témoin de fin de la création de la configuration
    fin_creation_config = True

def liste_configs():
    """Permet de charger une configuration dans une liste des configurations"""
    global bouton_Random
    global bouton_Pile
    global bouton_Max_stable
    global bouton_Identity
    global a
    a = 1
    #On créee les boutons (on verra plus tard pour la sauvegarde)
    bouton_Random = tk.Button(racine, text="config Random", command=config_Random)
    bouton_Pile = tk.Button(racine, text="config Pile", command=config_Pile)
    bouton_Max_stable = tk.Button(racine, text="config Max stable", command=config_Max_stable)
    bouton_Identity = tk.Button(racine, text="config Identity", command=config_Identity)
    #On les positionne
    bouton_Random.grid(row=0, column=3)
    bouton_Pile.grid(row=1, column=3)
    bouton_Max_stable.grid(row=2, column=3)
    bouton_Identity.grid(row=3, column=3)
    #On vérifie ensuite s'il y a des rectangles pour les supprimer et éviter les bugs.
    #On parcours tous le canevas avec les deux "for":
    for ligne in range(len(L)):
        for colonne in range(len(L[ligne])):
            #S'il y a au moins un grain de sable dans la case...
            if L[ligne][colonne] != 0:
                objet = canvas.find_closest(1 + 5*colonne, 1 + 5*ligne)
                #la fonction find_closest retourne une liste contenant l'identifiant des objets les plus proches du point (x, y).
                #...on supprime le rectangle de la case...
                if len(objet) != 0:
                    canvas.delete(objet[0])
                #...et on initialise L aux coordonnées:
                L[ligne][colonne] = 0

def liste_configs_fin(liste):
    global L
    global bouton_Random
    global bouton_Pile
    global bouton_Max_stable
    global bouton_Identity
    global a
    L = liste
    #On supprime les boutons :
    bouton_Random.destroy()
    bouton_Pile.destroy()
    bouton_Max_stable.destroy()
    bouton_Identity.destroy()
    #On réinitialise le témoin
    a = 0
    #On appelle la fonction "couleurs" pour afficher les changements dans le canevas.
    couleurs()

def additionner_configs():
    """Permet d'additionner la configuration courante avec une configuration choisie dans la liste des configuration"""
    global bouton_Random
    global bouton_Pile
    global bouton_Max_stable
    global bouton_Identity
    global b
    global Text2
    b = 1
    #On créee les boutons (on verra plus tard pour la sauvegarde)
    bouton_Random = tk.Button(racine, text="config Random", command=config_Random)
    bouton_Pile = tk.Button(racine, text="config Pile", command=config_Pile)
    bouton_Max_stable = tk.Button(racine, text="config Max stable", command=config_Max_stable)
    bouton_Identity = tk.Button(racine, text="config Identity", command=config_Identity)
    #On les positionne
    bouton_Random.grid(row=0, column=3)
    bouton_Pile.grid(row=1, column=3)
    bouton_Max_stable.grid(row=2, column=3)
    bouton_Identity.grid(row=3, column=3)
    #text d'explication:
    Text2 = tk.Label(racine, text="Cliquez sur la configuration avec laquelle vous voulez additionner la configuration courante")
    Text2.grid(row=6, column=1)

def additionner_configs_fin(liste):
    global L
    global bouton_Random
    global bouton_Pile
    global bouton_Max_stable
    global bouton_Identity
    global Text2
    global b
    bouton_Random.destroy()
    bouton_Pile.destroy()
    bouton_Max_stable.destroy()
    bouton_Identity.destroy()
    Text2.destroy()
    b = 0
    #On vérifie ensuite s'il y a des rectangles pour les supprimer et éviter les bugs.
    #On parcours tous le canevas avec les deux "for":
    for ligne in range(len(L)):
        for colonne in range(len(L[ligne])):
            #S'il y a au moins un grain de sable dans la case...
            if L[ligne][colonne] != 0:
                objet = canvas.find_closest(1 + 5*colonne, 1 + 5*ligne)
                #...on supprime le rectangle de la case...
                if len(objet) != 0:
                    canvas.delete(objet[0])
    for ligne in range(len(L)):
        for element in range(len(L[ligne])):
            L[ligne][element] = L[ligne][element] + liste[ligne][element]
    #On appelle la fonction "couleurs" pour afficher les changements dans le canevas.
    couleurs()

def soustraire_configs():
    """Permet de soustraire une configuration choisie dans la liste des configuration à la configuration courante """
    global bouton_Random
    global bouton_Pile
    global bouton_Max_stable
    global bouton_Identity
    global c
    global Text3
    c = 1
    #On créee les boutons (on verra plus tard pour la sauvegarde)
    bouton_Random = tk.Button(racine, text="config Random", command=config_Random)
    bouton_Pile = tk.Button(racine, text="config Pile", command=config_Pile)
    bouton_Max_stable = tk.Button(racine, text="config Max stable", command=config_Max_stable)
    bouton_Identity = tk.Button(racine, text="config Identity", command=config_Identity)
    #On les positionne
    bouton_Random.grid(row=0, column=3)
    bouton_Pile.grid(row=1, column=3)
    bouton_Max_stable.grid(row=2, column=3)
    bouton_Identity.grid(row=3, column=3)
    #text d'explication:
    Text3 = tk.Label(racine, text="Cliquez sur la configuration qui soustraira la configuration courante")
    Text3.grid(row=6, column=1)

def soustraire_configs_fin(liste):
    global L
    global bouton_Random
    global bouton_Pile
    global bouton_Max_stable
    global bouton_Identity
    global Text3
    global c
    bouton_Random.destroy()
    bouton_Pile.destroy()
    bouton_Max_stable.destroy()
    bouton_Identity.destroy()
    Text3.destroy
    c = 0
    #On vérifie ensuite s'il y a des rectangles pour les supprimer et éviter les bugs.
    #On parcours tous le canevas avec les deux "for":
    for ligne in range(len(L)):
        for colonne in range(len(L[ligne])):
            #S'il y a au moins un grain de sable dans la case...
            if L[ligne][colonne] != 0:
                objet = canvas.find_closest(1 + 5*colonne, 1 + 5*ligne)
                #...on supprime le rectangle de la case...
                if len(objet) != 0:
                    canvas.delete(objet[0])
    for ligne in range(len(L)):
        for element in range(len(L[ligne])):
            if liste[ligne][element] <= L[ligne][element]:
                L[ligne][element] = L[ligne][element] - liste[ligne][element]
            else: L[ligne][element] = 0
    #On appelle la fonction "couleurs" pour afficher les changements dans le canevas.
    couleurs()

#fonctions liées aux configurations de la liste des configurations

def config_Random():
    global lconfig_Random
    global a
    global b
    global c
    for ligne in range(len(lconfig_Random)):
        for element in range(len(lconfig_Random[ligne])):
            lconfig_Random[ligne][element] = random.randint(0, 3)
    if a == 1:
        liste_configs_fin(lconfig_Random)
    elif b == 1:
        additionner_configs_fin(lconfig_Random)
    elif c == 1:
        soustraire_configs_fin(lconfig_Random)

def config_Pile():
    global lconfig_Pile
    global a
    global b
    global c
    N = int(input("Choisir le nombre de grains qui seront dans la case du milieu (max: 3) : "))
    lconfig_Pile[50][50] = N
    if a == 1:
        liste_configs_fin(lconfig_Pile)
    elif b == 1:
        additionner_configs_fin(lconfig_Pile)
    elif c == 1:
        soustraire_configs_fin(lconfig_Pile)

def config_Max_stable():
    global lconfig_Max_stable
    global a
    global b
    global c
    lconfig_Max_stable = [[3]*100 for i in range(100)]
    if a == 1:
        liste_configs_fin(lconfig_Max_stable)
    elif b == 1:
        additionner_configs_fin(lconfig_Max_stable)
    elif c == 1:
        soustraire_configs_fin(lconfig_Max_stable)

def config_Identity():
    global lconfig_identity
    global a
    global b
    global c

def automate1():
    """effectue une étape de l'automate"""
    #On créé une liste égale à L pour pouvoir modifier L en fonction de ce que L est à l'instant t où on appui sur le bouton.
    L2 = []
    for lignes in L:
        L2.append(list(lignes))
    #On vérifie s'il y a des rectangles pour les supprimer et éviter les bugs.
    #On parcours tous le canevas avec les deux "for":
    for ligne in range(len(L)):
        for colonne in range(len(L[ligne])):
            #S'il y a au moins un grain de sable dans la case...
            if L[ligne][colonne] != 0:
                objet = canvas.find_closest(1 + 5*colonne, 1 + 5*ligne)
                #...on supprime le rectangle de la case...
                if len(objet) != 0:
                    canvas.delete(objet[0])
                #...et on initialise L aux coordonnées:
    for lignes in range(len(L2)):
        for element in range(len(L2[lignes])):
            if L2[lignes][element] >= 4:
                L[lignes][element] -= 4
                if element != 0:
                    L[lignes][element - 1] += 1
                if lignes != 0:
                    L[lignes - 1][element] += 1
                if element != 99:
                    L[lignes][element + 1] += 1
                if lignes != 99:
                    L[lignes + 1][element] += 1
    #On appelle la fonction "couleurs" pour afficher les changements dans le canevas.
    couleurs()

def calcul_stabilisation():
    """Calcul la stabilisation de la configuration courante"""
    L2 = []
    for lignes0 in L:
             L2.append(list(lignes0))
    for lignes in range(len(L)):
        for element in range(len(L[lignes])):
            while L[lignes][element] >= 4:
                for lignes1 in range(len(L2)):
                    for element1 in range(len(L2[lignes])):
                        if L2[lignes1][element1] >= 4:
                            L[lignes1][element1] -= 4
                        if element1 != 0:
                            L[lignes1][element1 - 1] += 1
                        if lignes1 != 0:
                            L[lignes1 - 1][element1] += 1
                        if element1 != 99:
                            L[lignes1][element1 + 1] += 1
                        if lignes1 != 99:
                            L[lignes1 + 1][element1] += 1
        for lignes2 in range(len(L)):
                    for element2 in range(len(L[lignes2])):
                        if L[lignes2][element2] >= 4:
                            #calcul_stabilisation()
                            0


    
#Widgets
racine.title("Projet tas de sable")
Bouton1 = tk.Button(racine, text="créer une configuration aléatoire", command=config_aleatoire)
init_config_courante()
Bouton2 = tk.Button(racine, text="charger une configuration dans la liste", command=liste_configs)
Bouton3 = tk.Button(racine, text="construire une configuration", command=creer_config)
Bouton_somme = tk.Button(racine, text="Additionner", command=additionner_configs)
Bouton_soustraire = tk.Button(racine, text="Soustraire", command=soustraire_configs)
Bouton_automate1 = tk.Button(racine, text="Effectuer une étape de l'automate", command=automate1)

#placement des widgets
canvas.grid(row=0, column=1, rowspan=6, columnspan=2)
Bouton1.grid(row=0, column=0)
Bouton2.grid(row=1, column=0)
Bouton3.grid(row=2, column=0)
Bouton_somme.grid(row=3, column=0)
Bouton_soustraire.grid(row=4, column=0)
Bouton_automate1.grid(row=5, column=0)

#Fin
canvas.mainloop()
#calcul_stabilisation()

#Choses faites:
#13/03
#- création fonction config_Identity (mais pas encore écrite)
#- correction de la fonction coordonnées (plusieurs clics sur la même case l.130), + fait qu'on pouvait continuer 
#à modifier la configuration après avoir appuyé sur le bouton fin (création variable fin_creation_config)
#- écriture fonctions liste_config et liste_config_fin
#- écriture fonctions config_Random, config_Max_stable et config_Pile
#- écriture fonctions additionner_config et additionner_config_fin
#- écriture fonctions soustraire_configs et soustraire_configs_fin
# 21/03
#- écriture fonction automate1

#PROBLEMES:
#- la fonction coordonnées prend en conpte les clic à gauche du canvas et sur le bouton fin