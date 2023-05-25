from tp_python.III_enregistrement.Etudiant import Etudiant
from tp_python.III_enregistrement.Promotion import Promotion

if __name__ == "__main__":
    # Exemple d'utilisation
    etudiants: [Etudiant] = [Etudiant("Jean", {"Mathematiques": 15, "Physique": 16, "Francais": 14}),
                             Etudiant("Marie", {"Mathematiques": 18, "Physique": 17, "Francais": 16}),
                             Etudiant("Pierre", {"Mathematiques": 12, "Physique": 14, "Francais": 13})]

    promotion: Promotion = Promotion(etudiants)

    # Moyenne d'un étudiant
    moyenne_etudiant: float = promotion.etudiants[0].moyenne()
    print("Moyenne de l'etudiant Jean:", moyenne_etudiant)

    # Moyenne d'une discipline pour la promotion
    moyenne_mathematiques: float = promotion.moyenne_discipline("Mathematiques")
    print("Moyenne en mathematiques pour la promotion:", moyenne_mathematiques)

    # Meilleur étudiant de la promotion
    meilleur_etudiant: Etudiant = promotion.meilleur_etudiant()
    print("Meilleur etudiant de la promotion:", meilleur_etudiant.nom)
