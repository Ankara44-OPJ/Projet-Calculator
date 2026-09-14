
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
    print("11. Quitter")

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

#ajout de l'historique des calculs
historique = []
    
#boucle principale
while True: 
    
    afficher_menu()


    

    #Demande du choix de l'utilisateur
    choix=int(input("Entrer votre choix:"))
    if choix==11:
        print("Merci d'avoir utilisé la calculatrice!")
        break
    if choix not in [1,2,3,4,5,6,7,8,9,10]:
        print("Choix invalide, veuillez réessayer.")
        continue
    if choix==7:
        nombre=demander_nombre("Entrer le nombre pour calculer la racine carrée:")
        resultat = racine_carre(nombre)
        print("Résultat:", resultat)
        calcul = f"√{nombre} = {resultat}"
        historique.append(calcul)
        continue
    if choix==8:
        nombre=demander_nombre("Entrer le nombre pour calculer la valeur absolue:")
        resultat = valeur_absolue(nombre)
        print("Résultat:", resultat)
        calcul = f"|{nombre}| = {resultat}"
        historique.append(calcul)
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
        elif choix==2:
            symbole = "-"
            print("Vous avez choisi la soustraction")
            resultat = soustraction(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
        elif choix==3:
            symbole = "*"
            print("Vous avez choisi la multiplication")
            resultat = multiplication(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
        elif choix==4:
            symbole = "/"
            print("Vous avez choisi la division")
            resultat = division(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
        elif choix==5:
            symbole = "%"
            print("Vous avez choisi le modulo")
            resultat = modulo(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
        elif choix==6:
            symbole = "**"
            print("Vous avez choisi la puissance")
            resultat = puissance(nombre1,nombre2)
            print("Résultat:", resultat)
            calcul = f"{nombre1} {symbole} {nombre2} = {resultat}"
            historique.append(calcul)
        else:
            print("Choix invalide, veuillez réessayer.")
        
          
    except ValueError:
        print("Veuillez entrer des nombres valides.")

    

   




