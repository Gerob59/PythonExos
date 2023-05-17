from exercices.chapitre8.exo2.Point import Point


class Segment:
    def __init__(self, x1: float = 0.0, y1: float = 0.0, x2: float = 0.0, y2: float = 0.0):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def __str__(self):
        return "{} --> {}".format(self.orig, self.extrem)


if __name__ == "__main__":
    s1 = Segment(1.0, 2.0, 3.0, 4.0)
    print(s1)  # affiche : (1.0, 2.0) --> (3.0, 4.0)
