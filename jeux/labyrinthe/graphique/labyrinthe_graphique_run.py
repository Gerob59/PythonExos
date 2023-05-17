import pygame

from labyrinthe_graphique import Labyrinthe
from jeux.labyrinthe.compos_labyrinthe import compo2


def run():
    # Initialisation du labyrinthe
    labyrinthe = Labyrinthe(compo2(), 48)
    taille_case = labyrinthe.taille_case

    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((labyrinthe.longueur * taille_case, labyrinthe.hauteur * taille_case))
    pygame.display.set_caption('Labyrinthe')

    # Boucle de jeu
    finis = False
    while not finis:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finis = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    labyrinthe.deplacer_joueur("haut")
                elif event.key == pygame.K_DOWN:
                    labyrinthe.deplacer_joueur("bas")
                elif event.key == pygame.K_LEFT:
                    labyrinthe.deplacer_joueur("gauche")
                elif event.key == pygame.K_RIGHT:
                    labyrinthe.deplacer_joueur("droite")

        # Affichage du labyrinthe
        labyrinthe.afficher_labyrinthe(screen)
        pygame.display.flip()

        # Vérifier si le joueur a atteint la sortie
        if labyrinthe.position_joueur == labyrinthe.position_sortie:
            print("Bravo, vous avez trouvé la sortie !")
            finis = True
            pygame.quit()


if __name__ == "__main__":
    run()
