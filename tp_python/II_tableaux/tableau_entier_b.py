from random import shuffle, randint
from tableau_entier_a import calculer_moyenne, element_present
import time


def tableau_aleatoire(n: int) -> [int]:
    tableau = [randint(0, 100) for _ in range(n)]
    return tableau


def tableau_n_premier_entiers_melanges(n: int) -> [int]:
    tableau = list(range(1, n+1))
    shuffle(tableau)
    return tableau


def mesurer_temps_execution(ma_fonction):
    debut = time.time()
    # Permet de lancer la fonction passer en paramètre
    ma_fonction()
    fin = time.time()
    temps_execution = fin - debut
    print("Temps écoulé :", temps_execution, "secondes")


if __name__ == "__main__":
    grand_tableau = tableau_aleatoire(1000000)

    # le lambda est une fonction anonyme qui encapsule la fonction calculer_moyenne
    # on est obligé de l'utilisé ici, car `mesurer_temps_execution` attend une fonction avec 0 paramètre
    # alors que calculer_moyenne en possède 1
    print("Temps calcul moyenne :")
    mesurer_temps_execution(lambda: calculer_moyenne(grand_tableau))

    # De même ici pour les 2 paramètres de element_present
    print("Temps recherche élément :")
    mesurer_temps_execution(lambda: element_present(grand_tableau, 42))

