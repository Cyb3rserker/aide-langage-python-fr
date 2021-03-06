#coding:utf-8

"""
Les méthodes sont des fonctions qui soit agissent sur 
une instance d'une classe (méthode), soit agissent sur 
la classe elle même (méthode de classe) ou soit sont 
décritent dans une classe mais qui peuvent être utilisées 
sur n'importe quoi (à condition de préciser de quelle 
classe elle vient). Comme les méthodes sont comme des 
fonctions, elles ont aussi des arguments mais il y en a des 
spéciaux :

- self : la méthode agit sur l'objet en lui même
- cls  : la méthode agit sur la classe

Pour les explications, je vais prendre les mêmes classes 
que classe_attributs.py.
"""

"""
Exceptionnellement, je définis les classes au fur et à mesure 
du programme et pas au début car cela sera plus pratique pour
les exemples que je vais présenter.
"""

# METHODES :
print("\n_____METHODES CLASSIQUES_____\n")

class LancePierre :
    # ici exceptionnellement, je n'ai pas mis de documentation 
    # parce que je ne veux pas allourdir encore le fichier. La 
    # documentation se trouve dans classe_attributs.py 
    
    nombre_lance_pierre = 0

    def __init__(self): 
        print("Fabrication d'un lance pierre...")
        print()
        # (pour sauter je ne pense sdjf jr une ligne)

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

# METHODE DE CLASSE :
print("\n_____METHODES DE CLASSE_____\n")

"""
Les méthodes de classe sont des fonctions qui n'auront pas un impact 
sur l'objet seulement, mais sur toute la classe. Dans l'exemple suivant, 
je vais définir une méthode de classe qui va changer la race de tous les 
personnages du jeu :
"""

class Personnage :
    race_personnages = "Humain"

    def __init__(self, c_nom = "_DEFAUT_", c_taille_cm = 170, c_force = 50) :
        print("\nCréation d'un personnage...\n")
        self.nom = c_nom
        self.taille_cm = c_taille_cm
        self.force = c_force
        print("Nouveau personnage créé !\nNom : {}\nTaille : {}\nForce : {}\n".format(self.nom, self.taille_cm, self.force))

    # Au lieu d'utiliser le mot "self" pour agir sur un objet, on va 
    # utiliser le mot "cls" qui est une abréviation de "class"
    def changer_race_persos(cls, c_nouvelle_race) :
        Personnage.race_personnages = c_nouvelle_race
        # Attention à bien préciser le nom de la classe avant de faire référence 
        # à sa variable car sinon elle sera considérée comme nouvelle et totalement 
        # différentes !
    """
    Maintenant notre méthode est créée, mais celle-ci est encore 
    considérée comme une méthode standard par python. On va donc 
    faire les instructions suivantes :
    """

    changement_race_joueurs = classmethod(changer_race_persos)
    """
    Désormais, la méthode de classe est bien définie et elle porte le nom 
    de "changement_race_joueur" (on peut donner le même nom que la méthode 
    considérée comme standard à la méthode de classe, je ne l'ai pas fait 
    pour montrer que ce n'est pas obligé).
    """

personnage_1 = Personnage("Jojo", 195, 1000)

print("Race des joueurs présent dans la partie :",personnage_1.race_personnages)

Personnage.changement_race_joueurs("Cyborg")

print("Race des joueurs présent dans la partie :",personnage_1.race_personnages)

"""
sortie au terminal :

Création d'un personnage...

Nouveau personnage créé !
Nom : Jojo
Taille : 195
Force : 1000

Race des joueurs présent dans la partie : Humain
Race des joueurs présent dans la partie : Cyborg
"""


# METHODES STATIQUES : 
print("\n_____METHODES STATIQUES_____\n")

"""
Les méthodes statiques sont des méthodes qui sont liées à une 
classe, mais qui sont indépendante de celle-ci. Cela permet de les 
catégoriser pour avoir un programme organisé. Pour l'exemple, je vais 
faire une classe qui rassemble les méthodes en rapport avec des 
annonces sur un chat général :
"""

class AnnonceSurChat :
    def serveur_en_maintenance(c_heure_debut_maintenance, c_heure_fin_maintenance) :
        print("\nLe serveur sera en maintenance de {}h à {}h.\n".format(c_heure_debut_maintenance, c_heure_fin_maintenance))

    serveur_en_maintenance = staticmethod(serveur_en_maintenance)
    # On utilise cette syntaxe, comme pour les méthodes de classes

    def serveur_plus_en_maintenance() :
        print("\nLe serveur n'est plus en maintenance.\n")

    serveur_plus_en_maintenance = staticmethod(serveur_plus_en_maintenance)

    def arrivee_nouveau_membre(c_nom_nouveau_membre) :
        print("\n{} vient de rejoindre le chat !\n".format(c_nom_nouveau_membre))

    arrivee_nouveau_membre = staticmethod(arrivee_nouveau_membre)

    def depart_membre(c_nom_membre_parti) :
        print("{} vient de quitter le chat.\n".format(c_nom_membre_parti))

    depart_membre = staticmethod(depart_membre)


"""
Ces définitions de méthodes statiques me permettent de les
catégoriser lors de l'écriture du code source :
"""
AnnonceSurChat.serveur_en_maintenance(14, 17)
AnnonceSurChat.serveur_plus_en_maintenance()
AnnonceSurChat.arrivee_nouveau_membre("xX_NoobSlayer999_Xx")
AnnonceSurChat.depart_membre("xX_NoobSlayer999_Xx")

"""
sortie au terminal :

Le serveur sera en maintenance de 14h à 17h.


Le serveur n'est plus en maintenance.


xX_NoobSlayer999_Xx vient de rejoindre le chat !

xX_NoobSlayer999_Xx vient de quitter le chat.
"""