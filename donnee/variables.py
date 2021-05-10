#coding:utf-8

"""
Le langage python utilise un typage dynamique.
Cela signifie que lors de la création de variables,
on ne doit pas préciser le type de variables qui
sera acceptées, contrairement au langage c.

Les différentes règles pour définir une variable :
    - doit commencer par une lettre
    - ne pas contenir de caractères spéciaux (%, é...)
    - ne pas contenir d'espaces mais on peut utiliser des underscore (_)
    - (pas vraiment une règle mais) faire des noms de variables très explicites
    pour pouvoir se retrouver dans le code source.

Les différents types de données standard :
    - entier numérique (int)
    - nombre flottant (float)
    - chaîne de caractères (str)
    - booléen (bool) qui ne peut avoir que deux valeurs (vrai / faux, 0 / 1...)
"""

"""
-----------------------------------
INITIALISATION DE BASE DE VARIABLES
-----------------------------------
"""

age_majorite = 18
# Le "=" permet d'affecter une valeur à une variable.
"""
On peut voir ici que dans la définition de ma variable, j'ai utilisé des _
pour symboliser les espaces et je n'ai pas utilisé les caractères avec un accent.
On peut voir aussi que, contrairement au langage c, je n'ai pas à préciser le
type de données de la variables car c'est l'interpréteur qui va le faire.
Cette variable étant implicitement du type int, on peut faire des calculs avec
ou des opérations mais on ne peut pas l'utiliser comme un texte :
age_majorite = 18 et age_majorite = "18" ne sont pas les même choses car le premier
contient un entier et le deuxième contient une chaîne de caractères (un texte) et on peut
le remarquer grâce aux "" lors de l'affectation de valeurs. On peut vérifier le type
de donnée de la variables grâce à une fonction s'appelant type :
"""
age_majorite2 = "18"

print("age_majorite :", age_majorite)
print(type(age_majorite), "\n")
# (je rajoute le "\n" seulement pour plus de clareté dans le terminal)
print("age_majorite2 :", age_majorite2)
print(type(age_majorite2), "\n")
# Pour comprendre print, voir "print.py" dans aide/fonction/affichage
"""
On peut voir que la sortie au terminal est :

    age_majorite : 18
    <class 'int'>

    age_majorite2 : 18
    <class 'str'>
"""

# Il y a aussi les nombres flottants (à virgule) :
taille_patient_m = 1.82
print("taille_patient_m :", taille_patient_m)
print(type(taille_patient_m), "\n")
"""
sortie au terminal :

taille_patient_m : 1.82
<class 'float'>
"""

# Aussi les booléens qui sont des données avec seulement deux valeurs possibles :
choix_utilisateur = True
# (On ne peut affecter que "True" et "False")
print("choix_utilisateur :", choix_utilisateur)
print(type(choix_utilisateur), "\n")
"""
sortie au terminal :

choix_utilisateur : True
<class 'bool'>
"""

"""
Il existe encore plein de type de données comme les nombre hexadécimaux, les nombres
octaux, les long etc mais je ne peux pas tous les listées ici pour l'instant. Je les
rajouterai sûrement au fur et à mesure que je les utilise.
"""

"""
---------------
FORMATAGE TEXTE
---------------
"""

"""
Avec des variables de texte, on peut faire ce qu'on appelle un formatage. En effet,
On peut initialiser une variable de texte avec des "emplacements" que l'on pourra
remplir avec des variables ou des valeurs, et on utilise cette syntaxe :
"""

texte = "L'âge du patient est {} ans et sa taille est de {} m"

print(texte.format(age_majorite, taille_patient_m))
print(texte, "\n")
"""
sortie terminal :

L'âge du patient est 18 ans et sa taille est de 1.82 m
L'âge du patient est {} ans et sa taille est de {} m
"""

"""
En utilisant "format" (les explications seront sûrement dans un autre fichier), on
demande à l'interpréteur de remplacer les {} que l'on a mises par les variables que
l'on met entre parenthèse (ici age_majorite et taille_patient_m).
"""

# On peut aussi coder en dur et sans variable texte avec cette syntaxe là :

print("La taille du patient est {} m et il est âgé de {} ans".format(taille_patient_m, age_majorite), "\n")
"""
sortie au terminal :

La taille du patient est 1.82 m et il est âgé de 18 ans
"""

"""
Pour la saisie d'information et l'affectation à des variables,
voir aide/fonction/lecture_donnees
"""

"""
On peut parfois avoir le besoin de changer le type de donnée d'une variable pour effectuer une
opérations par exemple, et dans ce cas on "cast" la variable, c'est à dire qu'on la convertie.
Voici un exemple :

double_age_majorite = age_majorite + age_majorite2

Ce calcul est impossible car on tente d'additionner un entier avec une chaîne de caractères.
Si on veut additionner les deux variables, il faut les caster :
"""

double_age_majorite = age_majorite + int(age_majorite2)
# (On additionne un entier avec un entier donc double_age_majorite sera un entier)
print("Le double de l'âge de la majorité est", double_age_majorite, "ans.\n")
"""
sortie au terminal :

Le double de l'âge de la majorité est 36 ans.
"""

"""
Il existe autant de cast que de type de donnée comme :
- int(),
- float(),
- str(),
- bool()
- et plein d'autres encore.
"""

"""
ATTENTION !!! Le cast ne change pas le type de donnée de la variable définitivement, elle est
juste interprétée différement lorsqu'on la cast.
"""
