import math


def cube(valeur):
    return valeur**3


def sphere(rayon):
    return 4 * math.pi * cube(rayon) / 3


if __name__ == "__main__":
    print(sphere(2))
