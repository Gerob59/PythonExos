class Etudiant:
    def __init__(self, nom: str, notes: dict):
        self.nom = nom
        self.notes = notes

    def moyenne(self) -> float:
        taille = len(self.notes)
        return sum(self.notes.values()) / taille if taille > 0 else 0

