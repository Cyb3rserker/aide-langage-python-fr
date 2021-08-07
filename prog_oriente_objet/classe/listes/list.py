#coding:utf-8

"""
Les listes sont un peu comme les tableaux dans les autres langages comme 
le c car elles permettent de faire des séquences d'informations rangées. 
mais on peut y rassembler des informations de types différents.
Contraiement aux chaînes de caractères, on manipule directement les listes
et pas des copies.
"""

#_____CREATION D'UNE LISTE :_____

print()
print("\nCREATION DE LISTE\n".center(50, "*"))
print()

# Voici les différentes syntaxes pour instancier une liste :

# (les éléments de la liste se mettent entre les crochets)
liste_exemple = list([]) # plus explicite
# ou
liste_exemple = [] # plus rapide

# Voici comment y mettre des éléments :

liste_exemple = ["banane", 50, "origami", "abacus", 345]
print(liste_exemple)
print(type(liste_exemple))

"""
Pour accéder à ces éléments, on peut aussi utiliser l'index, comme les 
chaînes de caractères :
"""

print(f"Element à l'index 2 : {liste_exemple[2]}")
print(f"Element à l'index 3 : {liste_exemple[3]}")

"""
sortie au terminal :

***************
CREATION DE LISTE
****************

['banane', 50, 'origami', 'abacus', 345]
<class 'list'>
Element à l'index 2 : origami
Element à l'index 3 : abacus
"""

print()
print("\nMULTIPLICATION D'ELEMENTS SEMBLABLES\n".center(50, "*"))
print()

"""
Si on a plusieurs éléments semblables, ont peut utiliser cette syntaxe 
plus rapide :
"""

inventaire_joueur = ["arc"] * 4

print(inventaire_joueur)

print()
print("\nRANGE DANS UNE LISTE\n".center(50, "*"))
print()

"""
On peut aussi utiliser la fonction range pour avoir directement une 
suite de nombre dans notre liste. Dans mon exemple, je veux mettre 
tous les nombres entiers de 0 à 20 dans ma liste :
"""

liste_exemple = range(0, 20 + 1)

print()
print("\nPARCOURIR LA LISTE AVEC FOR\n".center(50, "*"))
print()

"""
Pour parcourir une liste, on peut utiliser une boucle for et je vais 
illustrer mon exemple avec l'inventaire d'un joueur que je souhaite 
parcourir :
"""

inventaire_joueur = ["arc ", "bouclier", "tunique"] 
# C'est une liste de tous les nombres entiers de 0 à 4.

print("Objet dans l'inventaire du joueur :")

for objet_dans_inventaire_joueur in inventaire_joueur :
    print(objet_dans_inventaire_joueur)

"""
sortie au teminal :

**********
PARCOURIR LA LISTE AVEC FOR
***********

Objet dans l'inventaire du joueur :
arc
bouclier
tunique
"""