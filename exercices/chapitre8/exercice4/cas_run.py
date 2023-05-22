from exercices.chapitre8.exercice4.CasNormal import CasNormal
from exercices.chapitre8.exercice4.CasSpecial import CasSpecial


def casQuiConvient(estNormal: bool = True):
    return CasNormal() if estNormal else CasSpecial()


if __name__ == "__main__":
    instance = casQuiConvient()
    instance.uneMethode()  # Affiche "normal"
    instance = casQuiConvient(False)
    instance.uneMethode()  # Affiche "spécial"