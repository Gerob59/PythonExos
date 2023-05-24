from typing import Any


def calculer_moyenne(tableau: [int]) -> float:
    if len(tableau) == 0:
        return 0
    else:
        return sum(tableau) / len(tableau)


def compter_occurrences(tableau: [int], element: int) -> int:
    return tableau.count(element)


def compter_superieur_ou_egal_dix(tableau: [int]) -> int:
    return sum(1 for element in tableau if element >= 10)


def trouver_max(tableau: [int]) -> int | None:
    if len(tableau) == 0:
        return None
    else:
        return max(tableau)


def element_present(tableau: [int], element: int) -> bool:
    return element in tableau


if __name__ == "__main__":
    tab = [7, 42, 42, 59]
    print("calculer_moyenne :", calculer_moyenne(tab))  # 37.5
    print("compter_occurrences 12 :", compter_occurrences(tab, 12))  # 0
    print("compter_occurrences 42 :", compter_occurrences(tab, 42))  # 2
    print("compter_superieur_ou_egal_dix :", compter_superieur_ou_egal_dix(tab))  # 3
    print("trouver_max :", trouver_max(tab))  # 59
    print("element_present 12 :", element_present(tab, 12))  # False
    print("element_present 42 :", element_present(tab, 42))  # True
