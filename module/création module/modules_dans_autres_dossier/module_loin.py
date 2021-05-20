#coding:utf-8

def calcul_age_user():
    age_user = int(input("Quel âge avez-vous ? "))
    print("Vous êtes âgé de {} jours ou {} mois.".format(age_user * 365, age_user * 12))