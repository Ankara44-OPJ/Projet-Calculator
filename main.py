
#importation des bibliothèques nécessaires

import operations
import historique
import interface




def faire_un_choix():
    while True:
        try:
            choix = int(input("Entrez votre choix: ").strip())
            return choix
        except ValueError:
            print("\n")
            print("╔" + "="*38 + "╗")
            print("║Veuillez entrer un nombre valide.     ║")
            print("╚" + "="*38 + "╝")



def lancer_calculatrice():
    #fonctions de menu
    
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

    def afficher_dernier_resultat():
        if dernier_resultat is None:
            print("╔" + "="*38 )
            print("║ Aucun dernier résultat disponible.   ")
            print("╚" + "="*38 )
        else:
            print("╔" + "="*38 )
            print("║ Dernier résultat:", dernier_resultat)
            print("╚" + "="*38 )
            print("\n")

    
    

    #boucle principale
    while True: 
        
        interface.afficher_menu()
        afficher_dernier_resultat()


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

        #Demande du choix de l'utilisateur
        print("\n")
        print("╔" + "="*38 + "╗")
        print("║ Veuillez choisir une opération:")
        choix=faire_un_choix()
        print("╚" + "="*38 + "╝")

        if choix in operation_config and operation_config[choix]["arguments"] == 2 and choix not in [9, 10, 11]:
            nombre1=demander_nombre("Entrer le premier nombre:")
            nombre2=demander_nombre("Entrer le deuxième nombre:")
            resultat = operation_config[choix]["operation"](nombre1, nombre2)
            symbole = operation_config[choix]["symbol"]
            interface.afficher_resultat(resultat)
            historique.ajouter_historique(historique_data, nombre1, symbole, nombre2, resultat)
            historique.sauvegarder_historique(historique_data)
            dernier_resultat = resultat
            continue

        if choix in operation_config and operation_config[choix]["arguments"] == 1:
            nombre=demander_nombre("Entrer le nombre:")
            resultat = operation_config[choix]["operation"](nombre)
            symbole = operation_config[choix]["symbol"]
            interface.afficher_resultat(resultat)
            if choix == 8:
                print("\n")
                print("╔" + "="*38)
                print(f"║{symbole}{nombre}{symbole} = {resultat}")
                print("╚" + "="*38)
            else:
                print("\n")
                print("╔" + "="*38)
                print(f"║{symbole}({nombre}) = {resultat}")
                print("╚" + "="*38  )
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
                print("\n")
                print("╔" + "="*38)
                print(f"║{taux}% de {nombre} = {resultat}")
                print("╚" + "="*38)
            else:
                print("\n")
                print("╔" + "="*38)
                print(f"║{taux}% de {symbole} sur {nombre} = {resultat}")
                print("╚" + "="*38)
                historique.ajouter_historique(historique_data, nombre, symbole, taux, resultat)
                historique.sauvegarder_historique(historique_data)
            continue
        

        if choix not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
            print("\n")
            print("╔" + "="*38 + "╗")
            print("║Choix invalide. Veuillez réessayer.  ║")
            print("╚" + "="*38 + "╝")
            continue
        
        if choix==19:
            historique.afficher_historique(historique_data)
            continue
        
        if choix==20:
            historique_data.clear()
            historique.sauvegarder_historique(historique_data)
            print("\n")
            print("╔" + "="*38 + "╗")
            print("║L'historique des calculs a été effacé. ║")
            print("╚" + "="*38 + "╝")
            continue

        if choix==21:
                resultat = operations.dernier_resultat_utiliser(dernier_resultat)
                print("\n")
                print("╔" + "="*38 + "╗")
                print("║Résultat:", resultat)
                print("╚" + "="*38 + "╝")
                continue
        
        if choix==22:
            print("\n")
            print("╔" + "="*38)
            print("║Merci d'avoir utilisé la calculatrice.\nAu revoir!")
            print("╚" + "="*38)
            break

        #Entrée des nombres
        try:
            nombre1=demander_nombre("Entrer le premier nombre:")
            nombre2=demander_nombre("Entrer le deuxième nombre:")
            print("\n")
            print("="*40)
            print("nombre1:",nombre1)
            print("="*40)
            print("="*40)
            print("nombre2:",nombre2)
            print("="*40)
            
        except ValueError:
            print("\n")
            print("╔" + "="*38 + "╗")
            print("║Veuillez entrer des nombres valides.  ║")
            print("╚" + "="*38 + "╝")

if __name__ == "__main__":
    lancer_calculatrice()