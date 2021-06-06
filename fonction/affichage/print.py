#coding:utf-8

"""
La fonction print est une fonction de base du python qui permet
d'afficher du contenu sur le terminal ou quelqu'autres canals de
sortie (canal de sortie ~= là où sortent les inforamtions du programme).
On peut afficher du texte, des données et autres.
"""

print("\n_____AFFICHAGE BASIQUE ET RETOUR A LA LIGNE_____\n")
print("Je suis une ligne qui sera afficher dans le terminal.")
# On met le texte que l'on veut afficher entre parenthèse.

# Lorsque l'on affiche des phrases, on peut faire des retours à la ligne :

print("Je suis aussi une phrase qui sera dans le terminal\nEt moi une qui sera retournée à la ligne.")
# Comme on peut le voir, on utiliser "\n" pour faire un retour à la ligne (comme en langage c).

"""
La sortie (output) sera :
Je suis aussi une phrase qui sera dans le terminal
Et moi une qui sera retournée à la ligne.
"""
"""
Attention ! il ne faut pas mettre d'espace après le \n car il sera compté pour la ligne d'en
dessous et cela donnera :
Je suis aussi une phrase qui sera dans le terminal
 Et moi une qui sera retournée à la ligne.
"""

print("\n_____AFFICHAGE DE VARIABLES SANS ET AVEC TEXTE_____\n")
"""
On peut aussi afficher des variables
(voir aide/donnees/variables.py) de la manière suivante :
"""

age_majorite = 18
pas_age_majorite = 22

print(age_majorite)
print(pas_age_majorite)

"""
Cela affichera cela dans le terminal :
18
22
"""

"""
Pour afficher des variables avec du texte, on met notre morceau
de phrase entre guillemets puis une virgule pour séparer
les arguments(= ce qui se trouve entre parenthèses) puis
on met nos variables. On peut le faire plusieurs fois de
suite dans un print :
"""


print("L'age de la majorité est", age_majorite, "ans en France et pas", pas_age_majorite, "ans")

"""
ATTENTION !!! Cette syntaxe ne marche que pour python3,
la version la plus récente à l'heure où j'écrit ce texte
(07/05/2021).
Il faut bien penser à mettre "python3 print.py" dans le
terminal pour que cette syntaxe marche. Si on utilise
python tout court alors il faut utiliser cette syntaxe
là qui est sans les parenthèses :

print "L'age de la majorité est", age_majorite, "ans en France et pas", pas_age_majorite, "ans"
"""

print("\n_____AFFICHAGE DE VARIABLES DANS DU TEXTE FORAMTE_____\n")
"""
Ceci n'est pas la seule manière d'afficher du texte avec des variables. En effet, on peut
afficher du texte formaté, c'est à dire du texte qui aura du contenu remplacé par des variables,
du texte et autres en utilisant cette syntaxe (je reviendrai sûrement pour mieux expliquer cette
syntaxe) :
"""
print("L'age de la majorité est {} ans en France et pas {} ans".format(age_majorite, pas_age_majorite))
# Les accolades seront remlacés par les variables.
"""
A partir de python 3.6, on peut utiliser une syntaxe beaucoup 
compréhensible pour afficher des variables dans une chaîne de 
caractères :
"""
print("(Avec la nouvelle syntaxe : )")
# On met f pour montrer que l'on fait un formatage puis 
# on met le nom des variables dans les accolades :
print(f"L'age de la majorité est {age_majorite} ans en France et pas {pas_age_majorite} ans")

# On peut aussi le faire avec des variables de textes :

texte = "L'age de la majorité est {} ans en France et pas {} ans"
print(texte.format(age_majorite, pas_age_majorite))

print("\n_____AFFICHAGE RETOUR FONCTION_____\n")
"""
On peut aussi afficher le résultat de fonction. Pour cette
exemple, on va utiliser la fonction "type" qui permet de
connaître le type de donnée d'une variable
(voir aide/donnees/variables.py pour avoir des renseignements sur les variables en python et
aide/fonction/affichage/type.py pour avoir des renseignements sur la fonction) :
"""
print(type(age_majorite))
print(type(pas_age_majorite))
# attention au nombre de parenthèses

"""
Cela affichera :
<class 'int'>
<class 'int'>
"""

print("_____CHANGEMENT DE END_____")
"""
Ceux qui ont fait du c et du c++ se sont rendu compte que le retour à la ligne se fait 
automatiquement, sans avoir à préciser \n. En fait, la fonction print a un argument 
"end" qui est la fin de la chaîne de caractères à afficher et qui a "\n" comme 
valeur par défaut (voir aide/fonction/fonctions.py). On peut donc préciser la valeur 
de cette arguement pour empêcher le retour à la ligne automatique. Pour l'exemple, on 
va lister tout les nombres divisibles par 7 entre 0 et 100 non inclu et tout ça sur la 
même ligne. On aurai donc habituelement fait comme ceci :
"""

for i in range(0, 100) : 
    if i % 7 == 0 :
        print(i, ",")

"""
sortie au terminal :

0 ,
7 ,
14 ,
21 ,
28 ,
35 ,
42 ,
49 ,
56 ,
63 ,
70 ,
77 ,
84 ,
91 ,
98 ,

Ce n'est pas ce qu'on veut faire, donc on va changer la valeur de end, car 
il est égal à "\n" pour l'instant :
"""

for i in range(0, 100) : 
    if i % 7 == 0 :
        print(i, ",", end = ' ')
        # C'est un espace.

"""
sortie au terminal :

0 , 7 , 14 , 21 , 28 , 35 , 42 , 49 , 56 , 63 , 70 , 77 , 84 , 91 , 98 ,

On a donc bien ce qu'on voulais au départ.
"""