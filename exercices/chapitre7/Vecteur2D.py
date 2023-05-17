class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, vecteur):
        return Vecteur2D(self.x + vecteur.x, self.y + vecteur.y)


if __name__ == "__main__":
    vecteur_un = Vecteur2D()
    print(f"vecteur_un : {vecteur_un}")
    vecteur_deux = Vecteur2D(10, 15)
    print(f"vecteur_deux : {vecteur_deux}")
    vecteur_trois = Vecteur2D(5, 15)
    print(f"vecteur_trois : {vecteur_trois}")
    vecteur_quatre = vecteur_deux.__add__(vecteur_trois)
    print(f"vecteur_quatre : {vecteur_quatre}")
