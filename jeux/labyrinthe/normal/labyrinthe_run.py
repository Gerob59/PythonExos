from labyrinthe import Labyrinthe
from jeux.labyrinthe.compos_labyrinthe import compo2


def run_labyrinthe():
    # création d'un objet labyrinthe
    lab: Labyrinthe = Labyrinthe(compo2())

    # boucle de jeux
    while True:
        # affichage du labyrinthe
        lab.afficher_labyrinthe()

        # saisie de la direction
        direction: str = input(
            "Dans quelle direction voulez-vous aller ?\n(z pour haut, q pour gauche, s pour bas, d pour droite) ")

        try:
            # déplacement du joueur
            sortie_trouvee: bool = lab.deplacer_joueur(direction)

            # vérification si le joueur a trouvé la sortie
            if sortie_trouvee:
                print("Bravo, vous avez trouvé la sortie !")
                break
        except TypeError:
            print("veuillez n'utiliser que z, q, s ou d")
            lab.afficher_labyrinthe()


if __name__ == "__main__":
    run_labyrinthe()
