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