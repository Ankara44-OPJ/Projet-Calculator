
#importation des bibliothèques nécessaires

import operations
import historique

def lancer_calculatrice():
    #fonctions de menu
    def afficher_menu():

    #Presentation du projet
        print("==== PROJET CALCULATRICE====")
        print("Ce projet est un projet de calculatrice permettant de faire des calculs simples et évolutifs")

        print("=== Operations a deux nombres: ===")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Puissance")

        print("=== Operations a un nombre: ===")
        print("7. Racine carrée")
        print("8. valeur absolue")
        print("9. Pourcentage")
        print("10. Augmentation")
        print("11. Reduction")
        print("12. factorielle")
        print("13.cosinus")
        print("14. sinus")
        print("15. tangente")
        print("16. logarithme")
        print("17. logarithme népérien")
        print("18. exponentielle")

        print("19. Historique des calculs")
        print("20. Effacer l'historique des calculs")
        print("21. Afficher le dernier résultat")
        print("22. Quitter")

    def demander_nombre(prompt):
        while True:
                valeur =(input(prompt)).strip()
                if valeur.upper()== "ANS":
                    if dernier_resultat is not None:
                        return dernier_resultat
                    else:
                        print("Aucun résultat disponible.")
                        continue
                try:
                    return float(valeur)
                except ValueError:
                    print("Veuillez entrer un nombre valide.")


    #ajout de l'historique des calculs
    historique_data = historique.charger_historique()
    dernier_resultat = None


    operation_config ={
        1 : {
            "operation": operations.addition,
            "symbol": "+",
            "arguments": 2
        },
        2 : {
            "operation": operations.soustraction,
            "symbol": "-",
            "arguments": 2
        },
        3 : {
            "operation": operations.multiplication,
            "symbol": "*",
            "arguments": 2
        },
        4 : {
            "operation": operations.division,
            "symbol": "/",
            "arguments": 2
        },
        5 : {
            "operation": operations.modulo,
            "symbol": "%",
            "arguments": 2
        },
        6 : {
            "operation": operations.puissance,
            "symbol": "**",
            "arguments": 2
        },
        7 : {
            "operation": operations.racine_carre,
            "symbol": "√",
            "arguments": 1
        },
        8 : {
            "operation": operations.valeur_absolue,
            "symbol": "|",
            "arguments": 1
        },
        9 : {
            "operation": operations.pourcentage,
            "symbol": "%",
            "arguments": 2
        },
        10 : {
            "operation": operations.augmentation,
            "symbol": "augmentation",
            "arguments": 2
        },
        11 : {
            "operation": operations.reduction,
            "symbol": "réduction",
            "arguments": 2
        },
        12 : {
            "operation": operations.factorielle,
            "symbol": "!",
            "arguments": 1
        },
        13 : {
            "operation": operations.cosinus,
            "symbol": "cos",
            "arguments": 1
        },
        14 : {
            "operation": operations.sinus,
            "symbol": "sin",
            "arguments": 1
        },
        15 : {
            "operation": operations.tangente,
            "symbol": "tan",
            "arguments": 1
        },
        16 : {
            "operation": operations.logarithme,
            "symbol": "log",
            "arguments": 1
        },
        17 : {
            "operation": operations.logarithme_neperien,
            "symbol": "ln",
            "arguments": 1
        },
        18 : {
            "operation": operations.exponentielle,
            "symbol": "exp",
            "arguments": 1
        }

    }
    

    #boucle principale
    while True: 
        
        afficher_menu()

        #Demande du choix de l'utilisateur
        choix=int(input("Entrer votre choix:"))

        if choix in operation_config and operation_config[choix]["arguments"] == 2 and choix not in [9, 10, 11]:
            nombre1=demander_nombre("Entrer le premier nombre:")
            nombre2=demander_nombre("Entrer le deuxième nombre:")
            resultat = operation_config[choix]["operation"](nombre1, nombre2)
            symbole = operation_config[choix]["symbol"]
            print("Résultat:", resultat)
            historique.ajouter_historique(historique_data, nombre1, symbole, nombre2, resultat)
            historique.sauvegarder_historique(historique_data)
            dernier_resultat = resultat
            continue

        if choix in operation_config and operation_config[choix]["arguments"] == 1:
            nombre=demander_nombre("Entrer le nombre:")
            resultat = operation_config[choix]["operation"](nombre)
            symbole = operation_config[choix]["symbol"]
            if choix == 8:
                print(f"{symbole}{nombre}{symbole} = {resultat}")
            else:
                print(f"{symbole}({nombre}) = {resultat}")
                historique.ajouter_historique(historique_data, nombre, symbole, None, resultat)
                historique.sauvegarder_historique(historique_data)
                dernier_resultat = resultat
            continue

        if choix in [9, 10, 11]:  # Pourcentage, augmentation, réduction nécessitent un taux
            nombre=demander_nombre("Entrer le nombre:")
            taux=demander_nombre("Entrer le taux:")
            resultat = operation_config[choix]["operation"](nombre, taux)
            symbole = operation_config[choix]["symbol"]
            if choix == 9:
                print(f"{taux}% de {nombre} = {resultat}")
            else:
                print(f"{taux}% de {symbole} sur {nombre} = {resultat}")
                historique.ajouter_historique(historique_data, nombre, symbole, taux, resultat)
                historique.sauvegarder_historique(historique_data)
            continue
        

        if choix not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
            print("Choix invalide. Veuillez réessayer.")
            continue
        
        if choix==19:
            historique.afficher_historique(historique_data)
            continue
        
        if choix==20:
            historique.clear()
            historique.sauvegarder_historique(historique_data)
            print("L'historique des calculs a été effacé.")
            continue

        if choix==21:
                resultat = operations.dernier_resultat_utiliser(dernier_resultat)
                print("Résultat:", resultat)
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
            
        except ValueError:
            print("Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    lancer_calculatrice()