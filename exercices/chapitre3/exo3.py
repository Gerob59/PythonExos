from easygui import *


def tabuler(fonction, borne_inf, borne_sup, nb_pas):
    for i in range(borne_inf, borne_sup+1, nb_pas):
        print(fonction(i))


def ma_fonction(x):
    return 2*x**3 + x - 5


def my_integer_box():
    # Afficher une boîte de dialogue pour saisir les bornes et le nombre de pas
    title = "Cours 3, exo3 - Tabulation de fonction"
    msg = "Entrer les bornes et le pas pour tabuler la fonction ma_fonction"
    fieldNames = ["Borne inférieure", "Borne supérieure", "Pas de calcul"]
    fieldValues = multenterbox(msg, title, fieldNames)

    # convertir les entrées de chaîne en entiers et renvoyer un tuple
    return int(fieldValues[0]), int(fieldValues[1]), int(fieldValues[2])

if __name__ == "__main__":
    # Appeler la fonction my_interger_box pour demander à l'utilisateur les bornes et le nombre de pas
    borneInf, borneSup, nbPas = my_integer_box()

    # Appeler la fonction tabuler avec ma_fonction et les valeurs saisies
    tabuler(ma_fonction, borneInf, borneSup, nbPas)