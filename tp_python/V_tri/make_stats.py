import random
import time
from matplotlib import pyplot as plt
from extract_data_from_file import get_data_from_file
from tri import tri_bulle, tri_insertion, tri_extraction
import statistics


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


def temps_methode_tri(t, methode_tri):
    copie_t = t.copy()
    debut = time.time()
    methode_tri(copie_t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution


def stats_melange(methode_tri, nmin, nmax, pas, fois):
    fichier = "temps_tris_melange.txt"
    tableau = tableau_premiers_entiers_melanges(nmax)
    __stats(tableau, fichier, methode_tri, nmin, nmax, pas, fois)


def stats_ordonne(methode_tri, nmin, nmax, pas, fois):
    fichier = "temps_tris_ordonne.txt"
    tableau = tableau_premiers_entiers(nmax)
    __stats(tableau, fichier, methode_tri, nmin, nmax, pas, fois)


def stats_inverse(methode_tri, nmin, nmax, pas, fois):
    fichier = "temps_tris_inverse.txt"
    tableau = tableau_premiers_entiers_inverses(nmax)
    __stats(tableau, fichier, methode_tri, nmin, nmax, pas, fois)


def __stats(tableau, fichier, methode_tri, nmin, nmax, pas, fois):
    with open(fichier, 'w') as f:
        f.write("Taille Temps_moyen\n")
        for taille in range(nmin, nmax + 1, pas):
            temps_total = sum(temps_methode_tri(tableau, methode_tri) for _ in range(fois))
            temps_moyen = temps_total / fois
            f.write(f"{taille} {temps_moyen}\n")

    print("Les temps moyens ont été enregistrés dans le fichier", fichier)


def compare_temps_tris(methode_tri, nmin, nmax, pas, fois):
    stats_melange(methode_tri, nmin, nmax, pas, fois)
    stats_ordonne(methode_tri, nmin, nmax, pas, fois)
    stats_inverse(methode_tri, nmin, nmax, pas, fois)

    files = ['temps_tris_inverse.txt', 'temps_tris_ordonne.txt', 'temps_tris_melange.txt']
    data = {}

    for file in files:
        data[file] = get_data_from_file(file)

    for file, values in data.items():
        # Calculer l'écart-type
        temps = values['tableau_y']
        ecart_type = statistics.stdev(temps)
        print("Écart-type pour", file, ":", ecart_type)

        # Créer le graphique combiné
        plt.plot(values['tableau_x'], values['tableau_y'], label=file)

    __pyplot_display(data[files[0]]['titre_x'], data[files[0]]['titre_y'])


def compare_methode_tri(type_data, nmin, nmax, pas, fois):
    data = {}
    methodes = [tri_bulle, tri_extraction, tri_insertion]
    if type_data == "inverse":
        for methode in methodes:
            stats_inverse(methode, nmin, nmax, pas, fois)
            data[methode.__name__] = get_data_from_file("temps_tris_inverse.txt")

    elif type_data == "melange":
        for methode in methodes:
            stats_melange(methode, nmin, nmax, pas, fois)
            data[methode.__name__] = get_data_from_file("temps_tris_melange.txt")

    elif type_data == "ordonne":
        for methode in methodes:
            stats_ordonne(methode, nmin, nmax, pas, fois)
            data[methode.__name__] = get_data_from_file("temps_tris_ordonne.txt")

    for file, values in data.items():
        plt.plot(values['tableau_x'], values['tableau_y'], label=file)

    __pyplot_display(data[methodes[0].__name__]['titre_x'], data[methodes[0].__name__]['titre_y'])


def __pyplot_display(titre_x, titre_y):
    plt.xlabel(titre_x)
    plt.ylabel(titre_y)
    plt.title('Comparaison des temps moyens')
    plt.legend()
    plt.show()


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

    # === question 5 === #
    # tableau = [5, 2, 8, 1, 9]*1000
    # print("Temps de tri à bulles :", temps_methode_tri(tableau, tri_bulle), "secondes")

    # === question 6 & 7 & 8 & 9 === #
    nmin = 100
    nmax = 1000
    pas = 100
    fois = 5
    # stats_melange(tri_bulle, nmin, nmax, pas, fois)
    # stats_ordonne(tri_bulle, nmin, nmax, pas, fois)
    # stats_inverse(tri_bulle, nmin, nmax, pas, fois)

    # === question 10 === #
    # methode_de_tri = tri_bulle
    methode_de_tri = tri_extraction
    # methode_de_tri = tri_insertion
    compare_temps_tris(methode_de_tri, nmin, nmax, pas, fois)

    # type_tableau = "melange"
    # type_tableau = "ordonne"
    # type_tableau = "inverse"
    # compare_methode_tri(type_tableau, nmin, nmax, pas, fois)

    # === question 11 === #
    # ecart_type_echantillon = statistics.pstdev((1, 2))
    # print("L'écart-type (échantillon) est :", ecart_type_echantillon)
