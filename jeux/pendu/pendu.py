import random


def choisir_mot():
    mots = ["MERCURE", "VENUS", "TERRE", "MARS", "JUPITER", "SATURNE", "URANUS", "NEPTUNE"]
    return random.choice(mots)


def get_proposition(alphabet, lettres_utilisees, lettres_mot, tentatives):
    proposition = input("Entrez une lettre ou '?' pour abandonner : ").strip().upper()[0:1]

    if proposition == "?":
        return proposition, lettres_utilisees, lettres_mot, tentatives, True
    elif proposition in alphabet - lettres_utilisees:
        lettres_utilisees.add(proposition)
        if proposition in lettres_mot:
            lettres_mot.remove(proposition)
        else:
            tentatives += 1
    elif proposition in lettres_utilisees:
        print('Vous avez deja utilise ce caractere.')
    else:
        print('Caractere invalide.')

    return proposition, lettres_utilisees, lettres_mot, tentatives, False


def play_game():
    mot = choisir_mot()
    lettres_mot = set(mot)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lettres_utilisees = set()
    trouve = False
    tentatives = 1

    while not trouve:
        print("\nLettres utilisees:", " ".join(lettres_utilisees))

        # afficher le mot en cours
        word_list = [lettre if lettre in lettres_utilisees else '_' for lettre in mot]
        print("Mot: ", " ".join(word_list))

        proposition, lettres_utilisees, lettres_mot, tentatives, abandon = get_proposition(alphabet, lettres_utilisees,
                                                                                           lettres_mot, tentatives)

        if abandon:
            break

        # Vérifier si toutes les lettres ont été devinées
        if lettres_mot.issubset(lettres_utilisees):
            print(f"Bravo ! Le mot {mot} a été trouvé en {tentatives - 1} coups")
            trouve = True


if __name__ == '__main__':
    play_game()
