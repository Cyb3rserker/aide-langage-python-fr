"""
En python, on peut avoir ce que l'on appelle une classe 
mère avec une class fille qui hérite de la classe mère et 
qui sont plus spécialisées.
"""

#coding:utf-8

# Définition des classes :
class Animal :
    """
    Documentation de Animal :
    une classe qui représente des animaux.
    Ses différents attributs sont :
        - c_nom_animal : Ce que l'on veut
        - c_etat       :
            - "HOSTILE"
            - "DOCILE"
    """

    def __init__(self, c_nom_animal, c_etat_animal) :
        self.nom = c_nom_animal
        self.etat = c_etat_animal

    def description_etat_animal(self) :
        if self.etat == "HOSTILE" :
            print(f"{self.nom} est hostile.")

        elif self.etat == "DOCILE" :
            print(f"{self.nom} est docile.")

    def annonce_nom_animal(self) :
        print(f"Nom : {self.nom}")

"""
Dans la définition d'une classe fille, on met le nom de la classe 
mère entre les parenthèses de la classe. Ici, on dit que Chien est 
une sorte de Animal ou encore que Animal est la super classe de 
Chien. La classe fille possède tous les attributs et méthodes de 
sa super classe, et donc dans notre cas la classe Chien possède 
non seulement les attributs race et taille, mais aussi les 
attributs nom et etat et de la méthode description_etat_animal. Il
est aussi possible d'avoir une classe petite fille, arrière petite 
fille etc mais je ne pense pas que je vais le montrer dans ce fichier 
car le principe reste le même.
"""
class Chien(Animal) :
    """
    Documentation de Chien :
    Une classe fille de Animal qui permet d'instancier des 
    chiens.
    Les attributs de sa classe mère Animal :
        - c_nom_animal : Ce que l'on veut
        - c_etat       :
            - "HOSTILE"
            - "DOCILE"

    Ses nouveaux attributs sont :
        - c_race : Ce que l'on veut
        - c_taille : 
            - "PETIT"
            - "MOYEN"
            - "GRAND"
    """
    
    """
    La classe fille doit avoir les mêmes arguments que la classe 
    mère dans son constructeur. Il n'est pas obligatoire que ceux 
    de la classe mère et ceux de la classe fille aient le même nom
    voir le même ordre mais il faut qu'ils soient présents :
    """
    def __init__(self, c_nom_chien, c_etat_chien, c_race_chien, c_taille_chien) :
        """
        Dans le constructeur de la classe fille, on ne va pas 
        initialiser les attributs déjà présents dans la classe 
        mère car le constructeur le la classe mère va le faire :
        """

        # On appel le constructeur de Animal avec les attributs de Chien.  
        Animal.__init__(self, c_nom_chien, c_etat_chien)

        # Les nouveaux attributs que l'on créé s'initialisent 
        # de la manière suivante :
        self.race_chien = c_race_chien
        self.taille_chien = c_taille_chien
    
    def annonce_taille_chien(self) :
        if self.taille_chien == "PETIT" :
            print(f"{self.nom} est un petit chien.")

        if self.taille_chien == "MOYEN" :
            print(f"{self.nom} est un chien de moyenne taille.")

        if self.taille_chien == "GRAND" :
            print(f"{self.nom} est un grand chien.")

    """
    On peut aussi redéfinir des méthodes de la classe mère pour la 
    classe fille. Ces méthodes ne seront différentes que quand on les 
    utilisera à partir d'un objet de la classe fille, dans notre cas 
    un chien :
    """

    # On met exactement le même nom que la méthode originelle.
    def description_etat_animal(self) :
        if self.etat == "HOSTILE" :
            print(f"{self.nom} est un chien hostile.")

        elif self.etat == "DOCILE" :
            print(f"{self.nom} est un chien docile.")
    
    """
    Au niveau de l'exectution, l'interpréteur python va parcourir les 
    classes du plus bas de la hiérarchie au plus haut pour trouver la 
    méthode que l'on emploira dans le code jusqu'à la trouver. Cela 
    veut dire que si j'ai un objet appartenant à une classe fille de 
    Chien se nommant BergerAllemand, et donc petit fille de Animal, 
    l'interpréteur va utiliser la méthode description_etat_animal 
    que j'ai redéfinie dans la classe Chien.
    """ 


# Programme principal :

animal_1 = Chien("Médor", "DOCILE", "golden retriever", "GRAND")
animal_2 = Animal("Mia", "DOCILE")

animal_1.annonce_nom_animal()
animal_1.annonce_taille_chien()
animal_1.description_etat_animal()
animal_2.description_etat_animal()
"""
sortie au terminal :

Nom : Médor
Médor est un grand chien.
Médor est un chien docile.
Mia est docile.
"""

"""
On peut bien voir que l'objet animal_1 possède ses attributs et aussi 
de sa classe mère Animal. On peut aussi voir qu'il peut utiliser les 
méthodes de sa classe et de la classe Chien et que la méthode que l'on 
a redéfinie, descritption_etat_animal, a un comportement différent 
différent pour ces objets de classe différentes.
"""

"""
On peut donc créer des classes filles autant que l'on veut. J'aurais pu 
faire une classe Chat, Dauphin, Lezard etc.
"""

"""
Il existe aussi quelques fonctions qui concernent les classes et 
qui sont très utile en programmation orienté objet. Je vais donner 
l'explications de chaque fonction, puis un exemple, puis encore une 
autre fonction :
"""

print("\n_____DIFFERENTES FONCTIONS UTILES :_____")

print("\n___ISINSTANCE___\n")
"""
- isinstance(<variable_ou_objet_a_verfier>, <classe>) :
    cette fonction permet de vérifier si une variable est une 
    instance de la classe renseignée. Cette fonction revoie une valeur 
    booléenne, soit True soit False.
"""


print("Est-ce que animal_1 est un objet de la classe Chien ?")

if (isinstance(animal_1, Chien)) == True :
    print("Oui.")
elif (isinstance(animal_1, Chien)) == False :
    print("Non.")
"""
sortie au terminal :

_____DIFFERENTES FONCTIONS UTILES :_____

___ISINSTANCE___

Est-ce que animal_1 est un objet de la classe Chien ?
Oui.
"""

"""
Cela marche aussi avec des super classes car, en soit, les objets 
de la classe fille sont juste des objets de la classe mère mais avec
des fonctionnalités en plus. D'ailleurs, on peut le comprendre car 
il y a le constructeur de la classe mère dans une classe fille.
"""

print("Est-ce que animal_1 est un objet de la classe Animal ?")

if (isinstance(animal_1, Animal)) == True :
    print("Oui.")
elif (isinstance(animal_1, Animal)) == False :
    print("Non.")
"""
sortie au terminal :

Est-ce que animal_1 est un objet de la classe Animal ?
Oui.
"""

print("\n___ISSUBCLASS___\n")
"""
- issubclass(<présumée_class_fille>, <présumée_class_mere>) :
    Cette fonction permet de vérifier si une classe est bien 
    fille d'une autre classe. Elle renvoie aussi une valeur 
    booléenne.
"""

print("Est-ce que la classe Animal est une classe fille de la classe Chien ?")

if issubclass(Animal, Chien) == True :
    print("Oui.")
elif issubclass(Animal, Chien) == False :
    print("Non.")

print("Est-ce que la classe Chien est une classe fille de la classe Animal ?")

if issubclass(Chien, Animal) == True :
    print("Oui.")
elif issubclass(Chien, Animal) == False :
    print("Non.")


"""
Sortie au terminal :

___ISSUBCLASS___

Est-ce que la classe Animal est une classe fille de la classe Chien ?
Non.
Est-ce que la classe Chien est une classe fille de la classe Animal ?
Oui.
"""