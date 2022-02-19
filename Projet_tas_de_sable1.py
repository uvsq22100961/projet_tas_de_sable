# Projet tas de sable
# Groupe TD02
# Thibault ROYERE
# Camille ROESSLER
# Manira MAHAMAT HAGGAR
# url du dépôt github https://github.com/uvsq22100961/projet_tas_de_sable

#######################################################################

#variables
HEIGHT = 500
WIDTH = 500
L = [[0]*100 for i in range(100)]
bouton_fin = 0
Text = 0
grille_créée = False

#bibliothèques
import tkinter as tk
import random

#fenêtre 
racine = tk.Tk()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)

#fonctions
def init_config_courante():
    """fonction qui crée la grille"""
    global grille_créée
    #Si la grille n'est pas créée, on le fait(cela évite de créer plusieurs fois la grille):
    if grille_créée == False:
        #Pour chaque pixel...
        for i in range(500):
            #...on n'en choisis qu'un sur 5...
            if i%5 == 0:
                #...et on crée une ligne horizontale.
                canvas.create_line((i,0), (i,500), width=1, fill="black")
        for i in range(500):
            if i%5 == 0:
                #/...et on crée une ligne verticale.
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
            elif L[ligne][element] == 3:
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
    Text.grid(row=4, column=2)
    #bouton pour arrêter la création de la configuration
    bouton_fin = tk.Button(racine, text="J'ai fini", command=creation_config_finie)
    bouton_fin.grid(row=4, column=3)
    #Enfin, on lie le clic gauche de la souris avec une fonction:
    racine.bind("<Button-1>", coordonnees)

def coordonnees(event):
    global L
    #On récupère les coordonnées du clic:
    x = event.x
    y = event.y
    #On transforme les coordonnées en valeurs qui seront adaptées à la liste:
    x1 = x//5
    y1 = y//5
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
    #On supprime le text et le bouton:
    bouton_fin.destroy()
    Text.destroy()

    
#Widgets
racine.title("Projet tas de sable")
Bouton1 = tk.Button(racine, text="créer une configuration aléatoire", command=config_aleatoire)
init_config_courante()
Bouton2 = tk.Button(racine, text="choisir une configuration dans la liste")
Bouton3 = tk.Button(racine, text="construire une configuration", command=creer_config)

#placement des widgets
canvas.grid(row=0, column=1, rowspan=3, columnspan=2)
Bouton1.grid(row=0, column=0)
Bouton2.grid(row=1, column=0)
Bouton3.grid(row=2, column=0)

#Fin
canvas.mainloop()