class MaClasse:
    x = 23

    def __init__(self):
        self.y = self.x + 5

    def __str__(self):
        self.z = 42
        return "y = {}, z = {}".format(self.y, self.z)


if __name__ == "__main__":
    ma_classe = MaClasse()
    print(ma_classe)
