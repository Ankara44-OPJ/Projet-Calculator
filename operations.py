
import math


#fonction de calcul
def addition(nombre1,nombre2):
    return nombre1+nombre2

def soustraction(nombre1,nombre2):
    return nombre1-nombre2

def multiplication(nombre1,nombre2):
    return nombre1*nombre2

def division(nombre1,nombre2):
    if nombre2 == 0:
        return "Erreur: Division par zéro n'est pas permise."
    return nombre1/nombre2

def modulo(nombre1,nombre2):
    if nombre2 == 0:
        return "Erreur: Division par zéro n'est pas permise."
    return nombre1 % nombre2

def puissance(nombre1,nombre2):
    return nombre1 ** nombre2

def racine_carre(nombre):
    if nombre < 0:
        return "Erreur: La racine carrée d'un nombre négatif n'est pas définie."
    return math.sqrt(nombre)

def valeur_absolue(nombre):
    return abs(nombre)

def dernier_resultat_utiliser(dernier_resultat):
    if dernier_resultat is not None:
        return dernier_resultat
    else:
        return "Aucun résultat disponible."

def pourcentage(nombre, taux):
    return (nombre * taux) / 100

def augmentation(nombre, taux):
    return nombre + (nombre * taux) / 100

def reduction(nombre, taux):
    return nombre - (nombre * taux) / 100

def factorielle(nombre):
    if nombre < 0:
        return "Erreur: La factorielle d'un nombre négatif n'est pas définie."
    elif nombre == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, int(nombre) + 1):
            resultat *= i
        return resultat
    
def cosinus(nombre):
    return math.cos(math.radians(nombre))

def sinus(nombre):
    return math.sin(math.radians(nombre))

def tangente(nombre):
    return math.tan(math.radians(nombre))

def logarithme(nombre):
    if nombre <= 0:
        return "Erreur: Le logarithme d'un nombre non positif n'est pas défini."
    return math.log10(nombre)

def logarithme_neperien(nombre):
    if nombre <= 0:
        return "Erreur: Le logarithme népérien d'un nombre non positif n'est pas défini."
    return math.log(nombre)

def exponentielle(nombre):
    return math.exp(nombre)
