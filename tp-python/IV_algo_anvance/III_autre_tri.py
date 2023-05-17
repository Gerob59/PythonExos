from I_tableaux_quelconques import index_minimum
from II_tableau_trie import insertion


def tri_extraction(t):
    n = len(t)
    for i in range(n - 1):
        indice_min = index_minimum(t, i, n - 1)
        t[i], t[indice_min] = t[indice_min], t[i]


def tri_insertion(t):
    n = len(t)
    for i in range(1, n):
        element = t[i]
        insertion(t, element)


if __name__ == "__main__":
    tableau = [5, 2, 8, 3, 1, 7]
    print("tableau", tableau)

    tri_extraction(tableau)
    print("Tableau trié :", tableau)

    tableau = [5, 2, 8, 3, 1, 7]
    tri_insertion(tableau)
    print("Tableau trié :", tableau)
