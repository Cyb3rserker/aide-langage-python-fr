#coding:utf-8

"""
FICHIER D'AIDE SUR TKINTER

Tkinter est un outile natif python qui permet 
de faire des intérfaces graphiques.
"""

# On commence par importer la bibliothèque :

import tkinter

#_____CREATION ET LANCEMENT FENETRE_____#
"""
Pour créer une fenêtre, on créer une variable 
qui va la représenter grâce au constructeur 
Tk() de la bibliothèque :
"""
fenetre = tkinter.Tk()
"""
On utilise ensuite la méthode mainloop() permettant 
de lancer la fenêtre et de la laisser pendant une 
durée indéfinie :
fenetre.mainloop()
(Je le met à la fin du programme car sinon les modifications 
que je renseigne plus bas ne seront pas appliquées)
"""

#-------------------------------------------------------------

#______METHODE SUR LA FENETRE_____

#___TITRE___
"""
On peut donner un titre à la fenêtre avec la méthode title() 
à utiliser avec la fenêtre. Ici, ce serait :
"""
fenetre.title("Programme d'aide sur l'utilisation de tkinter")

#___DIMENSIONS FENETRE___
"""
Pour définir les dimensions de la fenêtre, on utilise la méthode 
geometry à utiliser avec la fenêtre. Sa définition est :
ma_fenetre.geometry(nb_pixels_axe_Xxnbpixels_axeY)
Cette définition n'empêche pas l'utilisateur de modifier la 
taille de la fenêtre avec sa souris.
"""

#___FERMETURE FENETRE___

"""
On peut enclencher la ferméture de la fenêtre avec 
la méthode quit() à appliquer sur la fenêtre. Ici, 
ce serait :
fenetre.quit()
"""

#Je le met ici pour que toutes les modifications soient prises
fenetre.mainloop()