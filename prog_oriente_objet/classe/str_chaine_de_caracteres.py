#coding:utf-8
"""
La classe str est une classe qui permet d'instancier des chaînes de 
caractères.
"""

"""
Pour instancier une chaîne de caractères, il faut utiliser cette 
syntaxe :
"""

chaine_de_caracteres = "Je suis une chaîne de caractères."
# Il faut mettre la chaîne entre guillemets.

print("\n_____AFFICHAGE BASIQUE DE LA CHAINE DE CARACTERES_____\n")
print(chaine_de_caracteres)

"""
sortie au terminal :

_____AFFICHAGE BASIQUE DE LA CHAINE DE CARACTERES_____

Je suis une chaîne de caractères.
"""

"""
Comme str est une classe, elle possède aussi des méthodes. Je vais 
montrer les méthodes au fur et à mesure avec des exemples. 
"""

"""
La méthodes upper permet de faire passer la chaine de caractères de 
minuscule à majuscule. Les méthodes de chaînes de caractères travail
sur des copie et les retournent ce qui veut dire que la chaîne de 
caractère n'est pas modifier si on ne le fait pas nous même : 
"""

print("\n_____UPPER_____\n")

print('''Dans le code :
    print(chaine_de_caractere.upper()\n
Le résultat : \n''')
print(chaine_de_caracteres.upper())

print()

#-----------------------------------------------------

print('''Dans le code :
    print(chaine_de_caracteres)\n
Le résultat : \n''')
print(chaine_de_caracteres)

print()

#-----------------------------------------------------

print('''Dans le code :
    chaine_de_caracteres = chaine_de_caracteres.upper()
    print(chaine_de_caracteres)\n
Le résultat : \n''')

chaine_de_caracteres = chaine_de_caracteres.upper()
print(chaine_de_caracteres)
print()

"""
sortie au terminal :

_____UPPER_____

Dans le code :
    print(chaine_de_caractere.upper()

Le résultat :

JE SUIS UNE CHAÎNE DE CARACTÈRES.

Dans le code :
    print(chaine_de_caracteres)

Le résultat :

Je suis une chaîne de caractères.

Dans le code :
    chaine_de_caracteres = chaine_de_caracteres.upper()
    print(chaine_de_caracteres)

Le résultat :

JE SUIS UNE CHAÎNE DE CARACTÈRES.
"""

"""
On a aussi sont inverse, lower, qui va passer tous les caractères en 
minuscule :
"""

print("\n_____LOWER_____\n")

print('''Dans le code :
    chaine_de_caracteres = chaine_de_caracteres.lower()
    print(chaine_de_caracteres)

Le résultat :\n''')
chaine_de_caracteres = chaine_de_caracteres.lower()
print(chaine_de_caracteres)

"""
sortie au terminal :

_____LOWER_____

Dans le code :
    chaine_de_caracteres = chaine_de_caracteres.lower()

    print(chaine_de_caracteres)

Le résultat :

je suis une chaîne de caractères.
"""

""""
On a aussi la méthode capitalize qui met en majuscule le début de 
la chaîne, la méthode title qui met chaque début de mot en majuscule.
Je ne vais pas montrer ces méthodes car cela allongerait le code pour 
rien car ce sont des méthodes très simple.
"""

"""
La méthode center permet de centrer du texte sur le terminal en affichant
une chaine de caractère plus longue que l'initial, et l'initial sera 
entre des caractères de remplissage. Voici sa définition :

str.center(<largeur du texte>, <caractères de remplissage>)
"""

print("\n_____CENTER_____\n")
print(chaine_de_caracteres.center(50, "_"))

"""
sortie au terminal :

_____CENTER_____

________je suis une chaîne de caractères._________

On peut voir que la ligne fait 50 cases de long et que les cases qui 
ne sont pas remplies par les caractères de ma phrases sont remplacées 
par des _, car je les ai renseignés dans les paramètres de la méthode.
Je vais d'ailleurs utiliser cette technique pour la mise en forme des 
titres dans le terminal.
"""

"""
On a aussi la méthodes find qui permet de chercher dans une chaîne de 
caractères :

str.find(<chaîne à trouver>, <début de la chaîne>, <fin>) 

Elle retourne l'indicee (= l'emplacement) du premier caractère qui 
correspond à la chaîne précisée dans les paramètres et si elle ne 
la trouve pas, elle retourne -1. D'ailleurs, la méthodes est sensible
à la casse, c'est à dire qu'il faut être rigoureux avec les majuscules.
(note : les ordinateurs commencent à compter à partir de 0, donc 
si ma chaîne à trouver commence dès le premier caractère de l'initial,
l'indice sera de 0.)
"""

print()
print("FIND".center(50, "*"))
print()

print("Indice de 'une' dans 'je suis une chaîne de caractères' : \
", chaine_de_caracteres.find("une"))

print("Indice de 'une' dans 'je suis une chaîne de caractères' : \
", chaine_de_caracteres.find("Je"))

"""
sortie au terminal :

***********************FIND***********************

Indice de 'une' dans 'je suis une chaîne de caractères' :  8
Indice de 'Je' dans 'je suis une chaîne de caractères' :  -1


On peut donc voir que 'une' se situe à l'indice 8 de notre chaîne et 
que 'Je' n'est pas dans la chaîne.
"""

"""
La méthode index est pareil, sauf qu'elle engendre une ValueError :
"""

print()
print("INDEX".center(50, "*"))
print()

try :
    chaine_de_caracteres.index("une")
except ValueError :
    print("Je n'ai pas trouvé 'une' dans 'je suis une chaîne de caractères'.")
else :
    print("Indice de 'une' dans 'je suis une chaîne de caractères' : \
", chaine_de_caracteres.index("une"))

try :
    chaine_de_caracteres.index("Je")
except ValueError :
    print("Je n'ai pas trouvé 'Je' dans 'je suis une chaîne de caractères'.")
else :
    print("Indice de 'Je' dans 'je suis une chaîne de caractères' : \
", chaine_de_caracteres.index("Je"))

"""
sortie au terminal :

**********************INDEX***********************

Indice de 'une' dans 'je suis une chaîne de caractères' :  8
Je n'ai pas trouvé 'Je' dans 'je suis une chaîne de caractères'.
"""