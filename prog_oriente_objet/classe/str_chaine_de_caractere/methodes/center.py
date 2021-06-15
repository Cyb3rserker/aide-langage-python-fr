#coding:utf-8
"""
La méthode center permet de centrer du texte sur le terminal en affichant
une chaine de caractère plus longue que l'initiale, et l'initiale sera 
entre des caractères de remplissage. Voici sa définition :

str.center(<largeur du texte>, <caractère de remplissage>)
"""

print("\n_____CENTER_____\n")

chaine_de_caracteres =  "je suis une chaîne de caractères."
print(chaine_de_caracteres.center(50, "_"))

"""
sortie au terminal :

_____CENTER_____

________je suis une chaîne de caractères._________

On peut voir que la ligne fait 50 cases de long et que les cases qui 
ne sont pas remplies par les caractères de ma phrases sont remplacées 
par des _, car je les ai renseignés dans les paramètres de la méthode.
Je vais d'ailleurs utiliser cette technique pour la mise en forme des 
titres dans le terminal.
"""