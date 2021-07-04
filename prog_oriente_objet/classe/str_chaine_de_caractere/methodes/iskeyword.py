#coding:utf-8

"""
La méthode iskeyword permet de vérifier si la chaîne de caractère
est un mot réservé en Python. Cette méthode n'est pas directement 
affiliée à la class str, mais elle est utilisée avec ces objets 
la grande majorité du temps. iskeyword se situe dans le module keyword.
Elle peut être utilisée en complément de la méthode isidentifier de 
la classe str pour vérifier la validité d'un identifiant.
"""

import keyword

user_str = input("Votre mot : ")

if keyword.iskeyword(user_str) == True :
    print("Votre mot est un mot réservé en Python.")
else :
    print("Votre mot n'est pas un mot réservé en Python.")

user_str = input("Votre nouveau mot : ")

if keyword.iskeyword(user_str) == True :
    print("Votre mot est un mot réservé en Python.")
else :
    print("Votre mot n'est pas un mot réservé en Python.")

"""
sortie au terminal :

Votre mot : class
Votre mot est un mot réservé en Python.
Votre nouveau mot : banane
Votre mot n'est pas un mot réservé en Python.
"""