import unittest
from context import Etudiant, Promotion


class TestEtudiant(unittest.TestCase):
    def test_moyenne(self):
        etudiant = Etudiant("Jean", {"Mathematiques": 15, "Physique": 16, "Francais": 14})
        moyenne = etudiant.moyenne()
        self.assertEqual(moyenne, 15)  # Vérifie si la moyenne est égale à 15


class TestPromotion(unittest.TestCase):
    def setUp(self):
        etudiants = {
            "Jean": Etudiant("Jean", {"Mathematiques": 15, "Physique": 16, "Francais": 14}),
            "Marie": Etudiant("Marie", {"Mathematiques": 18, "Physique": 17, "Francais": 16}),
            "Pierre": Etudiant("Pierre", {"Mathematiques": 12, "Physique": 14, "Francais": 13})
        }
        self.promotion = Promotion(etudiants)

    def test_moyenne_discipline(self):
        moyenne_mathematiques = self.promotion.moyenne_discipline("Mathematiques")
        self.assertEqual(moyenne_mathematiques, 15)  # Vérifie si la moyenne en mathématiques est égale à 15

    def test_meilleur_etudiant(self):
        meilleur_etudiant = self.promotion.meilleur_etudiant()
        self.assertEqual(meilleur_etudiant.nom, "Marie")  # Vérifie si le meilleur étudiant est "Marie"


if __name__ == "__main__":
    unittest.main()
