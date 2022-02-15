#coding:utf-8

"""
FICHIER D'AIDE SUR TKINTER

Tkinter est un outile natif python qui permet 
de faire des intérfaces graphiques grâce à des 
fenêtres. Tout ce qui se trouve sur la fenêtre 
est un widget, et la fenêtre elle même est un widget.
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

#---------------------------

#___TITRE___
"""
On peut donner un titre à la fenêtre avec la méthode title() 
à utiliser avec la fenêtre. Ici, ce serait :
"""
fenetre.title("Programme d'aide sur l'utilisation de tkinter")

#---------------------------

#___DIMENSIONS ET POSITION DE LA FENETRE___
"""
Pour définir les dimensions de la fenêtre, on utilise la méthode 
geometry à utiliser avec la fenêtre. Sa définition est :
ma_fenetre.geometry("<Longueur_fenetre>x<hauteur_fenetre>+<position_axe_x>+<position_axe_y>")
Les positions de référence pour placer la fenêtre partent du coin
supérieur gauche de l'écran. L'axe x part du haut vers le bas et 
l'axe y part de la gauche vers la droite donc si ma valeur 
position_axe_x est de 25, la fenêtre aura un écart de 25 pixels 
vers le bas par rapport au coin supérieur gauche et si ma valeur position_axe_y
est de 25, la fenêtre aura un écart de 25 pixels vers la droite par 
rapport au coin supérieur gauche.

exemple : 
"""
fenetre.geometry("800x600+25+25")
"""
Cette méthode n'empêche pas l'utilisateur de modifier la 
taille de la fenêtre avec sa souris.

On peut aussi center la fenêtre grâce à un calcul mathématique simple. 
On définit d'abord les positions de la fenêtre :

position_X = (<largeur_ecran> // 2) - (<largeur_fenetre> // 2)
position_Y = (<hauteur_ecran> // 2) - (<hauteur_fenetre> // 2)

exemple et méthode pour l'appliquer :
"""
ecran_x = fenetre.winfo_screenwidth()
# Longueur écran
ecran_y = fenetre.winfo_screenheight()
# Hauteur écran

fenetre_x = 800
# Longueur fenêtre
fenetre_y = 600
# Hauteur fenêtre

pos_x = (ecran_x // 2) - (fenetre_x // 2)
pos_y = (ecran_y // 2) - (fenetre_y // 2)

geo = "{}x{}+{}+{}".format(fenetre_x, fenetre_y, pos_x, pos_y)

fenetre.geometry(geo)
"""
Ce calcul, mathématiquement, centre parfaitement la fenêtre 
mais en réalité la fenêtre ne sera pas parfaitement centrée 
mais ça fait l'affaire.
"""

#-------------

"""
On peut aussi définir la taille minimale que la fenêtre peut 
avoir avec la méthode minsize(<longueur_min_fenetre>, <hauteur_min_fenetre>)
à appliquer sur la fenêtre.

exemple :
"""
#fenetre.minsize(400, 200)

#-------------

"""
On peut définir la taille maximale que la fenêtre peut 
avoir avec la méthode maxsize(<longueur_min_fenetre>, <hauteur_min_fenetre>)
à appliquer sur la fenêtre.

exemple :
"""
#fenetre.maxsize(1280, 720)
#!!!!!! VERIFIER LE FONCTIONNEMENT CAR NE S'APPLIQUE PAS

#-------------

"""
On peut interdire le redimensionnement de la fenêtre avec la 
méthode resizable(width = <True ou False>, height=<True ou False>)
Si la valeur est égale à True, on peut alors redimensionner cette 
partie de la fenêtre, la longueur ou la hauteur et inversement 
si la valeur est égale à False.

exemple :
"""
fenetre.resizable(width=True, height=True)

#-------------

"""
La méthode sizefrom permet de définir la dimensions de 
la fenêtre par rapport à un élément, par exemple l'utilisateur.

exemple :
"""
#fenetre.sizefrom("user")
"""
Je rajouterai des infos au fur et à mesure.
"""

#-------------

"""
On peut interdire le redimensionnement de la fenêtre avec la 
méthode resizable(width = <True ou False>, height=<True ou False>)
Si la valeur est égale à True, on peut alors redimensionner cette 
partie de la fenêtre, la longueur ou la hauteur et inversement 
si la valeur est égale à False.

exemple :
"""
fenetre.resizable(width=True, height=True)

#---------------------------

"""
La méthode positionfrom permet de définir la depuis où est positionnée 
la fenêtre, comme par exemple l'utilisateur.

exemple :
"""
#fenetre.positionfrom("user")
"""
Ici, la fenêtre sera positionnée en haut à gauche de l'écran.
Je rajouterai des infos au fur et à mesure.
"""


#___FERMETURE FENETRE___

"""
On peut enclencher la ferméture de la fenêtre avec 
la méthode quit() à appliquer sur la fenêtre. Ici, 
ce serait :
fenetre.quit()
"""
 
#-------------------------------------------------------------

#______WIDGETS______

#---------------------------

#___CREATION D'UN WIDGET___
"""
<nom_variable> = <nom_widget>(<widget_parent>, <parametres>...)
<widget_parent> est le widget sur lequel <nom_variable> va agir.
Par exemple, pour faire un widget de titre affiché sur la fenêtre, 
le widget parent sera fenetre et mon nom de variable titre_fenêtre, 
pour qu'il soit plus facil à indentifier dans le code.
Après avoir fait le widget, il faut ensuite positionner le widget sur 
la fenêtre.
"""

#---------------------------

#___POSITIONNEMENT WIDGET___
"""
Après avoir initialiser le widget, il faut le positionner sur la fenêtre 
pour qu'il puisse être vu. Pour cela, on peut utiliser la méthode pack 
avec la définition suivante :

<mon_widget>.pack()
"""

#---------------------------

#___RECUPERATION / MODIFICATION INFORMATIONS SUR UN WIDGET___
"""
On peut accéder au informations concernant les widgets que l'on a 
initialisés comme on le ferai avec un dictionnaire. En effet, les 
widgets on des attributs avec des valeurs et pour accéder à ces valeurs, 
on procède de la manière suivantes :

<nom_widget>["<nom_attribut>"]

On peut y accéder par un autre moyen. On utilise la méthode cget :

<nom_widget>.cget("<nom_attribut>")

Avec cette méthode, on ne peut que lire la valeur de l'attribut mais 
si on veut la modifier, on peut utiliser la méthode configure :

<nom_widget>.configure(<nom_attribut> = <nouvelle_valeur>)
ou 
<nom_widget>.config(<nom_attribut> = <nouvelle_valeur>)
"""

#---------------------------

#___AFFICHAGE TEXTE / IMAGE___

"""
Le widget Label permet d'afficher du texte ou bien 
une image. Le texte s'affiche sur une ligne mais on 
peut faire des retours à la ligne avec des \n. 
Sa structure est la suivante :

<nom_variable> = tkinter.Label(<widget_parent>, text=<mon_texte>)
ou
<nom_variable> = tkinter.Label(<widget_parent>, justify=<mon_texte>)
pour que le texte soit centré

exemple :
"""
exemple_Label = tkinter.Label(fenetre, text="Exemple du widget Label")
exemple_Label.pack()

#-------------

"""
On peut aussi utiliser le widget Message qui permet l'affichage 
d'un texte sur plusieurs lignes. Il le fait automatiquement mais 
on peut faire des retours à la lignes nous-mêmes en mettant des \n 
comme avec Label.

exemple :
"""
exemple_Message = tkinter.Message(fenetre, text="Exemple du widget Message")
exemple_Message.pack()

#---------------------------

#___SAISIE DE DONNEES___

"""
Le widget Entry permet de mettre un champs de saisie. Sa 
structure est la suivante :

<nom_variable> = tkinter.Entry(<widget_parent>)

Par défaut, il faut une taille d'affichage de 20 caractères 
mais on peut le changer avec l'attribut width :

<nom_variable> = tkinter.Entry(<widget_parent>, width=<longueur_voulue>)

exemple :
"""
exemple_Entry = tkinter.Entry(fenetre, width=20)
exemple_Entry.pack()
"""
On peut aussi masquer la saisie de l'utilisateur avec l'attribut show :
<nom_variable> = tkinter.Entry(<widget_parent>, show=<texte_a_afficher_a_la_place>)

exemple :
"""
exemple_Entry_show = tkinter.Entry(fenetre, show="*")
exemple_Entry_show.pack()
"""
On peut aussi empêcher la selection du texte saisie avec l'attribut 
exportselection. C'est un booléen donc il prend 0 pour interdire la 
séléction et 1 pour l'autoriser :

<nom_variable> = tkinter.Entry(<widget_parent>, exportselection=<0 ou 1>)
"""
exemple_Entry_exportselection = tkinter.Entry(fenetre, exportselection=1)
exemple_Entry_exportselection.pack()
#NE FONCTIONNE PAS NON PLUS, VERIFIER

#---------------------------

#___BOUTON___

"""
Pour initialiser un bouton, on utilise le widget Button. 
Sa structure est la suivante :

<nom_variable> = tkinter.Button(<widget_parent>, text=<texte_affiche_sur_bouton>)

On peut aussi regler la taille du boutton en caractères en 
modifiant les attibuts height et width.

exemple
"""
exemple_Button = tkinter.Button(fenetre, text="Exemple du widget Button")
exemple_Button.pack()
"""
On peut aussi y associer une commande qui sera executée lorque 
le bouton sera cliqué à l'aide de l'attribut command.
"""
def banane() :
    print("Banane sur le terminal")

exemple_Button_command = tkinter.Button(fenetre, text="Exemple du widget Button avec command", command=banane)
#On indique juste le nom de la commande, pas de parenthèses ou autres.
exemple_Button_command.pack()



#Je le met ici pour que toutes les modifications soient prises
fenetre.mainloop()