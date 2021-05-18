#coding:utf-8

"""
MARQUER UNE SEPARATION ENTRE LES DIFFERENTES PARTIES DE LA FICHE
"""

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

print("\n_____FONCTION AVEC PARAMETRE PAR DEFAUT_____\n")

"""
On peut définir des fonctions avec des paramètres 
optionnels, c'est-à-dire qu'on peut assigner une valeur par défaut
aux paramètres que l'on veut dans la définition de la fonction.
Voici un exemple :
"""

# envoyer_message("Médoune")
"""
sortie au terminal :

TypeError: envoyer_message() missing 1 required positional 
argument: 'message_envoyeur'

On peut voir que l'interpréteur python me dit qu'un 
argument manque lors de l'appel de la fonction. C'est donc
dans ces cas là que l'on défini des paramètres par 
défaut de la manière suivante :
"""
def envoyer_message_2(nom_envoyeur = "Administrateur", message_envoyeur = "Pas de nouveau message") :
    print("{} : {} ".format(nom_envoyeur, message_envoyeur))

envoyer_message_2()
envoyer_message_2("Médoune")

"""
sortie au terminal :

Administrateur : Pas de nouveau message
Médoune : Pas de nouveau message

On peut voir que le programme c'est déroulé correctement grâce aux 
valeurs par défaut que l'on a définis. Tout ça c'est bien, mais si 
dans cette situation on ne peut que renseigner le nom de l'envoyeur 
si on ne connaît qu'un des paramètres. Heureusement, en python, on 
peut renseigner les arguments dans le désodre, mais en précisant à 
quoi ils correspondent. Voici un exemple :
"""
print("\n_____PARAMETRE DANS LE DESORDRE_____\n")

"""
Je veux collecter des informations avec le prénom, l'âge et la 
taille de chaque utilisateur utilisant mon programme. Les print(s) 
inscriront les informations dans un fichier, un terminal, un pc 
ou n'importe quoi :
"""

def save_identite(nom = "inconnu", prenom = "inconnu", taille = "inconnue") :
    print("nom : {}\nprenom : {}\ntaille : {}".format(nom, prenom, taille))

"""
Imaginons que le premier utilisateur se nomme Francis Lefevre et 
qu'il fait 1.86 m mais que celui-ci oublie de préciser son prénom :
"""

save_identite("Lefevre", "1.86 m")
"""
la sortie au terminal sera donc ça :

nom : Lefevre
prenom : 1.86 m
taille : inconnue

Ce qui n'est pas du tout ce que l'on veut. On va alors préciser à 
quel argument correspond quel valeur :
"""

print()
# (Pour plus de clareté dans le terminal)
save_identite(nom = "Lefevre", taille = "1.86 m")

"""
la sortie au terminal sera donc ça :

nom : Lefevre
prenom : inconnu
taille : 1.86 m

On peut donc voir qu'en précisant quel valeur correspond à quel 
argument optionnel qu'on obtient quelque chose de cohérent à la fin.
"""

print("\n_____NOMBRE D'ARGUMENTS VARIABLE_____\n")
"""
En python, on définir des fonctions qui n'ont pas un nombre défini 
d'argument. En effet, dans ce genre de fonction, on peut avoir 1 
argument comme 100 et voici un exemple :
"""

def affichage_personnel(*liste_personnel) :
    for une_personne in liste_personnel :
        print(une_personne)
"""
On met une étoile pour signifier que le nombre d'argument n'est 
pas défini.

La boucle va donc parcourir toute la liste du personnel, et donc 
tout les arguments que l'on aura spécifiés. On peut maintenant 
l'utiliser :
"""

# Cela marche aussi bien avec un argument :
print("(1 ARGUMENT)")
affichage_personnel("Nicole")

# Qu'avec 5 arguments :
print()
print("(5 ARGUMENT)")
affichage_personnel("Thérèse", "Marcelle", "Bertrand", "René", "Robert")

print("\n_____RETOUR FONCTION_____\n")
"""
Comme dit plus tôt, les fonctions peuvent avoir des retours et on 
peut s'en servir. Voici un exemple avec la syntaxe qui va avec :
"""

# On va faire une fonction qui retourne le carré du nombre en argument :

def retour_carre(nombre) :
    carre_nombre = nombre * nombre
    # On utilise alors le mot clé return :
    return carre_nombre
    # Dès que la fonction retourne une valeur, elle s'arrête.

# Maintenant que ma fonction retourne un résultat, je peux l'expoloiter :

carre_douze = retour_carre(12)

print("Le carré de 12 est", carre_douze)