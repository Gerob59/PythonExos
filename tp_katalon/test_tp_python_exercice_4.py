import unittest
from context import index_minimum, tri_bulle, recherche_lineaire, recherche_dichotomique, insertion, tri_extraction, tri_insertion


class TestFonctions(unittest.TestCase):
    def test_index_minimum(self):
        tableau = [5, 2, 8, 1, 9]
        indice = index_minimum(tableau, 0, len(tableau) - 1)
        self.assertEqual(indice, 3)  # Vérifie si l'indice du minimum est égal à 3

        indice = index_minimum(tableau, 2, 4)
        self.assertEqual(indice, 4)  # Vérifie si l'indice du minimum est égal à 4

        indice = index_minimum(tableau, 3, 1)
        self.assertEqual(indice, -1)  # Vérifie si -1 est retourné pour des indices invalides

    def test_tri_bulle(self):
        tableau = [5, 2, 8, 1, 9]
        tri_bulle(tableau)
        self.assertEqual(tableau, [1, 2, 5, 8, 9])  # Vérifie si le tableau est trié correctement

        tableau = [9, 8, 7, 6, 5]
        tri_bulle(tableau)
        self.assertEqual(tableau, [5, 6, 7, 8, 9])  # Vérifie si le tableau est trié correctement

        tableau = [1, 2, 3, 4, 5]
        tri_bulle(tableau)
        self.assertEqual(tableau, [1, 2, 3, 4, 5])  # Vérifie si le tableau déjà trié reste inchangé

    def test_recherche_lineaire(self):
        tableau = [1, 2, 3, 4, 5]
        element = 3
        index = recherche_lineaire(tableau, element)
        self.assertEqual(index, 2)  # Vérifie si l'index retourné est égal à 2

        element = 6
        index = recherche_lineaire(tableau, element)
        self.assertEqual(index, -1)  # Vérifie si l'index retourné est -1

    def test_recherche_dichotomique(self):
        tableau = [1, 2, 3, 4, 5]
        element = 3
        index = recherche_dichotomique(element, tableau)
        self.assertEqual(index, 2)  # Vérifie si l'index retourné est égal à 2

        element = 6
        index = recherche_dichotomique(element, tableau)
        self.assertEqual(index, -1)  # Vérifie si l'index retourné est -1

    def test_insertion(self):
        tableau = [1, 3, 4, 5]
        element = 2
        n = 4
        insertion(element, tableau, n)
        self.assertEqual(tableau, [1, 2, 3, 4, 5])  # Vérifie si l'élément 2 est inséré correctement

        tableau = [1, 3, 4, 5]
        element = 6
        n = 4
        insertion(element, tableau, n)
        self.assertEqual(tableau, [1, 3, 4, 5, 6])  # Vérifie si l'élément 6 est inséré correctement

    def test_tri_extraction(self):
        tableau = [5, 2, 8, 1, 9]
        tri_extraction(tableau)
        self.assertEqual(tableau, [1, 2, 5, 8, 9])  # Vérifie si le tableau est trié correctement

        tableau = [9, 8, 7, 6, 5]
        tri_extraction(tableau)
        self.assertEqual(tableau, [5, 6, 7, 8, 9])  # Vérifie si le tableau est trié correctement

        tableau = [1, 2, 3, 4, 5]
        tri_extraction(tableau)
        self.assertEqual(tableau, [1, 2, 3, 4, 5])  # Vérifie si le tableau déjà trié reste inchangé

    def test_tri_insertion(self):
        tableau = [5, 2, 8, 1, 9]
        tri_insertion(tableau, len(tableau))
        self.assertEqual(tableau, [1, 2, 5, 8, 9])  # Vérifie si le tableau est trié correctement

        tableau = [9, 8, 7, 6, 5]
        tri_insertion(tableau, len(tableau))
        self.assertEqual(tableau, [5, 6, 7, 8, 9])  # Vérifie si le tableau est trié correctement

        tableau = [1, 2, 3, 4, 5]
        tri_insertion(tableau, len(tableau))
        self.assertEqual(tableau, [1, 2, 3, 4, 5])  # Vérifie si le tableau déjà trié reste inchangé


if __name__ == "__main__":
    unittest.main()
