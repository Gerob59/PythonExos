class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)