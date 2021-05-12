#coding:utf-8

"""
input est une fonction qui permet de saisir des inforamtions et de pouvoir
les utiliser ensuite.
"""

age_utilisateur = input("Veuillez saisir votre âge : ")
# Bien penser à affecter la saisie à une variable sinon la saisie sera perdue
print("Vous avez", age_utilisateur, "ans")

"""
La fonction input va afficher le texte que l'on lui met entre parenthèses puis
renvoyer une chaîne de caractères qui sera la saisie de l'utilisateur, donc la variable
age_utilisateur sera la valeur que l'utilisateur a saisie. D'ailleurs,
on sait que c'est une chaîne de caractères car lorsque l'on met cette
ligne dans notre programme :
"""
print(type(age_utilisateur), "\n")
"""
la sortie au terminal est :
<class 'str'>
"""

"""
Le fait que la fonction input revoie une chaîne de caractères peut poser problème si
on veut faire des opérations ou autres, et c'est pour ça que l'on utilise les casts
qui sont expliquées dans aide/donnee/cast.py . Donc pour affecter directement le
type de donnée que l'on veut à une variable, on fait cela :
"""

age_utilisateur2 = int(input("Veuillez saisir votre âge à nouveau :"))
# (input renvoie un str et int le convertie en int, donc age_utilisateur2 est un int)
"""
On peut aussi utiliser cette méthode :
age_utilisateur2 = input("Veuillez saisir votre âge à nouveau :")
age_utilisateur2 = int(age_utilisateur2)
"""

annee_naissance_utilisateur_2021 = 2021 - age_utilisateur2

print("Votre année de naissance est ", annee_naissance_utilisateur_2021, ".\n")
# On a put faire nos opérations grâce au cast qui a changé la chaîne de caractères en entiers.
