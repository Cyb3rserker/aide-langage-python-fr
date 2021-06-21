#coding:utf-8
"""
La méthode strip permet de supprimer les espaces inutiles qui se 
trouvent en début et fin de chaîne de caractères. Par espaces 
inutiles, je veux parler des espaces qui commencent la chaîne 
puis continuent jusqu'à un caractères et des espaces qui commencent 
à partir du dernier caractères et qui termine la chaîne. Voici un 
exemple :
"""

chaine_de_caracteres = "     Je suis une chaîne avec 5 espaces au début et 5 à la fin.     "

print(chaine_de_caracteres)
print(chaine_de_caracteres.strip())

"""
sortie au terminal :

     Je suis une chaîne avec 5 espaces au début et 5 à la fin.     
Je suis une chaîne avec 5 espaces au début et 5 à la fin.
"""

"""
Si la chaîne commence par un caractère et se termine avec un caractère, 
strip n'aura aucun effet :
""" 

chaine_de_caracteres = "[  Je suis une chaîne avec un crochet et 2 espaces au début et un crochet et 2 espaces à la fin.  ]"

print(chaine_de_caracteres)
print(chaine_de_caracteres.strip())

"""
sortie au terminal :

[  Je suis une chaîne avec un crochet et 2 espaces au début et un crochet et 2 espaces à la fin.  ]
[  Je suis une chaîne avec un crochet et 2 espaces au début et un crochet et 2 espaces à la fin.  ]
"""