#coding:utf-8

"""
En python, comme en mathématiques, il y a des opérateurs qui nous permettent de faire des
calculs comme +, - ou /. Les opérations garde le même sens de priorité que dans les maths
classiques. Les différents opérateurs en python, et dans la programmation en générale, sont :
    + pour l'addition
    - pour la soustraction
    * pour la multiplication
    / pour la division (entraîne des erreurs si on essaie de diviser par 0)
    % (modulo) pour donner le reste d'une division Euclidienne
        ex : 10 % 8 = 2
        il peut être très utile et peut notament servir à savoir si un nombre est pair ou
        pas par exemple :
        si ma_variable % 2 n'est pas égal à 0, alors...
        (le reste d'une division Euclidienne d'un nombre pair par 2 est forcément nul)
    ** pour une puissance.
       Exemple :
            2 ** 3 = 8
            10 ** 6 = 1 000 000

On peut utiliser les opérateurs pour changer la valeurs d'une variables ) :
"""
ma_variable = 5
ma_variable = ma_variable + 1
# ma_variable sera alors égal à 6.

# On peut aussi utiliser une autre syntaxe :

ma_variable += 1
# Ici, ma_variable est égal à 7

"""
C'est une syntaxe équivalent qui fait exactement la même chose que les lignes
au dessus et on peut le faire avec tous les opérateurs :
"""
ma_variable *= 2
# Ici, ma_variable est égal à 14
