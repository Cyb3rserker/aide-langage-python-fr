#coding:utf-8

"""
Les boucles en python, et dans la programmation en 
générale, servent à reproduire plusieurs une ou plusieurs
actions. Voici un exemple :
Je veux afficher plusieurs fois une variable dans le 
terminal et à chaque affichage, cette variable augmente de
+1 en valeur :
"""

variable = 1
print(variable)
variable+=1
print(variable)
variable+=1
print(variable)
variable+=1
print(variable)
variable+=1
print(variable)

"""
sortie au terminal :

1
2
3
4
5
"""

"""
Cette manière de coder n'est pas du tout pratique et ne rend 
pas le code plus lisible. Pour automatiser cette tâche, on 
utilise alors une boucle. Il en existe de plusieurs types, 
mais on va commencer par la boucle while, qui peut se traduire 
par "tant que {condition} est vraie, alors faire cette partie 
du programme" :
"""

print("\n_____WHILE_____\n")

compteur = 0

while compteur < 5 :
# ATTENTION !!! les ordinateurs commencent à compter à partir de 0
# et ici c'est SCRICTEMENT plus petit que 5, donc il n'est pas inclu.
    print(compteur)
    compteur+=1
    # (attention à changer la variable du compteur sinon ça fera une 
    # boucle infinie)

"""
sortie au terminal :
0
1
2
3
4
"""

"""
On peut voir que 5 valeurs sont affichées mais qu'elles vont de 0 à 
4. Pour afficher les valeurs de 1 à 5, on aurai pu faire comme 
ça :

compteur = 1

while compteur <= 5 :
    print(compteur)
    compteur+=1

et la sortie au terminal serai comme ça :
1
2
3
4
5
"""

# On peut voir que c'est beaucoup plus optimisé et pratique avec beaucoup 
# moins de ligne de code.

"""
On peut faire plusieurs sortes de manipulations dans les boucles while 
(et celles de la suite du programme) avec les mots clés suivant :

    continue : si le programme atteint ce mot clé, la boucle revient 
    au tout début et, bien sûr, ne s'exectute que si la condition est vraie.

    break : si le programme atteint ce mot clé, la boucle s'arrêtera 
    (break = casser)

Voici quelques exemples d'utilisation :
"""

print("\n_____CONTINUE ET BREAK_____\n")

"""
On va faire un jeu qui demande l'âge de l'utilisateur en années 
puis le programme le lui donne en mois et en jours (oui c'est nul) :
"""

while 1 :
# (1 est toujours vrai)
    age_user = int(input("Quel est votre âge ? "))
    print("Vous êtes âgé de {} mois, soit {} jours.".format(age_user * 12, age_user * 365))

    choix_menu = input("Continuer ? (O / N)\n> ")

    if choix_menu == 'O' :
        continue
        # On retourne directement au début de la boucle

    elif choix_menu == 'N' :
        print("D'accord. A bientôt.")
        break
        # On "casse" la boucle
    else :
        print("Commande introuvable.")
        # On sait jamais.

"""
Il y a aussi un autre type de boucles, qui sont les for.
Les boucles for créent une varibales temporaire qui prendra la 
valeur de chaque objet d'un ensemble et une fois arrivé à la fin de 
l'ensemble, la boucle s'arrête : 
(A mettre à jour lorsque j'aurai plus de notions.)
"""

print("\n_____FOR_____\n")
# Prenons un ensemble de lettre, donc une phrase :

phrase = "Je suis une phrase."

for letter in phrase :
    print(letter)

"""
sortie au terminal :

J
e

s
u
i
s

u
n
e
 
p
h
r
a
s
e
.
"""