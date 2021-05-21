#coding:utf-8

"""
La gestion d'erreur est nécessaire pour perfectionner 
notre programme et prendre toutes les précautions pour 
que notre programme se comporte bien durant sont 
utilisation. Pour l'exemple, on va faire un programme qui 
prend un entier de l'utilisateur et retourne son carré :
"""

print("\n_____AUCUNE SECURITE_____\n")

nombre_user = input("Votre nombre : ")
# Je rappelle que input retourne une chaîne de caractère
nombre_user = int(nombre_user)
# On change la chaîne de caractères en entier

print("Votre nombre au carré :", nombre_user * nombre_user)

"""
Sortie au terminal :

Votre nombre : 4
Votre nombre au carré : 16

On peut voir que le programme c'est bien comporté, mais 
voici ce qui arrive quand on ne prévoit pas le fait que 
l'utilisateur entre autres choses que des caractères 
représentant des chiffres : 

sortie au terminal :
(J'ai coupé une partie du chemin car cela créer des problèmes.)

Votre nombre : G
Traceback (most recent call last):
  File "\aide\divers\gestion d'erreurs\gestion_erreurs.py", line 15, in <module>
    nombre_user = int(nombre_user)
ValueError: invalid literal for int() with base 10: 'G'

L'interpréteur me dit que 'G' n'est pas une valeur qui peut
passer dans un cast d'int, et je n'ai malheureusement pris aucune 
précaution contre ces cas car il faut absolument vérifier 
des informations qui sont récupérées que ce soit pas des 
utilisateurs, des bases etc car c'est dans ces cas là qu'on 
rencontre des erreurs de sécurité. Je vais maintenant 
commencer à prendre des précautions en utilisant une 
première technique qui est le try exept, ce qui est le 
strict minimum dans la gestion d'erreur :
"""

print("\n_____TRY, EXCEPT, ELSE ET FINALLY_____\n")

nombre_user = input("Votre nombre : ")

try :
# essaie les prochaines intructions :
    nombre_user = int(nombre_user)
except :
# Si tu rencontres une exeption, fait les prochaines intructions
    print("Vous n'avez pas précisez un nombre !")
else :
# Sinon, fait ces instructions : 
    print("Votre nombre au carré :", nombre_user * nombre_user)
finally :
# Mais dans peu importe ce qui se passe, exectutes ces instructions :
    print("\nFin du programme. Au revoir.")

"""
Dans ce cas, on a qu'une seule instructions à essayer 
et elle ne peut provoquer qu'un seule type d'erreur 
(je crois) donc on n'a eu qu'à préciser un seul message 
d'erreur. Si on met plusieurs instructions ou qu'une 
instructions peut occasionner plusieurs type d'erreurs, 
on peut préciser le type d'erreur et cumuler les except :
"""

print("\n_____PRECISIONS TYPES ERREURS ET ACCUMULATIONS EXCEPT_____\n")

age_user = input("Entrez votre âge qui sera divisé : ")
diviseur = input("Entrez le diviseur : ")

try :
    age_user = int(age_user)
    diviseur = int(diviseur)
    resultat = age_user / diviseur
    print("{} / {} = {}".format(age_user, diviseur, resultat))

# On sait donc que les erreurs qui peuvent survenir sont :
# - une division par zero si l'utilisateur rentre 0 pour le diviseur,
# - une erreur de valeur si l'utilisateur ne rentre pas de chiffre.
# 
# On peut donc commencer à prendre nos mesures en précisant 
# nous même les types d'erreurs que l'on a listé et en cumulant 
# les except :

# Chaque type d'erreurs à son code, et on peut l'utiliser :
except ValueError :
    print("Vous n'avez pas enter les bonnes valeurs !")
except ZeroDivisionError :
# Par exemple ici, la division par zéro.
    print("Vous ne pouvez pas diviser par 0 !")
except :
# On met un dernier except pour d'autres types d'erreurs que l'on aurait oubliées
    print("Valeur incorrecte !")
finally :
    print("\nFin du programme.\n")

"""
On n'est pas obligé de retenir les noms de tous les types 
d'exeptions mais en voici certains :
(Je pense que je vais étoffer la liste au fil du temps)

- ValueError
- NameError si on indique une variable qui n'existe pas
- TypeError pour des problèmes de types de variables
- ZeroDivisionError si on divise par 0
- OSError s'il y a des problème avec le système
- AssertionError
"""