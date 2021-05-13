#coding:utf-8

"""
Les conditions permettent d'execter certaines actions seuelement si les conditions 
que l'on a spécifiés sont respectées. Voici un exemple d'utilisation avec la syntaxe :
"""

# (Cette exemple est inspiré de celui de la vidéo de FormationVidéo sur le sujet)

"""
Dans cet exemple, on va créer une phrase secret qui ne peut être vue que grâce à un mot de 
passe. Pour faire la vérification de ce mot de passe, on va utiliser les conditions (ne pas 
faire attention au mot utilisés, je n'avais pas d'inspiration) :
"""

phrase_secrete = "I have achieve perfection"
mot_de_passe = "Oi Josuke"

mot_de_passe_utilisateur = input("Veuillez taper le mot de passe : ")

"""
On fait maintenant une vérification avec le mot clé "if" pour savoir si le mot de passe 
de l'uilisateur correspond :
"""

if mot_de_passe_utilisateur == mot_de_passe:
# ATTENTION A LA TABULATION !!! (juste au dessus de shift ou "la flèche à gauche")
    print("Vous avez saisie le bon mot de passe. Voici la phrase secrete :", phrase_secrete)
"""
Si l'utilisateur tape le bon mot de passe, le terminal ressemblera à ça :

Veuillez taper le mot de passe : Oi Josuke
Vous avez saisie le bon mot de passe. Voici la phrase secrete : I have achieve perfection
"""
"""
Cette version est bonne, mais pas complète. En effet, si l'utilisateur ne saisi pas bien le 
mot de passe, son terminal ne ressemblera qu'à ça :

Veuillez taper le mot de passe : eh bien je ne sais pas. 

et le programme va s'arrêter. Pour contrecarrer cela, je vais utiliser le mot clé "else". Ce 
mot clé s'utilise comme le if, mais après un d'eux au cas où la première condition n'est pas 
remplie :
"""

else:
    print("Vous n'avez pas saisi le bon mot de passe.")

"""
Maintenant, le terminal ressemblera à ça si l'utilisateur rate sa tentative :


On peut voir que maintenant le programme est complet.
"""

"""
On peut parfois avoir plusieurs vérification de condition dans le même if. Pour mettre en 
place cela, on utilise les conditions multiples :
    and : ... et ...
    ou  : ... ou ...
    
