import pygame


class LabyrintheGraphique:
    def __init__(self, compo, taille_case=32):
        self.hauteur: int = compo[0]
        self.longueur: int = compo[1]
        self.position_entre: tuple[int, int] = compo[2]
        self.position_sortie: tuple[int, int] = compo[3]
        self.murs: list[tuple[int, int]] = compo[4]
        self.position_joueur: tuple[int, int] = self.position_entre  # position initiale du joueur
        self.passage: list[tuple[int, int]] = []
        self.taille_case: int = taille_case

    def afficher_labyrinthe(self, screen):
        # Couleurs
        couleurs: dict = {
            "mur": (0, 0, 0),
            "entree": (0, 0, 255),
            "sortie": (255, 0, 0),
            "joueur": (0, 255, 0),
            "passage": (255, 255, 0),
            "vide": (255, 255, 255)
        }

        # Positionner les carrés de couleurs
        for i in range(self.hauteur):
            for j in range(self.longueur):
                couleur: tuple[int, int, int] = couleurs["vide"]
                if (i, j) == self.position_joueur:
                    couleur = couleurs["joueur"]
                elif (i, j) == self.position_entre:
                    couleur = couleurs["entree"]
                elif (i, j) == self.position_sortie:
                    couleur = couleurs["sortie"]
                elif (i, j) in self.murs:
                    couleur = couleurs["mur"]
                elif (i, j) in self.passage:
                    couleur = couleurs["passage"]
                pygame.draw.rect(screen, couleur,
                                 pygame.Rect(j * self.taille_case, i * self.taille_case, self.taille_case,
                                             self.taille_case))

    def deplacer_joueur(self, direction: str) -> bool:
        deplacement: tuple[int, int] = {
            "haut": (-1, 0),
            "bas": (1, 0),
            "gauche": (0, -1),
            "droite": (0, 1),
        }.get(direction)

        nouvelle_position: tuple[int, int] = tuple(sum(x) for x in zip(self.position_joueur, deplacement))

        if nouvelle_position in self.murs:
            return False

        self.position_joueur = nouvelle_position
        self.passage.append(nouvelle_position)

        return nouvelle_position == self.position_sortie
