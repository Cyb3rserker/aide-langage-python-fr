#coding:utf-8

"""
La fonction print est une fonction de base du python qui permet
d'afficher du contenu sur le terminal ou quelqu'autres canals de
sortie (canal de sortie ~= là où sortent les inforamtions du programme).
On peut afficher du texte, des données et autres.
"""

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

"""
On peut aussi afficher le résultat de fonction. Pour cette
exemple, on va utiliser la fonction "type" qui permet de
connaître le type de donnée d'une variable
(voir aide/donnees/variables.py) :
"""
print(type(age_majorite))
print(type(pas_age_majorite))
# attention au nombre de parenthèses

"""
Cela affichera :
<class 'int'>
<class 'int'>
"""
