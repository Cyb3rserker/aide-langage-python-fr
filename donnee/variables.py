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
contient un entier et le deuxième contient un texte et on peut remarquer grâce aux "" lors
de l'affectation de valeurs. On peut vérifier le type de donnée de la variables grâce à
une fonction s'appelant type :
"""
age_majorite2 = "18"

print(type(age_majorite))
print(type(age_majorite2))
# Pour comprendre print, voir "print.py" dans aide/fonction/affichage
"""
On peut voir que la sortie au terminal est :
    <class 'int'>
    <class 'str'>
