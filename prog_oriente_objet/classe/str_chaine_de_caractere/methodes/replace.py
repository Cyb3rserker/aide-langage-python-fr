#coding:utf-8
"""
La méthode replace permet de remplacer certains caractères d'une 
chaîne par d'autres. Voici sa définition :

str.replace(<caractère à remplacer>, <caractère qui remplace>, <nombre de fois que le remplacement s'effectuera>) 

Le dernier paramètre est optionnel. Voici des exemples d'utilisation :
"""

chaine_de_caracteres = "Je suis une chaîne de caractères."

print(chaine_de_caracteres)
print(chaine_de_caracteres.replace(" ", "_"))
# Je remplace tous les espaces par des tirets du 8

"""
sortie au terminal :

Je suis une chaîne de caractères.
Je_suis_une_chaîne_de_caractères.
"""

"""
Je vais maintenant remplacer tout les e par un E 3 fois :
"""

print(chaine_de_caracteres.replace("e", "E", 3))

"""
sortie au terminal :

JE suis unE chaînE de caractères.
"""