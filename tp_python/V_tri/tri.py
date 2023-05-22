def tri_bulle(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]


def index_minimum(t, d, f):
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


def tri_extraction(t):
    n = len(t)
    for i in range(n - 1):
        indice_min = index_minimum(t, i, n - 1)
        t[i], t[indice_min] = t[indice_min], t[i]


def insertion(e, t, n):
    i = 0
    while i < n and t[i] < e:
        i += 1

    for j in range(n - 1, i - 1, -1):
        t[j] = t[j - 1]

    t[i] = e


def tri_insertion(t, n):
    for i in range(1, n):
        element = t[i]
        insertion(element, t, i + 1)