# on avance dans le tableau tant qu'on a touvé notre element ou qu'on a dépassé la taille du tableau.
def recherche_lineaire(tableau, element):
    index = 0
    while index < len(tableau) and tableau[index] < element:
        index += 1
    if index < len(tableau) and tableau[index] == element:
        return index
    else:
        return -1


# la recherche dichotomique est l'une des méthodes les plus rapide.
# on possede deux variable debut et fin.
# on compare notre valeur avec le milieu du tableau.
# si notre élément est plus petit, on défini fin a l'indice de la case milieu.
# et inversement si l'élement est plus grand.
# on s'arrete quand on a trouvé l'élément, ou quand debut == fin qui envoie une erreur.
def recherche_dichotomique(tableau, element):
    debut = 0
    fin = len(tableau) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tableau[milieu] == element:
            return milieu
        elif tableau[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1


# insert l'élément à la fin et le fais descendre à sa place.
def insertion(tableau, element):
    i = len(tableau) - 1
    tableau.append(element)  # Ajouter l'élément à la fin du tableau
    while i >= 0 and tableau[i] > element:
        tableau[i + 1] = tableau[i]
        i -= 1
    tableau[i + 1] = element


# def insertion(tableau, element, taille):
#     index = taille - 1
#     while index >= 0 and tableau[index] > element:
#         tableau[index + 1] = tableau[index]
#         index -= 1
#     tableau[index + 1] = element


def __affichage_resultat(element_recherche, index):
    if index != -1:
        print(f"L'élément {element_recherche} a été trouvé à l'index {index}")
    else:
        print(f"L'élément {element_recherche} n'a pas été trouvé dans le tableau")


if __name__ == "__main__":
    my_tab = [1, 3, 5, 7, 9, 11]

    # Test de la recherche linéaire
    element_recherche = 7
    index = recherche_lineaire(my_tab, element_recherche)
    __affichage_resultat(element_recherche, index)

    # Test de la recherche dichotomique
    element_recherche = 9
    index = recherche_dichotomique(my_tab, element_recherche)
    __affichage_resultat(element_recherche, index)

    # Test de la procédure d'insertion
    element_insertion = 4
    insertion(my_tab, element_insertion)
    print("Tableau après insertion :", my_tab)

