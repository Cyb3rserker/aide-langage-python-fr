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
Les chaines de caractères peuvent être visualisée comme une série 
de case qui sont chacune remplie avec un caractères dedans. Ces 
case sont identifiées avec des numéros que l'on appelle indice. Cette 
numérotation commence à partir de 0 car les ordinateurs commencent à 
compter à partir de 0. On peut utiliser ces indice pour lire les 
caractères, les manipuler et autres. Par exemple, dans ma chaîne 
de caractère, le caractère à l'indice 8 est un u car la lettre u se 
trouve à la neuvième case de ma chaîne composée de 32 caractères. 
Voici un exemple pour appuyer mes propos : je vais faire une boucle 
pour que chacun de mes caractères, jusqu'à la fin de "chaîne" donc 
les 18 premiers, soient affichés à la suite dans le terminal :
"""

print()
print("UTILISATION DE L'INDEX".center(50, "*"))
print()

for i in range(0, 18) :
    print(chaine_de_caracteres[i])
    # On utilise les crochets pour utiliser un index

"""
Sortie au terminal :

**************UTILISATION DE L'INDEX**************

J
e

s
u
i
s

u
n
e

c
h
a
î
n
e
"""

"""
Comme str est une classe, elle possède aussi des méthodes. Les 
différentes méthodes seront expliquées dans le même dossier.
Les méthodes de chaînes de caractères travaillent sur des copies 
et les retournent ce qui veut dire que la chaîne de caractère 
n'est pas modifier si on ne le fait pas nous même. Pour l'exemple, je 
vais utiliser la méthode lower :  
"""

print()
print("EXEMPLE QUI MONTRE QUE LES CHAINES NE SONT PAS MODIFIEES".center(50, "*"))
print()

print("chaine_de_caracteres :", chaine_de_caracteres)

chaine_de_caracteres.lower()
print('''Dans le code :

    chaine_de_caracteres.lower()

Le résultat :\n''')
print(chaine_de_caracteres)

#--------------------------------------------------------------

chaine_de_caracteres = chaine_de_caracteres.lower()

print('''Dans le code :

    chaine_de_caracteres = chaine_de_caracteres.lower()

Le résultat :\n''')
print(chaine_de_caracteres)

"""
sortie au terminal :

EXEMPLE QUI MONTRE QUE LES CHAINES NE SONT PAS MODIFIEES

chaine_de_caracteres : Je suis une chaîne de caractères.
Dans le code :

    chaine_de_caracteres.lower()

Le résultat :

Je suis une chaîne de caractères.
Dans le code :

    chaine_de_caractere = chaine_de_caracteres.lower()

Le résultat :

Je suis une chaîne de caractères.
"""

"""
On peut voir que le premier lower n'a eu aucune incidence sur l'original mais 
que le deuxième a changé le 'J' au début en 'j'.
"""