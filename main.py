

#Presentation du projet
print("==== PROJET CALCULATRICE====")
print("Ce projet est un projet de calculatrice permettant de faire des calculs simples et évolutifs")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

#Entrée des nombres
nombre1=int(input("Entrer le premier nombre:"))
nombre2=int(input("Entrer le deuxième nombre:"))
print("nombre1:",nombre1)
print("nombre2:",nombre2)

#Différentes opérations
addition=nombre1+nombre2
soustraction=nombre1-nombre2
multiplication=nombre1*nombre2
division=nombre1/nombre2    

#Choix de l'opération
choix=int(input("Entrer votre choix:"))
if choix==1:
    print("Vous avez choisi l'addition")
    print("Résultat:", addition)
elif choix==2:
    print("Vous avez choisi la soustraction")
    print("Résultat:", soustraction)
elif choix==3:
    print("Vous avez choisi la multiplication")
    print("Résultat:", multiplication)  
elif choix==4:
    print("Vous avez choisi la division")
    print("Résultat:", division)
else:
    print("Choix invalide") 





