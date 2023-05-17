def compo1():
    # Définir les caractéristiques du labyrinthe
    hauteur, longueur = 6, 5
    position_entre = (3, 1)
    position_sortie = (1, 4)

    # Créer les murs du labyrinthe
    murs_interieur = [(1, 2), (2, 4), (3, 2), (3, 4), (4, 2), (4, 4)]
    murs = murs_interieur + __murs_exterieur(longueur, hauteur)
    murs.remove(position_sortie)

    # Retourner les caractéristiques du labyrinthe
    return hauteur, longueur, position_entre, position_sortie, murs


def compo2():
    # Caractéristiques du labyrinthe
    hauteur, longueur = 10, 25
    position_entre = (1, 1)
    position_sortie = (3, 24)

    # Création des murs
    murs_interieur = [(1, 2), (1, 4), (1, 8), (1, 19), (1, 20),
                      (2, 2), (2, 4), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 12), (2, 13), (2, 14), (2, 15),
                      (2, 16), (2, 17), (2, 19), (2, 20), (2, 21), (2, 22),
                      (3, 2), (3, 4), (3, 6), (3, 8), (3, 10), (3, 12), (3, 20), (3, 21), (3, 22),
                      (4, 6), (4, 8), (4, 10), (4, 12), (4, 13), (4, 14), (4, 16), (4, 17), (4, 18), (4, 20), (4, 21),
                      (4, 22),
                      (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 8), (5, 12), (5, 13), (5, 14), (5, 16), (5, 18),
                      (5, 19), (5, 21), (5, 22),
                      (6, 10), (6, 16),
                      (7, 1), (7, 2), (7, 4), (7, 5), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 14),
                      (7, 15), (7, 16), (7, 17), (7, 19), (7, 20), (7, 21), (7, 22),
                      (8, 5), (8, 22)]
    murs = murs_interieur + __murs_exterieur(longueur, hauteur)
    murs.remove(position_sortie)

    # Retourner les caractéristiques du labyrinthe
    return hauteur, longueur, position_entre, position_sortie, murs


def __murs_exterieur(longueur, hauteur):
    return [(i, j) for i in range(hauteur) for j in range(longueur)
            if i == 0 or j == 0 or j == longueur-1 or i == hauteur-1]
