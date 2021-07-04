#coding:utf-8

"""
La méthode islower permet de savoir si une chaîne de caractères 
est entièrement en minuscule en revoyant une valeur booléenne :
"""

user_str = input("Votre phrase :\n")

if user_str.islower() == True :
    print("Votre phrase est en minuscule.")
else :
    print("Votre phrase n'est pas en minuscule.")

user_str = input("Votre nouvelle phrase :\n")

if user_str.islower() == True :
    print("Votre phrase est en minuscule.")
else :
    print("Votre phrase n'est pas en minuscule.")

"""
sortie au terminal :

Votre phrase :
LE SAUCISSON C'EST MA PASSION
Votre phrase est en minuscule.
Votre nouvelle phrase :
Le saucisson n'est pas ma passion
Votre phrase n'est pas en minuscule.
"""