#coding:utf-8

"""
La méthode split permet de séparer différent élément d'une chaîne 
de caractère. Pour les séparer, on doit renseigner un carctère qui 
inscrit la limite entre nos différents éléments. Pour l'exemple, 
je vais faire un personnage qui aura sa classe, dans mon cas 
"Magicien", ses points de vie, dans mon cas "100", et sa puissance, 
dans mon cas "150". Je vais utiliser | comme élément de séparation :
"""

personnage1 = "Magicien|100|150"

print("Voici la fiche du personnage 1 :")
print(personnage1.split("|"))

"""
sortie au terminal :

Voici la fiche du personnage 1 :
['Magicien', '100', '150']
"""