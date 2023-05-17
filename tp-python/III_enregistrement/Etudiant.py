class Etudiant:
    def __init__(self, nom, notes):
        self.nom = nom
        self.notes = notes

    def moyenne(self):
        if len(self.notes) == 0:
            return 0
        else:
            total = sum(self.notes.values())
            return total / len(self.notes)
