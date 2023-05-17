dico = {
    "Au": {
        "Te/Tf": [2970, 1063],
        "Z/A": [79, 196.967]
    },
    "Ga": {
        "Te/Tf": [2237, 29.8],
        "Z/A": [31, 69.72]
    }
}


def info_element(nom):
    if nom in dico:
        print(f"Information de {nom}")
        print("Température d’ébullition :", dico[nom]["Te/Tf"][0], "°C")
        print("Température de fusion :", dico[nom]["Te/Tf"][1], "°C")
        print("Numéro atomique :", dico[nom]["Z/A"][0])
        print("Masse atomique :", dico[nom]["Z/A"][1])
    else:
        print(f"l'élément chimique {nom} n'existe pas ou n'est pas encore référencé dans le dictionnaire")


if __name__ == "__main__":
    info_element("Au")
    info_element("C")
