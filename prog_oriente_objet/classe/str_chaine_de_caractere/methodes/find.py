#coding:utf-8
"""
La méthode find permet de chercher une chaîne de caractères 
dans une autre chaîne de caractères :

str.find(<chaîne à trouver>, <début de la chaîne>, <fin>) 

Elle retourne l'indice (= l'emplacement) du premier caractère qui 
correspond à la chaîne précisée dans les paramètres et si elle ne 
la trouve pas, elle retourne -1. D'ailleurs, la méthodes est sensible
à la casse, c'est à dire qu'il faut être rigoureux avec les majuscules.
(note : les ordinateurs commencent à compter à partir de 0, donc 
si ma chaîne à trouver commence dès le premier caractère de l'initial,
l'indice sera de 0.)
"""

print()
print("FIND".center(50, "*"))
print()

chaine_de_caracteres = "je suis une chaîne de caractères"

print("Indice de 'une' dans 'je suis une chaîne de caractères' : \
", chaine_de_caracteres.find("une"))

print("Indice de 'une' dans 'je suis une chaîne de caractères' : \
", chaine_de_caracteres.find("Je"))

"""
sortie au terminal :

***********************FIND***********************

Indice de 'une' dans 'je suis une chaîne de caractères' :  8
Indice de 'Je' dans 'je suis une chaîne de caractères' :  -1


On peut donc voir que 'une' se situe à l'indice 8 de notre chaîne et 
que 'Je' n'est pas dans la chaîne.
"""