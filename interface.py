



def afficher_resultat(resultat):
    if isinstance(resultat, float) and (resultat.is_integer()):
        resultat = int(resultat)
    print("\n" + "="*40)
    print("Résultat:", resultat)
    print("="*40 + "\n")


def afficher_menu():
        print("\n")

    #Presentation du projet
        print("╔" + "="*38 + "╗")
        print("║    ==== PROJET CALCULATRICE====      ║")
        print("╚" + "="*38 + "╝")
        print("\n")
        print("="*40)
        print("Ce projet est un projet de calculatrice \npermettant de faire des calculs simples \net évolutifs")
        print("="*40 + "\n")

        

        print("╔" + "="*38 + "╗")
        print("║  === Operations a deux nombres: ===  ║")
        print("╚" + "="*38 + "╝")
        print("╔" + "="*38 + "╗")
        print("║1. Addition                           ║")
        print("║2. Soustraction                       ║")
        print("║3. Multiplication                     ║")
        print("║4. Division                           ║")
        print("║5. Modulo                             ║")
        print("║6. Puissance                          ║")
        print("╚" + "="*38 + "╝")
        print("\n")

        print("╔" + "="*38 + "╗")
        print("║    === Operations a un nombre: ===   ║")
        print("╚" + "="*38 + "╝")
        print("╔" + "="*38 + "╗")
        print("║7. Racine carrée                      ║")
        print("║8. valeur absolue                     ║")
        print("║9. Pourcentage                        ║")
        print("║10. Augmentation                      ║")
        print("║11. Reduction                         ║")
        print("║12. factorielle                       ║")
        print("║13.cosinus                            ║")
        print("║14. sinus                             ║")
        print("║15. tangente                          ║")
        print("║16. logarithme                        ║")
        print("║17. logarithme népérien               ║")
        print("║18. exponentielle                     ║")
        print("╚" + "="*38 + "╝")
        print("\n")

        print("╔" + "="*38 + "╗")
        print("║        === Autres options: ===       ║")
        print("╚" + "="*38 + "╝")
        print("╔" + "="*38 + "╗")
        print("║19. Historique des calculs            ║")
        print("║20. Effacer l'historique des calculs  ║")
        print("║21. Afficher le dernier résultat      ║")
        print("║22. Expression                        ║")
        print("║23. Quitter                           ║")
        print("╚" + "="*38 + "╝")




