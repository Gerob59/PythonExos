import math


def vol_masse_ellipsoide(longueur, largeur, hauteur, masse):
    volume = (4/3) * math.pi * longueur * largeur * hauteur
    return volume, masse


if __name__ == "__main__":
    print(vol_masse_ellipsoide(12, 10, 5, 456))
