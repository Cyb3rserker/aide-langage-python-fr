#coding:utf-8

"""
Les méthodes sont des fonctions qui soit agissent sur 
une instance d'une classe (méthode), soit agissent sur 
la classe elle même (méthode de classe) ou soit sont 
décritent dans une classe mais qui peuvent être utilisées 
sur n'importe quoi (à condition de préciser de quelle 
classe elle vient). Pour les explications, je vais 
prendre les mêmes classes que classe_attributs.py.

On définit
"""

# DEFINITION DES CLASSES :

class Personnage :
    def __init__(self, c_nom = "_DEFAUT_", c_taille_cm = "170", c_force = "50") :
        print("\nCréation d'un personnage...\n")
        self.nom = c_nom
        self.taille_cm = c_taille_cm
        self.force = c_force

class LancePierre :
    # ici exceptionnellement, je n'ai pas mis de documentation 
    # parce que je ne veux pas allourdir encore le fichier. La 
    # documentation se trouve dans classe_attributs.py 
    
    nombre_lance_pierre = 0

    def __init__(self): 
        print("Fabrication d'un lance pierre...")
        print()
        # (pour sauter une ligne)

        """
        Pour définir un attibut pour un objet, on utilise 
        cette syntaxe : 
        """
        self.taille_corde = 160
        # On met self, puis un point, puis le nom de l'attribut.
        self.taille_baton = "MOYEN"
        self.couleur_corde = "ROUGE"
        self.projectile = "CAILLOU"

        LancePierre.nombre_lance_pierre += 1
    
    # On définit une méthode comme on définit une fonction normale :

    def tirer(self, c_force_tire) :
        print("BANG ! Un joueur a tiré un projectile avec une force de {} !".format(c_force_tire))
        # Comme une fonction, on peut utiliser une valeur de retour
        toucher_autre_joueur = bool(input("Autre joueur touché ? "))
        return toucher_autre_joueur


# PROGRAMME PRINCIPAL :

lance_pierre_1 = LancePierre()

"""
Comme la méthode tirer est une fonction d'instance, 
on utilise cette syntaxe :
"""

if (lance_pierre_1.tirer(15)) == True :
    print("Autre joueur touché ! Quelle précision !")

"""
sortie au terminal :

Fabrication d'un lance pierre...

BAM ! Un joueur a tiré un projectile avec une force de 15 !
Autre joueur touché ? True
Autre joueur touché ! Quelle précision !
"""