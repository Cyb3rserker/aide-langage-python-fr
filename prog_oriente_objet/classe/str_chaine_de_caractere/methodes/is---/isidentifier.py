#coding:utf-8

"""
La méthode isidentifier permet de vérifier si la chaîne de caractère
est un mot pour indentifer des choses en python comme des classes, 
des variables et autres. On peut aussi le combiner avec la méthode 
iskeyword pour avoir une vérification complète mais je ne vais pas 
le faire dans ce fichier :
"""

user_str = input("Votre mot : ")

while user_str.isidentifier() == False :
    user_str = input("Votre mot n'est pas un identifieur valide. Veuillez réessayer : \n")

print(f"{user_str} est un identifiant valide.")

"""
sortie au terminal :

Votre mot : 2banane
Votre mot n'est pas un identifieur valide. Veuillez réessayer : 
2 banane
Votre mot n'est pas un identifieur valide. Veuillez réessayer : 
2banane
Votre mot n'est pas un identifieur valide. Veuillez réessayer : 
banane2
banane2 est un identifiant valide.
"""