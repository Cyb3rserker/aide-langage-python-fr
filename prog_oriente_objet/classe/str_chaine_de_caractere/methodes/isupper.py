#coding:utf-8

"""
La méthode isupper permet de savoir si une chaîne de caractères 
est entièrement en majuscule en revoyant une valeur booléenne :
"""

user_str = input("Votre phrase :\n")

if user_str.isupper() == True :
    print("Votre phrase est en majuscule.")
else :
    print("Votre phrase n'est pas en majuscule.")

user_str = input("Votre nouvelle phrase :\n")

if user_str.isupper() == True :
    print("Votre phrase est en majuscule.")
else :
    print("Votre phrase n'est pas en majuscule.")

"""
sortie au terminal :

Votre phrase :
LE SAUCISSON C'EST MA PASSION
Votre phrase est en majuscule.
Votre nouvelle phrase :
Le saucisson n'est pas ma passion
Votre phrase n'est pas en majuscule.
"""