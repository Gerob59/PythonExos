from exercices.chapitre8.exercice1.Rectangle import Rectangle


class Carre(Rectangle):
    def __init__(self, cote=0):
        super().__init__(cote, cote)


if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(rect)
    print(f"Surface du Rectangle : {rect.surface()}")

    carre = Carre(4)
    print(carre)
    print(f"Surface du carré : {carre.surface()}")
