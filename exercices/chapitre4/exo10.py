from collections import deque


class Pile:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.pile = deque(elements)

    def empile(self, element):
        self.pile.append(element)

    def depile(self):
        if len(self.pile) == 0:
            return None
        else:
            return self.pile.pop()


if __name__ == "__main__":
    ma_pile = Pile()
    ma_pile.empile(1)
    ma_pile.empile(2)
    print(ma_pile.depile())  # Sortie attendue : 2
    ma_pile.empile(3)
    print(ma_pile.depile())  # Sortie attendue : 3
    print(ma_pile.depile())  # Sortie attendue : 1
    print(ma_pile.depile())  # Sortie attendue : None

