from collections import deque


class File:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.file = deque(elements)

    def empile(self, element):
        self.file.append(element)

    def depile(self):
        if len(self.file) == 0:
            return None
        else:
            return self.file.popleft()


if __name__ == "__main__":
    f = File()
    f.empile(1)
    f.empile(2)
    print(f.depile())  # Sortie attendue : 1
    f.empile(3)
    print(f.depile())  # Sortie attendue : 2
    print(f.depile())  # Sortie attendue : 3
    print(f.depile())  # Sortie attendue :  None
