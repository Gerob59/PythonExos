import random

# Liste les mots possible
choix = ["MERCURE", "VENUS", "TERRE", "MARS", "JUPITER", "SATURNE", "URANUS", "NEPTUNE"]
solution = random.choice(choix)  # choix aleatoire d'un mot dans la liste
tentatives = 1
affichage = ""
lettres_trouvees = []
trouve = False

# premier build pour l'affichage
for lettre in solution:
    affichage += "_ "

# Boucle du jeu, se termine quand le mot est trouve
while not trouve:
    print(affichage)
    proposition = input("Entrez une lettre ou '?' pour abandonner : ")[0:1].upper()  # force la premiere lettre en maj

    # verifie si la lettre est dans le mot
    if proposition == '?':  # cas d'arret
        break
    elif proposition in solution:  # cas lettre présente
        lettres_trouvees.append(proposition)
    else:  # cas non présente
        tentatives += 1

    # build pour l'affichage
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    # cas d'arret ou le mot a ete trouve
    if "_" not in affichage:
        trouve = True
        break

if trouve:
    print(f"Bravo ! Le mot {solution} a été trouvé en {tentatives-1} coups")
