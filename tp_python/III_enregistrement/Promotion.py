from tp_python.III_enregistrement.Etudiant import Etudiant


class Promotion:
    def __init__(self, etudiants: [Etudiant]):
        self.etudiants = etudiants

    def moyenne_discipline(self, discipline: str) -> float:
        notes_discipline = [etudiant.notes[discipline] for etudiant in self.etudiants if discipline in etudiant.notes]
        return sum(notes_discipline) / len(notes_discipline) if notes_discipline else 0

    def meilleur_etudiant(self) -> Etudiant:
        return max(self.etudiants, key=lambda etudiant: etudiant.moyenne(), default=None)

