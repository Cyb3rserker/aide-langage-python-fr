#coding:utf-8
"""
La méthode title permet de mettre en majuscule le premier 
caractère de chaque mot de la chaîne :
"""

print()
print("TITLE".center(50, "*"))
print()

chaine_de_caracteres = "je suis une chaîne de caractères"
chaine_de_caracteres = chaine_de_caracteres.title()

print('''Dans le code :

    chaine_de_caracteres = "je suis une chaîne de caractères"
    chaine_de_caracteres = chaine_de_caracteres.title()

Le résultat :\n''')
print(chaine_de_caracteres)

"""
sortie au terminal :

**********************TITLE***********************

Dans le code :

    chaine_de_caracteres = "je suis une chaîne de caractères"
    chaine_de_caracteres = chaine_de_caracteres.title()      

Le résultat :

Je Suis Une Chaîne De Caractères
"""