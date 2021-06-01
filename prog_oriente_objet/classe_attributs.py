#coding:utf-8

"""
Les classes sont des plans de "construction", de conception 
d'objet (ex : une classe lance-pierre avec une corde et un 
morceau de bois). Un attibuts est une variable appartenant 
à une classe.
Un objet est un "exemplaire", une instance d'une classe 
(ex : le lance-pierre A, le lance pierre B...). 
Les différents mots clés sont :

    - class    : permet de définir une classe
    - __init__ : mot clé qui désigne le "constructeur" de 
                 la méthode
    - self     : en argument de méthode, permet d'identifier 
                 l'objet que l'on est en train de créer, de 
                 le retourner et de lui appliquer ladite 
                 méthode en lui même et de le retourner


Voici un exemple d'utilisation avec un lance-pierre :
"""

# Pour définir une classe, on utilise cette syntaxe :
class LancePierre :
    """
    Par convention, on nomme les classe avec une majuscule pour 
    chaque mots. Généralement, on utilise des commentaires de 
    cette forme pour donner des informations sur la classe 
    (attention à bien indenter dans la définition de la classe 
    car cette oublie causerai des erreurs) donc dans notre cas, 
    ce serai :

    classe de lance pierre

    différents attributs autorisés :
    (ATTENTION !!! Je n'y connais rien en lance pierre. C'est juste 
    un exemple qui m'a paru bien pour les explications donc ce qui 
    peut être mis dans mon code peut parraître totalement incensé 
    dans la vie réelle.)

        - taille de la corde : en millimètre 
            - "TRES PETIT"
            - "PETITE"
            - "MOYENNE"
            - "GRANDE"
            - "TRES GRANDE"

        - taille du baton :
            - "TRES PETIT"
            - "PETIT"
            - "MOYEN"
            - "GRAND"
            - "TRES GRAND"
            
        - couleur de la corde :
            - "VERTE"
            - "JAUNE"
            - "ROUGE"
            - "BLEUE"

        - projectile : 
            - "CAILLOU"
            - "BILLE"
            - "BALLE"
            - "FLECHE"

    On peut rajouter des informations au fur et à mesure du 
    développement.
    
    On peut aussi faire des variables qui sont propres à des classes et 
    pas des objets :
    """

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

"""
Maintenant que l'on a notre plan de conception, on va pouvoir 
instancier un objet :
"""

print("Lancement du programme...")

lance_pierre_1 = LancePierre()
lance_pierre_2 = LancePierre()
# On fait appel à la classe LancePierre où se trouve la méthode init
"""
sortie au terminal :

Lancement du programme...
Fabrication d'un lance pierre...

Fabrication d'un lance pierre...
"""

"""
Pour accéder à l'attribut d'un objet, j'utilise cette syntaxe :
dans mon cas, imaginons que je veuille accéder à la taille du baton 
de lance_pierre_1 pour pouvoir l'afficher. Je vais devoir faire :
"""

print("taille baton lance_pierre_1 -> {}".format(lance_pierre_1.taille_baton))
print("Nombre lance pierre : {}".format(LancePierre.nombre_lance_pierre))
"""
sortie au terminal :

taille baton lance_pierre_1 : MOYEN
Nombre lance pierre : 2
"""

"""
On met le nom de l'objet, puis un point, puis la donnée à laquelle 
on veut accéder. On utilise la même syntaxe pour la modification de 
cette donnée :
"""

lance_pierre_1.taille_baton = "GRAND"
print("taille baton lance_pierre_1 -> {}".format(lance_pierre_1.taille_baton))

"""
sortie au terminal :

taille baton lance_pierre_1 : GRAND
"""

"""
Dans l'exemple précédent, je créé des valeurs par défauts mais je peux 
aussi définir ces valeurs comme je définis les  
arguements dans les fonctions. Elles peuvent être 
définies par des variables que j'aurai choisi, 
que l'utilisateur a choisies, elles peuvent être 
plusieurs voir même avoir une infinités de paramètres.
Pour illustrer ceci, je vais créer une class personnage :
"""

class Personnage :
    # Il faut toujours mettre le self en premier et il ne sera pas 
    # compté dans l'ordre de la saisie des paramètres.
    def __init__(self, c_nom = "_DEFAUT_", c_taille_cm = "170", c_force = "50") :
    # Je met c_ devant les paramètres pour qu'on sache que ce sont des 
    # paramètres de classe et j'ai aussi mis des paramètres par défaut.
    # On peut aussi renseigner les arguments dans le désordre lors d'une 
    # instance mais on peut déjà le voir dans aide/fonction/fonctions.py
    # et je ne vais pas allourdir plus le code.
        print("\nCréation d'un personnage...\n")
        self.nom = c_nom
        self.taille_cm = c_taille_cm
        self.force = c_force

print("\n(ATTENTION ! Pas de vérification de cast, ceci est un programme d'exemple.)\n")

nom_saisi = input("Nom personnage : ")
taille_saisie = int(input("Taille personnage (cm) : "))
force_saisie = int(input("Force personnage : "))

personnage_1 = Personnage(nom_saisi, taille_saisie, force_saisie)

print("Nom : ", personnage_1.nom)
print("Taille : ", personnage_1.taille_cm)
print("Force : ", personnage_1.force)

"""
sortie au terminal : 

Nom personnage : Jojo
Taille personnage (cm) : 195
Force personnage : 1000

Création d'un personnage...

Nom :  Jojo
Taille :  195
Force :  1000
"""