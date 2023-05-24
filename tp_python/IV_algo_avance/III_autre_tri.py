from I_tableaux_quelconques import index_minimum
from II_tableau_trie import insertion


# on fait n tour de boucle entre i et n, i commence à 0, et on intervertit le plus petit à la case i à chaque boucle.
def tri_extraction(t: [int]):
    n = len(t)
    for i in range(n - 1):
        indice_min = index_minimum(t, i, n - 1)
        t[i], t[indice_min] = t[indice_min], t[i]


def tri_insertion(t: [int], n: int):
    for i in range(1, n):
        element = t[i]
        insertion(element, t, i + 1)


if __name__ == "__main__":
    tableau = [5, 2, 8, 3, 1, 7]
    print("tableau", tableau)

    tri_extraction(tableau)
    print("Tableau trié avec tri_extraction :", tableau)

    tableau = [5, 2, 8, 3, 1, 7]
    tri_insertion(tableau, len(tableau))
    print("Tableau trié avec tri_insertion :", tableau)
