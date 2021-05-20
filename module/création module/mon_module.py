#coding:utf-8

"""
On rassemble ici les différentes fonctions du module 
"mon module"
"""

def envoyer_message(envoyeur, message) :
    print("{} : {}".format(envoyeur, message))

def message_quitter(joueur_quittant) :
    print(joueur_quittant, "vient de se déconnecter.")