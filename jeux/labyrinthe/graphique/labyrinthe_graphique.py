import pygame


class Labyrinthe:
    def __init__(self, compo, taille_case=32):
        self.hauteur, self.longueur, self.position_entre,  self.position_sortie, self.murs = compo
        self.position_joueur = self.position_entre  # position initiale du joueur
        self.passage = []
        self.taille_case = taille_case

    def afficher_labyrinthe(self, screen):
        # Couleurs
        couleurs = {
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
                couleur = couleurs["vide"]
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

    def deplacer_joueur(self, direction):
        deplacement = {
            "haut": (-1, 0),
            "bas": (1, 0),
            "gauche": (0, -1),
            "droite": (0, 1),
        }.get(direction)

        nouvelle_position = tuple(sum(x) for x in zip(self.position_joueur, deplacement))

        if nouvelle_position in self.murs:
            return False

        self.position_joueur = nouvelle_position
        self.passage.append(nouvelle_position)

        return nouvelle_position == self.position_sortie
