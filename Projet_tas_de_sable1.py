# Projet tas de sable
# Groupe TD02
# Thibault ROYERE
# Camille ROESSLER
# Manira MAHAMAT HAGGAR
# url du dépôt github https://github.com/uvsq22100961/projet_tas_de_sable

HEIGHT = 500
WIDTH = 500

import tkinter as tk

racine = tk.Tk()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)
Bouton1 = tk.Button(racine, text="créer la configuration aléatoire")


canvas.grid(row=0, culumn=1)
Bouton1.grid(row=0, column=0)
canvas.mainloop()