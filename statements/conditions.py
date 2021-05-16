#coding:utf-8

"""
Les conditions permettent d'exucter certaines actions seuelement si les conditions 
que l'on a spécifiés sont respectées. Voici un exemple d'utilisation avec la syntaxe :
"""

# (Cette exemple est inspiré de celui de la vidéo de FormationVidéo sur le sujet)

"""
Dans cet exemple, on va créer une phrase secret qui ne peut être vue que grâce à un mot de 
passe. Pour faire la vérification de ce mot de passe, on va utiliser les conditions (ne pas 
faire attention aux mots utilisés, je n'avais pas d'inspiration) :
"""

print("\n_____IF ET ELSE_____")
print("(mdp : Oi Josuke)\n")

phrase_secrete = "I have achieved perfection"
mot_de_passe = "Oi Josuke"

mot_de_passe_utilisateur = input("Veuillez taper le mot de passe : ")

"""
On fait maintenant une vérification avec le mot clé "if" ("si" en français) pour savoir 
si le mot de passe de l'uilisateur correspond :
"""

if mot_de_passe_utilisateur == mot_de_passe:
# ATTENTION A LA TABULATION !!! (juste au dessus de shift ou "la flèche à gauche")
    print("Vous avez saisie le bon mot de passe. Voici la phrase secrete :", phrase_secrete)
# (Je commente la suite avec des # car les commentaires avec """ entre if et else ne marchent pas)

# Si l'utilisateur tape le bon mot de passe, le terminal ressemblera à ça :

# Veuillez taper le mot de passe : Oi Josuke
# Vous avez saisie le bon mot de passe. Voici la phrase secrete : I have achieve perfection
# 
# Cette version est bonne, mais pas complète. En effet, si l'utilisateur ne saisi pas bien le 
# mot de passe, son terminal ne ressemblera qu'à ça :
#
# Veuillez taper le mot de passe : eh bien je ne sais pas. 
#
# et le programme va s'arrêter. Pour contrecarrer cela, je vais utiliser le mot clé "else" qui 
# peut se traduire par "sinon". Ce mot clé s'utilise comme le if, mais après un d'eux au cas 
# où la première condition n'est pas remplie :
else:
    print("Vous n'avez pas saisi le bon mot de passe.")
#
# 
# Maintenant, le terminal ressemblera à ça si l'utilisateur rate sa tentative :
#
# Veuillez taper le mot de passe : eh bien je ne sais pas. 
# Vous n'avez pas saisi le bon mot de passe.
#
# On peut voir que maintenant le programme est complet.

"""
Il y a aussi un autre mot réservé qui est "elif". Il permet de faire un else, mais en précisant une 
ou des conditions. Il est l'équivalent du "sinon si" en français :
"""

age_user = int(input("Quel âge avez vous ? ")) 

if age_user >= 30 :
    print("Vous êtes un adulte mature (j'espère).")
elif age_user <= 15 :
    print("Vous êtes un adolescent ou un enfant.")

# On peut aussi faire des conditions avec des fourchettes :

saisie_user = input("Veuillez saisir un charactère (lettre, chiffre...) : ")

if 'a' < saisie_user < 'z' :
    print("Vous avez saisie une lettre.")

print("\n_____VERIFICATIONS MULTIPLES_____\n")

"""
On peut parfois avoir plusieurs vérification de conditions dans le même if. Pour mettre en 
place cela, on utilise les conditions multiples :

    and : ... et ... ; avec cette vérification, si une seule des conditions n'est pas respectée 
    alors le code dans le if ne s'executera pas

    or  : ... ou ... avec cette vérification, si au moins une des conditions est respectée 
    alors le code dans le if executera

    in / not in : ... est dans ... / ... n'est pas dans ... ; ces mots réservés permettent de vérifier si 
    une donnée est dans un ensemble ou pas et il y aura un exemple plus bas pour comprendre.
"""

print("\n___IF AVEC AND___")
print("(ident : Boss ; mdp : Kazuhira hamburgers)\n")

identifiant = "Boss"
mot_de_passe = "Kazuhira hamburgers"
phrase_secrete = "Kept you waiting uh ?"


indentifiant_utilisateur = input("Veuillez saisir l'identifiant : ")
mot_de_passe_utilisateur2 = input("Veuillez maintenant saisir le mot de passe : ")

if indentifiant_utilisateur == identifiant and mot_de_passe_utilisateur2 == mot_de_passe :
    print("Authentification réussie. Voici la phrase secrète :", phrase_secrete)
else :
    print("Authentification ratée.")

# On peut faire des fourchettes avec and, mais c'est moins pratique :

saisie_user = input("Veuillez saisir un charactère (lettre, chiffre...) : ")

if saisie_user > 'a' and saisie_user < 'z' :
    print("Vous avez saisie une lettre.")

print("\n___IF AVEC OR___")
print("(rep : Macron ; Emmanuel ; Emmanuel Macron)\n")
# (J'écris ce bout de code le 16/05/2021)

prenom_macron = "Emmanuel"
nom_macron = "Macron"
nom_prenom_macron = "Emmanuel Macron"

rep_user = input("Comment s'appelle l'actuel président français ? ")

if rep_user == prenom_macron or rep_user == nom_macron or rep_user == nom_prenom_macron :
    print("Vous avez raison.")
else :
    print("Vous vous êtes trompé.")

print("\n___IF AVEC IN ET NOT IN___\n")

lettre_user = input("Veuillez saisir une lettre : ")

if lettre_user in "aeiouy" :
# (Si la lettre de l'utilisateur est dans cette séquences de lettres, alors...)
    print(lettre_user, "est une voyelle.")
else :
    print(lettre_user, "est une consonne")

lettre_user = input("Veuillez saisir une autre lettre : ")

if lettre_user not in "aeiouy" :
# (Si la lettre de l'utilisateur n'est pas dans cette séquences de lettres, alors...)
    print(lettre_user, "est une consonne")
else :
    print(lettre_user, "est une voyelle.")


"""
On peut encore les utiliser avec plein d'autres ensembles, mais je n'ai pour l'instant pas 
le niveau et je reviendrai mettre à jour ce fichier pour qu'il soit complet.
"""