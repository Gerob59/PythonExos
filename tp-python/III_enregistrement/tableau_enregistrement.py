from tp.III_enregistrement.Etudiant import Etudiant
from tp.III_enregistrement.Promotion import Promotion

if __name__ == "__main__":
    # Exemple d'utilisation
    etudiants = {
        "Jean": Etudiant("Jean", {"Mathematiques": 15, "Physique": 16, "Francais": 14}),
        "Marie": Etudiant("Marie", {"Mathematiques": 18, "Physique": 17, "Francais": 16}),
        "Pierre": Etudiant("Pierre", {"Mathematiques": 12, "Physique": 14, "Francais": 13})
    }

    promotion = Promotion(etudiants)

    # Moyenne d'un étudiant
    moyenne_etudiant = promotion.etudiants["Jean"].moyenne()
    print("Moyenne de l'etudiant Jean:", moyenne_etudiant)

    # Moyenne d'une discipline pour la promotion
    moyenne_mathematiques = promotion.moyenne_discipline("Mathematiques")
    print("Moyenne en mathematiques pour la promotion:", moyenne_mathematiques)

    # Meilleur étudiant de la promotion
    meilleur_etudiant = promotion.meilleur_etudiant()
    print("Meilleur etudiant de la promotion:", meilleur_etudiant.nom)
