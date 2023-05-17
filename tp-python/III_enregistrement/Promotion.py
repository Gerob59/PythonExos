class Promotion:
    def __init__(self, etudiants):
        self.etudiants = etudiants

    def moyenne_discipline(self, discipline):
        total = 0
        count = 0
        for etudiant in self.etudiants.values():
            if discipline in etudiant.notes:
                total += etudiant.notes[discipline]
                count += 1
        if count == 0:
            return 0
        else:
            return total / count

    def meilleur_etudiant(self):
        meilleur_etudiant = None
        meilleure_moyenne = 0
        for etudiant in self.etudiants.values():
            moyenne_etudiant = etudiant.moyenne()
            if moyenne_etudiant > meilleure_moyenne:
                meilleure_moyenne = moyenne_etudiant
                meilleur_etudiant = etudiant
        return meilleur_etudiant
