import sys
import pygame
from labyrinthe_graphique import LabyrintheGraphique
from jeux.labyrinthe.compos_labyrinthe import compo2


def run():
    # Initialisation du labyrinthe
    labyrinthe: LabyrintheGraphique = LabyrintheGraphique(compo2(), 48)
    taille_case: int = labyrinthe.taille_case

    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((labyrinthe.longueur * taille_case, labyrinthe.hauteur * taille_case))
    pygame.display.set_caption('Labyrinthe')

    # Boucle de jeux
    finis: bool = False
    while not finis:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    finis = labyrinthe.deplacer_joueur("haut")
                elif event.key == pygame.K_DOWN:
                    finis = labyrinthe.deplacer_joueur("bas")
                elif event.key == pygame.K_LEFT:
                    finis = labyrinthe.deplacer_joueur("gauche")
                elif event.key == pygame.K_RIGHT:
                    finis = labyrinthe.deplacer_joueur("droite")

        # Affichage du labyrinthe
        labyrinthe.afficher_labyrinthe(screen)
        pygame.display.flip()

        # Vérifier si le joueur a atteint la sortie
        if finis:
            print("Bravo, vous avez trouvé la sortie !")
            pygame.quit()


if __name__ == "__main__":
    run()
