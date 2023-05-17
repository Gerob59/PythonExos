import re


def compter_mots(chaine):
    # On transforme la chaîne en une liste de mots
    mots = chaine.split()
    # On initialise un dictionnaire vide
    freq = {}
    # Pour chaque mot dans la liste, on incrémente son compteur dans le dictionnaire
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1
    return freq


if __name__ == "__main__":
    sample = "Pikachu et Salamèche jouaient tranquillement dans la forêt. Soudain, Pikachu aperçut un Magicarpe " \
             "coincé dans une flaque d'eau et décida de l'aider. Salamèche, en revanche, préféra rester en arrière " \
             "pour éviter de se mouiller les pattes. Pikachu réussit finalement à sortir Magicarpe de l'eau et " \
             "tous les trois rentrèrent chez eux en héros."
    sample_sans_ponctuation = re.sub(r'[^\w\s]', '', sample)
    resultat = sorted(compter_mots(sample_sans_ponctuation).items())
    print(resultat)
