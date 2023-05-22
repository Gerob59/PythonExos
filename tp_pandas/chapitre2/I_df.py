import random

import pandas as pd

df = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert", sep=",")

# sample(n, frac, replace, weights, random_state)
# n : nombre d'éléments tirés
# frac : 0<n<1, tire le nombre lignes de la probavilité
# replace : True or False, permet de tirer un element plusieurs fois ou non
# weights : tableau de int, permet de spécifier les poids sur chaque échantillon
# random_state : fixe la seed pour la reproductibilité


if __name__ == "__main__":
    # 1
    # print("10 premieres valeurs :", df.head(10))
    # print("15 dernières valeurs :", df.tail(15))
    # print("10 valeurs aléatoire :", df.sample(10))

    # 2
    # sample_5_percent = df.sample(frac=0.05, replace=False)
    # print(sample_5_percent)

    # 3
    # first_10_rows = df.head(10)
    # sample_100 = first_10_rows.sample(n=100, replace=True)
    # print(sample_100)

    # 4
    first_6_rows = df.head(6)

    # Créer une liste des poids pour les tirages
    weights = [0.5] + [0.5 / (len(first_6_rows) - 1)] * (len(first_6_rows) - 1)

    # Effectuer les 100 tirages avec les poids spécifiés
    sample_100_with_weights = random.choices(first_6_rows.index, k=100, weights=weights)

    # Compter combien de fois chaque échantillon a été choisi
    counts = pd.Series(sample_100_with_weights).value_counts()

    print(counts)
