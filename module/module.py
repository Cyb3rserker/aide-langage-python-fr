#coding:utf-8

"""
En python, il y a ce qu'on appel des modules, c'est à dire des 
fichiers comprenant des fonctions n'étant pas native du langage 
(~= fonctions par défaut on va dire). Pour les adeptes du language 
c, c'est comme des bibliothèques. Il existe des documentations de 
module précisant quelle fonction fait quoi et comment l'utiliser.
Pour l'exemple, on va utiliser la fonction sqrt qui permet de 
calculer la racine carré du nombre en argument (square root) :
"""
 
"""
resultat = sqrt(100)
print(resultat)

On peut voir que le terminal affiche cette erreur :

NameError: name 'sqrt' is not defined

Si l'interpréteur ne reconnait pas la fonction, c'est parce que 
cette fonction n'est pas une fonction native mais elle appartient 
à un module appeler "math", un module rassemblant un grand nombre 
de fonctions en rapport avec les maths. Pour que mon programme 
marche, je vais devoir "importer" (je sais pas comment dire en 
français) le module math avec cette syntaxe :
"""

print("\n_____IMPORT SIMPLE_____\n")

import math

resultat = math.sqrt(100)
# Explications du math. plus bas
print(resultat)

"""
sortie au terminal :
10.0

On peut donc voir que le programme fonctionne. Lorsqu'on utilise 
une fonction venant d'un certain module, on doit préciser le nom du 
module. Ceci n'est pas obligé si on utilise cette syntaxe :
"""

print("\n_____FROM IMPORT_____\n")

from math import sqrt

resultat = sqrt(100)
print(resultat)

"""
sortie au terminal :
10.0

Même sans les lignes du dessus, le programme aurai tout aussi bien 
marcher, et en plus sans la nécessité de préciser le nom du module 
avant utilisation de la fonction sqrt.
Si on va utiliser un grand nombre de fonctions d'un module et 
qu'on ne veut pas préciser le nom du module avant chaque utilisation 
de fonction, on peut simplement mettre cette ligne :
"""

from math import *
# Tu importes toutes (*) les fonctions du module math

"""
On peut aussi utiliser cette syntaxe et quand même préciser le nom 
du module avant la fonction pour ne pas avoir des conflits de nom 
semblable 
(ex : menu_principal.afficher_menu /= menu_pause.afficher_menu)
ou bien même savoir quel module a été utile où.
"""

"""
On peut aussi créer nos propres modules 
(suite dans aide/module/création module)
"""