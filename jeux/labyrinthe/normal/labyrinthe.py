class Labyrinthe:
    def __init__(self, compo):
        self.hauteur: int = compo[0]
        self.longueur: int = compo[1]
        self.position_entre: tuple[int, int] = compo[2]
        self.position_sortie: tuple[int, int] = compo[3]
        self.murs: list[tuple[int, int]] = compo[4]
        self.position_joueur: tuple[int, int] = self.position_entre  # position initiale du joueur
        self.passage: list[tuple[int, int]] = []

    def afficher_labyrinthe(self):
        for i in range(self.hauteur):
            for j in range(self.longueur):
                if (i, j) == self.position_joueur:
                    print("J", end=" ")
                elif (i, j) == self.position_entre:
                    print("E", end=" ")
                elif (i, j) == self.position_sortie:
                    print("S", end=" ")
                elif (i, j) in self.murs:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def deplacer_joueur(self, direction: str) -> bool:
        deplacement: tuple[int, int] = {
            "z": (-1, 0),
            "s": (1, 0),
            "q": (0, -1),
            "d": (0, 1),
        }.get(direction)

        nouvelle_position: tuple[int, int] = tuple(sum(x) for x in zip(self.position_joueur, deplacement))

        if nouvelle_position in self.murs:
            return False

        self.position_joueur = nouvelle_position
        self.passage.append(nouvelle_position)

        return nouvelle_position == self.position_sortie
