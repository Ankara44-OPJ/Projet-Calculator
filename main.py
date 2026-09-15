
import math

#fonctions de menu
def afficher_menu():

#Presentation du projet
    print("==== PROJET CALCULATRICE====")
    print("Ce projet est un projet de calculatrice permettant de faire des calculs simples et évolutifs")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Puissance")
    print("7. Racine carrée")
    print("8. valeur absolue")
    print("9. Historique des calculs")
    print("10. Effacer l'historique des calculs")
    print("11. Utiliser le dernier résultat")
    print("12. Pourcentage")
    print("13. Augmentation")
    print("14. Reduction")
    print("15. factorielle")
    print("16.cosinus")
    print("17. sinus")
    print("18. tangente")
    print("19. logarithme")
    print("20. logarithme népérien")
    print("21. exponentielle")
    print("22. Quitter")

def demander_nombre(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

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
def dernier_resultat_utiliser(derniere_resultat):
    if derniere_resultat is not None:
        return derniere_resultat
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


#ajout de l'historique des calculs
historique = []
derniere_resultat = None
    
#boucle principale
while True: 
    
    afficher_menu()

    #Demande du choix de l'utilisateur
    choix=int(input("Entrer votre choix:"))
    if choix not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]:
        print("Choix invalide. Veuillez réessayer.")
        continue
    
    if choix==7:
        nombre=demander_nombre("Entrer le nombre pour calculer la racine carrée:")
        resultat = racine_carre(nombre)
        print("Résultat:", resultat)
        calcul = f"√{nombre} = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==8:
        nombre=demander_nombre("Entrer le nombre pour calculer la valeur absolue:")
        resultat = valeur_absolue(nombre)
        print("Résultat:", resultat)
        calcul = f"|{nombre}| = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==9:
        if not historique:
            print("Aucun calcul effectué pour le moment.")
        else:
            print("=== Historique des calculs: ===")
            for calcul in historique:
                print(calcul)
        continue
    if choix==10:
        historique.clear()
        print("L'historique des calculs a été effacé.")
        continue
    if choix==11:
            resultat = dernier_resultat_utiliser(derniere_resultat)
            print("Résultat:", resultat)
            continue
    if choix==12:
        nombre=demander_nombre("Entrer le nombre pour calculer le pourcentage:")
        taux=demander_nombre("Entrer le taux de pourcentage:")
        resultat = pourcentage(nombre, taux)
        print(f"{taux}% de {nombre} = {resultat}")
        calcul = f"{taux}% de {nombre} = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==13:
        nombre=demander_nombre("Entrer le nombre pour calculer l'augmentation:")
        taux=demander_nombre("Entrer le taux d'augmentation:")
        resultat = augmentation(nombre, taux)
        print(f"{taux}% d'augmentation sur {nombre} = {resultat}")
        calcul = f"{taux}% d'augmentation sur {nombre} = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==14:
        nombre=demander_nombre("Entrer le nombre pour calculer la réduction:")
        taux=demander_nombre("Entrer le taux de réduction:")
        resultat = reduction(nombre, taux)
        print(f"{taux}% de réduction sur {nombre} = {resultat}")
        calcul = f"{taux}% de réduction sur {nombre} = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==15:
        nombre=demander_nombre("Entrer le nombre pour calculer la factorielle:")
        resultat = factorielle(nombre)
        print(f"{nombre}! = {resultat}")
        calcul = f"{nombre}! = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==16:
        nombre=demander_nombre("Entrer le nombre pour calculer le cosinus:")
        resultat = cosinus(nombre)
        print(f"cos({nombre}) = {resultat}")
        calcul = f"cos({nombre}) = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==17:
        nombre=demander_nombre("Entrer le nombre pour calculer le sinus:")
        resultat = sinus(nombre)
        print(f"sin({nombre}) = {resultat}")
        calcul = f"sin({nombre}) = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==18:
        nombre=demander_nombre("Entrer le nombre pour calculer la tangente:")
        resultat = tangente(nombre)
        print(f"tan({nombre}) = {resultat}")
        calcul = f"tan({nombre}) = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==19:
        nombre=demander_nombre("Entrer le nombre pour calculer le logarithme:")
        resultat = logarithme(nombre)
        print(f"log({nombre}) = {resultat}")
        calcul = f"log({nombre}) = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==20:
        nombre=demander_nombre("Entrer le nombre pour calculer le logarithme népérien:")
        resultat = logarithme_neperien(nombre)
        print(f"ln({nombre}) = {resultat}")
        calcul = f"ln({nombre}) = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==21:
        nombre=demander_nombre("Entrer le nombre pour calculer l'exponentielle:")
        resultat = exponentielle(nombre)
        print(f"e^{nombre} = {resultat}")
        calcul = f"e^{nombre} = {resultat}"
        historique.append(calcul)
        derniere_resultat = resultat
        continue
    if choix==22:
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break
    #Entrée des nombres
    try:
        nombre1=demander_nombre("Entrer le premier nombre:")
        nombre2=demander_nombre("Entrer le deuxième nombre:")
        print("nombre1:",nombre1)
        print("nombre2:",nombre2)

    

    #Choix de l'opération
        
        if choix==1:
            symbole = "+"
            print("Vous avez choisi l'addition")
            resultat = addition(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
            derniere_resultat = resultat
        elif choix==2:
            symbole = "-"
            print("Vous avez choisi la soustraction")
            resultat = soustraction(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
            derniere_resultat = resultat
        elif choix==3:
            symbole = "*"
            print("Vous avez choisi la multiplication")
            resultat = multiplication(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
            derniere_resultat = resultat
        elif choix==4:
            symbole = "/"
            print("Vous avez choisi la division")
            resultat = division(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
            derniere_resultat = resultat
        elif choix==5:
            symbole = "%"
            print("Vous avez choisi le modulo")
            resultat = modulo(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
            derniere_resultat = resultat
        elif choix==6:
            symbole = "**"
            print("Vous avez choisi la puissance")
            resultat = puissance(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
            derniere_resultat = resultat
        else:
            print("Choix invalide, veuillez réessayer.")
        
          
    except ValueError:
        print("Veuillez entrer des nombres valides.")

    

   




