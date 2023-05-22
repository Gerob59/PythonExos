class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        return "({}, {})".format(self.longueur, self.largeur)

    def surface(self):
        return self.longueur * self.largeur
