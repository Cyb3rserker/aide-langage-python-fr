#coding:utf-8
"""
La méthode index est la même que la fonction find, c'est à dire qu'elle 
cherche une chaîne de caractères dans une autre, sauf qu'elle engendre 
une ValueError et on peut donc s'en servir :
"""

print()
print("INDEX".center(50, "*"))
print()

chaine_de_caracteres = "je suis une chaîne de caractères"

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