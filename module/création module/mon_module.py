#coding:utf-8

"""
On rassemble ici les différentes fonctions du module 
"mon module"
"""

def envoyer_message(envoyeur, message) :
    print("{} : {}".format(envoyeur, message))

def message_quitter(joueur_quittant) :
    print(joueur_quittant, "vient de se déconnecter.")

"""
Les modules rassemblent des fonctions, des classes etc mais peuvent 
aussi contenir du code à executer. Mais si on a du code dans ce module 
par exemple : 

print("Bonjour")

Ce code va s'exectuter au moment où on importe le module dans le fichier 
principal. Cela peut être très embêtant si on a du code qui permet 
de tester les fonctions. Voici comment faire :
"""

if __name__ == '__main__' :
# "Si le fichier est executé en tant que fichier principal, alors :"
    print('''Message qui devrait apparaître : \n
        Médoune : Bonjour tout le monde !\n''')
    
    print("Ce qui apparaît :\n")
    envoyer_message("Médoune", "Bonjour tout le monde !")

    """
    sortie au terminal :

    Message qui devrait apparaître : 

        Médoune : Bonjour tout le monde !

    Ce qui apparaît :

    Médoune : Bonjour tout le monde !

On peut voir que notre phase de test c'est bien passée. Grâce à 
ma syntaxe, mon bout de code ne sera pas executé s'il n'est pas 
le fichier principal et donc il ne le sera que quand je voudrais le 
tester.
"""