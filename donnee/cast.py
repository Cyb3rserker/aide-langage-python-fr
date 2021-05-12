#coding:utf-8

"""
Dans certaines situations, on peut avoir besoin de changer le type de donnée d'une variable
pour effectuer une opérations par exemple, et dans ce cas on "cast" la variable,
c'est à dire qu'on la convertie pour que l'interpréteur considére la variable autrement.
Voici un exemple :
"""

age_majorite = 18
age_majorite2 = "18"

# double_age_majorite = age_majorite + age_majorite2

"""
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
