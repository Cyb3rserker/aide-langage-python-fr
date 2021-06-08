#3:23
#coding:utf-8

"""
Les propriétés permettent de manipuler les attributs des classes. 

"""

# Je met la prochaine partie en commentaire pour ne pas avoir à 
# recréer une nouvelle classe pour la suite du programme.

#class Chien :
#    """
#    documentation :
#    - c_race : ce que l'on veut
#    - c_taille :
#        - "PETIT"
#        - "MOYEN"
#        - "GRAND"
#    """
#
#    def __init__(self, c_race, c_taille) :
#        print("\nGénération d'un chien...")
#        self.race = c_race
#        self.taille = c_taille
#        print("Chien généré !\n\nRace : {}\nTaille :{}\n".format(c_race, c_taille))
#
#
#chien_1 = Chien("Bulldog", "MOYEN")
#
#print("Race du chien n°1 :", chien_1.race)
#chien_1.race = "Rottweiler"
#print("Race du chien n°1 :", chien_1.race)
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
accesseurs. Les accesseurs sont comme des cages qui contiennent 
les attributs ce qui empêche d'y avoir accès. 
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
        # Par convention, on représente les attributs non accessibles
        # avec un underscore _ avant leurs noms. Comme dit, c'est une 
        # convention donc ça n'a aucune incidence sur le déroulemment du 
        # programme.
        self._race = c_race
        self._taille = c_taille
        print("Chien généré !\n\nRace : {}\nTaille :{}\n".format(c_race, c_taille))

    """
    Dans mon exemple, il faut une sorte de mot de passe 
    administrateur pour lire ou changer les attributs d'un Chien.
    Je vais donc créer des propriétés pour age et race 
    grâce à property, une méthode ayant les arguments 
    suivant :

    property(<getter>, <setter>, <deleter>, <helper>)

    - getter  : obtenir la valeur d'un attribut
    - setter  : modifier la valeur d'un attribut
    - deleter :
    - helper  :

    Ces arguments ne sont pas obligatoire et on peut 
    juste se contenter du getter dans notre cas. On va 
    d'abord définir une méthode qui retourne l'attribut 
    _age seulement si on note le bon mot de passe 
    administrateur :
    """

    mdp_admin = "1234"

    """
    Ici, on va autorisé la lecture de l'age seulement 
    si l'utilisateur tape le bon mot de passe :
    """
    def _getrace(self) :
        mdp_user = input("Mot de passe pour connaitre la race : ")

        if mdp_user == Chien.mdp_admin :
            print("Accès autorisé.")
            return self._race
        else :
            print("Accès non autorisé.")

    """
    Là, on va faire une propriété qui va limiter la 
    possibilité de modifier un attribut, ici la race :
    """
    def _setrace(self, nouvelle_race) :
        mdp_user = input("Mot de passe pour changer la race : ")
        if mdp_user == Chien.mdp_admin :
            print("Accès autorisé.")
            self._race = nouvelle_race
        else :
            print("Accès non autorisé.")
        
    # On créé ensuite la propriété : 
    race = property(_getrace, _setrace)
    # note : ici, race est le nom de la propriété
    """
    """

# Début du programme :

chien_1 = Chien("Bulldog", "MOYEN")

print("\n_____UTILISATION DU GETTER_____")
print("(mdp : 1234)\n")

print("Race du chien n°1 : ", chien_1.race)
                             # Ici, c'est la propriété 
                             # race et pas l'attribut 
                             # _race.

"""
sortie au terminal :

Génération d'un chien...
Chien généré !

Race : Bulldog
Taille :MOYEN


_____UTILISATION DU GETTER_____
(mdp : 1234)

Mot de passe pour connaitre la race : 1234
Accès autorisé.
Race du chien n°1 :  Bulldog
"""

print("\n_____UTILISATION DU SETTER EN PLUS_____\n")
print("(mdp : 1234)")

print("Race chien n°1 :", chien_1.race)
chien_1.race = "Rottweiler"
print("Race chien n°1 :", chien_1.race)

"""
sortie au terminal :

_____UTILISATION DU SETTER EN PLUS_____

(mdp : 1234)
Mot de passe pour connaitre la race : 1234
Accès autorisé.
Race chien n°1 : Bulldog
Mot de passe pour changer la race : 1234 
Accès autorisé.
Mot de passe pour connaitre la race : 1234 
Accès autorisé.
Race chien n°1 : Rottweiler
"""