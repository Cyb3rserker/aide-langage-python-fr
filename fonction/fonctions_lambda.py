#conding:utf-8

"""
Une fonction lamba est une fonction qui retourne le resultat d'une 
seule instruction ou n'execute qu'une seule instruction. Je n'ai 
pas encore trouvé de réelle utilité, mais celle que je vois là 
est d'occuper beaucoup moins de ligne de code.
"""

print("\n_____FONCTION LAMBA SANS ARGUMENTS_____\n")

lasalle = lambda : print("Salut à tous c'est Lasalle")
# La fonction est stockée dans la variable lasalle

lasalle()
print(type(lasalle))
"""
sortie au terminal : 

Salut à tous c'est Lasalle
<class 'function'>

Ces fonctions peuvent aussi avoir des arguments :
"""

print("\n_____FONCTION LAMBA AVEC ARGUMENTS_____\n")

mutliplication = lambda nombre1, nombre2 : nombre1 + nombre2
print(mutliplication(6, 7))

"""
Cette définitions de fonctions aura pris 3 lignes de codes 
(ou 2 si on est radin) :

def multiplication(nombre1, nombre2) :
    resultat = nombre1 * nombre2
    return resultat
"""