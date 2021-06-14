#coding:utf-8

import mon_module

mon_module.envoyer_message("Médoune", "Salut, je viens de me connecter.")
mon_module.message_quitter("Médoune")

"""
La première utilisation de ce code va créer un dossier 
cache qui, en quelques sortes, contient les configurations 
optimales pour que le programme s'execute le plus 
rapidement possible. On peut avoir plusieurs modules 
dans plusieurs dossiers pour être très organisé. Il 
faut juste que notre module soit dans le même dossier 
que notre programme. Voici un exemple : mon module se 
nomme module_loin.py est il est dans le 
dossier modules_dans_autres_dossier. 
Pour l'inclure, je vais devoir utiliser 
cette syntaxe :
"""

import modules_dans_autres_dossier.module_loin
# On utilise un point pour faire la séparation des fichiers.
"""
ATTENTION !!! Il faut faire des noms de dossier sans espaces 
l'importation ne marche pas. Je n'ai pas encore trouver de solution.
D'ailleurs, le cache d'utilisation du module est dans  
modules_dans_autres_dossier.
"""

"""
Comme j'ai utiliser seulement import, je dois préciser le 
nom du module mais je dois aussi préciser son chemin :
"""

modules_dans_autres_dossier.module_loin.calcul_age_user()

"""
Si je ne veux pas avoir à préciser tout le chemin avant chaque 
fonction mais que je veux quand même le nom du module, j'utilise 
cette syntaxe :
"""

import modules_dans_autres_dossier.module_loin as module_loin
"""
note:je peux le nommer comme je veux et mêmes avec des 
modules communs.
"""

module_loin.calcul_age_user()

"""
Je vais faire les précisions sur les tests des fonctions dans le 
module mon_module.py.
"""