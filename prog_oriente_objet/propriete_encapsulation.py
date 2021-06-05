#3:23
#coding:utf-8

"""
Les propriétés permettent de manipuler les attributs des classes. 

"""

class Chien :
    """
    documentation :
    - c_race : ce que l'on veut
    - c_taille :
        - "PETIT"
        - "MOYEN"
        - "GRAND"
    """

    def __init__(self, c_race, c_taille) :
        print("\nGénération d'un chien...")
        self.race = c_race
        self.taille = c_taille
        print("Chien généré !\n\nRace : {}\nTaille :{}\n".format(c_race, c_taille))


chien_1 = Chien("Bulldog", "MOYEN")

print("Race du chien n°1 :", chien_1.race)
chien_1.race = "Rottweiler"
print("Race du chien n°1 :", chien_1.race)
"""
sortie au terminal :

Génération d'un chien...
Chien généré !

Race : Bulldog
Taille :MOYEN

Race du chien n°1 : Rottweiler
"""

"""
Comme on a pu le voir au dessus, j'ai pu accéder sans problème à 
l'attribut "race" de l'objet chien_1 en affichant sa race et en 
la modifiant. Normalement, il faut interdire ce genre d'accès 
aux attributs et pour cela, on utilise ce qu'on appelle des 
accesseurs. 