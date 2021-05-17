#coding:utf-8

"""
Une fonction est un algotithme qui permet d'effecuter 
certaines actions comme afficher des informations pour 
print, récupérer des inforamtions saisies pour input, 
caster des données pour int(), float(), etc. On peut 
voir les fonctions un peut comme une recette car on y 
entre des informations, il y a une préparation et un 
nouvel élément en sort, exemple : 

on a pour ingrédient variable qui est égal à 5 :
"""
variable = 5

"""
La recette est la fonction type qui retourne le type 
d'une variable :
"""

type_variable = type(variable)
"""
On met l'ingrédient dans le four et le plat final sera 
type_variable.
"""

"""
Ces recettes ont un retour de fonction, c'est à dire le 
résultat de la recette. Par exemple, le retour de la 
fonction input est une chaîne de caractères. Ces retours 
peuvent aussi servir à faire du débug, mais on verra ça 
plus tard.
Donc :
    - les fonctions sont comme des recettes, elle font 
    des manipulations avec des ingrédients qui sont les 
    paramètres (ce qui est entre parenthèses)
    - les fonctions ne sont pas obligées d'avoir des 
    paramètres, comme le montre la fonctions input()
    - on peut récupérer le plat final de ces recettes, 
    les retours de fonctions, pour les stocker ou faire 
    débug avec
"""

"""
On peut aussi créé nos propres fonctions en utilisant 
le mot clé def. Généralement, on définit des fonctions 
pour éviter les répétitions et raccourcir le code. 
Le nommage des fonctions suit les mêmes règle que le 
nommage des variables (pas de caractères spéciaux, 
nom unique, etc.) et il faut que les noms de 
fonctions soient les plus explicite possible. Ce n'est 
pas obligatoire, mais ça aide au développement. Les 
fonctions ne sont pas obligées d'avoir des paramètres.
"""

print("\n_____FONCTION SANS PARAMETRE______\n")
# Sans paramètre :

def afficher_bonjour() :
    print("Bonjour.")
    # Attention à la tabulation.

afficher_bonjour()

"""
sortie au terminal :

Bonjour.
"""

print("\n_____FONCTION AVEC PARAMETRE______\n")
# Avec des paramètres :

def envoyer_message(nom_envoyeur, message_envoyeur) :
    print("{} : {} ".format(nom_envoyeur, message_envoyeur))

envoyer_message("Médoune", "Salut tout le monde")
envoyer_message("Doge", "Salut")

"""
sortie au terminal :

Médoune : Salut tout le monde
Doge : Salut
"""

print("\n_____FONCTION AVEC PARAMETRE OPTIONNEL______\n")

"""
On peut définir des fonctions avec des paramètres 
optionnels, c'est-à-dire
"""

envoyer_message("Médoune")
"""
sortie au terminal :

TypeError: envoyer_message() missing 1 required positional 
argument: 'message_envoyeur'

On peut voir que l'interpréteur python me dit qu'un 
argument manque lors de l'appel de la fonction. C'est donc
dans ces cas là que l'on défini des paramètres par 
défaut.
"""
def envoyer_message_2(nom_envoyeur, message_envoyeur) :
    print("{} : {} ".format(nom_envoyeur, message_envoyeur))

"""