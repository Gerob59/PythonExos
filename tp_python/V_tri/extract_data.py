import random
import time
from matplotlib import pyplot as plt
from extract_data_from_file import get_data_from_file
# from III_autre_tri import tri_extraction, tri_insertion
# from ..I_tableaux_quelconques import tri_bulle
from tri import tri_bulle, tri_insertion, tri_extraction


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
        f.write("Taille Temps moyen\n")
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

    # Créer le graphique combiné
    for file, values in data.items():
        plt.plot(values['tableau_x'], values['tableau_y'], label=file)

    plt.xlabel(data[files[0]]['titre_x'])
    plt.ylabel(data[files[0]]['titre_y'])
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

    # # === question 5 === #
    # tableau = [5, 2, 8, 1, 9]
    # print("Temps de tri à bulles :", temps_tri_bulles(tableau), "secondes")

    # === question 6 & 7 & 8 & 9 === #
    # ont été faite puis refactor pour convenir à la question 10

    # === question 10 === #
    nmin = 100
    nmax = 1000
    pas = 100
    fois = 5
    methode_de_tri = tri_bulle
    compare_temps_tris(methode_de_tri, nmin, nmax, pas, fois)

