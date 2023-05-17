def un_dictionnaire(dictionnaire_de_longueur_variable):
    for key, value in dictionnaire_de_longueur_variable.items():
        print(f"key: {key}, value: {value}")


if __name__ == "__main__":
    pokemon = {
        "Bulbizarre": {"Type": ["Plante", "Poison"], "Niveau": 5, "Attaques": ["Charge", "Fouet Lianes"]},
        "Salameche": {"Type": ["Feu"], "Niveau": 5, "Attaques": ["Griffe", "Flammèche"]},
        "Carapuce": {"Type": ["Eau"], "Niveau": 5, "Attaques": ["Charge", "Pistolet à O"]},
        "Aspicot": {"Type": ["Insecte", "Poison"], "Niveau": 2, "Attaques": ["Dard-Venin", "Mimi-Queue"]},
        "Roucool": {"Type": ["Normal", "Vol"], "Niveau": 3, "Attaques": ["Charge", "Cru-aile"]}
    }
    un_dictionnaire(pokemon)
