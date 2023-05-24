def index_minimum(t: [int], d: int, f: int) -> int:
    # vérifie si on reste bien dans le tableau
    if d < 0 or f >= len(t) or f < d:
        return -1  # Indice invalide

    # variable temporaire qui stocke le premier nombre en tant que plus petit du tableau
    indice_minimum = d

    # on itére pas sur le premier indice, car on l'a déjà dans la variable
    for i in range(d + 1, f + 1):
        # si egalité, on garde le premier indice
        if t[i] < t[d]:
            indice_minimum = i

    return indice_minimum


# Le tri à bulle est un algorithme peu optimal qui effectue n² itérations.
# À chaque itération, il déplace le plus grand nombre du tableau vers la fin.
def tri_bulle(t: [int]):
    n = len(t)
    # On ne parcourt pas le dernier indice car on compare l'élément n avec n+1.
    for i in range(n - 1):
        # On ne parcourt pas le dernier indice car on compare l'élément n avec n+1.
        # De plus, on réduit la plage de recherche de i, car à chaque itération, un élément supplémentaire est bien placé à la fin du tableau.
        for j in range(n - 1 - i):
            # Si la valeur de la case de gauche est supérieure à celle de la case de droite, on les inverse.
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]


if __name__ == "__main__":
    # test index_minimum
    tableau = [7, 2, 9, 5, 1, 6, 3]
    debut = 1
    fin = 5
    indice_min = index_minimum(tableau, debut, fin)
    print(f"L'indice du minimum entre les cases {debut} et {fin} est : {indice_min} avec pour valeur {tableau[4]}")

    # test tri_bulle
    print("avant tri à bulle", tableau)
    tri_bulle(tableau)
    print("après tri à bulle", tableau)
