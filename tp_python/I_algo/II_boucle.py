# 1
# i = 0
# while i <= 100:
#     print(i)
#     i += 1
#
# for i in range(101):
#     print(i)


# 2
def carre(cote: int):
    for i in range(cote):
        for j in range(cote):
            print("X", end=" ")
        print()


def carre_creux(cote: int):
    for i in range(cote):
        for j in range(cote):
            if i == 0 or j == 0 or j == cote - 1 or i == cote - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()


def triangle(taille: int):
    for i in range(taille):
        for j in range(i + 1):
            print("X", end=" ")
        print()


def triangle_creux(taille: int):
    for i in range(taille):
        for j in range(i + 1):
            if j == 0 or j == i or i == taille - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    triangle(5)
