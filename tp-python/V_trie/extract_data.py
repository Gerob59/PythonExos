import random
import time
from PyGnuplot import gp
from matplotlib import figure


def copie(t):
    return t.copy()  # Créer une copie du tableau


def inverse(t):
    return t[::-1]  # Slicing avec un pas -1 pour inverser l'ordre


def tableau_premiers_entiers(n):
    return [i for i in range(1, n+1)]


def tableau_premiers_entiers_melanges(n):
    tableau = tableau_premiers_entiers(n)
    random.shuffle(tableau)
    return tableau


def tableau_premiers_entiers_inverses(n):
    return [i for i in range(n, 0, -1)]


def ligne_dans_fichier(f, n, t):
    with open(f, 'a') as fichier:  # 'a' pour append. Ajoute à la fin du fichier.
        ligne = str(n) + ' ' + str(t) + '\n'  # cast 't' et 'n' en string pour pouvoir les concaténer
        fichier.write(ligne)


def tri_a_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]


def temps_tri_bulles(t):
    copie_t = t.copy()
    debut = time.time()
    tri_a_bulles(copie_t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution


def stats_melange(nmin, nmax, pas, fois):
    tableau = tableau_premiers_entiers_melanges(nmax)
    __stats(tableau, nmin, nmax, pas, fois)


def stats_ordonne(nmin, nmax, pas, fois):
    tableau = tableau_premiers_entiers(nmax)
    __stats(tableau, nmin, nmax, pas, fois)


def stats_inverse(nmin, nmax, pas, fois):
    tableau = tableau_premiers_entiers_inverses(nmax)
    __stats(tableau, nmin, nmax, pas, fois)


def __stats(t, nmin, nmax, pas, fois):
    fichier = "temps_tris.txt"

    with open(fichier, 'a') as f:
        f.write("Taille Temps moyen\n")

    for taille in range(nmin, nmax + 1, pas):
        temps_total = 0

        for _ in range(fois):
            temps_execution = temps_tri_bulles(t)
            temps_total += temps_execution

        temps_moyen = temps_total / fois

        with open(fichier, 'a') as f:
            f.write(f"{taille} {temps_moyen}\n")

    with open(fichier, 'a') as f:
        f.write("\n")

    print("Les temps moyens ont été enregistrés dans le fichier", fichier)


if __name__ == "__main__":
    # # === question 1 === #
    # tableau = [1, 2, 3, 4, 5]
    # copie_tableau = copie(tableau)
    # print("tableau :", tableau)  # Output: [1, 2, 3, 4, 5]
    # print("copie du tableau :", copie_tableau)  # Output: [1, 2, 3, 4, 5]
    #
    # # Modification de la copie
    # copie_tableau[0] = 10
    # print("tableau :", tableau)  # Output: [1, 2, 3, 4, 5]
    # print("modification du tableau copier :", copie_tableau)  # Output: [10, 2, 3, 4, 5]

    # # === question 2 === #
    # tableau = [1, 2, 3, 4, 5]
    # inverse_tableau = inverse(tableau)
    # print(inverse_tableau)  # Output: [5, 4, 3, 2, 1]

    # # === question 3 === #
    # taille = 10
    # print("tableau_premiers_entiers :", tableau_premiers_entiers(taille))
    # print("tableau_premiers_entiers_melanges :", tableau_premiers_entiers_melanges(taille))
    # print("tableau_premiers_entiers_inverses :", tableau_premiers_entiers_inverses(taille))

    # # === question 4 === #
    # my_file = 'stats.dat'
    # ligne_dans_fichier(my_file, 10, 5.7)  # ne pas oublier de supprimer le test après dans 'stats.dat'

    # # === question 5 === #
    # tableau = [5, 2, 8, 1, 9]
    # print("Temps de tri à bulles :", temps_tri_bulles(tableau), "secondes")

    # # === question 9 === #
    # nmin = 100
    # nmax = 1000
    # pas = 100
    # fois = 5
    #
    # # === question 6 & 9 === #
    # stats_melange(nmin, nmax, pas, fois)
    #
    # # === question 7 & 9 === #
    # stats_ordonne(nmin, nmax, pas, fois)
    #
    # # === question 8 & 9 === #
    # stats_inverse(nmin, nmax, pas, fois)

    # Génération du script gnuplot
    # script = "plot 'stats.dat' with lines"

    # Exécution du script gnuplot
    figure1 = gp()  # Create a new figure handle
    figure2 = gp(r"C:\Program Files\gnuplot\bin\gnuplot.exe")  # Can also specify which gnuplot to use
    figure1.a("plot sin(x)")
    figure2.a("plot cos(x)")
    # pi = figure.a("print pi")
