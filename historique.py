
import json

def ajouter_historique(historique, nombre1, operation, nombre2, resultat):
    calcul = {
        "nombre1": nombre1,
        "operation": operation,
        "nombre2": nombre2,
        "resultat": resultat
    }
    historique.append(calcul)


def afficher_historique(historique):
    if not historique:
                    print("Aucun calcul effectué pour le moment.")
    else:
        print("=== Historique des calculs: ===")
        for calcul in historique:
            if calcul["nombre2"] is not None:
                print(
                    calcul["nombre1"],
                    calcul["operation"],
                    calcul["nombre2"], "=",
                    calcul["resultat"]
                )
            if calcul["nombre1"] is not float:
                print(
                    calcul["nombre1"],
                    "=",
                    calcul["resultat"]
                    ) 
            else:
                print(
                    calcul["operation"],
                    calcul["nombre1"],
                    "=",
                    calcul["resultat"]
            )


def sauvegarder_historique(historique, nom_fichier="historique.json"):
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        json.dump(historique, fichier, ensure_ascii=False, indent=4)


def charger_historique(nom_fichier="historique.json"):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            try:
                return json.load(fichier)
            except FileNotFoundError:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []